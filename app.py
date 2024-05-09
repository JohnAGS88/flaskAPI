import requests
from flask import Flask, request, jsonify



@app.route('/')
def hello():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


app = Flask(__name__)

# Almacenamiento temporal de usuarios (simulado)
users = {
    "portal": "BvPortal2024"
}

@app.route('/api/authorization/token', methods=['POST'])
def generate_token():
    # Obtener datos de la solicitud
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Verificar las credenciales del usuario
    if username in users and users[username] == password:
        # Generar tokens (solo simulado en este ejemplo)
        access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb3J0YWwtYWRtaW4iLCJpYXQiOjE3MTE1NzY3NDYsImV4cCI6MTcxMTU4Mzk0Nn0.CG8p9U91W19LgqjQT_44UsVokmia30GJjsM9cYjihKg"
        token_expire_in_minute = 120
        refresh_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb3J0YWwtYWRtaW4iLCJpYXQiOjE3MTE1NzY3NDYsImV4cCI6MTcxMTU4Mzk0Nn0.CG8p9U91W19LgqjQT_44UsVokmia30GJjsM9cYjihKg"
        refresh_token_expire_in_minute = 240

        # Construir la respuesta
        response = {
            "accessToken": access_token,
            "tokenExpireInMinute": token_expire_in_minute,
            "refreshToken": refresh_token,
            "refreshTokenExpireInMinute": refresh_token_expire_in_minute
        }
        
        # Retornar la respuesta
        return jsonify(response), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

if __name__ == '__main__':
    app.run(debug=True)




# Endpoint para generar token (simulado)
# token_endpoint = "http://tu_servidor/api/authorization/token"

# Endpoint para consultar tasa de cambio
tasa_endpoint = "http://172.17.0.2:5000/api/services/bank/tasa"

# Simulación de almacenamiento de token (se obtendría del endpoint de generación de token)
# access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb3J0YWwtYWRtaW4iLCJpYXQiOjE3MTE1NzY3NDYsImV4cCI6MTcxMTU4Mzk0Nn0.CG8p9U91W19LgqjQT_44UsVokmia30GJjsM9cYjihKg"

@app.route('/api/services/bank/tasa', methods=['GET'])
def get_tasa_de_cambio():
    # Verificar si se proporcionó el token en la solicitud
    if 'Authorization' not in request.headers:
        return jsonify({"error": "Token de autorización no proporcionado"}), 401

    # Obtener el token de autorización de los headers
    token = request.headers['Authorization']

    # Verificar la validez del token
    if token != f"Bearer {access_token}":
        return jsonify({"error": "Token de autorización inválido"}), 401

    # Hacer la solicitud GET al servidor externo para obtener la tasa de cambio
    response = requests.get(tasa_endpoint)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Procesar la respuesta y devolver los datos
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "No se pudo obtener la tasa de cambio"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)


# Simulación de almacenamiento de tokens
tokens = {}

@app.route('/api/authorization/refresh/token', methods=['POST'])
def refresh_token():
    # Obtener el refreshToken del cuerpo de la solicitud
    data = request.json
    refresh_token = data.get('refreshToken')

    # Verificar si el refreshToken está presente y válido
    if refresh_token in tokens:
        # Generar un nuevo accessToken (simulado)
        access_token = "nuevo_access_token_generado"
        token_expire_in_minute = 120
        # Actualizar el refreshToken (simulado)
        tokens[refresh_token]["accessToken"] = access_token
        tokens[refresh_token]["tokenExpireInMinute"] = token_expire_in_minute
        # Devolver la respuesta con el nuevo accessToken y refreshToken
        return jsonify(tokens[refresh_token]), 200
    else:
        return jsonify({"error": "Refresh token inválido"}), 401

if __name__ == '__main__':
    app.run(debug=True)   


# Endpoint para generar token (simulado)
# token_endpoint = "http://tu_servidor/api/authorization/token"

# Endpoint para enviar solicitud de formulario
# solicitud_endpoint = "http://tu_servidor/api/services/bank/pw-solicitudes"

# Simulación de almacenamiento de token (se obtendría del endpoint de generación de token)
# access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb3J0YWwtYWRtaW4iLCJpYXQiOjE3MTE1NzY3NDYsImV4cCI6MTcxMTU4Mzk0Nn0.CG8p9U91W19LgqjQT_44UsVokmia30GJjsM9cYjihKg"

@app.route('/api/services/bank/pw-solicitudes', methods=['POST'])
def enviar_solicitud():
    # Verificar si se proporcionó el token en la solicitud
    if 'Authorization' not in request.headers:
        return jsonify({"error": "Token de autorización no proporcionado"}), 401

    # Obtener el token de autorización de los headers
    token = request.headers['Authorization']

    # Verificar la validez del token
    if token != f"Bearer {access_token}":
        return jsonify({"error": "Token de autorización inválido"}), 401

    # Obtener los datos del formulario de la solicitud
    data = request.json

    # Hacer la solicitud POST al servidor externo para enviar el formulario de solicitud
    response = requests.post(solicitud_endpoint, json=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Procesar la respuesta y devolver los datos
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "No se pudo enviar el formulario de solicitud"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)




# Endpoint para generar token (simulado)
token_endpoint = "http://tu_servidor/api/authorization/token"

# Endpoint para enviar formulario de autorización de contacto
autorizacion_contacto_endpoint = "http://tu_servidor/api/services/bank/pw-autorizacion-contacto"

# Simulación de almacenamiento de token (se obtendría del endpoint de generación de token)
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwb3J0YWwtYWRtaW4iLCJpYXQiOjE3MTE1NzY3NDYsImV4cCI6MTcxMTU4Mzk0Nn0.CG8p9U91W19LgqjQT_44UsVokmia30GJjsM9cYjihKg"

@app.route('/api/services/bank/pw-autorizacion-contacto', methods=['POST'])
def autorizacion_contacto():
    # Verificar si se proporcionó el token en la solicitud
    if 'Authorization' not in request.headers:
        return jsonify({"error": "Token de autorización no proporcionado"}), 401

    # Obtener el token de autorización de los headers
    token = request.headers['Authorization']

    # Verificar la validez del token
    if token != f"Bearer {access_token}":
        return jsonify({"error": "Token de autorización inválido"}), 401

    # Obtener los datos del formulario de autorización de contacto
    data = request.json

    # Hacer la solicitud POST al servidor externo para enviar el formulario de autorización de contacto
    response = requests.post(autorizacion_contacto_endpoint, json=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Procesar la respuesta y devolver los datos
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "No se pudo enviar el formulario de autorización de contacto"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
