import platform
import psutil
import datetime

def get_sistema_info():
    try:
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        agora = datetime.datetime.now()
        tempo_ligado = str(agora - boot_time).split('.')[0] # Tira os milissegundos
        return {
            "so": f"{platform.system()} {platform.release()}",
            "arquitetura": platform.machine(),
            "tempo_ligado": tempo_ligado
        }
    except:
        return {"so": "Desconhecido", "arquitetura": "N/A", "tempo_ligado": "0:00:00"}