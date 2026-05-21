import wmi
import GPUtil
from utils import bytes_para_gb

def get_gpu_info():
    info = {"placas": []}
    try:
        w = wmi.WMI()
        for gpu in w.Win32_VideoController():
            nome = gpu.Name or "GPU Desconhecida"
            nome_upper = nome.upper()
            # Detecta se é integrada
            is_integrada = any(x in nome_upper for x in ["INTEL", "RADEON", "UHD", "IRIS", "VEGA", "APU"])
            
            info["placas"].append({
                "nome": nome,
                "tipo": "Integrada" if is_integrada else "Dedicada",
                "uso": 5, # Valor estático por limitação de permissão no Windows
                "driver_versao": gpu.DriverVersion or "N/A"
            })
    except: pass
    return info