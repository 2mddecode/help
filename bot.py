import time
ts = time.time()
import json
import os
from os.path import join
from vkbottle import Bot
from routes import labelers
TEXT = {}
TEXT.update({"text": "Создатель бота: [id216110960|Илья]\n"})
TEXT['text'] += "Псевдоним: 2md\'decode\n"
TEXT['text'] += "Имя бота: North Fade\n"
TEXT['text'] += "Версия бота: Release 1.0.2\n"
TEXT['text'] += "Авторские права: 2md\'decode&Co"
os.system('rm -Rf info.json')
dirik = os.getcwd()
with open(join(dirik, "info.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(TEXT, ensure_ascii=False, indent=2))

token = c587ff882a1a0ed24231e1ae24c7dbaa321d6ff6dd48f1dffa652cd9983074e0c455e8e685104fa07dc7b 
bot = Bot(token=token)
bot.labeler.vbml_ignore_case = True

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

te = time.time()
time = round(te - ts, 2)
print(f"INFO: Я включился за {time}с.")

bot.run_forever()
