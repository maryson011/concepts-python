from model.usuario import Usuario

usuario = Usuario('leonardo leitão', 'm@email.com')
print(usuario)
print(usuario.nome.primeiro_nome)
print(usuario.nome.ultimo_sobrenome)
print(usuario.nome.segundo_nome)