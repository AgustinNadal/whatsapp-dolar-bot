# utils.py

import requests

API_BASE_URL = "https://dolarapi.com/v1"

# Mapeo de términos comunes a nombres de endpoint
MAPEO_MONEDAS = {
    "dólar oficial": "dolares/oficial",
    "dolar oficial": "dolares/oficial",
    "oficial": "dolares/oficial",

    "dólar blue": "dolares/blue",
    "dolar blue": "dolares/blue",
    "blue": "dolares/blue",

    "dólar bolsa": "dolares/bolsa",
    "dolar bolsa": "dolares/bolsa",
    "bolsa": "dolares/bolsa",

    "contado con liqui": "dolares/contadoconliqui",
    "dolar CCL": "dolares/contadoconliqui",
    "dólar CCL": "dolares/contadoconliqui",
    "dolar ccl": "dolares/contadoconliqui",
    "dólar ccl": "dolares/contadoconliqui",
    "CCL": "dolares/contadoconliqui",
    "ccl": "dolares/contadoconliqui",

    "dolar tarjeta": "dolares/tarjeta",
    "dólar tarjeta": "dolares/tarjeta",
    "tarjeta": "dolares/tarjeta",

    "dolar mayorista": "dolares/mayorista",
    "dólar mayorista": "dolares/mayorista",
    "mayorista": "dolares/mayorista",

    "dólar cripto": "dolares/cripto",
    "dolar cripto": "dolares/cripto",
    "cripto": "dolares/cripto",
    
    
    "euro": "cotizaciones/eur",

    "real": "cotizaciones/brl",

    "peso chileno": "cotizaciones/clp",
    "chileno": "cotizaciones/clp",

    "peso uruguayo": "cotizaciones/uyu",
    "uruguayo": "cotizaciones/uyu",
}

def obtener_cotizacion(texto_usuario):
    texto_usuario = texto_usuario.lower()

    # 👉 Mostrar todos los tipos de dólar
    if "todos los dólares" in texto_usuario or "todos los dolares" in texto_usuario or "ver dolares" in texto_usuario:
        return obtener_todos_los_dolares()

    # 👉 Mostrar todas las monedas extranjeras
    if "todas las monedas" in texto_usuario or "todas las cotizaciones" in texto_usuario or "ver monedas" in texto_usuario:
        return obtener_todas_las_cotizaciones()

    # Buscar una moneda específica
    for clave, endpoint in MAPEO_MONEDAS.items():
        if clave in texto_usuario:
            url = f"{API_BASE_URL}/{endpoint}"
            response = requests.get(url)

            if response.status_code != 200:
                raise Exception("Error al consultar la API")

            data = response.json()
            compra = data.get("compra")
            venta = data.get("venta")
            moneda = clave.title()

            return f"💱 {moneda}:\nCompra: ${compra}\nVenta: ${venta}"

    return "❓ No entendí qué cotización querés consultar. Escribí 'dólar blue', 'euro', o 'todas las monedas'."


def obtener_todos_los_dolares():
    url = f"{API_BASE_URL}/dolares"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error al consultar la API de dólares")

    data = response.json()
    mensaje = "💵 Cotización de todos los tipos de DÓLAR:\n\n"

    for d in data:
        tipo = d.get("nombre", "Desconocido").title()
        compra = d.get("compra", "N/A")
        venta = d.get("venta", "N/A")
        mensaje += f"🟦 {tipo}:\n  Compra: ${compra}\n  Venta: ${venta}\n\n"

    return mensaje.strip()


def obtener_todas_las_cotizaciones():
    url = f"{API_BASE_URL}/cotizaciones"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error al consultar la API de cotizaciones")

    data = response.json()
    mensaje = "🌐 Cotización de monedas extranjeras:\n\n"

    for m in data:
        moneda = m.get("moneda", "Desconocida").upper()
        simbolo = m.get("nombre", "")
        compra = m.get("compra", "N/A")
        venta = m.get("venta", "N/A")
        mensaje += f"💱 {moneda} ({simbolo}):\n  Compra: ${compra}\n  Venta: ${venta}\n\n"

    return mensaje.strip()
