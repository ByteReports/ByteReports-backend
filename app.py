from placa_mae import get_placa_mae_info
from cpu import get_cpu_info
from ram import get_ram_info
from disco import get_disco_info
from gpu import get_gpu_info
import json

def gerar_relatorio_geral():
    relatorio = {
        "placa_mae": get_placa_mae_info(),
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "armazenamento": get_disco_info(),
        "video": get_gpu_info()
    }
    
    # Imprime um JSON formatado no terminal
    print(json.dumps(relatorio, indent=4, ensure_ascii=False))
    return relatorio

if __name__ == "__main__":
    gerar_relatorio_geral()