# Gerenciamento de tarefas ( Python )

## Descrição

API para controle de tarefas com sistema de login por usuário 

## Ferramentas utilizadas

- Flask
- SQLite ( db local )
- JWT

## Como instalar?

```bash
1. sudo
2. pip install -r requirements.txt # install pythom modules
3. flask run --host=0.0.0.0 --port=80 # execute server
```


# Rotas 

> Documentação para testes :D
## Autenticação

**Cadastro de usuário**

> [ POST ] http://144.126.213.60/auth/register

-> Exemplo de body
```json
{
  "username": "alandev"
}
```

**Autenticar usuário**

> [ POST ] http://144.126.213.60/auth/login

-> Exemplo de body
```json
{
  "username": "alandev"
}
```

-> Exemplo de resposta
```json
{
  "token": "adiwjdiajida..."
}

```

## Rotas autenticadas ( Gerenciar tarefas / Perfil do usuário)

> Necessário passar token JWT de acesso. 

**Puxar informações completa do usuário**

> [ GET ] http://144.126.213.60/profile

**Criar tarefa**

> [ POST ] http://144.126.213.60/tasks

-> Exemplo de body
```json
{
	"title": "title",
	"description": "desc",
	"status": "status"
}
```

**Editar tarefa**

> [ PUT ] http://144.126.213.60/tasks/{task_id}

-> Exemplo de body
```json
{
	"title": "title",
	"description": "desc",
	"status": "status"
}
```

**Deletar tarefa**

> [ DELETE ] http://144.126.213.60/tasks/{task_id}

**Listar tarefas**

> [ GET ] http://144.126.213.60/tasks

**Consultar tarefa especifica**
> [ GET ] http://144.126.213.60/tasks/{task_id}
