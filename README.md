# roit-bank-case

## Descrição do Case
Esse teste tem como intuito avaliar conhecimentos básicos, sendo que o principal objetivo é analisar o raciocínio lógico e a capacidade de solucionar problemas, mesmo 
que ainda desconhecidos pelo candidato.

1. O candidato deve montar uma solução utilizando arquitetura de
autoencoder capaz de limpar imagens disponibilizadas no dataset na
pasta 1.dirty que se encontram com diversos ruídos e retornar no padrão
em que se encontram na pasta 2. Cleaned document.

2. Montar uma API que seja capaz de receber uma imagem em base64 e
retornar a imagem limpa em base64 com seu respectivo OCR (Optical
Character Recognition) na resposta da API.

3. Guardar a imagem em base64 de entrada/saída em um banco de dados,
além de outras informações que o candidato julgar necessário.

4. Encapsular a aplicação utilizando Docker. Disponibilizar DockerFile.

5. Hospedar o código em um repositório do github utilizando conceitos de
Gitflow e Commit Semântico.

## Dataset
https://drive.google.com/file/d/1AnqFjRBOns6g3CaWi8nmDzEBdQLYyQ4N/view?usp=sharing

## Arquitetura
```
/models
    ConnectionFactory.py
    Images.py
main.py
requirements.txt
Dockerfile
```

```\models\ConnectionFactory.py``` : Classe que encapsula a criação de instâncias de conexões com o MongoDB;

```\models\Images.py``` : Classe que gerencia a inserção e manipulação das informações entre a aplicação e a base de dados;

```main.py``` : Arquivo principal da aplicação com as rotas da API;

```requirements.txt``` : Arquivo com as dependências da aplicação;

```Dockerfile``` : Arquivo de configuração do Docker;
