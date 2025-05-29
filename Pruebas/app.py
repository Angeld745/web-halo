from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    log_connection()
    return send_from_directory('.', 'Principal.html')

# Para servir todos los archivos adicionales (CSS, imágenes, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    log_connection()
    return send_from_directory('.', filename)

# Para registrar quién se conecta
def log_connection():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    print(f"[Conexión] IP: {ip} | Navegador: {user_agent}")

if __name__ == '__main__':
    # 0.0.0.0 permite acceso desde otros dispositivos en tu red
    app.run(host='0.0.0.0', port=8000, debug=True)
