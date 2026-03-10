import wmi
import GPUtil
from utils import bytes_para_gb, coletar_media


def _encontrar_gpu_nvidia(nome_placa, nvidia_gpus, indices_usados):
    nome_upper = (nome_placa or "").upper()

    for nv_gpu in nvidia_gpus:
        if nv_gpu.id in indices_usados:
            continue
        nome_nv = (nv_gpu.name or "").upper()
        if nome_nv in nome_upper or nome_upper in nome_nv:
            indices_usados.add(nv_gpu.id)
            return nv_gpu

    for nv_gpu in nvidia_gpus:
        if nv_gpu.id not in indices_usados:
            indices_usados.add(nv_gpu.id)
            return nv_gpu

    return None

def get_gpu_info():
    info = {
        "placas": []
    }
    
    try:
        w = wmi.WMI()
        wmi_gpus = w.Win32_VideoController()
        
        # O GPUtil fala direto com o driver da NVIDIA
        nvidia_gpus = GPUtil.getGPUs()
        nvidia_usadas = set()
        
        for gpu in wmi_gpus:
            nome_placa = gpu.Name or "Placa Desconhecida"
            vram_gb = 0
            is_nvidia = False
            temperatura_c = None
            temperatura_status = "Sensor indisponivel para esta placa"
            
            # TENTATIVA 1: Se for NVIDIA, puxamos o dado real e limpo do GPUtil
            if "NVIDIA" in nome_placa.upper():
                nv_gpu = _encontrar_gpu_nvidia(nome_placa, nvidia_gpus, nvidia_usadas)
                if nv_gpu:
                    # O GPUtil retorna a VRAM em Megabytes, dividimos por 1024 para GB
                    vram_gb = bytes_para_gb(nv_gpu.memoryTotal * 1024 * 1024)
                    is_nvidia = True
                    if nv_gpu.temperature is not None:
                            gpu_id = nv_gpu.id
                            temperatura_c = coletar_media(
                                lambda gid=gpu_id: next(
                                    (g.temperature for g in GPUtil.getGPUs() if g.id == gid),
                                    None
                                )
                            )
                            temperatura_status = "Média via driver NVIDIA (GPUtil)"
                    else:
                        temperatura_status = "Placa NVIDIA sem leitura de temperatura"
            
            # TENTATIVA 2: Se não for NVIDIA (Ex: AMD ou Intel HD Graphics)
            if not is_nvidia and gpu.AdapterRAM:
                vram_bytes = abs(int(gpu.AdapterRAM)) 
                vram_gb = bytes_para_gb(vram_bytes)
                
                # Tratamento do Bug para AMDs potentes
                # Se o WMI disser que a placa tem exatamente 4GB ou 0, e for placa dedicada,
                # é quase certeza que ela tem mais que 4GB e o WMI não funcionou.
                if vram_gb >= 4.0 or vram_gb == 0:
                    vram_gb = f"{vram_gb}GB (Pode ser maior, limite de leitura do Windows atingido)"

            placa = {
                "nome": nome_placa,
                "fabricante": gpu.AdapterCompatibility,
                "vram_gb": vram_gb,
                "temperatura_c": temperatura_c,
                "temperatura_status": temperatura_status,
                "driver_versao": gpu.DriverVersion,
                "resolucao_atual": f"{gpu.CurrentHorizontalResolution}x{gpu.CurrentVerticalResolution}" if gpu.CurrentHorizontalResolution else "Não configurada"
            }
            info["placas"].append(placa)
            
    except Exception as e:
        info["erro"] = f"Erro ao ler GPU: {str(e)}"
        
    return info