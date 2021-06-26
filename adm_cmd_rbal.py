from vkbottle.bot import BotLabeler, Message
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

limit_rbal = 100000

@bl.message(text="++крышки <a:int>")
async def give_rbal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if user1
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(а) юзеру {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'
    
@bl.message(text="++крышки <a:int> [id<vk_user_id:int>|<other>")
async def give_rbal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(а) юзеру {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'

@bl.message(text="--крышки <a:int>")
async def take_rbal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if user['rbal'] < a:
            a = user['rbal']
        await loual.rbal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(а) юзеру {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'
    
@bl.message(text="--крышки <a:int> [id<vk_user_id:int>|<other>")
async def take_rbal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if user['rbal'] < a:
            a = user['rbal']
        await loual.rbal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(а) юзера {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'

@bl.message(text="==крышки <a:int>")
async def set_rbal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(а) у юзера {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'
    
@bl.message(text="==крышки <a:int> [id<vk_user_id:int>|<other>")
async def set_rbal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 3 and user['admin_lvl'] != 6:
            return
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_set(id=vk_user_id, a=a)
        return f"Установил(а) юзеру {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "5" - > "Владелец"'

@bl.message(text="+крышки <a:int>")
async def give_rbal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 4:
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_give(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(а) себе {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "4" - > "Помошник" и выще'

@bl.message(text="-крышки <a:int>")
async def take_rbal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 4:
        if user['rbal'] < a:
            a = user['rbal']
        await loual.rbal_take(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(а) у себя {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "4" - > "Помошник" и выще'

@bl.message(text="=крышки <a:int>")
async def set_rbal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 4:
        if a > limit_rbal:
            a = limit_rbal
        await loual.rbal_set(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(а) {sub_a} крышек"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "4" - > "Помошник" и выще'
