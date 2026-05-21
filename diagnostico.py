def gerar_sugestoes(relatorio):
    ram_gb = relatorio.get("ram", {}).get("total_gb", 0)
    gpus = relatorio.get("video", {}).get("placas", [])
    tempo_ligado = relatorio.get("sistema", {}).get("tempo_ligado", "")
    
    tem_dedicada = any(g.get("tipo") == "Dedicada" for g in gpus)
    tem_integrada = any(g.get("tipo") == "Integrada" for g in gpus)

    dicas = {
        "Trabalho Leve (Navegação, Pacote Office)": [],
        "Trabalho Médio (Multitarefas, Sistemas Web)": [],
        "Trabalho Pesado (Programação, VMs, Dados)": [],
        "Jogos": [],
        "Gravação de Vídeos (Streaming)": [],
        "Design e Edição": []
    }

    if ram_gb < 8:
        dicas["Trabalho Leve (Navegação, Pacote Office)"].append(f"⚠️ CRÍTICO: O sistema conta com apenas {ram_gb}GB de RAM. O próprio Windows e navegadores consomem isso apenas para manter o computador ligado. A Bytebros recomenda um upgrade urgente para 8GB ou 16GB para evitar travamentos rotineiros.")
    else:
        dicas["Trabalho Leve (Navegação, Pacote Office)"].append(f"✅ PERFEITO: Com {ram_gb}GB de RAM, o computador tem folga para rodar o sistema e pacotes de escritório de forma totalmente fluida.")

    if ram_gb < 16:
        falta = round(16 - ram_gb, 1)
        dicas["Trabalho Médio (Multitarefas, Sistemas Web)"].append(f"⚠️ AVISO: Multitarefas eficientes hoje exigem 16GB de RAM. Como você possui {ram_gb}GB, o Windows usará o armazenamento como 'memória quebra-galho', causando lentidão. Recomendamos adicionar mais {falta}GB.")
    else:
        dicas["Trabalho Médio (Multitarefas, Sistemas Web)"].append(f"✅ PERFEITO: {ram_gb}GB de RAM é o cenário ideal corporativo para operar múltiplos sistemas e planilhas complexas simultaneamente.")

    if ram_gb < 16:
        dicas["Trabalho Pesado (Programação, VMs, Dados)"].append(f"⚠️ CRÍTICO: Programação pesada, Docker e Bancos de Dados devoram memória. {ram_gb}GB é insuficiente e causará travamentos. Mínimo exigido: 16GB. Ideal: 32GB.")
    elif ram_gb < 32:
        dicas["Trabalho Pesado (Programação, VMs, Dados)"].append(f"💡 SUGESTÃO: Você tem {ram_gb}GB de RAM. É funcional, mas para rodar múltiplas Máquinas Virtuais, o padrão do mercado de T.I. é 32GB.")
    if not tem_dedicada:
        dicas["Trabalho Pesado (Programação, VMs, Dados)"].append("⚠️ AVISO: Sem uma Placa de Vídeo Dedicada, compilações que usam aceleração de hardware demorarão muito mais tempo.")

    if not tem_dedicada:
        dicas["Jogos"].append("⚠️ CRÍTICO: Nenhuma Placa de Vídeo Dedicada detectada! O vídeo integrado 'rouba' parte da sua memória RAM. Jogos pesados terão engasgos graves e baixo FPS. Este setup serve apenas para jogos leves (e-sports) no gráfico mínimo.")
        dicas["Jogos"].append("💡 SUGESTÃO: A Bytebros sugere serviços de Cloud Gaming (GeForce Now, Xbox Cloud) ou o investimento em uma placa de vídeo dedicada (caso seja um desktop).")
    else:
        dicas["Jogos"].append("✅ PERFEITO: Hardware de vídeo dedicado ativo. Mantenha as manutenções preventivas (limpeza e pasta térmica) em dia com a Bytebros para evitar perda de FPS por superaquecimento.")

    if ram_gb < 16:
        dicas["Jogos"].append(f"⚠️ AVISO: Jogos atuais exigem 16GB de RAM. Com os seus {ram_gb}GB, faltará espaço para carregar as texturas, causando os famosos 'stutterings' (travadas de 1 segundo) no meio da partida.")

    if not tem_dedicada:
        dicas["Gravação de Vídeos (Streaming)"].append("⚠️ CRÍTICO: Fazer transmissões ao vivo sem GPU dedicada é inviável em alta qualidade. Placas dedicadas possuem chips físicos para codificação (NVENC). Sem isso, a sua live vai travar e o processador ferverá.")
    if ram_gb < 16:
        dicas["Gravação de Vídeos (Streaming)"].append(f"⚠️ CRÍTICO: Streaming exige muito do sistema simultaneamente. Com apenas {ram_gb}GB, seu PC sofrerá travamentos catastróficos.")

    if not tem_dedicada:
        dicas["Design e Edição"].append("⚠️ CRÍTICO: Softwares como Premiere, Photoshop e AutoCAD dependem de aceleração gráfica por hardware. O seu chip integrado causará uma lentidão absurda em renderizações.")
    if ram_gb < 16:
        dicas["Design e Edição"].append(f"⚠️ CRÍTICO: Edição de vídeo consome muita RAM para o 'preview'. Com {ram_gb}GB, edições além de 1080p básico serão um pesadelo técnico.")
    elif ram_gb < 32:
        dicas["Design e Edição"].append(f"💡 SUGESTÃO: Para fluxos de trabalho profissionais em 4K e 3D, os seus {ram_gb}GB ainda podem gargalar. A Bytebros recomenda fortemente o upgrade para 32GB de RAM.")

    if "day" in tempo_ligado or "days" in tempo_ligado:
        try:
            dias = int(tempo_ligado.split(" ")[0])
            if dias >= 5:
                aviso_tempo = f"⚠️ CRÍTICO: Esta máquina não é desligada corretamente há {dias} dias! Apenas abaixar a tampa (hibernar) acumula lixo na memória RAM (Memory Leak), causando lentidão. A Bytebros.TI exige a reinicialização imediata (Iniciar > Ligar/Desligar > Reiniciar)."
                for perfil in dicas:
                    dicas[perfil].insert(0, aviso_tempo)
        except:
            pass

    for perfil in dicas:
        if not dicas[perfil]:
            dicas[perfil].append("✅ PERFEITO: A máquina supera de forma robusta todas as especificações técnicas recomendadas pela Bytebros.")

    return dicas

