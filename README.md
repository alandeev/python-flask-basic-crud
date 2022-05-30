# Gerenciamento de tarefas ( Python )

## Descrição
API para controle de tarefas com sistema de login por usuário 

## Ferramentas utilizadas
- Flask
- SQLite ( db local )
- JWT

## Como instalar?
```bash
pip install -r requirements.txt

flask run
```


## Rotas 
> Documentação para testes local.
### Autenticação
**Cadastro de usuário**

> [ POST ] http://localhost:5000/auth/register

-> Exemplo de body
```json
{
  "username": "alandev"
}
```

**Autenticar usuário**

> [ POST ] http://localhost:5000/auth/login

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

### Rotas autenticadas ( Gerenciar tarefas / Perfil do usuário)
> Necessário passar token JWT de acesso. 

**Puxar informações completa do usuário**

> [ GET ] http://localhost:5000/users/profile

**Criar tarefa**

> [ POST ] http://localhost:5000/tasks

-> Exemplo de body
```json
{
	"title": "title",
	"description": "desc",
	"status": "status"
}
```

**Editar tarefa**

> [ PUT ] http://localhost:5000/tasks/{task_id}

-> Exemplo de body
```json
{
	"title": "title",
	"description": "desc",
	"status": "status"
}
```

**Deletar tarefa**

> [ DELETE ] http://localhost:5000/tasks/{task_id}

**Listar tarefas**

> [ GET ] http://localhost:5000/tasks

**Consultar tarefa especifica**
> [ GET ] http://localhost:5000/tasks/{task_id}