<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>ERRO 404</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .conteudo {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .erro {
            color: red;  
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="conteudo">
        <h1 align="center">Opa! Espera um pouco...</h1>
        <p align="center">Parece que a página que você quer acessar não existe...</p>
        <div align="center">
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExczhiNHI5M2JoZm1nOWhscWYzNzdoc2dhaTlua3poajJjMHB5eTdzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eieBGj2bKVWYXH1tu4/giphy.gif">
        </div>
        <div class="erro"; align="center">
            <h2>{{erro}} - {{req_url}}</h2>
        </div>
    </div>
</body>
</html>