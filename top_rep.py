from vkbottle.bot import BotLabeler, Message
import os
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True



@bl.message(text="топ")
async def top(message: Message):
    dirik = os.getcwd()
    files = os.listdir(f'{dirik}/db')
    count = len(files)
    info = {}
    for i in range(0, count):
        try:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
        except: None
        else:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
            try:
                id = files[i]
                id = id.replace('users', '')
                id = id.replace('.json', '')
                rep = data['reputation']
                nick = data['nick']
                pf = data['own_prefix']
                info.update({i: {"id": id, "nick": nick, "pf": pf, "rep": rep}})
            except: None
    d = info.keys()
    allRep = sorted(d, key=lambda i: info[i]['rep'], reverse=True)
    c = len(allRep)
    send = ''
    if c > 10:
        c = 10
    for i in range(0, c):
        ii = i + 1
        key = allRep[i]
        id = info[key]['id']
        rep = info[key]['rep']
        nick = info[key]['nick']
        pf = info[key]['pf']
        send += f'{ii}. @id{id}({nick}) - {rep}&#128081; -> "{pf}"\n'
    return f"Топ {c} пользователей по репутации:\n" \
           f"{send}"

@bl.message(text="топ <c:int>")
async def topC(message: Message, c: int):
    dirik = os.getcwd()
    files = os.listdir(f'{dirik}/db')
    count = len(files)
    info = {}
    for i in range(0, count):
        try:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
        except: None
        else:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
            try:
                id = files[i]
                id = id.replace('users', '')
                id = id.replace('.json', '')
                rep = data['reputation']
                nick = data['nick']
                pf = data['own_prefix']
                info.update({i: {"id": id, "nick": nick, "pf": pf, "rep": rep}})
            except: None
    d = info.keys()
    allRep = sorted(d, key=lambda i: info[i]['rep'], reverse=True)
    send = ''
    if c > 10:
        c = 10
    for i in range(0, c):
        ii = i + 1
        key = allRep[i]
        id = info[key]['id']
        rep = info[key]['rep']
        nick = info[key]['nick']
        pf = info[key]['pf']
        send += f'{ii}. @id{id}({nick}) - {rep}&#128081; -> "{pf}"\n'
    return f"Топ {c} пользователей по репутации:\n" \
           f"{send}"


@bl.message(text="топ баланс")
async def top(message: Message):
    dirik = os.getcwd()
    files = os.listdir(f'{dirik}/db')
    count = len(files)
    info = {}
    for i in range(0, count):
        try:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
        except: None
        else:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
            try:
                id = files[i]
                id = id.replace('users', '')
                id = id.replace('.json', '')
                balance = data['balance']
                nick = data['nick']
                pf = data['own_prefix']
                info.update({i: {"id": id, "nick": nick, "pf": pf, "balance": balance}})
            except: None
    d = info.keys()
    allRep = sorted(d, key=lambda i: info[i]['balance'], reverse=True)
    c = len(allRep)
    send = ''
    if c > 10:
        c = 10
    for i in range(0, c):
        ii = i + 1
        key = allRep[i]
        id = info[key]['id']
        balance = info[key]['balance']
        nick = info[key]['nick']
        pf = info[key]['pf']
        send += f'{ii}. @id{id}({nick}) - {balance}$ -> "{pf}"\n'
    return f"Топ {c} пользователей по репутации:\n" \
           f"{send}"

@bl.message(text="топ баланс <c:int>")
async def topC(message: Message, c: int):
    dirik = os.getcwd()
    files = os.listdir(f'{dirik}/db')
    count = len(files)
    info = {}
    for i in range(0, count):
        try:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
        except: None
        else:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
            try:
                id = files[i]
                id = id.replace('users', '')
                id = id.replace('.json', '')
                balance = data['balance']
                nick = data['nick']
                pf = data['own_prefix']
                info.update({i: {"id": id, "nick": nick, "pf": pf, "balance": balance}})
            except: None
    d = info.keys()
    allRep = sorted(d, key=lambda i: info[i]['balance'], reverse=True)
    send = ''
    if c > 10:
        c = 10
    for i in range(0, c):
        ii = i + 1
        key = allRep[i]
        id = info[key]['id']
        balance = info[key]['balance']
        nick = info[key]['nick']
        pf = info[key]['pf']
        send += f'{ii}. @id{id}({nick}) - {balance}$ -> "{pf}"\n'
    return f"Топ {c} пользователей по репутации:\n" \
           f"{send}"

@bl.message(text=["топ дуэли", "топ дуэлистоп"])
async def top(message: Message):
    dirik = os.getcwd()
    files = os.listdir(f'{dirik}/db')
    count = len(files)
    info = {}
    for i in range(0, count):
        try:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
        except: None
        else:
            data = json.load(open(f'db/{files[i]}', encoding='utf-8'))
            try:
                id = files[i]
                id = id.replace('users', '')
                id = id.replace('.json', '')
                repDuels = data['repDuels']
                nick = data['nick']
                pf = data['own_prefix']
                info.update({i: {"id": id, "nick": nick, "pf": pf, "rep": repDuels}})
            except: None
    d = info.keys()
    allRep = sorted(d, key=lambda i: info[i]['rep'], reverse=True)
    c = len(allRep)
    send = ''
    if c > 10:
        c = 10
    for i in range(0, c):
        ii = i + 1
        key = allRep[i]
        id = info[key]['id']
        rep = info[key]['rep']
        nick = info[key]['nick']
        pf = info[key]['pf']
        send += f'{ii}. @id{id}({nick}) - {rep}&#11088; -> "{pf}"\n'
    return f"Топ {c} пользователей по репутации:\n" \
           f"{send}"
