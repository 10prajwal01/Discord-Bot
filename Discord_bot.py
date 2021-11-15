import discord
import random

TOKEN = 'OTA5NDU1NTIxMDg4NjkyMzA3.YZEidQ.5dw60CtHbOIJsijmu0h0QZgxSgU'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
        
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hi {username}')
            return
        elif user_message.lower() == 'hi':
            await message.channel.send(f'Hi {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number:{random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!game':
            await message.channel.send(f'Anyone gaming with {username}?')
            return
        elif user_message.lower() == '!valorant':
            await message.channel.send(f'Make a group of 5 people.')
            return
        elif user_message.lower() == '!channel':
            await message.channel.send(f'This is a test channel.')
            return
        elif user_message.lower() == '!available':
            await message.channel.send(f'I am here to serve you.')
            return
        elif user_message.lower() == '!follow':
            await message.channel.send(f'Youtube - https://www.youtube.com/ \n Instagram - https://www.instagram.com/ \n Twitter - https://twitter.com/?lang=en')
            return

    if user_message.lower() == '!language':
        await message.channel.send('Python')
        return
    

client.run(TOKEN)

