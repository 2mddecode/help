from vkbottle.bot import BotLabeler, Message
import loual
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text="+код <type> <count:int> <cact:int> <name>")
async def createCode(message: Message, type, count: int, cact: int, name):
    await loual.prov(message.from_id)
    await loual.bCode()
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        if type in ['баланс', '$', 'деньги']:
            data = json.load(open('bonusCodes.json'))
            data.update({name: {"type": "$", "count": count, "cact": cact}})
            with open('bonusCodes.json', 'w') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2))
            return f"Создал код {name}\n" \
                   f"Тип: $\n" \
                   f"Кол-во к выдаче: {count}\n" \
                   f"Кол-во активаций: {cact}"
        elif type in ['крышки', 'крышечки']:
            data = json.load(open('bonusCodes.json'))
            data.update({name: {"type": "рубли", "count": count, "cact": cact}})
            with open('bonusCodes.json', 'w') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2))
            return f"Создал код {name}\n" \
                   f"Тип: Рубли\n" \
                   f"Кол-во к выдаче: {count}\n" \
                   f"Кол-во активаций: {cact}"
        elif type in ['реп', 'репутация']:
            data = json.load(open('bonusCodes.json'))
            data.update({name: {"type": "реп", "count": count, "cact": cact}})
            with open('bonusCodes.json', 'w') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2))
            return f"Создал код {name}\n" \
                   f"Тип: Очки репутации\n" \
                   f"Кол-во к выдаче: {count}\n" \
                   f"Кол-во активаций: {cact}"
        elif type == 'вип':
            data = json.load(open('bonusCodes.json'))
            data.update({name: {"type": "вип", "count": count, "cact": cact}})
            with open('bonusCodes.json', 'w') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2))
            return f"Создал код {name}\n" \
                   f"Тип: Статус VIP\n" \
                   f"Кол-во к выдаче: {count}\n" \
                   f"Кол-во активаций: {cact}"
        

@bl.message(text="код <code>")
async def enterCode(message: Message, code):
    await loual.prov(message.from_id)
    await loual.bCode()
    data = json.load(open('bonusCodes.json'))
    user = json.load(open(f'db/users{message.from_id}.json', encoding='utf-8'))
    if code in user['act_codes']:
        return "Ты уже вводил этот код"
    else:
        try:
            infoCode = data[code]
        except:
            return "Код введён не верно или его не существует"
        else:
            infoCode = data[code]
            if infoCode['cact'] != 0:
                type = infoCode['type']
                count = infoCode['count']
                sub_count = await loual.sub(count)
                user['act_codes'].append(code)
                infoCode['cact'] -= 1
                if type == '$':
                    if user['admin_lvl'] < 1:
                        user['balance'] += count
                        send = f"Ты получил {sub_count}$"
                elif type == 'реп':
                    if user['admin_lvl'] < 2:
                        user['reputation'] += count
                        send = f"Ты получил {sub_count} очков репутации"
                elif type == 'рубли':
                    if user['admin_lvl'] < 4:
                        user['rbal'] += count
                        send = f"Ты получил {sub_count} крышек"
                elif type == 'вип':
                    if user['vip'] == False:
                        user['vip'] == True
                        send = f"Ты получил VIP статус"
                
                with open('bonusCodes.json', 'w') as f:
                    f.write(json.dumps(data, ensure_ascii=False, indent=2))
                with open(f'db/users{message.from_id}.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(user, ensure_ascii=False, indent=2))
                return f"При активации кода: {code}\n" \
                       f'{send}'
                       
            else:
                return f'Код {code} уже был активирован определенное кол-во раз'
            







    
