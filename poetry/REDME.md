Nov 14 22:00
Estudando Pacotes e Ambientes com Poetry

 - A ideia é fazer gerenciamento de pacotes

Roteiro

Pacotes
 - Uma historia, uma odisseia
 *  uma pasta onde temos varios códigos dentro
 *  tudo que trazemos de fora da API padrão do python
 *  Workflow dos pacotes
    *   virtualenv
        python -m venv ./venv
        source ./venv/bin/activate
    *   PyPI (onde estão essas bibliotecas)
        pacote A
        pacote B
        pacote C
    *   pip trás esses pacotes para mim
        pip install pacote
        - ele vai lá no PyPI e pega esses pacotes pra mim
        - requirements.txt
 *  Build
    *   seu código --> build --> pacote
    setup.py
    *   meta dados sobre o projeto
    *   setuptools

        maryson@maryson:~/python/concepts-python/poetry$ mkdir meu_pacote
        maryson@maryson:~/python/concepts-python/poetry$ touch setup.py
        maryson@maryson:~/python/concepts-python/poetry$ touch meu_pacote/minha_lib.py
        maryson@maryson:~/python/concepts-python/poetry$ python setup.py build
        running build
        running build_py
        creating build/lib/meu_pacote
        copying meu_pacote/minha_lib.py -> build/lib/meu_pacote
        maryson@maryson:~/python/concepts-python/poetry$ python -m venv ./venv
        maryson@maryson:~/python/concepts-python/poetry$ source ./venv/bin/activate
        (venv) maryson@maryson:~/python/concepts-python/poetry$ pip3 install wheel
        

        (venv) maryson@maryson:~/python/concepts-python/poetry$ pip3 install setuptools
        
        (venv) maryson@maryson:~/python/concepts-python/poetry$ python setup.py sdist bdist_wheel
        
        (venv) maryson@maryson:~/python/concepts-python/poetry$ pip3 install twine
        
        (venv) maryson@maryson:~/python/concepts-python/poetry$ twine upload dist/*

    *   No final das contas utilizamos varias ferramentas para criar um pacote aqui
    *   pyproject.toml
        - arquivo para consolidar as definições do projeto
    

Projeto
 - Conhecendo o poetry
    * 2018
    * builds independentes
    * faz todo o esquema junto. Digo, tudo o que era feito anteriormente
    23:08
    - poetry new bagulho
    - poetry shell
    - poetry install
    - poetry show
    - poetry show --tree
    - poetry add httpx
    - poetry add --dev pytest-asyncio
    - poetry remove --dev pytest-asyncio
    - poetry build
    - poetry publish (PyPI)
Pacote
 - Empacotando nossa aplicação
Distribuição
 - Distribuindo a aplicação