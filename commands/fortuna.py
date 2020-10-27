import random


async def run(message, args, utilidad):
    await message.channel.send(random.choice(['Dejate de preguntar weas', 'Si es como lo veo, SÍ', 'Pregunta de nuevo más tarde', 'Es mejor que no te diga ahora', 'No lo puedo predecir ahora', 'Concentrate y pregunta de nuevo', 'No cuentes con ello', 'Es cierto', 'Es muy probable', 'No.', 'Sí']))


info = {
    "nombre": "fortuna",
    "des": "el bot adivinara tu fortuna",
    "uso": "fortuna [pregunta]"
}
