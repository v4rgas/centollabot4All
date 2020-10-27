async def run(message, args, utilidad):
    await message.channel.send('Pong!')
    if message.author.id == 557976603624341510:
        await message.channel.send(str(message))
        await message.channel.send(str(args))
        await message.channel.send(str(utilidad))


info = {
    "nombre": "ping",
    "des": "Pong!",
    "uso": "ping"
}
