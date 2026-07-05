# Projeto Final de Mercado E-Commerce (Mercadinho) (POO-2)

Este é um sistema de Mercadinho e-commerce desenvolvido em __Python__, focado nos conceitos de __Programação Orientada a Objetos (POO)__ e Persistência de Dados, construído em volta de um sistema website pelo __Bottle__.

Projeto baseado no modelo [BMVC](https://github.com/hgmachine/bmvc_start_from_this) desenvolvido pelo professor de Programação Orientada a Objetos (POO) Henrique G. de Moura, Universidade de Brasília (UnB).

---

## Estrutura de Pastas:

~~~
poo-project-2/
└── app/
    ├── controllers/
    │   └── data/
    ├── models/
    ├── static/
    │   ├── css/
    │   ├── img/
    │   └── js/
    └── views/
        └── html/
~~~


---

## Como executar o sistema:

###  1. BMVC pelo BASH/PowerShell/Cmd:

#### 1. Certifique-se de que tem o Python 3.x instalado na sua máquina:

```
python --version
```
Caso não tenha instalado, baixe-o pelo site oficial do [python.org](https://www.python.org/).

#### 2. Clone este repositório na sua máquina local:

```
git clone https://github.com/EduardoSauber/poo-project-2.git
```

#### 3. Acesse a pasta do projeto através do terminal:

```
cd poo-project-2
```

#### 4. Crie um Virtual Environment pelo terminal do seu sistema e ative-o:

```
python -m venv venv
```
Para ativar o "Virtual Environment" (venv), digite no seu terminal:

- Linux
```
source venv/bin/activate
```
- Windows
```
venv\Scripts\activate
```

#### 5. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

#### 6. Execute o arquívo "route.py":

```
python route.py
```
Caso tudo ocorra normalmente, o Bottle irá retornar um link.


### 2. BMVC pelo DOCKER

#### 1. Certifique-se de que tem o Docker instalado na sua máquina:

```
docker --version
```
Caso não tenha instalado, baixe e instale o [Docker Desktop](https://docs.docker.com/desktop/) (Windows/Linux) ou a [Docker Engine](https://docs.docker.com/engine/install) (Linux).

#### 2. Clone este repositório na sua máquina local:

```
git clone https://github.com/EduardoSauber/poo-project-2.git
```

#### 3. Acesse a pasta do projeto através do terminal:

```
cd poo-project-2
```

#### 4. Construa a imagem Docker do projeto:

```
docker build -t bmvc-app .
```
<small>Em sistemas Linux, digite "__sudo__" antes do comando do Docker.</small>

#### 5. Execute o contêiner:

- No Linux (Bash) ou Windows (PowerShell)
```
docker run --name bmvcapp -p 8080:8080 -v $(pwd):/bmeta bmvc-app
```
<small>Em sistemas Linux, digite "__sudo__" antes do comando do Docker.</small>

- No Windows (Cmd)
```
docker run --name bmvcapp -p 8080:8080 -v %cd%:/bmeta bmvc-app
```

---
