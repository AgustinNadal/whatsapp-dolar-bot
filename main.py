# main.py

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os

from utils import obtener_cotizacion

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    mensaje_usuario = request.values.get("Body", "").lower().strip()
    respuesta = MessagingResponse()

    if not mensaje_usuario:
        respuesta.message("❌ No entendí tu mensaje. Escribí algo como 'dólar blue' o 'euro'.")
        return str(respuesta)

    try:
        texto_respuesta = obtener_cotizacion(mensaje_usuario)
        respuesta.message(texto_respuesta)
    except Exception as e:
        print(f"[ERROR] {e}")
        respuesta.message("⚠️ Ocurrió un error al procesar tu solicitud. Intentalo de nuevo más tarde.")

    return str(respuesta)

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
