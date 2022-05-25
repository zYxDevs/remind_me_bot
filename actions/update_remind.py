from db.database import _update

def update_remind(bot, update, args):
  try:
    user_message = ' '.join(args).split(" ", 3)
    remind_id=user_message[0]
    time_remind = f"{user_message[1]} {user_message[2]}"
    reminder_text = user_message[3]
    user_chat_id = update.message.chat_id
    _update(chat_id=user_chat_id, id=remind_id, time=time_remind, text=reminder_text)
    bot.send_message(chat_id=user_chat_id, text=" ✏️ Your remind has been changed.")
  except IndexError:
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Oops 😯, I need more facts to update remind. Please, Try again ✨",
    )
