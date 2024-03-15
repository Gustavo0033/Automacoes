import openai


chaveAPI = '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'
openai.api_key = chaveAPI



def enviarConversa(mensagem,listaMensagem=[]):
    listaMensagem.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt="Conversa iniciada:\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in listaMensagem])
    )
    return resposta.choices[0].message["content"]


listaMensagem = []
while True:
    texto = input("Digite sua mensagem: ")
    if texto  == 'sair':
        break
    else:
        resposta = enviarConversa(texto, listaMensagem)
        listaMensagem.append({"role": "user", "content": resposta})
        print("Chatbot:", resposta)
