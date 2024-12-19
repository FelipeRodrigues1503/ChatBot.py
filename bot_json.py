import json

# Carregar o arquivo JSON com os dados
def carregar_dados():
    with open("database.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def carregar_dados():
    with open("database.json", "r", encoding="utf-8") as file:
        dados = json.load(file)
        print("Dados carregados:", dados)  # Adicionado para verificar os dados carregados
        return dados

# Exibir perguntas predefinidas e obter a resposta correspondente
def exibir_opcoes_e_obter_resposta(dados):
    print("Escolha uma pergunta digitando o número correspondente:")
    
    # Exibir as perguntas numeradas
    opcoes = list(dados.keys())
    for i, pergunta in enumerate(opcoes, 1):
        print(f"{i}. {pergunta}")
    
    try:
        escolha = int(input("Digite o número da pergunta desejada: ").strip())
        if 1 <= escolha <= len(opcoes):
            pergunta_selecionada = opcoes[escolha - 1]
            resposta = dados[pergunta_selecionada]
            print(f"Bot: {resposta}")
        else:
            print("Opção inválida. Por favor, escolha um número válido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Chatbot principal
def chatbot():
    dados = carregar_dados()
    print("Olá! Sou seu assistente. Escolha uma das perguntas predefinidas ou digite 'sair' para encerrar.")
    
    while True:
        exibir_opcoes_e_obter_resposta(dados)
        
        # Perguntar ao usuário se deseja continuar ou sair
        continuar = input("Deseja fazer outra pergunta? (sim/não): ").strip().lower()
        if continuar not in ['sim', 's']:
            print("Bot: Até logo!")
            break

if __name__ == "__main__":
    chatbot()
