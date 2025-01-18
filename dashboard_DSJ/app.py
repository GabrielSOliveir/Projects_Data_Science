import os
from flask import Flask, render_template

# Inicializando o app Flask
app = Flask(__name__)

# Rota principal (Página inicial)
@app.route('/')
def home():
    return render_template('index.html')  # Renderiza o arquivo index.html dentro da pasta templates

# Rota para debug (opcional)
@app.route('/debug')
def debug():
    # Lista os arquivos dentro da pasta templates (para verificar se o Flask encontra o index.html)
    templates_path = os.path.join(os.getcwd(), 'templates')
    files = os.listdir(templates_path)
    return f"Templates disponíveis: {files}"

# Execução do servidor
if __name__ == '__main__':
    app.run(debug=True)
