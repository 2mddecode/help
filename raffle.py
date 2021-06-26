from vkbottle.bot import BotLabeler, Message
import loual
import time
import json
import os
import random
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="+розыгрыш <type> <count:int> <cSub:int> <name>")
async def raffleNew(message: Message, type, count: int, cSub: int, name):
    await loual.prov(message.from_id)
    await loual.raffle()
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 5:
        raffle = json.load(open('raffles.json'))
        if type in ["баланс", "$"]:
            type = "баланс"
        elif type == "крышки":
            type = "Крышки"
        elif type in ["реп", "репутация"]:
            type = "реп"
        elif type == "вип":
            type = "вип"
        else: None
        raffle.update({name: {"ids": 0, "type": type, "count": count, "cSub": cSub}})
        dirik = os.getcwd()
        with open(join('raffles.json'), 'w') as f:
            f.write(json.dumps(raffle, ensure_ascii=False, indent=2))
        return f"Создал розыгрыш {name}\n" \
               f"Кол-во: {count}\n" \
               f"Тип: {type}"

@bl.message(text="розыгрыш +<name>")
async def raffleAdd(message: Message, name):
    await loual.prov(message.from_id)
    await loual.raffle()
    raffle = json.load(open('raffles.json'))
    try:
        d = raffle[name]
    except:
        return "Такого розыгрыша нету"
    for i in range(len(raffle[name])):
        try:
            if raffle[f'{name}{name}'][str(i)]['id'] == message.from_id:
                return "Ты уже учавствуешь!"
            else: None
        except: None
    raffle[name]['ids'] += 1
    count = raffle[name]['ids']
    try:
        raf = raffle[f'{name}{name}']
    except:
        raffle.update({f'{name}{name}': {}})
    raffle[f'{name}{name}'].update({str(count): {'id': message.from_id}})
    dirik = os.getcwd()
    with open(join('raffles.json'), 'w') as f:
            f.write(json.dumps(raffle, ensure_ascii=False, indent=2))
    return "Зарегестрировался"

@bl.message(text="розыгрыш старт <name>")
async def raffleStart(message: Message, name):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    peer_id = message.peer_id
    if user['admin_lvl'] == 6:
        raffle = json.load(open('raffles.json'))
        await message.answer("Выбираю победителя")
        if raffle[name]['cSub'] > 1:
            send = 'Победили в розыгрыше:'
            sendd = 'Они выйграли:'
        else:
            send = 'Победил в розыгрыше:'
            sendd = 'Он выйграл:'
        for i in range(raffle[name]['cSub']):
            b = i
            cId = len(raffle[f'{name}{name}'])
            r = random.randint(1, cId)
            win = raffle[f'{name}{name}'][str(r)]['id']
            user = json.load(open(f'db/users{win}.json', encoding='utf-8'))
            type = raffle[name]['type']
            count = raffle[name]['count']
            if type in ["баланс"]:
                user['balance'] += count
            elif type == "крышки":
                user['rbal'] += count
            elif type in ["реп"]:
                user['reputation'] += count
            elif type == "вип":
                user['vip'] = True
                user['other']['limitBank'] = 50000000000
                user['other']['bcLimitFarms'] = 2500
                user['other']['xBets'] = [26, 25, 41, 40, 56, 55, 71, 70, 106, 105, 131, 130, 146, 145, 153, 152, 161]
                user['other']['limitTransfer'] = 10000000000
                user['remainTransfer'] = 10000000000
                user['vipPrefix'] = 'Профиль'
            dirik = os.getcwd()
            with open(join(dirik, 'db', f'users{win}.json'), 'w') as f:
                f.write(json.dumps(user, ensure_ascii=False, indent=2))
            message.peer_id = win
            try:
                await message.answer(f"Ты победил в розыгрыше {name}\n Ты выйграл: {count} {type}")
            except:
                message.peer_id = peer_id
                await message.answer(f"Не смог отправить сообщение победителю @id{win}")
            send += f'\n@id{win}'
        message.peer_id = peer_id
        del raffle[name]
        del raffle[f'{name}{name}']
        with open(join('raffles.json'), 'w') as f:
            f.write(json.dumps(raffle, ensure_ascii=False, indent=2))
        return f"{send} \n" \
               f"{sendd} {count} {type}"
    else: return
        
        
    
    
