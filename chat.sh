#!/bin/bash

# Defina o seu token de API
TOKEN="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"


# Defina o prompt
PROMPT="Olá, como posso ajudar?"

# Enviar a solicitação para o modelo GPT
RESPONSE=$(curl -X POST -H "Content-Type: application/json" \
                -H "Authorization: Bearer $TOKEN" \
                -d '{
                      "prompt": "'"$PROMPT"'",
                      "max_tokens": 50,
                      "temperature": 0.7
                    }' \
                https://api.openai.com/v1/engines/davinci-codex/completions)

# Extrair a resposta do JSON
REPLY=$(echo "$RESPONSE" | jq -r '.choices[0].text')

# Imprimir a resposta
echo "$REPLY"

