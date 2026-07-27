# Código da Aplicação - Agente MBA

Esta pasta traz a orientação sobre o código da aplicação do **Agente MBA**.

A aplicação principal do projeto foi implementada na raiz do repositório em [`app.py`](../app.py) para facilidade de execução direta com o Streamlit.

## Estrutura do Código:

```text
dio-lab-bia-do-futuro/
├── app.py              # Interface Streamlit e integração com API do Ollama
├── requirements.txt    # Dependências do projeto (streamlit, ollama, requests, pandas)
└── data/               # Base de conhecimento carregada dinamicamente pelo app.py
```

## Como Rodar:

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar a aplicação
streamlit run app.py
```