def gerar_resumo(relatorio):
    ram_gb = relatorio.get("ram", {}).get("total_gb", 0)
    gpus = relatorio.get("video", {}).get("placas", [])
    cpu_nome = relatorio.get("cpu", {}).get("nome", "Processador Desconhecido")
    tempo_ligado = relatorio.get("sistema", {}).get("tempo_ligado", "")
    
    tem_dedicada = any(g.get("tipo") == "Dedicada" for g in gpus)
    
    alerta_uptime = ""
    if "day" in tempo_ligado or "days" in tempo_ligado:
        try:
            dias = int(tempo_ligado.split(" ")[0])
            if dias >= 5:
                alerta_uptime = f" ATENÇÃO: Constatou-se uma grave falha de uso, com a máquina ligada ininterruptamente há {dias} dias. Reinicie o sistema imediatamente para limpar o cache."
        except: pass

    if ram_gb >= 16 and tem_dedicada:
        perfil_pc = "de alta performance"
        limitacao = "O sistema está plenamente capacitado para lidar com cargas de trabalho intensas, edição e jogos modernos. Recomenda-se apenas a manutenção preventiva semestral."
    elif ram_gb >= 16 and not tem_dedicada:
        perfil_pc = "com excelente capacidade multitarefa"
        limitacao = "A ausência de aceleração gráfica dedicada (Placa de Vídeo) limita severamente seu uso para renderização 3D e jogos de última geração, mantendo seu foco em trabalho ágil."
    elif ram_gb < 16 and tem_dedicada:
        perfil_pc = "com bom potencial de processamento gráfico"
        limitacao = f"Contudo, a quantidade de memória atual ({ram_gb}GB) atua como um 'gargalo' severo. Um upgrade de RAM é crucial para liberar a performance real do processador e da placa de vídeo."
    else:
        perfil_pc = "focada em eficiência básica e tarefas leves"
        limitacao = f"Para garantir uma sobrevida útil aceitável e evitar lentidão diária, o upgrade de memória RAM é uma intervenção técnica indispensável."

    resumo = f"O equipamento analisado opera com uma arquitetura baseada no {cpu_nome} e {ram_gb}GB de memória instalada. Trata-se de uma estação {perfil_pc}. {limitacao}{alerta_uptime} A Bytebros.TI coloca-se à disposição para realizar a manutenção preventiva e os upgrades pontuados neste diagnóstico."
    
    return resumo