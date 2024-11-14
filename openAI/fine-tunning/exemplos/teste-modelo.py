from utils import cliente

resposta = cliente.chat.completions.create(
    model = 'ft:gpt-3.5-turbo-0125:personal:emoji:ATSfylKd',
    messages= [
        {
            'role': 'system',
            'content': 'Você é um assistente útil que responde os usuários apenas usando emojis. Porém, junto com a sua resposta, você também inclui uma legenda para que o usuário possa traduzir seus emojis. com o significado de cada emoji individualmente'
        },
        {
            'role': 'user',
            'content': 'O que é fuso horário'
        }
    ]
)

print(resposta.choices[0].message.content)