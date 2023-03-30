import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from EdgeGPT import Chatbot
import json

# Set the cookie file
os.environ['COOKIE_FILE'] = './cookies.json'

# Create an instance of the EdgeGPT chatbot
chatbot = Chatbot(cookiePath='./cookies.json')

# Initialize the aiogram API with your bot token
bot = Bot(token="6160231980:AAGz70x3VQqYgKnVgXGx6o3R5wZaJzdBBVs")
dp = Dispatcher(bot)

# Define a handler for the /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi, I'm the EdgeGPT chatbot. Send me a message and I'll respond with something interesting!")
    
    
@dp.message_handler(commands=['about'])
async def send_welcome(message: types.Message):
    await message.reply("Hey there, I'm Patrick Medley, a lover of all things coding and proud Jamaican 🇯🇲 . I've always had a fascination with technology and the endless possibilities it presents. From building websites to developing software, I've dabbled in it all. I find great joy in creating things that not only look good but work seamlessly. If you have any questions or concerns about the bot, feel free to shoot me an email at pstriziomedley@gmail.com. I'm always happy to connect with fellow coders or anyone interested in the tech industry. Thanks for stopping by!")

@dp.message_handler()
async def echo_all(message: types.Message):
    # Get the text message from the user
    user_input = message.text


    # Generate a response using EdgeGPT
    json_data = await chatbot.ask(prompt=user_input)
       
        # assuming json_data is a dictionary object
    json_string = json.dumps(json_data)
    
    # now you can pass json_string to the json.loads() function
    response = json.loads(json_string)
    
    item = response['item']  
    messages = item['messages']
    
    
    response_messages = [message['text'] for message in messages if message['author'] == 'bot']
    
    text = '\n'.join(response_messages)
        

    # Send the response back to the user
    await message.reply(text)
    
# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
