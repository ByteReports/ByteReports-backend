import psutil
import cpuinfo
from utils import SEGUNDOS_MEDIA

def get_cpu_info():
    info = {
        "nome": "Desconhecido",
        "arquitetura": "Desconhecida",
        "nucleos_fisicos": 0,
        "threads": 0,
        "frequencia_base_mhz": 0.0,
        "frequencia_maxima_mhz": 0.0,
        "uso_medio_porcento": 0.0
    }
    
    try:
        # Dados estáticos (Nome, Arquitetura)
        cpu_data = cpuinfo.get_cpu_info()
        info["nome"] = cpu_data.get("brand_raw", "Desconhecido")
        info["arquitetura"] = cpu_data.get("arch", "Desconhecida")
        
        # Dados físicos (Núcleos, Frequência)
        info["nucleos_fisicos"] = psutil.cpu_count(logical=False)
        info["threads"] = psutil.cpu_count(logical=True)
        
        freq = psutil.cpu_freq()
        if freq:
            info["frequencia_base_mhz"] = round(freq.current, 2)
            info["frequencia_maxima_mhz"] = round(freq.max, 2)
            
        # Uso médio ao longo de SEGUNDOS_MEDIA (psutil já faz a média internamente)
        info["uso_medio_porcento"] = psutil.cpu_percent(interval=SEGUNDOS_MEDIA)

    except Exception as e:
        info["erro"] = f"Erro ao ler CPU: {str(e)}"
        
    return info