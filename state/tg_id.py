# id = message.text[9:].strip()

#     info = get_student_info(id)

#     text =f"ID: {info['tg_id']}\n"
#     text +=f"name: {info['full_name']}\n"
#     text +=f"group: {info['group']['name']}\n"

#     for i in info['marks']:
#         checks = "bugun darsga keldi ✅" if i["checks"] else "bugun darsga kelmadi ❌"
#         date = i["attendance"]['created']
#         text+=f"▪️{date}:\n{checks}"


#     text += "\n-----------------------\n"

#     text += "Xabarlar\n"
#     for i in info['messages']:
#         text += f"  🔹{i['body']}\n"
#         text += f"  🕔{i['created'][:10]}\n"

#     await message.reply(f"{text}")