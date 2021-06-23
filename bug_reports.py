from vkbottle.bot import BotLabeler, Message
import loual
import json
import os
from os.path import join

bl = BotLabeler()
bl.vbml_ignore_case = True



@bl.message(text="багрепорт <bug>")
async def bugReportCmd(message: Message, bug):
    await loual.bugReport()
    from_id = message.from_id
    dirik = os.getcwd()
    data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
    data['allBugs'] += 1
    data['sendBugs'] += 1
    allBugs = data['allBugs']
    data.update({allBugs: ["Отправлено", from_id, bug]})
    with open(join(dirik, 'db', 'other', 'bugReports.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    return "Репорт бага отправлен! Статус 'Отправлено'\n" \
           f"Узнать статус бага: багстатус id{allBugs}"

@bl.message(text="багрепорты стата")
async def bugsStats(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        allBugs = data['allBugs']
        sendBugs = data['sendBugs']
        fixedBugs = data['fixedBugs']
        fakeBugs = data['fakeBugs']
        return f"Статистика баг репортов:\n" \
               f"Всего репортов: {allBugs}\n" \
               f"Отправлено на данный момент: {sendBugs}\n" \
               f"Исправлено багов: {fixedBugs}\n" \
               f"Фейк багов: {fakeBugs}\n" \
               f"\n" \
               f"Просмотреть список ID багов: баглист"

@bl.message(text="баглист")
async def bugList(message: Message):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        idsBug = ''
        for i in range(0, data['allBugs'] + 1):
            str_i = str(i)
            try:
                get = data[str_i]
            except:
                None
            else:
                idsBug += f'ID:{i} \n'
        if idsBug == '':
            idsBug = 'Багрепортов не найдено'
        return f"Все найденные баги:\n" \
               f"{idsBug}\n" \
               "Просмотреть баг командой: багинфо id{id}"

@bl.message(text="багинфо id<id>")
async def bugInfo(message: Message, id):
    await loual.prov(message.from_id)
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        try:
            buginfo = data[str(id)]
        except:
            return "Не правильный ID бага"
        return f"Найденный баг от ID:{buginfo[1]}\n" \
               f"Статус багрепорта: {buginfo[0]}\n" \
               f"Текст багрепорта:\n {buginfo[2]}\n" \
               f"\nПринять баг репорт: дебаг принять id{str(id)}"

@bl.message(text="дебаг принять id<id>")
async def bugConfirm(message: Message, id):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        data[str(id)][0] = "Принято"
        whoId = data[str(id)][1]
        with open(join(dirik, 'db', 'other', 'bugReports.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        await message.answer(f"Багрепорт id{id} принят \n" \
                             f"Сообщаю @id{whoId}(отправителю) багрепорта")
        peer_id = message.peer_id
        message.peer_id = whoId
        await message.answer(f"Ваш багрепорт id{str(id)}, принял @id{message.from_id}\n Скоро исправим ;-)")
        message.peer_id = peer_id
        return f"Сообщение отправлено"

@bl.message(text="дебаг фикс id<id> <count:int> <type>")
async def bugFixed(message: Message, id, count:int, type):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        whoId = data[str(id)][1]
        del data[str(id)]
        data['sendBugs'] -= 1
        data['fixedBugs'] += 1
        with open(join(dirik, 'db', 'other', 'bugReports.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        await message.answer(f"Баг id{id} исправлен \n" \
                             f"Сообщаю @id{whoId}(отправителю) багрепорта")
        user1 = json.load(open(f'db/users{whoId}.json', encoding='utf-8'))
        peer_id = message.peer_id
        if type == "крышки":
            user1['rbal'] += count
            s = 'крышек'
        elif type == "$":
            user1['balance'] += count
            s = '$'
        elif type == "реп":
            user1['reputation'] += count
            s = 'очков репутации'
        with open(join(dirik, 'db', 'users{whoId}.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(user1, ensure_ascii=False, indent=2))
        message.peer_id = whoId
        await message.answer(f"Ваш найденный баг id{str(id)} был исправлен\n За помощь вам выдано {count} {s}")
        message.peer_id = peer_id
        return f"Сообщение отправлено"

@bl.message(text="дебаг фейк id<id> <reason>")
async def bugFake(message: Message, id, reason):
    await loual.prov(message.from_id)
    dirik = os.getcwd()
    user = json.load(open(f'db/users{message.from_id}.json'))
    if user['admin_lvl'] == 5:
        data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
        whoId = data[str(id)][1]
        del data[str(id)]
        data['sendBugs'] -= 1
        data['fakeBugs'] += 1
        with open(join(dirik, 'db', 'other', 'bugReports.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        await message.answer(f"Баг id{id} исправлен \n" \
                             f"Сообщаю @id{whoId}(отправителю) багрепорта")
        peer_id = message.peer_id
        message.peer_id = whoId
        await message.answer(f"Ваш найденный баг id{str(id)} не был исправлен\n Причина: {reason}")
        message.peer_id = peer_id
        return f"Сообщение отправлено"

@bl.message(text="багстатус id<id>")
async def bugFake(message: Message, id):
    data = json.load(open('db/other/bugReports.json', encoding='utf-8'))
    try:
        bug = data[str(id)]
    except:
        return f"Бага с id{id} не был найден, или был исправлен"
    else:
        bug = data[str(id)]
        if message.from_id == bug[1]:
            return f"ID: id{id}\n" \
                   f"Статус багрепорта: {bug[0]}\n" \
                   f"Текст багрепорта:\n {bug[2]}"
        else: return "Не вы отправитель этого багрепорта!"
    

    

