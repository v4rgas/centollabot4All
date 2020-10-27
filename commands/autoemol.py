from discord.ext import tasks
from datetime import datetime
import pytz


async def run(message, args, utilidad):
    global task
    if message.author.guild_permissions.administrator:

        if args[0] == "stop":
            task.cancel()
            await message.channel.send('Autoemol has been chao :( sqrt(👀)')
        else:
            if not (args[0].isnumeric() and args[1].isnumeric()):
                await message.channel.send('Debes enviar el argumentowo de la hora')
            else:
                await message.channel.send(
                    'Los avisos de la sección economía del diario emol serán publicados '
                    'todos los dias a las '
                    f'{args[0]}:{args[1]} hrs '
                    'por este canal de discord 👀 x 👀 = 👀^2')

                @tasks.loop(minutes=0.5)
                async def task():
                    if not ('enviado' in vars() or 'enviado' in globals()):
                        global enviado
                        enviado = False

                    hora = datetime.now(pytz.timezone('Chile/Continental')).hour
                    minuto = datetime.now(pytz.timezone('Chile/Continental')).minute

                    if hora == int(args[0]) and minuto == int(args[1]) and not enviado:
                        await __import__('emol').run(message, args, utilidad)
                        enviado = True
                    if not (hora == int(args[0]) and minuto == int(args[1])):
                        enviado = False
                    print(enviado, hora, minuto, args[0], args[1])
                task.start()

    else:
        await message.channel.send('Solo los admin pueden ejecutar este comando, sin verguenza!')

info = {
    "nombre": "autoemol",
    "des": "avisa diariamente las noticias mas bacanes de la seccion de economia del emol, \
        a la hora que le digas!",
    "uso": "<prefijo>autoemol horas(0 a 23)/stop"
}
