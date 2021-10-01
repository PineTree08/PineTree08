import discord, asyncio, pytz, datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇을 실행합니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("친목"))

@client.event
async def on_message(message):
    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.create_instant_invite:
            await message.delete()
            user = message.mentions[0]

            role = discord.utils.get(message.guild.roles, name = '유저')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="인증하는 방이 아닙니다.", description = message.author.mention + "", color = 0xff0000))

client.run('ODg5MDQ1NjUzMTkwMjQ2NDAx.YUbiSQ.zKDROXqVq_Y7U-pRN96aHwN5fSM')