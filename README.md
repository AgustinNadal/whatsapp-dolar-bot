# 💬 WhatsApp Currency Bot (Dólar y Monedas)

Bot de WhatsApp en Python que permite consultar la cotización del dólar (en todas sus variantes) y de otras monedas extranjeras (euro, real, peso chileno, etc.) en tiempo real. Utiliza la API pública de [dolarapi.com](https://dolarapi.com) y se conecta mediante la API de WhatsApp de Twilio.

---

## 🚀 Características

- Consulta por texto libre como "¿Cuánto está el dólar blue?"
- Soporta todos los tipos de dólar (oficial, blue, tarjeta, bolsa, CCL, etc.)
- Soporta monedas extranjeras como euro, real, peso chileno, uruguayo, etc.
- Comandos especiales para ver todos los valores de una vez
- Desarrollado en Flask y listo para desplegar en Replit o Render

---

## 💻 Requisitos

- Python 3.10+
- Cuenta de Twilio con sandbox de WhatsApp habilitado
- (Opcional) Cuenta de Replit o Render para desplegar online

---

## 📂 Estructura del Proyecto

```
.
├── main.py               # Servidor Flask principal
├── utils.py              # Funciones para consultar cotizaciones
├── .env                  # Variables de entorno (no subir a GitHub)
├── requirements.txt      # Dependencias del proyecto
├── Procfile              # Para despliegue en Render
└── README.md             # Este archivo
```

---

## ⚙️ Instalación

1. Cloná el proyecto:

```bash
git clone https://github.com/tu_usuario/whatsapp-currency-bot.git
cd whatsapp-currency-bot
```

2. Instalá dependencias:

```bash
pip install -r requirements.txt
```

3. Configurá el archivo `.env`:

```env
PORT=5000
```

4. Corré el servidor:

```bash
python main.py
```

5. Si estás en local, exponé el servidor con [ngrok](https://ngrok.com/):

```bash
ngrok http 5000
```

6. Pegá la URL pública en el webhook de Twilio:
```
https://xxxxxx.ngrok.io/webhook
```

---

## 💬 Comandos Soportados

### 🟦 Dólares

- `dólar blue`, `blue`
- `dólar oficial`, `oficial`
- `dólar tarjeta`, `tarjeta`
- `dólar bolsa`, `mep`, `bolsa`
- `dólar contado`, `ccl`, `contado con liqui`
- `dólar mayorista`, `mayorista`
- `dólar cripto`, `cripto`

### 🌍 Monedas Extranjeras

- `euro`
- `real`
- `peso chileno`, `chileno`
- `peso uruguayo`, `uruguayo`

### 🔄 Comandos globales

- `todos los dólares` → muestra todos los tipos de dólar
- `todas las monedas` → muestra todas las monedas extranjeras

---

## 🛠️ Tecnologías

- Python + Flask
- Twilio API (WhatsApp)
- [dolarapi.com](https://dolarapi.com/)
- Replit / Render (opcional para hosting)

---

## 📄 Licencia

MIT License - Agustín Nadal - 2025
