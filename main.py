import random
import os
import sys
from time import sleep

# Slow function
# It will print character by character!
def slow(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.1)
# Colors
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"


slow(bright_cyan + "Hello to " + bright_yellow + "Mides Company!")
slow(bright_cyan + "\nWho's Mides?\nMides is a character who needs to change the world to " + bright_yellow + "GOLD!")

os.system("clear")

length = int(input("How many times you need to repeat the game?\n> "))
for i in range(length):
  os.system("clear")
  name = random.choice(['James', 'Carlos', 'Kevin', 'Bill', 'Jeff', 'Mat', 'Tim'])
  slow(bright_red + "A new person need to make for him GOLD!!\nHe is " + name + "!")
  os.system("clear")
  yes_or_no = input("Need to help him?(y/n)\n> ")
  if yes_or_no == "y":
    slow(bright_blue + "You helped " + name + "!")
  elif yes_or_no == "n":
    slow(bright_red + "You rejected " + name + "... :(")
  else:
    slow(red + "INVALID!")


# YAY! DONE >:)
