import random
import colorama
import emoji
from colorama import Fore, Style
from emoji import emojize

randoColors=list(vars(colorama.Fore).values())
randoColors.remove(Fore.WHITE)
randoColors.remove(Fore.BLACK)
proceed='y'
goodEnding="WOW! WHAT AN INCREDIBLE NAME, I LOVE YOU BRO! GOOD JOB!!! 100/10!!!!"
print("WELCOME to the AMAZING AI NAME RATING MACHINE 5000 ALPHA 9.1.3!!!")
while proceed != 'n':
  print(Fore.RED + "Please enter a name you want to rate:")
  name=input()
  if name.lower() == "taylor" or name.lower == "vandenberg" or name.lower() == "taylor vandenberg":
    colorMessage = [random.choice(randoColors) + char for char in goodEnding]
    print(''.join(colorMessage))
  else:
    print(Fore.WHITE + "Erm... That name kinda sucks bruh... I'll get rid of that for you...\n\n\n")
    nameLength=len(name)
    print(name)
    for i in name:
      print(emojize(":fire:"), end='')
    
    print("\n\n\n...\nAlright, I cremated it. You're welcome.")
  print(Fore.WHITE + "Would you like me to rate another name? (y/n)")
  proceed=input()
print("Thank you for using the AI NAME RATING MACHINE 5000!")
exit()