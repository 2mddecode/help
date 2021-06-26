from vkbottle.bot import BotLabeler, Message
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

limit_rep = 77777777777777777777

async def count_k(a, k):
    if k in ['к', 'кк', 'ккк', 'кккк', 'ккккк', 'кккккк']:
        lk = len(k)
        a = a * (1000**lk)
        return a
    else:
        return None

@bl.message(text=["++реп <a:int>", "++репутация <a:int>"])
async def give_rep_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["++реп <a:int> [id<vk_user_id:int>|<other>", "++репутация <a:int> [id<vk_user_id:int>|<other>"])
async def give_rep_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["--реп <a:int>", "--репутация <a:int>"])
async def take_rep_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["--реп <a:int> [id<vk_user_id:int>|<other>", "--репутация <a:int> [id<vk_user_id:int>|<other>"])
async def take_rep_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["==реп <a:int>", "==репутация <a:int>"])
async def set_rep_reply(message: Message, a: int):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["==реп <a:int> [id<vk_user_id:int>|<other>", "==репутация <a:int> [id<vk_user_id:int>|<other>"])
async def set_rep_id(message: Message, a: int, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["+реп <a:int>", "+репутация <a:int>"])
async def give_rep_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) себе {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'

@bl.message(text=["-реп <a:int>", "-репутация <a:int>"])
async def take_rep_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    sub_a = await loual.sub(i=a)
    if user['admin_lvl'] >= 2:
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у себя {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'

@bl.message(text=["=реп <a:int>", "=репутация <a:int>"])
async def set_rep_me(message: Message, a: int):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'







@bl.message(text=["++реп <a:int> <k>", "++репутация <a:int> <k>"])
async def give_rep_reply(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["++реп <a:int> <k> [id<vk_user_id:int>|<other>", "++репутация <a:int> <k> [id<vk_user_id:int>|<other>"])
async def give_rep_id(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["--реп <a:int> <k>", "--репутация <a:int> <k>"])
async def take_rep_reply(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["--реп <a:int> <k> [id<vk_user_id:int>|<other>", "--репутация <a:int> <k> [id<vk_user_id:int>|<other>"])
async def take_rep_id(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у юзера {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["==реп <a:int> <k>", "==репутация <a:int> <k>"])
async def set_rep_reply(message: Message, a: int, k):
    vk_user_id = message.reply_message.from_id
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'
    
@bl.message(text=["==реп <a:int> <k> [id<vk_user_id:int>|<other>", "==репутация <a:int> <k> [id<vk_user_id:int>|<other>"])
async def set_rep_id(message: Message, a: int, k, vk_user_id: int, **kwargs):
    await loual.prov(message.from_id)
    await loual.prov(vk_user_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 3:
        user1 = json.load(open(f'db/users{vk_user_id}.json'))
        if user1['admin_lvl'] <= 2 and user['admin_lvl'] != 6:
            return
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=vk_user_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) юзеру {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "3" -> "Гл.Администратор" и выше'

@bl.message(text=["+реп <a:int> <k>", "+репутация <a:int> <k>"])
async def give_rep_me(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        if a > limit_rep:
            a = limit_rep
        await loual.rep_give(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Выдал(a) себе {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'

@bl.message(text=["-реп <a:int> <k>", "-репутация <a:int> <k>"])
async def take_rep_me(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    sub_a = await loual.sub(i=a)
    if user['admin_lvl'] >= 2:
        if user['reputation'] < a:
            a = user['reputation']
        await loual.rep_take(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Забрал(a) у себя {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'

@bl.message(text=["=реп <a:int> <k>", "=репутация <a:int> <k>"])
async def set_rep_me(message: Message, a: int, k):
    await loual.prov(message.from_id)
    a = await count_k(a, k)
    if a == None:
        return
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] >= 2:
        if a > limit_rep:
            a = limit_rep
        await loual.rep_set(id=message.from_id, a=a)
        sub_a = await loual.sub(i=a)
        return f"Установил(a) {sub_a} очков репутации"
    else: return f"Твой уровень администратирования {user['admin_lvl']}\n" \
                  'Для этой команды необходим уровень администратирования "2" -> "Администратор" и выше'


