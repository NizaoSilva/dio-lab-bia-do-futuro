# 💼 Agente MBA - Documentação e Escopo

## 1. Caso de Uso
O **Agente MBA (Copiloto de Negócios e Aprendizado)** foi concebido para atender profissionais e estudantes (com foco em Engenharia Civil e Ciência/Engenharia de Dados) que necessitam de:
- **Processamento e Síntese de Texto:** Leitura analítica de estudos de caso, artigos ou ideias brutas de projetos.
- **Identificação de Oportunidades:** Transforma teoria em oportunidades reais de monetização e prestação de serviços (freelances, consultorias de BI, automações PropTech).
- **Mapeamento Just-in-Time de Skills:** Identifica exatamente o que precisa ser aprendido (SQL, Python, LLMs, Streamlit) para executar a oportunidade.
- **Planos de Ação Pragmáticos:** Gera planos passo a passo estruturados.

## 2. Persona e Tom de Voz
- **Nome:** Agente MBA
- **Perfil:** Mentor e analista executivo de negócios altamente pragmático.
- **Tom de Voz:** Direto, estruturado, encorajador e livre de jargão desnecessário.
- **Linguagem:** Português do Brasil.

## 3. Arquitetura da Solução
```mermaid
flowchart TD
    A[Usuário] -->|Texto / Pedido| B[Interface Streamlit app.py]
    B -->|System Prompt + Contexto| C[Ollama - LLM Local]
    D[Base de Conhecimento JSON] -->|Injeção no Contexto| B
    C -->|Plano Estruturado| B
    B -->|Resposta em Chat| A
```

## 4. Diretrizes de Segurança e Anti-Alucinação
- **Limites Estritos:** O agente responde exclusivamente o que lhe foi pedido, sem divagações.
- **Fontes Locais:** Utiliza os arquivos da pasta `data/` como âncora de conhecimento para precificação e competências.
- **Aviso de Isenção:** Não emite pareceres jurídicos, fiscais ou financeiros definitivos sem sinalizar a necessidade de validação.