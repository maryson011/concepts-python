from utils import cliente, arquivo

mensagem = input('O que você quer dizer no seu e-mail? ')

resposta = cliente.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{
        'role':'system',
        'content':'Você é um especialista em criação de e-mails corporativos e se preocupa em escrever e-mails de uma forma agradável e educada, passando uma mensagem de forma clara e respeitosa. Seu objetivo é transformar uma mensagem do usuário em um e-mail que este usuário possa enviar para um dos seus colegas de trabalho. Retorne apenas o texto do email e o assunto'
    },
    {
        'role':'user',
        'content':mensagem
    }
    ],
    n = 3
)

nome_arquivo_output = arquivo.formatar_caminho('email.txt')
with open(nome_arquivo_output, 'w') as arquivo:
    for opcao in resposta.choices:
        arquivo.write(f'{'='*50}\n')
        arquivo.write(opcao.message.content)
        arquivo.write(f'{'='*50}\n')

print(f'Os e-mails foram gerados. Cheque {nome_arquivo_output}')