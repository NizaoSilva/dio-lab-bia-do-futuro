# Base de Conhecimento

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Estruture a documentação da base de conhecimento do Agente MBA, listando os arquivos JSON de dados mockados (oportunidades em Ciência de Dados, Engenharia e Cibersegurança, e os frameworks de negócios NIST/OWASP/Lean MVP). Preencha o template oficial.

---

## Dados Utilizados

A base de conhecimento do Agente MBA foi construída na pasta `data/` usando o formato JSON para garantir fácil carregamento e consumo dinâmico pela aplicação local em Streamlit.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `oportunidades_data_science.json` | JSON | Alimenta o agente com o perfil do usuário (Engenharia Civil -> Ciência de Dados/Cibersegurança) e categorias de projetos monetizáveis (PropTech, SecOps & LGPD, BI para PMEs, IA Local). |
| `frameworks_negocios.json` | JSON | Fornece frameworks estratégicos (NIST CSF, OWASP Top 10 para LLMs, SWOT, Lean MVP) e faixas de precificação de serviços de mercado para embasar os planos de ação. |

> [!TIP]
> **Quer um dataset mais robusto?** Além dos dados locais em JSON, você pode integrar dados públicos do [Hugging Face](https://huggingface.co/datasets) ou relatórios de vulnerabilidade (CVEs/NVD) e vagas em data/cybersecurity para expandir o conhecimento do agente.

---

## Adaptações nos Dados

Os dados originais do repositório base foram adaptados para refletir a proposta do **Agente MBA**:
1. **`oportunidades_data_science.json`:** Substituiu os dados fictícios de investimentos de varejo por categorias reais de serviços em Engenharia de Dados, Ciência de Dados, Cibersegurança e Automação de Processos.
2. **`frameworks_negocios.json`:** Incorporou normas corporativas de Cibersegurança (NIST, ISO 27001 e OWASP para LLMs) e faixas orientativas de precificação de consultorias de dados e segurança (R$ 800 a R$ 15.000).
