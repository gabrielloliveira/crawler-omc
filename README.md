# Crawler-OhMyCode
- Crawler para pegar as últimas postagens do blog OhMyCode

# Requisitos:
- Python 3.6
- Database no Firebase

# Instalação:
- Clone o projeto ```git clone https://github.com/gabrielloliveira/crawler-omc.git```
- Entre na pasta crawler-omc com ```cd crawler-omc/```
- Crie um virtualenv com o comando ```python3.6 -m venv env```
- Ative o virtualenv: ```source env/bin/activate```
- Instale as dependências: ```pip install -r requeriments.txt```
- Adicione a url da aplicação firebase no arquivo ```spider.py```

# Execução:
- Rode a aranha. ```scrapy runspider spider.py```
- Veja no console do firebase os posts salvos.