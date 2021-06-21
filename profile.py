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
    b = await loual.sub(i=bal)
    r = await loual.sub(i=rep)
    rb = await loual.sub(i=rbal)
    ba = await loual.sub(i=bank)
    return [b, r, rb, ba]

async def check_statuses(data):
    if data['vip'] == True:
        vip_text = '&#11088;Наличие VIP: Навсегда\n'
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
    sub = await subs(data)
    if data['inventory'] == []:
            inv = 'Пуст'
    else: inv = 'Что-то есть'
    return f"Вот твой профиль\n" \
           f"{statuses[1]}" \
           f"{statuses[0]}" \
           f"&#127380;ID: {message.from_id}\n" \
           f"&#128223;Ник: {data['nick']}\n" \
           f"&#128280;Крышечки: {sub[2]} ₽\n" \
           f"&#128179;Баланс: {sub[0]}$\n" \
           f"&#128176;Баланс в банке: {sub[3]}$\n" \
           f"&#128081;Репутация: {sub[1]}\n" \
           f"&#128230;Инвентарь: {inv}\n" \
           f"\n" \
           f"&#128273;Твоё имущество\n" \
           f"&#127981;Бизнес: {data['buisnes_name']}"

@bl.message(text="гет")
async def get_id(message: Message):
    vk_user_id = message.reply_message.from_id
    await loual.prov(vk_user_id)
    data = json.load(open(f'db/users{vk_user_id}.json', 'r', encoding='utf-8'))
    if data['invisible_profile'] != True: 
        statuses = await check_statuses(data)
        sub = await subs(data)
        if data['inventory'] == []:
            inv = 'Пуст'
        else: inv = 'Что-то есть'
        return f"Вот его профиль\n" \
               f"{statuses[1]}" \
               f"{statuses[0]}" \
               f"&#127380;ID: {vk_user_id}\n" \
               f"&#128223;Ник: {data['nick']}\n" \
               f"&#128280;Крышечки: {sub[2]} ₽\n" \
               f"&#128179;Баланс: {sub[0]}$\n" \
               f"&#128176;Баланс в банке: {sub[3]}$\n" \
               f"&#128081;Репутация: {sub[1]}\n" \
               f"&#128230;Инвентарь: {inv}\n" \
               f"\n" \
               f"&#128273;Его имущество\n" \
               f"&#127981;Бизнес: {data['buisnes_name']}"

@bl.message(text="гет [id<vk_user_id:int>|<other>")
async def get_id(message: Message, vk_user_id: int, **kwargs):
    await loual.prov(vk_user_id)
    data = json.load(open(f'db/users{vk_user_id}.json', 'r', encoding='utf-8'))
    if data['invisible_profile'] != True: 
        statuses = await check_statuses(data)
        sub = await subs(data)
        if data['inventory'] == []:
            inv = 'Пуст'
        else: inv = 'Что-то есть'
        return f"Вот его профиль\n" \
               f"{statuses[1]}" \
               f"{statuses[0]}" \
               f"&#127380;ID: {vk_user_id}\n" \
               f"&#128223;Ник: {data['nick']}\n" \
               f"&#128280;Крышечки: {sub[2]} ₽\n" \
               f"&#128179;Баланс: {sub[0]}$\n" \
               f"&#128176;Баланс в банке: {sub[3]}$\n" \
               f"&#128081;Репутация: {sub[1]}\n" \
               f"&#128230;Инвентарь: {inv}\n" \
               f"\n" \
               f"&#128273;Его имущество\n" \
               f"&#127981;Бизнес: {data['buisnes_name']}"
               

@bl.message(text=["профиль невидимость <a>", "проф невидимость <a>", "профиль инвиз <a>", "проф инвиз <a>"])
async def invisible_profile(message: Message, a):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', 'r', encoding='utf-8'))
    invis_prof = data['invisible_profile']
    if data['vip'] == True:
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

@bl.message(text=["уровень", "уа", "lvl"])
async def invisible_profile(message: Message):
    await loual.prov(message.from_id)
    data = json.load(open(f'db/users{message.from_id}.json', 'r', encoding='utf-8'))
    adm_lvl = data['admin_lvl']
    o_pf = data['own_prefix']
    return f'Ваш уровень администратирования - "{adm_lvl}" -> "{o_pf}"'
    



    
