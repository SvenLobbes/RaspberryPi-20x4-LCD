from __future__ import division
from email import message
import discord
import os
import asyncio

#imports for lcd
from RPLCD import *
from RPLCD.i2c import CharLCD

from time import sleep

#vars for lcd
lcd = CharLCD('PCF8574', 0x27)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def lcd_clear():
    lcd.cursor_pos = (0,0)
    lcd.write_string('                    ')
    lcd.cursor_pos = (1,0)
    lcd.write_string('                    ')
    lcd.cursor_pos = (2,0)
    lcd.write_string('                    ')
    lcd.cursor_pos = (3,0)
    lcd.write_string('                    ')

def calculate_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = (seconds % 3600) %60

    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def lcd_Test():
    lcd.cursor_pos = (0,0)
    lcd.write_string('Hello World')
    lcd.cursor_pos = (2,0)
    lcd.write_string('If you can read this')
    lcd.cursor_pos = (3,0)
    lcd.write_string('It Works!')

async def lcd_Coding(message):
    lcd.cursor_pos = (0,0)
    lcd.write_string('Coding Session')
    lcd.cursor_pos = (1,0)
    lcd.write_string('pls dont disturb')
    lcd.cursor_pos = (2,0)
    lcd.write_string('coding since:')

    #timer
    k = 0
    BREAKOUT = 0
    while BREAKOUT != 1:
        if message.content.startswith('!stop'):
             BREAKOUT = 1
        await asyncio.sleep(1)
        k = k + 1
        lcd.cursor_pos = (3,6)
        lcd.write_string(calculate_time(k))

    BREAKOUT = 0

def lcd_Meeting(message):
    #Code for LCD
        lcd.cursor_pos = (0,0)
        lcd.write_string('In a Meeting')
        lcd.cursor_pos = (1,0)
        lcd.write_string('pls dont disturb')
        lcd.cursor_pos = (2,0)
        lcd.write_string('running since:')

        #Timer
        k = 0

        while 1 == 1:

            sleep(1)
            k = k +1
            lcd.cursor_pos = (3,0)
            lcd.write_string(calculate_time(k))

        BREAKOUT = 0

def lcd_DoNotDisturb():
    lcd.cursor_pos = (0,0)
    lcd.write_string('PLS DONT DISTURB!')

def lcd_ImFree():
    lcd.cursor_pos = (0,0)
    lcd.write_string('Im Free')
    lcd.cursor_pos = (2,0)
    lcd.write_string('You can')
    lcd.curosor_pos = (3,0)
    lcd.write_string('come in!')

@client.event
async def on_ready():
    print('Start {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Hello, this is the menu for the LCD of the Raspberry Pi:')
        await message.channel.send('!lcd_Test')
        await message.channel.send('!lcd_ClearLCD')
        await message.channel.send('!lcd_Coding')
        await message.channel.send('!lcd_Meeting')
        await message.channel.send('!lcd_DoNotDisturb')
        await message.channel.send('!lcd_ImFree')

    if message.content.startswith('!lcd_Test'):
        print('lcd_Test')
        await message.channel.send('Printing on LCD')

        #Code for LCD
        lcd_Test()

    if message.content.startswith('!lcd_ClearLCD'):
        print('Clean the LCD!')
        await message.channel.send('Clear LCD')

        #Code for LCD
        lcd_clear()

    if message.content.startswith('!lcd_Coding'):
        print('lcd_Coding')
        await message.channel.send('Printing on LCD')
        await message.channel.send('send !stop for ending session')

        #Code for LCD
        asyncio.create_task(lcd_Coding(message))

    if message.content.startswith('!lcd_Meeting'):
        print('lcd_Meeting')
        await message.channel.send('Printing on LCD')

        #Code for LCD
        asyncio.create_task(lcd_Meeting(message))

    if message.content.startswith('!lcd_DoNotDisturb'):
        print('lcd_DoNotDisturb')

        lcd_DoNotDisturb()

    if message.content.startswith('!lcd_ImFree'):
        print('lcd_ImFree')
        lcd_ImFree()

client.run('') #INSERT TOKEN OF BOT

