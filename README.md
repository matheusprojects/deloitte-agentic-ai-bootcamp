# 🤖 Deloitte Agentic AI Bootcamp — Portfolio & Labs

Repositório dedicado ao acompanhamento de evolução, implementação de arquiteturas agênticas e exercícios práticos desenvolvidos durante o **Bootcamp de IA Agêntica com Python da Deloitte** (Recife).

O objetivo principal deste repositório é documentar a construção de fluxos determinísticos, multi-agentes autônomos, chamadas de ferramentas (*tool calling*), orquestração de grafos cíclicos e observabilidade.

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.11+
- **Orquestração & Frameworks:** LangGraph, LangChain
- **Modelos:** qualquer provedor suportado por `init_chat_model`, configurado por `LLM_PROVIDER` e `LLM_MODEL` (atualmente OpenAI, via `langchain-openai`)
- **Observabilidade & Avaliação:** Langfuse
- **Gerenciamento de Ambiente:** `venv`, `pip`

---

## 🗂️ Estrutura do Projeto

```
deloitte-agentic-ai-bootcamp/
├── docs/                             # Enunciados dos exercícios (Markdown)
│   ├── exercicio-1-introdutorio 4.md
│   └── exercicio-2-completo.md
├── src/                              # Código da aplicação (pacote Python)
│   ├── app/                          # Ponto de entrada (CLI)
│   │   ├── app.py                    # main(): recebe a pergunta e executa o grafo
│   │   └── dados/                    # Dados de entrada da frota (JSON)
│   ├── graph/                        # Grafo LangGraph
│   │   ├── builder.py                # Monta e compila o grafo
│   │   ├── state.py                  # Estado compartilhado entre os nós
│   │   ├── routing.py                # Arestas condicionais
│   │   ├── tools.py                  # Ferramentas (tool calling)
│   │   ├── nodes/                    # Um diretório por nó (receive, prepare, classify,
│   │   │                             #   analyze, decide, human_review, answer_rules,
│   │   │                             #   refuse, format_output)
│   │   └── prompts/                  # Templates de prompt
│   └── utils/                        # Infraestrutura
│       ├── llm_adapter.py            # get_llm(): instancia o LLM a partir do .env
│       └── langfuse_client.py        # Callbacks e flush de observabilidade
├── .env.example                      # Modelo de variáveis de ambiente (sem valores)
├── .gitignore                        # Ignora ambientes, .env, caches e arquivos de IDE
├── requirements.txt                  # Dependências diretas, com versões fixadas
└── README.md                         # Esta documentação
```

Arquivos locais que **não** são versionados: `.env` (suas chaves) e `.venv/` (ambiente virtual).

---

## 📂 Trilha de Aprendizado & Desafios

| Módulo / Semana | Foco Principal | Projetos / Exercícios | Status |
| :--- | :--- | :--- | :---: |
| **Semana 1** | Fundamentos de Agentes, Grafos de Estado e LLM APIs | • Tomada de Decisão em Logística Portuária (LangGraph 3 nós)<br>• Validação e Estruturação de Prompts | Concluído |
| **Semana 2** | *Tool Calling*, Memória e Roteamento Condicional | • Roteadores de Intenção e Execução de Tarefas | Em andamento |
| **Semana 3** | Sistemas Multi-Agente & Colaboração | • Agentes Especialistas e Críticos de Decisão | A iniciar |
| **Semana 4** | Observabilidade, Tracing e Produção | • Integração com Langfuse e Métricas de Custo/Tokens | A iniciar |

Enunciados completos: [exercício 1 (introdutório)](docs/exercicio-1-introdutorio%204.md) e [exercício 2 (completo)](docs/exercicio-2-completo.md).

---

## 🚀 Como Executar Localmente

Pré-requisito: Python 3.11 ou superior.

### 1. Clonar o repositório

```bash
git clone https://github.com/matheusprojects/deloitte-agentic-ai-bootcamp.git
cd deloitte-agentic-ai-bootcamp
```

### 2. Criar o ambiente virtual

```bash
# Windows (PowerShell ou Git Bash)
python -m venv .venv
source .venv/Scripts/activate   # no PowerShell: .venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o `.env`

Copie o modelo e preencha com suas chaves:

```bash
# Windows (cmd)
copy .env.example .env

# Linux / macOS / Git Bash
cp .env.example .env
```

| Variável | Obrigatória | Descrição |
| :--- | :---: | :--- |
| `LLM_PROVIDER` | Sim | Provedor do modelo (ex.: `openai`) |
| `LLM_MODEL` | Sim | Nome do modelo (ex.: `gpt-4o-mini`) |
| `OPENAI_API_KEY` | Sim | Chave do provedor configurado |
| `OPENAI_BASE_URL` | Não | Endpoint alternativo compatível com a API da OpenAI |
| `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Não | Habilitam o tracing no Langfuse; sem elas, ele fica desativado |
| `LANGFUSE_HOST` | Não | Host do Langfuse (padrão: `https://cloud.langfuse.com`) |

---

## ▶️ Executar a Aplicação

Na raiz do projeto, com o ambiente virtual ativado:

```bash
python -m src.app.app
```

Use `-m`: os imports são feitos a partir de `src.` e não funcionam com `python src/app/app.py`.

O programa pede a pergunta (`Pergunta:`) e, no exercício 2, pode pausar para aprovação humana (`Aprovar? (s/n):`).
