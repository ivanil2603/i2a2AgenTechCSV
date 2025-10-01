# 🤖 Agente de Análise de Dados com IA

Este projeto é uma solução de Análise Exploratória de Dados (E.D.A.) desenvolvida como parte da Atividade Obrigatória do Institut d'Intelligence Artificielle Appliquée (I2A2). [cite_start]O objetivo é fornecer uma ferramenta onde um usuário pode interagir com qualquer conjunto de dados em formato CSV, fazendo perguntas em linguagem natural e recebendo respostas analíticas, incluindo visualizações gráficas[cite: 18, 19, 20].

[cite_start]O agente foi projetado para ser genérico e autônomo, utilizando um Modelo de Linguagem (LLM) como seu mecanismo de raciocínio para interpretar as perguntas e executar as tarefas de análise necessárias[cite: 8, 61].

## ✨ Funcionalidades Principais

O agente é capaz de responder a uma ampla gama de perguntas analíticas, como:

* **Descrição dos Dados**:
    * [cite_start]Quais são os tipos de dados (numéricos, categóricos)? [cite: 23]
    * [cite_start]Qual a distribuição de cada variável (histogramas)? [cite: 24]
    * [cite_start]Qual o intervalo de valores (mínimo, máximo) de uma coluna? [cite: 25]
    * [cite_start]Quais são as medidas de tendência central (média, mediana)? [cite: 26]
* **Análise de Padrões e Relações**:
    * [cite_start]Existe correlação entre as variáveis? [cite: 43]
    * [cite_start]Quais são os valores mais frequentes? [cite: 31]
* [cite_start]**Geração de Gráficos**: O agente pode criar representações gráficas, como histogramas, para facilitar a visualização dos dados[cite: 20].
* [cite_start]**Conclusões**: O agente é capaz de resumir as conclusões obtidas a partir das análises que realizou[cite: 45].

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python
* **Interface Web**: Streamlit
* **Manipulação de Dados**: Pandas
* **Visualização de Dados**: Matplotlib & Seaborn
* **Framework de Agente IA**: LangChain
* **Modelo de Linguagem (LLM)**: OpenAI GPT-3.5-Turbo
* **Versionamento de Código**: Git & GitHub

## 🚀 Como Executar o Projeto

Para executar este agente em um ambiente local, siga os passos abaixo.

1.  **Clonar o Repositório**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

2.  **Criar e Ativar um Ambiente Virtual**
    ```bash
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instalar as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar a Chave de API**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave da OpenAI dentro dele, no seguinte formato:
    ```
    OPENAI_API_KEY="sk-..."
    ```

5.  **Executar a Aplicação**
    ```bash
    streamlit run app_streamlit.py
    ```
    A aplicação estará disponível em `http://localhost:8501`.

## 📖 Como Usar o Agente

1.  **Faça o Upload**: Na barra lateral, clique para fazer o upload de um arquivo CSV.
2.  **Aguarde**: Espere a mensagem "Agente pronto para uso!".
3.  **Interaja**: Use a caixa de chat na parte inferior da tela para fazer suas perguntas.

**Exemplos de Perguntas:**
* `Quantas linhas e colunas o arquivo tem?`
* `Gere os histogramas de todas as variáveis numéricas.`
* `Qual a média da coluna 'Amount'?`
* `Existe correlação entre as colunas?`