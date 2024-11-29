# Redis_Flask

Uma extensão simples para integração com Redis em aplicações Flask.

## Índice

- [Uso Básico](#uso-básico)
- [Configurações](#configurações)
- [API](#api)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Uso básico

Crie e configure sua aplicação Flask com a extensão:

```python

from flask import Flask
from redis_extension import Redis

app = Flask(__name__)

# Configurações do Redis
app.config["REDIS_HOST"] = "localhost"
app.config["REDIS_PORT"] = 6379
app.config["REDIS_DB"] = 0
app.config["REDIS_DECODE_RESPONSES"] = True

# Inicializando o Redis
redis = Redis(app)

@app.route("/")
def index():
    redis.hset("test", "key", "value")
    return redis.hgetall("test")

if __name__ == "__main__":
    app.run(debug=True)


```

## Configurações

| Parâmetro                       | Descrição                               | Valor Padrão |
| ------------------------------- | --------------------------------------- | ------------ |
| REDIS_HOST                      | Endereço Host Redis                     | `localhost`  |
| REDIS_PORT                      | Porta Redis                             | `6379`       |
| REDIS_DB                        | Banco de dados Redis                    | `0`          |
| REDIS_PASSWORD                  | Senha Redis                             | `None`       |
| REDIS_DECODE_RESPONSES          | Decodificar respostas Redis             | `False`      |
| REDIS_SOCKET_TIMEOUT            | Timeout de socket                       | `None`       |
| REDIS_SOCKET_CONNECT_TIMEOUT    | Timeout de conexão de socket            | `None`       |
| REDIS_SOCKET_KEEPALIVE          | Manter conexão ativa                    | `None`       |
| REDIS_SOCKET_KEEPALIVE_OPTIONS  | Opções de manter conexão ativa          | `None`       |
| REDIS_CONNECTION_POOL           | Pool de conexões                        | `None`       |
| REDIS_UNIX_SOCKET_PATH          | Caminho do socket Unix                  | `None`       |
| REDIS_ENCODING                  | Codificação                             | `utf-8`      |
| REDIS_ENCODING_ERRORS           | Erros de codificação                    | `strict`     |
| REDIS_RETRY_ON_TIMEOUT          | Retentar em timeout                     | `False`      |
| REDIS_RETRY_ON_ERROR            | Retentar em erro                        | `None`       |
| REDIS_SSL                       | Usar SSL                                | `False`      |
| REDIS_SSL_KEYFILE               | Arquivo de chave SSL                    | `None`       |
| REDIS_SSL_CERTFILE              | Arquivo de certificado SSL              | `None`       |
| REDIS_SSL_CERT_REQS             | Requisitos de certificado SSL           | `required`   |
| REDIS_SSL_CA_CERTS              | Certificados CA SSL                     | `None`       |
| REDIS_SSL_CA_PATH               | Caminho de certificados CA SSL          | `None`       |
| REDIS_SSL_CA_DATA               | Dados de certificados CA SSL            | `None`       |
| REDIS_SSL_CHECK_HOSTNAME        | Verificar nome de host SSL              | `False`      |
| REDIS_SSL_PASSWORD              | Senha SSL                               | `None`       |
| REDIS_SSL_VALIDATE_OCSP         | Validar OCSP                            | `False`      |
| REDIS_SSL_VALIDATE_OCSP_STAPLED | Validar OCSP STAPLED                    | `False`      |
| REDIS_SSL_OCSP_CONTEXT          | Contexto OCSP SSL                       | `None`       |
| REDIS_SSL_OCSP_EXPECTED_CERT    | Certificado OCSP esperado SSL           | `None`       |
| REDIS_SSL_MIN_VERSION           | Versão mínima SSL                       | `None`       |
| REDIS_SSL_CIPHERS               | Cifras SSL                              | `None`       |
| REDIS_MAX_CONNECTIONS           | Conexões máximas                        | `None`       |
| REDIS_SINGLE_CONNECTION_CLIENT  | Cliente de conexão única                | `False`      |
| REDIS_HEALTH_CHECK_INTERVAL     | Intervalo de verificação de integridade | `0`          |
| REDIS_CLIENT_NAME               | Nome do cliente                         | `None`       |
| REDIS_USERNAME                  | Nome de usuário                         | `None`       |
| REDIS_RETRY                     | Retentar                                | `None`       |
| REDIS_REDIS_CONNECT_FUNC        | Função de conexão Redis                 | `None`       |
| REDIS_PROTOCOL                  | Protocolo Redis                         | `2`          |
| REDIS_CREDENTIAL_PROVIDER       | Provedor de credenciais                 | `None`       |
| REDIS_CACHE                     | Cache                                   | `None`       |
| REDIS_CACHE_CONFIG              | Configuração do cache                   | `None`       |
