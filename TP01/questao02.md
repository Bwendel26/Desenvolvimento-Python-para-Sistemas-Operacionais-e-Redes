
# Sobre variáveis de ambiente, responda:<h1>

### O que são?<h3>

**R:** _São um atalho para o sistema do caminho do executável de um programa, normalmente processos comuns do sistema utilizam variáveis de ambiente, quando se vai utilizar o vscode para executar o código Python, ele busca nas variáveis de ambiente o Python instalado na máquina para usar como interpretador Python._
_São valores que podem ser nomeados dinamicamente ou manualmente no sistema, afetando o comportamento dos programas que as consomem._

###Como elas podem ser obtidas pelo módulo ‘os’ de Python?<h3>

**R:** _No módulo 'os' temos algumas funções como: 'getenv' e 'getenvb' que retornam a chave e valor da variável se ela existir._
_Outro método para retornar todas é com 'os.environ' ou 'os.environ'["path"], por exemplo, assim retornamos as variáveis de ambiente ou apenas uma parte delas se quisermos especificar._

**Exemplo de código:**
```python
import os

env = os.environ
print(env)

env_path = os.environ["path"]
print(env_path)
```

###Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?<h3>

**R:** __

