import psutil
import cpuinfo

def get_cpu_info():
    info = {"nome": "Desconhecido", "uso_medio_porcento": 0.0}
    try:
        cpu_data = cpuinfo.get_cpu_info()
        info["nome"] = cpu_data.get("brand_raw", "Desconhecido")
        info["uso_medio_porcento"] = psutil.cpu_percent(interval=0.1)
    except Exception as e:
        info["erro"] = str(e)
    return info