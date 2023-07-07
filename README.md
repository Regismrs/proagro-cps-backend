# Proagro - CPS (Backend)
## Comunicação de Perda Simplificada (CPS)
A Comunicação de perda simplificada foi criada para gerenciar de forma eficiente todo o fluxo de comunicação de perdas, otimizando essa etapa fundamental no processo de solicitação do benefício do Proagro para os produtores rurais.

Este repositório é destinado a parte **backend** do projeto. Para mais informações da aplicação Frontend desenvolvida com TypeScript/Angular confira o repositório [proagro-cps-frontend](http://google.com).

## Detalhes do projeto
O **backend** da solução CPS é desenvolvida em Python, utilizando o Django Rest Framework para criar uma API robusta, escalável e de fácil manutenção, garantindo a segurança e a confiabilidade dos dados. Mais detalhes sobre a api e exenplos de uso podem ser obtidos em [apiary.com](http://apiary.com).

# Instalação

### Clonando o repositório
```
git clone https://github.com/Regismrs/proagro-cps-backend
```

## Instalando dependências
```terminal
cd proagro-cps-backend
python -m venv venv
cd venv\scripts
activate
cd ..\..
pip install -r requeriments.txt
```
## Configurando o ambiente
Configure o arquivo **exemplo.env** de acordo com as suas variáveis de ambiente para conexão com o DB e renomeie-o apenas para "**.env**".
Os testes foram realizados com PostgreSql, outros bancos de dados podem exigir configurações adicionais.

### Criando as tabelas
```shell
pyhton manage.py makemigrations
python manage.py migrate
```
### Criando um admin
Execute o comando abixo e depois escolha o nome de usuário e senha que serão utilizados para gerenciar o DRF.
```shell
python manage.py createsuperuser
```
Configure o arquivo **settings.py** de acordo com a sua realidade em relação as urls que terão acesso permitido aos endpoints da api.

**settings.py**
```python
...
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
...
CORS_ORIGIN_WHITELIST = ["http://localhost:4200"]
```
## Execute a aplicação
```python
python manage.py runserver
```
Como admin, usando o usuário e senha criados anteriormente, você pode acessar a rest api no link [http://localhost:8000/admin](http://localhost:8000/admin)
## Testando a API
>Para mais informações sobre os endpoints e utilização da api aconselhamos que consulte a documentação disponível em [https://apiary.io/orgacps](http://google.com)

Localmente você pode testar os endpoints no endereço [http://localhost:8000/comunicados/](http://localhost:8000/comunicados/)