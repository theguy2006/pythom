import time, requests

TELEGRAM_TOKEN = "9107304608:AAGh8__Ab8ubK6tRVN0geYI44rCYpA4twzk"
CHAT_ID = "@seu_canal"
ML_TOKEN = "ACCESS_TOKEN_DO_MERCADO_LIVRE"

def buscar_produtos(termo, limite=5):
    r = requests.get(
        "https://meli.la/2UAqYcN",
        params={"q": termo, "limit": limite},
        headers={"Authorization": f"Bearer {ML_TOKEN}"},
        timeout=15,
    )
    r.raise_for_status()
    return r.json()["results"]

def enviar(texto):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": texto},
        timeout=15,
    )

enviados = set()  # evita repetir produto

while True:
    for p in buscar_produtos("fone bluetooth"):
        if p["id"] not in enviados:
            enviados.add(p["id"])
            enviar(f"{p['title']}\nR$ {p['price']}\n{p['permalink']}")
            time.sleep(3)
    time.sleep(3600)  # espera 1 hora