from vkbottle.bot import BotLabeler, Message
import loual
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True

async def subs(data):
    bal = data['balance']
    rep = data['reputation']
    rbal = data['rbal']
    bank = data['bank']
    bitcoin = data['bitcoin']
    b = await loual.sub(i=bal)
    r = await loual.sub(i=rep)
    rb = await loual.sub(i=rbal)
    ba = await loual.sub(i=bank)
    bc = await loual.sub(i=bitcoin)
    return [b, r, rb, ba, bc]

async def check_statuses(data):
    if data['vip'] >= 1:
        if data['vip'] == 2:
            vip_text = '&#11088;Имеется Premium статус\n'
        else:
            vip_text = '&#11088;Имеется VIP статус\n'
    else:
        vip_text = ''
    own_prefix = data['own_prefix']
    lvl_text = f'&#127344;Вы являетесь {own_prefix}\n'
    return [vip_text, lvl_text]

@bl.message(text=["проф", "профиль"])
async def profile(message: Message):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', 'r', encoding='utf-8'))
    statuses = await check_statuses(data)
    if data['vip'] >= 1:
        if data['vip'] == 2:
            vPrefix = data['pPrefix'] + ':'
        else:
            vPrefix = 'Твой ' + data['vPrefix'] + ':'
    else:
        vPrefix = 'Твой профиль'
    if data['bcFarmLvl'] >= 1:
        bcFarm = f"{data['bcFarmName']} [{data['bcFarmCount']} штук]"
    else:
        bcFarm = 'Нету'
    sub = await subs(data)
    space = '&#12288;'
    allDuels = data['duelsWin'] + data['duelsLost']
    ops = data['operationAll']
    if data['inventory'] == []:
            inv = 'Пуст'
    else: inv = 'Что-то есть'
    return f"{vPrefix}\n" \
           f"{statuses[1]}" \
           f"{statuses[0]}" \
           f"&#127380;ID: {message.from_id}\n" \
           f"&#128223;Ник: {data['nick']}\n" \
           f"&#128280;Крышечки: {sub[2]} ₽\n" \
           f"&#128179;Баланс: {sub[0]}$\n" \
           f"&#128176;Баланс в банке: {sub[3]}$\n" \
           f"&#128189;Биткоины: {sub[4]}₿\n" \
           f"&#128081;Репутация: {sub[1]}\n" \
           f"&#128230;Инвентарь: {inv}\n" \
           f"\n" \
           f"&#128273;Твоё имущество\n" \
           f"{space}Бизнес: {data['buisnes_name']}\n" \
           f"{space}Фермы: {bcFarm}\n" \
           f"{space}Вертолет: {data['helicopter_name']}\n" \
           f"{space}Компьютер: {data['pc_name']}\n" \
           f"{space}Телефон: {data['phone_name']}\n" \
           f"" \
           f"\n" \
           f"&#128377;Быстрая стата игр:\n" \
           f"{space}&#128299;Всего сыграно дуэлей {allDuels}\n" \
           f"{space}{space}&#10548;Статистика дуэлей: дуэли стата\n" \
           f"{space}&#128506;Всего операций: {ops}\n" \
           f"{space}{space}&#10548;Статистика операций: операция стата\n"

