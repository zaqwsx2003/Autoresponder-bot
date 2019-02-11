import urllib
import bs4
import discord
import asyncio
import random
import os
import sys
import json




client = discord.Client()

@client.event

async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------")
    await client.change_presence(game=discord.Game(name='띠독교 전도중', type=1))


class Request(object):
    pass


@client.event
async def on_message(message, clivent=None):
    if message.content.startswith('!띠독교 안녕하세요'):
        await client.send_message(message.channel, "안녕나는 띠독교를 전도하는 전도사라구해 도움말은 !띠독교 도움말 이야")

    if message.content.startswith('!띠독교 도움말'):
        await client.send_message(message.channel, "!띠독교 ~~ 로적어줘야해")
        await client.send_message(message.channel, "띠독교 안녕 : 인사하기")
        await client.send_message(message.channel, "띠독교 음식추천 : 음식을 추천해준다")
        await client.send_message(message.channel, "띠독교 추천게임 : 게임을 추천해준다")
        await client.send_message(message.channel, "띠독교 놀자 : 놀아줄 겁니다")
        await client.send_message(message.channel, "띠독교 싫어 : 싫어할겁니다.")
        await client.send_message(message.channel, "띠독교 들어와 : 방으로 들어옵니다.")
        await client.send_message(message.channel, "띠독교 나가 : 방에서 탈주합니다.")
        await client.send_message(message.channel, "띠독교 용한모금 : 좋은말을 해줍니다.")
        await client.send_message(message.channel, "띠독교 용자돌림 : 용으로 시작하는말을 해줄것입니다.")


    if message.content.startswith('!띠독교 음식추천'):
        food = "카레 설렁탕 오리훈제 연어 닭갈비 초밥 우동 장어구이 라면 굶기 치킨 굶기 파르페 도넛"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!띠독교 추천게임'):
        game = "리그오브레전드 모두의마블 서든어택 카트라이더 메이플스토리 오버워치 레인보우식스 마인크래프트 배틀그라운드 로스트아크 사이퍼즈 GTA5 테트리스 스타듀벨리 히오스"
        gamechoice = game.split(" ")
        gamenumber = random.randint(1, len(gamechoice))
        gameresult = gamechoice[gamenumber-1]
        await client.send_message(message.channel, gameresult)

    if message.content.startswith('!띠독교 놀자'):
        help = "거부합니다 시러요 넹! 귀찮아요 여물어 전도중~입니다. ?시룬?뒝? 싫어 전도하자 전도놀이하자"
        helpchoice = help.split(" ")
        helpnumber = random.randint(1, len(helpchoice))
        helpresult = helpchoice[helpnumber - 1]
        await client.send_message(message.channel, helpresult)

    if message.content.startswith('!띠독교 이모티콘'):
        ov = "-3- •ө• 0.< >.0 ㅗ.ㅗ ㅜㅜ ㅠㅠ >< >_< >~< +{_}+ @*@ ^*^ !+_)+!"
        ovchoice = ov.split(" ")
        ovnumber = random.randint(1, len(ovchoice))
        ovresult = ovchoice[ovnumber - 1]
        await client.send_message(message.channel, ovresult)

    if message.content.startswith('!띠독교 싫어'):
        help1 = "저리-가세요 회계-하시길... 저도요 손절"
        help1choice = help1.split(" ")
        help1number = random.randint(1, len(help1choice))
        help1result = help1choice[help1number - 1]
        await client.send_message(message.channel, help1result)



    if message.content.startswith('!띠독교 주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith("!띠독교 들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client == None:
            await client.send_message(message.channel, '들어왔습니다')
            await client.join_voice_channel(channel)
        else:
            await client.send_message(message.channel, '봇이 이미 들어와있습니다.')

    if message.content.startswith("!띠독교 나가"):
            server = message.server
            voice_client = client.voice_client_in(server)
            print("나가")
            print(voice_client)
            print("나가")
            if voice_client == None:
                await client.send_message(message.channel, '띠독교(님)이 음성채널에 접속하지 않았습니다.')
                pass
            else:
                await client.send_message(message.channel, '나갑니다')
                await voice_client.disconnect()

    if message.content.startswith('!띠독교 용한모금'):
        help0 = "세상은-넓고용자-돌림은-많다 용이-나룡으로-끝나는-단어는-다우를-붙인다"
        help0choice = help0.split(" ")
        help0number = random.randint(1, len(help0choice))
        help0result = help0choice[help0number - 1]
        await client.send_message(message.channel, help0result)

    if message.content.startswith('!띠독교 용자돌림'):
        help9 = "띠용우 이용우 준용우 느그용우 우리용우 사용우 용우초등학교 용우물 애풍용우 논산용우친목회 용우골 용우골재"
        help9choice = help9.split(" ")
        help9number = random.randint(1, len(help9choice))
        help9result = help9choice[help9number - 1]
        await client.send_message(message.channel, help9result)



















































































































access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
