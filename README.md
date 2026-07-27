# 🎓 Agente MBA - Copiloto de Negócios e Aprendizado

> Agente de Inteligência Artificial Generativa local e offline (Streamlit + Ollama) projetado para processar textos, identificar oportunidades de monetização em Ciência/Engenharia de Dados e gerar planos de ação pragmáticos.

---

## 💡 O Que é o Agente MBA?

O **Agente MBA** é um assistente analítico focado em ponte entre teoria de dados/engenharia e **aplicação prática de mercado**. Ele analisa textos, artigos ou ideias de projetos e devolve um planejamento estruturado focado em geração de valor e renda.

### 🌟 Destaques do Projeto:
- ✅ **100% Local e Gratuito:** Executado no seu computador via [Ollama](https://ollama.com) (privacidade total dos dados).
- ✅ **Execução Estrita:** Responde exatamente o que foi solicitado, no formato estruturado desejado.
- ✅ **Interface Web Prática:** Desenvolvida em Streamlit com histórico de conversa e seleção de modelos locais.

---

## 🏗️ Arquitetura do Sistema

```mermaid
flowchart TD
    A[Usuário] -->|Texto / Artigo / Ideia| B[Streamlit app.py]
    B -->|System Prompt + Contexto| C[Ollama - LLM Local]
    D[Base de Conhecimento JSON] -->|Dados de Mercado| B
    C -->|Resposta Estruturada| B
    B -->|Plano de Ação| A
```

---

## 📁 Estrutura do Repositório

```text
├── app.py                         # Aplicação principal em Streamlit
├── requirements.txt               # Dependências Python (streamlit, ollama, requests)
├── data/                          # Base de conhecimento local
│   ├── oportunidades_data_science.json
│   └── frameworks_negocios.json
└── docs/                          # Documentação dos 6 passos do desafio
    ├── 01-documentacao-agente.md  # Escopo, persona e diretrizes
    ├── 02-base-conhecimento.md    # Estrutura dos dados de conhecimento
    ├── 03-prompts.md              # System Prompt e exemplos
    ├── 04-metricas.md             # Matriz de avaliação de qualidade
    └── 05-pitch.md                # Pitch do projeto
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos:
1. Python 3.10+ instalado.
2. [Ollama](https://ollama.com) instalado e em execução na máquina local.
3. Modelo baixado no Ollama (exemplo: `ollama run llama3.2`).

### Passo a Passo:

1. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Garantir que o Ollama está rodando:**
   ```bash
   ollama list
   ```

3. **Iniciar a aplicação Streamlit:**
   ```bash
   streamlit run app.py
   ```

4. Acesse no seu navegador: `http://localhost:8501`.