@bl.message(text="гет")
async def get_id(message: Message):
    user = json.load(open(f'db/users{message.from_id}.json'))
    vk_user_id = message.reply_message.from_id
    if user['admin_lvl'] >= 1:
        if vk_user_id < 0:
            return
        else:
            await loual.prov(vk_user_id)
            data = json.load(open(f'db/users{id}.json', 'r', encoding='utf-8'))
            if data['admin_lvl'] == 0:
                return "Тебе нельзя так делать!"
            if data['invisible_profile'] != True: 
                statuses = await check_statuses(data)
                if data['vip'] >= 1:
                    if data['vip'] == 2:
                        vPrefix = data['pPrefix'] + ':'
                    else:
                        vPrefix = 'Твой ' + data['vPrefix'] + ':'
                else:
                    vPrefix = 'Его профиль'
                if data['bcFarmLvl'] >= 1:
                    bcFarm = f"{data['bcFarmName']} [{data['bcFarmCount']} штук]"
                else:
                    bcFarm = 'Нету'
                sub = await subs(data)
                space = '&#12288;'
                allDuels = data['duelsWin'] + data['duelsLost']
                ops = data['operationAll']
                if data['inventory'] == []:
                    inv = 'Пуст'
                else:
                    inv = 'Что-то есть'
                return f"{vPrefix}\n" \
                       f"{statuses[1]}" \
                       f"{statuses[0]}" \
                       f"&#127380;ID: {vk_user_id}\n" \
                       f"&#128223;Ник: {data['nick']}\n" \
                       f"&#128280;Крышечки: {sub[2]} ₽\n" \
                       f"&#128179;Баланс: {sub[0]}$\n" \
                       f"&#128176;Баланс в банке: {sub[3]}$\n" \
                       f"&#128189;Биткоины: {sub[4]}₿\n" \
                       f"&#128081;Репутация: {sub[1]}\n" \
                       f"&#128230;Инвентарь: {inv}\n" \
                       f"\n" \
                       f"&#128273;Его(её) имущество\n" \
                       f"{space}Бизнес: {data['buisnes_name']}\n" \
                       f"{space}Фермы: {bcFarm}\n" \
                       f"{space}Вертолет: {data['helicopter_name']}" \
                       f"{space}Компьютер: {data['pc_name']}\n" \
                       f"{space}Телефон: {data['phone_name']}\n" \
                       f"\n" \
                       f"&#128377;Быстрая стата игр:\n" \
                       f"{space}&#128299;Всего сыграно дуэлей {allDuels}\n" \
                       f"{space}{space}&#10548;Статистика дуэлей: дуэли стата\n" \
                       f"{space}&#128506;Всего операций: {ops}\n" \
                       f"{space}{space}&#10548;Статистика операций: операция стата\n"
    else: return

@bl.message(text="гет [id<vk_user_id:int>|<other>")
async def get_id(message: Message, vk_user_id: int, **kwargs):
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if vk_user_id < 0:
            return
        else:
            await loual.prov(vk_user_id)
            data = json.load(open(f'db/users{id}.json', 'r', encoding='utf-8'))
            if data['admin_lvl'] == 0:
                return "Тебе нельзя так делать!"
            if data['invisible_profile'] != True: 
                statuses = await check_statuses(data)
                if data['vip'] >= 1:
                    if data['vip'] == 2:
                        vPrefix = data['pPrefix'] + ':'
                    else:
                        vPrefix = 'Твой ' + data['vPrefix'] + ':'
                else:
                    vPrefix = 'Его профиль'
                if data['bcFarmLvl'] >= 1:
                    bcFarm = f"{data['bcFarmName']} [{data['bcFarmCount']} штук]"
                else:
                    bcFarm = 'Нету'
                sub = await subs(data)
                space = '&#12288;'
                allDuels = data['duelsWin'] + data['duelsLost']
                ops = data['operationAll']
                if data['inventory'] == []:
                    inv = 'Пуст'
                else:
                    inv = 'Что-то есть'
                return f"{vPrefix}\n" \
                       f"{statuses[1]}" \
                       f"{statuses[0]}" \
                       f"&#127380;ID: {vk_user_id}\n" \
                       f"&#128223;Ник: {data['nick']}\n" \
                       f"&#128280;Крышечки: {sub[2]} ₽\n" \
                       f"&#128179;Баланс: {sub[0]}$\n" \
                       f"&#128176;Баланс в банке: {sub[3]}$\n" \
                       f"&#128189;Биткоины: {sub[4]}₿\n" \
                       f"&#128081;Репутация: {sub[1]}\n" \
                       f"&#128230;Инвентарь: {inv}\n" \
                       f"\n" \
                       f"&#128273;Его(её) имущество\n" \
                       f"{space}Бизнес: {data['buisnes_name']}\n" \
                       f"{space}Фермы: {bcFarm}\n" \
                       f"{space}Вертолет: {data['helicopter_name']}" \
                       f"{space}Компьютер: {data['pc_name']}\n" \
                       f"{space}Телефон: {data['phone_name']}\n" \
                       f"\n" \
                       f"&#128377;Быстрая стата игр:\n" \
                       f"{space}&#128299;Всего сыграно дуэлей {allDuels}\n" \
                       f"{space}{space}&#10548;Статистика дуэлей: дуэли стата\n" \
                       f"{space}&#128506;Всего операций: {ops}\n" \
                       f"{space}{space}&#10548;Статистика операций: операция стата\n"
    else: return               

