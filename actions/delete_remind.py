from db.database import delete

def delete_remind(bot, update, args):
  user_chat_id = update.message.chat_id
  if args:
    try:
      delete(args, user_chat_id)
      bot.send_message(chat_id=update.message.chat_id, text="Your remind(s) has been deleted ☑️")
    except:
      bot.send_message(chat_id=update.message.chat_id, text="Sorry, there is no remind(s) with such id 😔")
  else:
    bot.send_message(chat_id=update.message.chat_id, text="Oops 😯, you forgot to specify id(s). Please, try again.")
  
