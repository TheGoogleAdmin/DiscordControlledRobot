from discord.ext import commands
import discord
import time
from gpiozero import CamJamKitRobot
 
robot = CamJamKitRobot()
 
bot = commands.Bot(command_prefix=',')
 
#currentcommand = ['a', 'b']
 
@bot.event
async def on_ready():
    print('Bot is ready.')
 
 
def move(currentcommand):
 
    coms = currentcommand.split(":")
    direction = coms[0]
    duration = coms[1]
    if direction.lower() == "left":
        robot.left()
        time.sleep(float(duration))
        print("go left")
    if direction.lower() == "right":
        robot.right()
        time.sleep(float(duration))
        print("go right")
    if direction.lower() == "forward":
        robot.forward()
        time.sleep(float(duration))
        print("go forward")
    if direction.lower() == "back":
        robot.backward()
        time.sleep(float(duration))
        print("go back")
    print("for time " + str(duration))
    robot.stop()
 
@bot.event
async def on_message(message):
 
    if message.content.startswith(',journey'):
        #!journey MOVE:TIME,MOVE:TIME
        commandlist = message.content
        commandlist = commandlist.split(" ")
        commandlist = commandlist[1]
        commandlist = commandlist.split(",")
        x = 0
        while x < len(commandlist):
            currentcommand = commandlist[x]
 
            move(currentcommand=currentcommand)
            x = x + 1
 
bot.run('BOT TOKEN IN HERE')
