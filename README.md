# FISIOFLASH BACK-END 💻

Este repositório contém as informações necessárias para facilitar a instalação e utilização do back-end do sistema no seu ambiente de desenvolvimento. 

## 1. Sobre o projeto

- [x] Cadastrar e listar usuários (paciente ou fisioterapeuta);
- [x] Realizar autenticação de usuários;
- [x] Cadastrar  e listar Serviços;
- [x] Casdastrar e listar Casos Clínicos;

## 2. Principais tecnologias e ferramentas utilizadas e necessárias para o funcionamento do projeto ⚙📲

- Python, Django, PostgreSQL e Insomnia.

## 3. Instruções 📚 
 
### Clonando o repositório do projeto

  - git clone <endereço-do-repositório-do-github>
  - Abrir a pasta clonada

### Configurações

- Criar uma base de dados para o projeto (PostgreSQL).

- Configure o Databases dentro do arquivo settings.py de acordo com as informações do seu banco de dados. Ex.:
  
![Captura de tela 2024-10-14 153634](https://github.com/user-attachments/assets/17789cb9-19fc-4dd7-b145-1019b1fd5130)
 
## 4. Comandos básicos para utilização e execução do projeto

Para usar os comandos abaixo é necessário abrir o terminal de comando e navegar até a pasta do projeto.

Abra a pasta do projeto com o terminal de comando:

`
cd nome-do-repositorio
`

Executar o comando abaixo para instalar as dependências do projeto:

`
pip install -r requirements.txt
`

Após a instalação das dependências, aplique as migrações para criar as tabelas no banco de dados:

`
python manage.py migrate
`

Executar o comando abaixo para iniciar o projeto, caso você não esteja utilizando o pycharm:

`
python manage.py runserver
`

Para baixar atualizações do projeto (fazer o git pull, iniciar o projeto com as novas atualizações):

`
$ git pull
`

-------------------------------------------------------------------------------------------------------------------
  

  
