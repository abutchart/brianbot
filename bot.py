import discord
from discord.ext import commands, tasks
import gpt_2_simple as gpt2
import tensorflow as tf
import random


TOKEN = # TOKEN
intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
links = open('links.txt', 'r').readlines()
emojis = open('emojis.txt', 'r').readlines()
images = open('images.txt', 'r').readlines()
# mentions are displayed in two alternate forms for some reason
mention = # BOT MENTION IN FORM <@!BOTID>
mention_alt = # BOT MENTION IN FORM <!BOTID>
sess = None

@client.event
async def on_ready():
    global sess
    await client.change_presence(activity=discord.Game('ping me!'))
    #generates session from model checkpoint located in /checkpoint/run1 by default
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    print('BOT ONLINE')

@client.command()
async def ping(ctx):
    print('PONG')
    await ctx.send(f'PONG! {round(client.latency * 1000)}ms')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        try:
            question = message.content.replace(mention, '').replace(mention_alt, '').strip()
            if not question:
                remove, newQuestion = await message.channel.history(limit=2).flatten()
                await remove.delete()
                question = newQuestion.content
            async with message.channel.typing():
                question = ''.join((i if ord(i) < 10000 else '(emoji)' for i in question))
                response = gpt2.generate(sess,
                      length=20,
                      temperature=1.0,
                      prefix=f'YOU:{question}\nME:',
                      nsamples=1,
                      batch_size=1,
                      truncate='<|endoftext|>',
                      include_prefix=False, 
                      return_as_list=True,
                      top_p=0.95 
                      )[0]
                response = response.replace('(link)', '<' + random.choice(links).strip() + '>')
                response = response.replace('(emoji)', random.choice(emojis).strip())
                response = response.replace('(image)', random.choice(images).strip())
                response = response.replace('YOU:', '').replace('ME:', '')
                response = response.replace(question, ' ')
                print(question)
                print(response)
                roll = random.randint(0, 45)
            if roll == 1:
                print('Sending image!')
                await message.channel.send(response)
                await message.channel.send(random.choice(images).strip())
            elif roll == 2:
                print('Sending link!')
                await message.channel.send(response)
                await message.channel.send('<' + random.choice(links).strip() + '>')
            elif roll == 3:
                print('Sending emoji!')
                await message.channel.send(response)
                await message.channel.send(random.choice(emojis).strip())
            else:
                await message.channel.send(response)

        except Exception as e:
            print(e)
            await message.channel.send('ERROR ERROR BRAIN ON FIRE')
    await client.process_commands(message)
        

client.run(TOKEN)
