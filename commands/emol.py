import re
import requests
from bs4 import BeautifulSoup
import discord
from datetime import datetime
import pytz


def update():
    titulares = {}

    emol = requests.get('https://www.emol.com/economia/')
    soup = BeautifulSoup(emol.text, 'lxml')

    principal = soup.find(id='cuEconomia_cuNoticias_titularPrin')
    titulares[principal.string] = principal.get('href')

    for titulo in soup.find_all(id=re.compile
                                ('^cuEconomia_cuNoticias_repNoticiasCetral_titulo_\d+')):
        titulares[titulo.string] = titulo.get('href')
    return titulares


titulares = update()


async def run(message, args, utilidad):

    titulares = update()

    embed = discord.Embed(
        title=f"Noticias de hoy {datetime.now(pytz.timezone('Chile/Continental')).strftime('%d/%m/%Y a las %H:%M hrs')}",
        description="Lista de todas las noticias hasta ahora!", color=0x00ff00)
    for key in titulares:
        linki = f'https://www.emol.com{titulares[key]}'
        embed.add_field(name=key, value=f'[Link de la noticia]({linki})\n', inline=False)

    await message.channel.send(embed=embed)
    print(message.created_at)


info = {
    "nombre": "emol",
    "des": "titulares emol",
    "uso": "emol"
}
