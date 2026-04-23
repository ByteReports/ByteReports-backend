import wmi
import psutil
from utils import bytes_para_gb, coletar_media

def obter_tipo_ddr(codigo):
    # Tabela de códigos SMBIOSMemoryType para gerações de RAM
    tipos = {20: "DDR", 21: "DDR2", 24: "DDR3", 26: "DDR4", 34: "DDR5"}
    return tipos.get(codigo, "Desconhecido")

def get_ram_info():
    info = {
        "total_gb": 0.0,
        "uso_medio_porcento": 0.0,
        "pentes_fisicos": []
    }
    
    try:
        mem_virtual = psutil.virtual_memory()
        info["total_gb"] = bytes_para_gb(mem_virtual.total)
        info["uso_medio_porcento"] = coletar_media(lambda: psutil.virtual_memory().percent)
        
        w = wmi.WMI()
        for stick in w.Win32_PhysicalMemory():
            tipo_ddr = obter_tipo_ddr(stick.SMBIOSMemoryType)
            pente = {
                "fabricante": stick.Manufacturer,
                "capacidade_gb": bytes_para_gb(stick.Capacity),
                "velocidade_mhz": stick.Speed,
                "tipo": tipo_ddr,
                "localizacao": stick.DeviceLocator
            }
            info["pentes_fisicos"].append(pente)
            
    except Exception as e:
        info["erro"] = f"Erro ao ler RAM: {str(e)}"
        
    return info