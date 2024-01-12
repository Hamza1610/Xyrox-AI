from db_wrapper import DB

wrapper = DB('chat_history')

wrapper.creat_table('Chats')

# wrapper.insert(['Xyrox', 'Hi Dear how are you today'])

chat_table_items = wrapper.get_table_last_ten('Chats')

print(chat_table_items)