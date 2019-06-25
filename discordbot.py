import discord
import configparser
from ibm_watson import LanguageTranslatorV3 as LanguageTranslator

inifile = configparser.ConfigParser()
inifile.read('./config.ini','UTF-8')
version = inifile.get('languageTranslator','version')
watson_url = inifile.get('languageTranslator','watson_url')
apikey = inifile.get('languageTranslator','apikey')
token = inifile.get('discord','token')

client = discord.Client()
language_translator = LanguageTranslator(
    version = version,
    url = watson_url,
    iam_apikey = apikey
)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    text = message.content
    jsonstr = language_translator.identify(text).get_result()
    source = jsonstr['languages'][0]['language']
    if client.user != message.author:
        if source in 'ja':
            target = 'en'
            data = language_translator.translate(
                text=text,
                source=source,
                target=target).get_result()
            msg = data['translations'][0]['translation']
            msg = message.author.name + " (en)> " + msg
            await message.channel.send(msg)

        if source in 'en':
            target = 'ja'
            data = language_translator.translate(
                text=text,
                source=source,
                target=target).get_result()
            msg = data['translations'][0]['translation']
            msg = message.author.name + " (ja)> " + msg
            await message.channel.send(msg)

client.run(token)
