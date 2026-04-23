def gerar_sugestoes(relatorio_bruto):
    sugestoes = []

    # Diagnóstico de RAM
    ram = relatorio_bruto.get("ram", {})
    if ram.get("uso_medio_porcento", 0) > 85:
        sugestoes.append({
            "componente": "Memória RAM",
            "alerta": "Uso crítico detectado.",
            "acao": f"Seu sistema está operando no limite dos {ram.get('total_gb')}GB de RAM. Um upgrade (ex: dobrar a memória) evitará travamentos com muitos programas abertos."
        })

    # Diagnóstico de Disco
    armazenamento = relatorio_bruto.get("armazenamento", {})
    for disco in armazenamento.get("discos_fisicos", []):
        if disco.get("saude_smart") != "OK":
            sugestoes.append({
                "componente": "Armazenamento",
                "alerta": "RISCO DE PERDA DE DADOS!",
                "acao": f"O disco {disco.get('modelo')} está relatando falha física iminente. Faça backup dos seus arquivos imediatamente e substitua a peça."
            })
            
    # Diagnóstico Básico de Disco C cheio (Partições)
    for part in armazenamento.get("particoes", []):
        if part.get("letra") == "C:" and part.get("uso_porcento", 0) > 90:
            sugestoes.append({
                "componente": "Sistema Operacional",
                "alerta": "Disco C: quase lotado.",
                "acao": f"Restam apenas {part.get('livre_gb')}GB livres. Limpe arquivos inúteis, pois o Windows fica extremamente lento sem espaço para operar."
            })

    # Se não houver problemas
    if not sugestoes:
        sugestoes.append({
            "componente": "Sistema Geral",
            "alerta": "Tudo em ordem",
            "acao": "Seu computador não apresenta gargalos críticos de hardware no momento."
        })

    return sugestoes