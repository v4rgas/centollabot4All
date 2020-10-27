import requests
URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url=URL)
data = r.json()
precio = data['bpi']['USD']['rate']


async def run(message, args, utilidad):
    await message.channel.send('El precio actual del bitcoin es: ' + precio + ' USD')

info = {
    "nombre": "bitcoin",
    "des": "el bot dira el precio del bitcoin en dolares",
    "uso": "bitcoin"
}
