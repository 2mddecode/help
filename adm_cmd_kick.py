from vkbottle.bot import BotLabeler, Message
import os
import loual
import json

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["Лог киков", "kicklog", "Лог к", "log kick", "lk", "лк"])
async def kick_member_id(message: Message):
    await loual.kickLog(message.chat_id)
    c_id = message.chat_id
    logKicks = json.load(open(f"kickLogs/{c_id}.json", encoding="utf-8"))
    count_kicks = logKicks['info']['count_kicks']
    text = logKicks['info']['text']
    c_kicks = count_kicks + 1
    if count_kicks >= 1:
        for i in range(0, c_kicks):
            if i == 0:
                send_logs = ''
            else:
                logs = logKicks[str(i)]
                who = logs['who']
                whom = logs['whom']
                reason = logs['reason']
                send_logs += f"{i}. {who} кикнул участника {whom} ({reason})\n"
        return f"&#10067; Сколько кикнули раз: {count_kicks}\n&#9851; {text} \n" \
                "&#8505; *Кто кикнул* кикнул участника *Кого кикнули* (*Причина*)\n" \
                f"{send_logs}"
    
    
@bl.message(text="кик [id<vk_user_id:int>|<other>]")
async def kick_member_id(message: Message, vk_user_id: int, **kwargs):
    f_id = message.from_id
    await loual.prov(f_id)
    await loual.kickLog(message.chat_id)
    user = json.load(open(f"db/users{f_id}.json"))
    if user['admin_lvl'] >= 3:
        c_id = message.chat_id
        sendReason = "Причина: <<Not specified>>"
        await loual.kickLogAdd(c_id=c_id, f_id=f_id, vk_user_id=vk_user_id, sendReason=sendReason)
        await message.ctx_api.messages.remove_chat_user(message.chat_id, vk_user_id)
        return f"<<Northfade>>Администратор ID:@id{f_id}({f_id}) кикнул участника с ID:@id{vk_user_id}({vk_user_id}) \n" \
               f"{sendReason}"

@bl.message(text="кик [id<vk_user_id:int>|<other>] <reason>")
async def kick_member_id_reason(message: Message, reason, vk_user_id: int, **kwargs):
    f_id = message.from_id
    await loual.prov(f_id)
    await loual.kickLog(message.chat_id)
    user = json.load(open(f"db/users{f_id}.json"))
    if user['admin_lvl'] >= 3:
        c_id = message.chat_id
        sendReason = f"Причина: {reason}"
        await loual.kickLogAdd(c_id=c_id, f_id=f_id, vk_user_id=vk_user_id, sendReason=sendReason)
        await message.ctx_api.messages.remove_chat_user(message.chat_id, vk_user_id)
        return f"<<Northfade>>Администратор ID:@id{f_id}({f_id}) кикнул участника с ID:@id{vk_user_id}({vk_user_id}) \n" \
               f"{sendReason}"

@bl.message(text="кик <reason>")
async def kick_member_reply(message: Message):
    f_id = message.from_id
    vk_user_id = message.reply_message.from_id
    await loual.prov(f_id)
    await loual.kickLog(message.chat_id)
    user = json.load(open(f"db/users{f_id}.json"))
    if user['admin_lvl'] >= 3:
        c_id = message.chat_id
        sendReason = f"Причина: <<Not specified>>"
        await loual.kickLogAdd(c_id=c_id, f_id=f_id, vk_user_id=vk_user_id, sendReason=sendReason)
        await message.ctx_api.messages.remove_chat_user(message.chat_id, vk_user_id)
        return f"<<Northfade>>Администратор ID:@id{f_id}({f_id}) кикнул участника с ID:@id{vk_user_id}({vk_user_id}) \n" \
               f"{sendReason}"

@bl.message(text="кик <reason>")
async def kick_member_reply_reason(message: Message, reason):
    f_id = message.from_id
    vk_user_id = message.reply_message.from_id
    await loual.prov(f_id)
    await loual.kickLog(message.chat_id)
    user = json.load(open(f"db/users{f_id}.json"))
    if user['admin_lvl'] >= 3:
        c_id = message.chat_id
        sendReason = f"Причина: {reason}"
        await loual.kickLogAdd(c_id=c_id, f_id=f_id, vk_user_id=vk_user_id, sendReason=sendReason)
        await message.ctx_api.messages.remove_chat_user(message.chat_id, vk_user_id)
        return f"<<Northfade>>Администратор ID:@id{f_id}({f_id}) кикнул участника с ID:@id{vk_user_id}({vk_user_id}) \n" \
               f"{sendReason}"

