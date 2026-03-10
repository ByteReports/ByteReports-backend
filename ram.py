import wmi
import psutil
from utils import bytes_para_gb, coletar_media

def get_ram_info():
    info = {
        "total_gb": 0.0,
        "uso_medio_porcento": 0.0,
        "pentes_fisicos": []
    }
    
    try:
        mem_virtual = psutil.virtual_memory()
        info["total_gb"] = bytes_para_gb(mem_virtual.total)

        # Média do uso ao longo de SEGUNDOS_MEDIA
        info["uso_medio_porcento"] = coletar_media(
            lambda: psutil.virtual_memory().percent
        )
        
        # Detalhes de cada pente físico (Stick)
        w = wmi.WMI()
        for stick in w.Win32_PhysicalMemory():
            pente = {
                "fabricante": stick.Manufacturer,
                "capacidade_gb": bytes_para_gb(stick.Capacity),
                "velocidade_mhz": stick.Speed,
                "localizacao": stick.DeviceLocator # Ex: DIMM 1
            }
            info["pentes_fisicos"].append(pente)
            
    except Exception as e:
        info["erro"] = f"Erro ao ler RAM: {str(e)}"
        
    return info