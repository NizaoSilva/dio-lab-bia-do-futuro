# 📊 Avaliação e Métricas do Agente MBA

Para garantir a qualidade, confiabilidade e utilidade das respostas geradas pelo Agente MBA, definimos a seguinte matriz de avaliação:

## Critérios de Avaliação

| Métrica | Objetivo | Forma de Medição | Meta |
|---------|----------|------------------|------|
| **Aderência ao Limite (Strict Adherence)** | Garantir que o agente respondeu exatamente o que foi pedido sem divagações. | Inspeção visual / Teste com prompts contendo restrições. | 100% de conformidade. |
| **Pragmatismo do Plano de Ação** | Avaliar se as etapas propostas são exequíveis e claras. | Avaliação pelo próprio usuário (Engenheiro/Cientista de Dados). | Média >= 4/5. |
| **Assertividade de Skills** | Verificar se os conhecimentos indicados correspondem às tecnologias reais do mercado de Data Science. | Comparação com a matriz de vagas. | 90%+ de relevância. |
| **Desempenho Local (Latência)** | Tempo de resposta do Ollama rodando offline na máquina local. | Medição em segundos por geração de resposta. | < 15 segundos (dependendo do hardware e modelo). |

## Histórico de Testes

- **Teste 1:** Pedido de plano para prestação de serviço de automação em Python para escritório de Engenharia.
  - *Resultado:* Resposta gerada em 4 seções estruturadas, respeitando o formato e indicando bibliotecas reais (`pandas`, `openpyxl`).