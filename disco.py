import wmi
import psutil
from utils import bytes_para_gb

def get_disco_info():
    info = {
        "discos_fisicos": [],
        "particoes": []
    }
    
    try:
        w = wmi.WMI()
        
        # Hardware: Discos físicos
        for disco in w.Win32_DiskDrive():
            tipo = "Desconhecido"
            if disco.MediaType and "Fixed" in disco.MediaType:
                tipo = "HDD/SSD"
                
            d = {
                "modelo": disco.Model,
                "tamanho_gb": bytes_para_gb(disco.Size),
                "tipo_interface": disco.InterfaceType,
                "saude_smart": disco.Status # Retorna "OK" ou indica falha iminente
            }
            info["discos_fisicos"].append(d)
            
        # Software: Partições no Windows (C:, D:)
        for part in psutil.disk_partitions(all=False):
            if part.fstype != "": # Ignora drives de CD/DVD vazios
                uso = psutil.disk_usage(part.mountpoint)
                p = {
                    "letra": part.device,
                    "formato": part.fstype, # NTFS, FAT32
                    "total_gb": bytes_para_gb(uso.total),
                    "livre_gb": bytes_para_gb(uso.free),
                    "uso_porcento": uso.percent
                }
                info["particoes"].append(p)
                
    except Exception as e:
        info["erro"] = f"Erro ao ler Discos: {str(e)}"
        
    return info