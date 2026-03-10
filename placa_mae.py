import wmi

def get_placa_mae_info():
    info = {
        "fabricante": "Desconhecido",
        "modelo": "Desconhecido",
        "numero_serie": "Desconhecido",
        "bios_fabricante": "Desconhecido",
        "bios_versao": "Desconhecido"
    }
    
    try:
        w = wmi.WMI()
        
        # Dados da Placa-Mãe
        for board in w.Win32_BaseBoard():
            info["fabricante"] = board.Manufacturer
            info["modelo"] = board.Product
            info["numero_serie"] = board.SerialNumber
            break # Pega a primeira placa listada
            
        # Dados da BIOS
        for bios in w.Win32_BIOS():
            info["bios_fabricante"] = bios.Manufacturer
            info["bios_versao"] = bios.Name
            break
            
    except Exception as e:
        info["erro"] = f"Erro ao ler placa-mãe: {str(e)}"
        
    return info