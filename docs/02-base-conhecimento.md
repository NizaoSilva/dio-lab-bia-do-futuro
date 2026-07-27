# 📚 Base de Conhecimento do Agente MBA

A base de conhecimento do Agente MBA está estruturada na pasta `data/` em arquivos padronizados JSON/CSV, permitindo fácil atualização e extensão.

## Estrutura de Arquivos

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `data/oportunidades_data_science.json` | JSON | Perfil do usuário (Engenharia Civil -> Ciência de Dados) e categorias de projetos monetizáveis (PropTech, BI para PMEs, IA Local). |
| `data/frameworks_negocios.json` | JSON | Metodologias de gestão (SWOT, Matriz de Viabilidade, Lean MVP) e médias de precificação de serviços no mercado nacional. |

## Como a Base é Utilizada pelo Agente

Ao iniciar a aplicação `app.py`, o conteúdo dos arquivos JSON é lido e injetado diretamente nas instruções de sistema (System Prompt) que alimentam o modelo local via Ollama. Isso garante que o agente responda considerando os nichos de atuação específicos do usuário.
