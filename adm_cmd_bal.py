from vkbottle.bot import BotLabeler, Message
import loual
import json


bl = BotLabeler()
bl.vbml_ignore_case = True

limit_bal = 228666228666228666228666

async def count_k(a, k):
    if k in ['к', 'кк', 'ккк', 'кккк', 'ккккк', 'кккккк']:
        lk = len(k)
        a = a * (1000**lk)
        return a
    else:
        return None

@bl.message(text="++баланс <a:int>")
async def give_bal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="++баланс <a:int> [id<vk_user_id:int>|<other>")
async def give_bal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="--баланс <a:int>")
async def take_bal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="--баланс <a:int> [id<vk_user_id:int>|<other>")
async def take_bal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="==баланс <a:int>")
async def set_bal_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="==баланс <a:int> [id<vk_user_id:int>|<other>")
async def set_bal_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="+баланс <a:int>")
async def give_bal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) себе {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'

@bl.message(text="-баланс <a:int>")
async def take_bal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у себя {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'

@bl.message(text="=баланс <a:int>")
async def set_bal_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'







@bl.message(text="++баланс <a:int> <k>")
async def give_bal_reply_k(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="++баланс <a:int> <k> [id<vk_user_id:int>|<other>")
async def give_bal_id_k(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="--баланс <a:int> <k>")
async def take_bal_reply_k(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал у юзера {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="--баланс <a:int> <k> [id<vk_user_id:int>|<other>")
async def take_bal_id_k(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="==баланс <a:int> <k>")
async def set_bal_reply_k(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'
    
@bl.message(text="==баланс <a:int> <k> [id<vk_user_id:int>|<other>")
async def set_bal_id_k(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] == 0 and user['admin_lvl'] != 6:
            return
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "2" - > "Администратор" и выше'

@bl.message(text="+баланс <a:int> <k>")
async def give_bal_me_k(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if a > limit_bal:
            a = limit_bal
        await loual.bal_give(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) себе {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'

@bl.message(text="-баланс <a:int> <k>")
async def take_bal_me_k(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if user['balance'] < a:
            a = user['balance']
        await loual.bal_take(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у себя {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'

@bl.message(text="=баланс <a:int> <k>")
async def set_bal_me_k(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 1:
        if a > limit_bal:
            a = limit_bal
        await loual.bal_set(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) {sub_a}$"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администротирования "1" - > "Модератор" и выше'
