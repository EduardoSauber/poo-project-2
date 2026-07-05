# Usar a imagem base do Python
FROM python:3.14-slim

# Definir o diretório de trabalho
WORKDIR /bmeta

# Instalar as bibliotecas necessárias
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expor a porta que o Bottle vai usar
EXPOSE 8080

# Comando para executar a aplicação
CMD ["python", "route.py"]

