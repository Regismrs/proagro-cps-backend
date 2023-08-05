# Proagro - CPS (Backend)
# 1.Introdução
## Comunicação de Perda Simplificada (CPS)
A Comunicação de perda simplificada foi criada para gerenciar de forma eficiente todo o fluxo de comunicação de perdas, otimizando essa etapa fundamental no processo de solicitação do benefício do Proagro para os produtores rurais.

Este repositório é destinado a parte **backend** do projeto. Para mais informações da aplicação Frontend desenvolvida com TypeScript/Angular confira o repositório [proagro-cps-frontend](https://github.com/Regismrs/proagro-cps-frontend).

## Detalhes do projeto
O **backend** da aplicação CPS é desenvolvido em Python, utilizando o Django Rest Framework, para criar uma API robusta, escalável e de fácil manutenção, garantindo a segurança e a confiabilidade dos dados. Mais detalhes sobre a api e exemplos de uso podem ser obtidos em [https://agrocps.docs.apiary.io/#](https://agrocps.docs.apiary.io/#).

# 2.Instalação

### Clonando o repositório
```
git clone https://github.com/Regismrs/proagro-cps-backend
```

## 2.1. Instalando dependências
```terminal
cd proagro-cps-backend
python -m venv venv
. venv/scripts/activate
pip install -r requeriments.txt
```
## 2.2. Configurando o ambiente (.env)
Configure o arquivo **exemplo.env** de acordo com as suas variáveis de ambiente para conexão com o DB e renomeie-o apenas para "**.env**".
Os testes foram realizados com PostgreSql, outros bancos de dados podem exigir configurações adicionais.

## 2.3. Criando as tabelas
```shell
pyhton manage.py makemigrations
python manage.py migrate
```
## 2.4. Criando um admin
Execute o comando abaixo e depois escolha o nome de usuário e senha que serão utilizados para gerenciar o DRF.
```shell
python manage.py createsuperuser
```
Configure o arquivo **settings.py** de acordo com as urls que terão acesso permitido aos endpoints da api.

**settings.py**
```python
...
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
...
CORS_ORIGIN_WHITELIST = ["http://localhost:4200"]
```
# 3. Execute a aplicação
```python
python manage.py runserver
```
Como admin, usando o usuário e senha criados anteriormente, você pode acessar a rest api localmente no link [http://localhost:8000/admin](http://localhost:8000/admin)
# 4. Testando a API
Localmente você pode testar os endpoints no endereço [http://localhost:8000/comunicados/](http://localhost:8000/comunicados/)

Para mais informações sobre os endpoints e utilização da api aconselhamos que consulte a documentação disponível em [https://agrocps.docs.apiary.io/#](https://agrocps.docs.apiary.io/#)

