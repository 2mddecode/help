from vkbottle.bot import BotLabeler, Message
import loual
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["инвентарь", "инв"])
async def inventorySee(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    if user['inventory'] == []:
        return "Вот твой инвентарь:\n" \
               "Пусто"
    else:
        indexInventory = len(user['inventory'])
        inv = user['inventory']
        invCount = user['inventory_count']
        send = 'Вот твой инвентарь:\n'
        for i in range(0, indexInventory):
            send += f'"{inv[i]}" {invCount[i]} штук(и)\n'
        return f'{send}\n' \
               '\nПродать предметы можно командой:\n' \
               'инв продать {название} {количество}\n' \
               'Вместо пробела ставьте символ "_"'

@bl.message(text=["инвентарь продать <name> <count:int>", "инв продать <name> <count:int>"])
async def inventorySell(message: Message, name: str, count: int):
    await loual.prov(message.from_id)
    name = name.replace('_', ' ')
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    if user['inventory'] == []:
        return "У тебя инвентарь пуст, продавать нечего"
    else:
        if name not in user['inventory']:
            return "У тебя нет такого предмета"
        else:
            index = user['inventory'].index(name)
            if user['inventory_count'][index] < count:
                return f'У тебя не столько "{name}"'
            else:
                names = ["Оставленный пакет", "Заначка", "Чаевые", "Жвачка", "Дошик", "Заплесневелый хлеб", "Телефон", "Золотые часы", "Паспорт", "Ценные бумаги", "Ботинок", "Дырявый носок", "Кофта", "Ржавые крышки", "Паштет", "Гучи тапок", "Парик"]
                sellCount = [1_000, 100_000, 15_000, 1_500, 5_000, 100, 35_000, 5_000_000, 1_000_000, 20_000_000, 500, 150, 5_000, 15_000_000, 3_000, 2_000_000, 50_000]
                sIndex = names.index(name)
                sell = sellCount[sIndex]
                sell_sub = await loual.sub(sell * count)
                user['balance'] += sell * count
                user['inventory_count'][index] -= count
                if user['inventory_count'][index] <= 0:
                    user['inventory'].remove(name)
                    user['inventory_count'].remove(0)
                dirik = os.getcwd()
                with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f'Ты продал(а) "{name}" {count} штук(и) за {sell_sub}$'