@bl.message(text=["профиль невидимость <a>", "проф невидимость <a>", "профиль инвиз <a>", "проф инвиз <a>"])
async def invisible_profile(message: Message, a):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', 'r', encoding='utf-8'))
    invis_prof = data['invisible_profile']
    if data['vip'] >= 1:
        if a in ['1', 'on', 'включить', 'yes', 'y', '+']:
            invis_prof = True
            st_inv = '"Включено"'
        elif a in ['0', 'off', 'включить', 'no', 'n', '-']:
            invis_prof = False
            st_inv = '"Выключено"'
        data['invisible_profile'] = invis_prof
        dirik = os.getcwd()
        with open(join(dirik, 'db', f'users{message.from_id}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        return f"Установил невидимость {st_inv}"
    else:
        return "Иди и покупай VIP\n" \
               "Командой: 'купить вип'"

@bl.message(text=["уровень", "lvl"])
async def invisible_profile(message: Message):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', 'r', encoding='utf-8'))
    adm_lvl = data['admin_lvl']
    o_pf = data['own_prefix']
    return f'Ваш уровень администратирования - "{adm_lvl}" -> "{o_pf}"'

@bl.message(text=["дуэли стата", "дуэли статистика", "дуэль стата", "дуэль статистика"])
async def duelsStat(message: Message):
    from_id = message.from_id
    await loual.prov(from_id)
    await loual.duels(message.chat_id)
    try:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
    except:
        allChatDuels = 0
    else:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
        allChatDuels = chatDuels['all_duels']
    duelStats = json.load(open(f'db/users{from_id}.json', encoding='utf-8'))
    wins = duelStats['duelsWin']
    losts = duelStats['duelsLost']
    repDuels = duelStats['repDuels']
    allFires = duelStats['allFires']
    allDuels = wins + losts
    return f"&#128202;Статистика дуэлей ID:{from_id}\n" \
           f"&#11088;Рейтинг дуэлиста: {repDuels}\n" \
           f"&#128299;Всего дуэлей: {allDuels}\n" \
           f"&#127942;Из них {wins} побед\n" \
           f"&#10060;Из них {losts} поражений\n" \
           f"&#128165;Всего сделано выстрелов: {allFires}\n" \
           f"&#128190;В этой беседе всего было дуэлей: {allChatDuels}"

@bl.message(text=["гет дуэли", "гет дуэль"])
async def duelsStat(message: Message):
    vk_user_id = message.reply_message.from_id
    await loual.prov(vk_user_id)
    await loual.duels(message.chat_id)
    try:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
    except:
        allChatDuels = 0
    else:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
        allChatDuels = chatDuels['all_duels']
    duelStats = json.load(open(f'db/users{vk_user_id}.json', encoding='utf-8'))
    wins = duelStats['duelsWin']
    losts = duelStats['duelsLost']
    repDuels = duelStats['repDuels']
    allFires = duelStats['allFires']
    allDuels = wins + losts
    return f"&#128202;Статистика дуэлей ID:{vk_user_id}\n" \
           f"&#11088;Рейтинг дуэлиста: {repDuels}\n" \
           f"&#128299;Всего дуэлей: {allDuels}\n" \
           f"&#127942;Из них {wins} побед\n" \
           f"&#10060;Из них {losts} поражений\n" \
           f"&#128165;Всего сделано выстрелов: {allFires}\n" \
           f"&#128190;В этой беседе всего было дуэлей: {allChatDuels}"
           
@bl.message(text=["гет дуэли [id<vk_user_id:int>|<other>", "гет дуэль [id<vk_user_id:int>|<other>"])
async def duelsStat(message: Message, vk_user_id: int, **kwargs):
    await loual.prov(vk_user_id)
    await loual.duels(message.chat_id)
    try:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
    except:
        allChatDuels = 0
    else:
        chatDuels = json.load(open(f'db/other/duel-chat{message.chat_id}.json'))
        allChatDuels = chatDuels['all_duels']
    duelStats = json.load(open(f'db/users{vk_user_id}.json', encoding='utf-8'))
    wins = duelStats['duelsWin']
    losts = duelStats['duelsLost']
    repDuels = duelStats['repDuels']
    allFires = duelStats['allFires']
    allDuels = wins + losts
    return f"&#128202;Статистика дуэлей ID:{vk_user_id}\n" \
           f"&#11088;Рейтинг дуэлиста: {repDuels}\n" \
           f"&#128299;Всего дуэлей: {allDuels}\n" \
           f"&#127942;Из них {wins} побед\n" \
           f"&#10060;Из них {losts} поражений\n" \
           f"&#128165;Всего сделано выстрелов: {allFires}\n" \
           f"&#128190;В этой беседе всего было дуэлей: {allChatDuels}"
    



    
