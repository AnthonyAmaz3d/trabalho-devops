from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Aqui criamos uma página HTML estilizada direto no Python
    html_page = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trabalho de DevOps</title>
        <style>
            body {
                background-color: #1a1a2e;
                color: #eaeaea;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #16213e;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                text-align: center;
                border-top: 5px solid #0f3460;
                max-width: 500px;
            }
            h1 {
                color: #e94560;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2rem;
                color: #a2a2bd;
                line-height: 1.5;
            }
            .badge {
                display: inline-block;
                background-color: #e94560;
                color: white;
                padding: 8px 20px;
                border-radius: 25px;
                font-size: 1rem;
                margin-top: 25px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            .emoji {
                font-size: 3rem;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="emoji">🐳🚀</div>
            <h1>Olá, Professor!</h1>
            <p>Missão DevOps concluída com sucesso!</p>
            <div class="badge">CI/CD + Docker</div>
        </div>
    </body>
    </html>
    """
    return html_page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Linguagem 1 teste
# Linguagem 2 teste
# Linguagem 3 teste
# Linguagem 4 teste