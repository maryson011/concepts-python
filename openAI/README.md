Poetry
 - é uma solução mais robusta do que o pip.
 - com pip eu tenho meu aambiente python para o ambiente global, e dentro a aplicação
 - a aplicação tem algunas dependencias, com pip, a instalação das dependencias será instaldo
 - na máquina, e não na aplicação apenas.
 - com o pip com vitual env, é criado um ambiente virtual na aplicação, para que fique isolado
 - essa abordagem de virtual env, embora funcione não é muito prática.
 - com o poetry, isso será feito de forma mais automatica.
 - ele atua como um gerenciador de dependencias mais robusta.
 - seria como um npm para python.
 - o pipx é uma versão do pip para utilização de ferramentas de linha de comando.

API de Chat
 - gpt 3.5, gpt 4
 - poetry new chatgpt-basico
 - cd chatgpt-basico
 - poetry shell
 - poetry add openai

 - cd ..
 - poetry new utils
 - cd utils
 - poetry shell
 - poetry add openai
 - poetry add python-dotenv
 - ---------
 - delete poetry.lock
 - pyproject.toml:
    [tool.poetry.dependencies]
    utils = {path="../utils", develop=true}
 - exit
 - cd chatgpt-basico
 - poetry shell
 - poetry install --no-root

 Moderação
  - poetry new moderacao
  - pyproject.toml -> utils = {path"../utils", develop=true}

Voz
 - poetry new voz
 - pyproject.toml -> utils = {path"../utils", develop=true}
 - poetry shell
 - poetry install --no-root

Chat Voz
 - poetry add pydub
 - poetry add sounddevice
 - poetry add soundfile
 - poetry add numpy

Modelos de Imagens
 - dalle3
 - poetry new imagens
 - poetry shell
 - poetry install --no-root
 - exit
 - cd ../utils
 - poetry shell
 - poetry add urllib3
 - deletar arquivo poetry.lock sempre que adicionar novas dependencias

 Embeddings
  - poetry add numpy
  - poetry add matplotlib

Fine tuning
 - permite alterar modelos da openai com dados propios
 - fell shot learning