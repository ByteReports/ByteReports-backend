import psutil

def get_bateria_info():
    try:
        bat = psutil.sensors_battery()
        if bat:
            return {
                "tem_bateria": True,
                "porcento": round(bat.percent, 1),
                "conectada": bat.power_plugged
            }
        return {"tem_bateria": False}
    except:
        return {"tem_bateria": False}