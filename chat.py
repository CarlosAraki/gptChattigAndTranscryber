import openai
import markdown
import sys
import emoji
import random
import os
from rich import print
# Obter todos os emojis conhecidos

historico = []

if os.path.exists('historico.txt'):
    with open('historico.txt', 'r') as arquivo:
        historico = arquivo.read().splitlines()

# Função para enviar uma solicitação para a API
def enviar_solicitacao(texto):
    historico.append(texto)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='\n'.join(historico),
        max_tokens=496,
        temperature=0.7,
        n=1
    )
    reply = response.choices[0].text.strip()
    # Check if the response exceeds the maximum token limit
    while response.choices[0].finish_reason == 'incomplete':
        continuation_token = response.choices[0].completion_token
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt='',
            max_tokens=496,
            n=1,
            continuation_token=continuation_token
        )
        #print("Computando ....   🚀 🛰️ ✈️  🛸 ")
        reply += response.choices[0].text.strip()
    historico.append(reply)
    return reply

# Laço de repetição para interação contínua
while True:
    # Obtenha a entrada do usuário
    user_input = input("Input 🚀🚀🚀-> : ")

    # Verifique se o usuário deseja sair
    if user_input.lower() == 'sair':
        break

    # Envie a solicitação para o modelo GPT
    reply = enviar_solicitacao(user_input)

    # Obtenha a resposta do modelo GPT
   
    print("GPT: \n" + reply + "\n")
    with open('historico.txt', 'w') as arquivo:
        arquivo.write('\n'.join(historico))

