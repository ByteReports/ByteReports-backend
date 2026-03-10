# 🖥️ ByteReports

Um aplicativo modular em Python projetado para ler informações detalhadas de hardware em computadores Windows e gerar relatórios simples, explicativos e úteis para usuários leigos.

## 🚀 Funcionalidades

* **Leitura Profunda:** Utiliza o WMI do Windows para acessar dados que bibliotecas comuns não conseguem (como pentes físicos de RAM e versão da BIOS).
* **Arquitetura Modular:** O back-end é dividido em módulos (`cpu.py`, `ram.py`, `gpu.py`, etc.), permitindo que o front-end solicite apenas os dados necessários.

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Bibliotecas principais: `wmi`, `psutil`, `py-cpuinfo`, `gputil`

## ⚙️ Como Instalar e Rodar (Windows)

1. Clone este repositório para a sua máquina:
```bash
git clone https://github.com/ByteReports/ByteReports-backend.git
cd ByteReports-backend