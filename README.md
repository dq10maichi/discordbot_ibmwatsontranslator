# English and Japanese Translator Discord BOT

![tlanslatBOT](https://user-images.githubusercontent.com/13410462/60209336-609d9580-9895-11e9-86dd-8dbcbcf9f8e9.gif)

日本語と英語を相互翻訳するDiscord BOTです。言語の判定および翻訳エンジンとして、IBM Watson language translatorを使っています。

## requirements
- python3
- IBM Cloud Account and Watson language translator
## SETUP
### set Config.ini
[languageTranslator]
- apikey

set watson language translator APIKEY(SEE IBM Cloud Dashboard)

- watson_url

set watson URL(SEE IBM Cloud Dashboard)

- version

set watson version.(e.g. version = 2019-06-21)

[discord]
- token

set discode BOT token

### pip install before you run on local machine
```bash
$ pip install discord.py
$ pip install ibm_watson
```

## run on local machine
```bash
$ python discordbot.py
```

## Author
- Github: [dq10maichi](https://github.com/dq10maichi)

## License
This software is released under the MIT License.


