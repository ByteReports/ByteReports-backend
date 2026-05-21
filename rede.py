import psutil
from utils import bytes_para_gb

def get_rede_info():
    try:
        net = psutil.net_io_counters()
        return {
            "enviado_gb": bytes_para_gb(net.bytes_sent),
            "recebido_gb": bytes_para_gb(net.bytes_recv)
        }
    except:
        return {"enviado_gb": 0, "recebido_gb": 0}