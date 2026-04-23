from placa_mae import get_placa_mae_info
from cpu import get_cpu_info
from ram import get_ram_info
from disco import get_disco_info
from gpu import get_gpu_info
from diagnostico import gerar_sugestoes # NOVO IMPORT
import json

def gerar_relatorio_geral():
    relatorio = {
        "placa_mae": get_placa_mae_info(),
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "armazenamento": get_disco_info(),
        "video": get_gpu_info()
    }
    
    # Roda o motor de diagnóstico com base nos dados coletados
    relatorio["diagnostico_e_sugestoes"] = gerar_sugestoes(relatorio)
    
    # Cria o JSON
    json_final = json.dumps(relatorio, indent=4, ensure_ascii=False)
    
    # Salva em um arquivo para o Front-end poder ler facilmente no teste
    with open("relatorio_teste.json", "w", encoding="utf-8") as f:
        f.write(json_final)
        
    print("Relatório gerado e salvo em 'relatorio_teste.json'.")
    return relatorio

if __name__ == "__main__":
    gerar_relatorio_geral()