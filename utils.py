import time

# Aumente para leituras mais estáveis; valores altos deixam o relatório mais lento.
SEGUNDOS_MEDIA = 10

def coletar_media(func_amostra, segundos=None, num_amostras=5):
    """Coleta `num_amostras` ao longo de `segundos` e retorna a média."""
    if segundos is None:
        segundos = SEGUNDOS_MEDIA
    amostras = []
    intervalo = segundos / num_amostras
    for i in range(num_amostras):
        try:
            valor = func_amostra()
            if valor is not None:
                amostras.append(float(valor))
        except Exception:
            pass
        if i < num_amostras - 1:
            time.sleep(intervalo)
    return round(sum(amostras) / len(amostras), 2) if amostras else None

def bytes_para_gb(bytes_val):
    try:
        gb = int(bytes_val) / (1024 ** 3)
        return round(gb, 2)
    except (ValueError, TypeError):
        return 0.0