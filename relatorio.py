from agente import AgenteEDA

def gerar_relatorio_para_pdf():
    """
    Executa um conjunto de perguntas e gera um texto formatado
    para ser copiado para o relatório em PDF.
    """
    agente = AgenteEDA()
    caminho_csv = 'dados/Kaggle - Credit Card Fraud.csv'
    agente.carregar_dados(caminho_csv)

    perguntas = [
        "Quais são os tipos de dados?",
        "Qual o intervalo da variável Amount?",
        "Qual a distribuição da variável Amount?",
        "Existe correlação entre as variáveis?",
        "Quais as conclusões que você obteve?"
    ]

    print("--- INÍCIO DO CONTEÚDO PARA O RELATÓRIO PDF ---")
    print("\n## Perguntas e Respostas Geradas pelo Agente\n")

    for i, pergunta in enumerate(perguntas, 1):
        print(f"### Pergunta {i}: {pergunta}\n")
        resposta = agente.analisar_pergunta(pergunta)
        print("**Resposta do Agente:**\n")
        print(f"```\n{resposta}\n```\n")
        if "gráfico salvo" in resposta:
            nome_arquivo_grafico = resposta.split("'")[1]
            print(f"![Gráfico da Pergunta {i}]({nome_arquivo_grafico})\n")

    print("--- FIM DO CONTEÚDO PARA O RELATÓRIO PDF ---")

if __name__ == '__main__':
    gerar_relatorio_para_pdf()