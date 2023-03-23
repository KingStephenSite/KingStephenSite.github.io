import random
import time
import os
import requests
import json
from replit import db

username = os.environ["REPL_OWNER"]

start_time = time.time()

if username in db:
  progress = {"lvl":1,"boba":False,"chinese":db[username]["chinese"],"emotional":db[username]["emotional"]}
else:
  progress = {"lvl":1,"boba":False,"chinese":False,"emotional":False}
  db[username] = progress

requests.packages.urllib3.disable_warnings()

logo = '''\u001b[31m
░█████╗░░██████╗██╗░█████╗░███╗░░██╗\u001b[34m    ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄\u001b[0m\u001b[31m
██╔══██╗██╔════╝██║██╔══██╗████╗░██║\u001b[34m    █░░░█░░░░░░░░░░▄▄░██░█\u001b[0m\u001b[31m
███████║╚█████╗░██║███████║██╔██╗██║\u001b[34m    █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█\u001b[0m\u001b[31m
██╔══██║░╚═══██╗██║██╔══██║██║╚████║\u001b[34m    █░░░▀░░░▄▄▄▄▄░░██░▀▀░█\u001b[0m\u001b[31m
██║░░██║██████╔╝██║██║░░██║██║░╚███║\u001b[34m    ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀\u001b[0m\u001b[31m
╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
██████╗░██╗███████╗███████╗██╗░█████╗░██╗░░░██╗██╗░░░░░████████╗██╗░░░██╗
██╔══██╗██║██╔════╝██╔════╝██║██╔══██╗██║░░░██║██║░░░░░╚══██╔══╝╚██╗░██╔╝
██║░░██║██║█████╗░░█████╗░░██║██║░░╚═╝██║░░░██║██║░░░░░░░░██║░░░░╚████╔╝░
██║░░██║██║██╔══╝░░██╔══╝░░██║██║░░██╗██║░░░██║██║░░░░░░░░██║░░░░░╚██╔╝░░
██████╔╝██║██║░░░░░██║░░░░░██║╚█████╔╝╚██████╔╝███████╗░░░██║░░░░░░██║░░░
╚═════╝░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░\u001b[0m
'''
print(logo)

def clear():
  print("\033c",end="")

reset = "\u001b[0m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
red = "\u001b[31m"
magenta = "\u001b[35m"
black = "\u001b[30m"

cheat = "l triangle square square circle"

input(f"Press [{blue}ENTER{reset}] To Start\n")
clear()

token = 'StevenHeGame'
def getDB():
  db = requests.get('https://gdb-server.austin2022.repl.co/get', data={"user":token},verify=False).text
  return db

def postDB(leaderboard):
  requests.post('https://gdb-server.austin2022.repl.co/update',data={"user":token, "db":json.dumps(leaderboard)})

def death(type):
  global progress
  time.sleep(0.7)
  clear()
  if type == "level_choice":
    if random.randint(0,1) == 0:
      print(f"{red}\nWhat A Failiure{reset}")
    else:
      print(f"{red}\nYou Made Your Parents Sad{reset}")
  elif type == "branch":
    print(f"{red}You Stepped On A Branch{reset}")
  elif type == "leaf":
    print(f"{red}You Were Hit By Leaf{reset}")
  elif type == "hit_aunty":
    print(f"{red}Your Hands Hurt Too Much{reset}")
  elif type == "emotional_damage":
    print(f"{red}Emotional Damage{reset}")
  elif type == "blocking":
    print(f"{red}Blocked Too Much{reset}")
  elif type == "idk":
    print(f"{red}Too Stupid To Type Correctly{reset}")
  elif type == "fall_damage":
    print(f"{red}Fall Damage{reset}")
  elif type == "poison_grass":
    print(f"{red}You Stepped On Poison Grass{reset}")
  elif type == "not_enough_hp":
    print(f"{red}Not Enough Hp{reset}")
  elif type == "social_anxiety":
    print(f"{red}Social Anxiety{reset}")
  elif type == "drank_fast":
    print(f"{red}Drank Too Fast{reset}")
  elif type == "coins":
    print(f"{red}Not Enough Coins{reset}")
  elif type == "highschool_memories":
    print(f"{red}Highschool Memories{reset}")
  elif type == "too_stupid":
    print(f"{red}Too Stupid For Harvard{reset}")
  elif type == "enemy_alerted":
    print(f"{red}Enemy Alerted{reset}")
  elif type == "adding":
    print(f"{red}Can't Add Properly{reset}")
  elif type == "cheating":
    print(f"{red}Cheating Is Bad{reset}")
  elif type == "bsian":
    print(f"{red}Bsian, Not Asian{reset}")
  elif type == "brand":
    print(f"{red}You Got Scammed{reset}")
  elif type == "fat":
    print(f"{red}Why You So FAT{reset}")
  elif type == "money":
    print(f"{red}Ate Cheap Food{reset}")
  elif type == "old_age":
    print(f"{red}You Died From Old Age{reset}")
  
  time.sleep(1.5)
  if random.randint(1,3) == 1:
    print(f"\n{blue}Omae Wa Mou, Shindeiru{reset}\n")
    progress = {"lvl":1,"boba":False,"chinese":False,"emotional":False}
    db[username] = progress
    time.sleep(1)
    os._exit(0)
  else:
    print("\nYou have died\n")
    progress = {"lvl":1,"boba":False,"chinese":db[username]["chinese"],"emotional":db[username]["emotional"]}
    db[username] = progress
  time.sleep(2)
  clear()
  menu()

def lvl1():
  global progress
  print(f"{green}You have spawned.{reset}\n")
  time.sleep(random.randint(6,33)*0.1)
  print(f"A {green}Leaf{reset} Falls!\n")
  start_time = time.time()
  action = input(f"1: {yellow}Walk Forward{reset}\n\n2: {blue}Block{reset}\n\n")
  response_time = time.time() - start_time
  if action == "1":
    death("branch")
  elif action == "2":
    if response_time < 2.1:
      print(f"\n+{blue}Block{reset}\n")
      time.sleep(1)
    else:
      death("leaf")
  else:
    death("leaf")
  time.sleep(1)
  clear()
  print(f"{blue}You have passed the warm-up level!{reset}")
  progress["lvl"] += 1
  time.sleep(2)
  clear()
  menu()

def lvl2():
  global progress
  print(f"{green}You have spawned.{reset}\n")
  time.sleep(1.3)
  print(f"{red}You Meet Aunty!{reset}\n")
  time.sleep(1.7)
  start_time = time.time()
  action = input(f"1: {yellow}Hit Aunty{reset}\n\n2: {blue}Block{reset}\n\n")
  response_time = time.time() - start_time
  if action == "1":
    death("hit_aunty")
  elif action == "2":
    if response_time < 1.9:
      print(f"\n{red}Aunty:{reset} Hello "+username+f". Since when did you grow so {red}fat{reset}?")
      time.sleep(2)
      print(f"\n+{blue}Block{reset}\n")
      time.sleep(1)
    else:
      print(f"\n{red}Aunty:{reset} Hello "+username+f". Since when did you grow so {red}fat{reset}?")
      time.sleep(1.5)
      death("emotional_damage")
  else:
    print(f"{red}Aunty:{reset} Hello "+username+". Since when did you grow so fat?")
    time.sleep(1.5)
    death("emotional_damage")
  clear()
  time.sleep(0.7)
  print(f"{red}Aunty:{reset} Hmph, not bad.\n")
  time.sleep(1)
  action = input(f"1: {yellow}Insult Aunty{reset}\n\n2: {blue}Block{reset}\n\n")
  if action == "1":
    insult = input(f"\nWhich Insult?\n\n1: {blue}I know how to code!{reset}\n\n2: You look {red}old{reset}!\n\n")
    if insult == "1":
      print("\n"+blue+username+f"{reset}: {blue}I know how to code!{reset}\n")
      time.sleep(1)
      print(f"{red}Aunty:{reset} What a {red}nerd{reset}.")
      time.sleep(0.85)
      death("emotional_damage")
    elif insult == "2":
      print("\n"+blue+username+f"{reset}: You look {red}old{reset}!\n")
      time.sleep(1)
      print(f"{red}-1000{reset} Dmg!")
      time.sleep(2.2)
      clear()
      print(f"{blue}You have defeated Aunty!{reset}")
      progress["lvl"] += 1
      time.sleep(2)
      clear()
      menu()
  elif action == "2":
    death("blocking")
  else:
    death("idk")
'''
repl = os.environ["REPL_SLUG"]
if repl != "Steven-Hes-ASIAN-Difficulty-Game":
  os._exit(0)
'''
def lvl3():
  global progress
  print(f"{green}You have spawned at the city park.{reset}\n")
  time.sleep(1)
  action = input(f"1: Cross the {green}street{reset}\n\n2: {yellow}Walk forwards{reset}\n\n3: {blue}Block{reset}\n\n")
  if action == "1":
    print(f"\n{red}You step onto the street...{reset}\n\n")
    time.sleep(1.7)
    death("fall_damage")
  elif action == "2":
    print("\nYou walk forwards...\n\n")
    time.sleep(1.7)
    death("poison_grass")
  elif action == "3":
    pass
  else:
    death("idk")
    
  action = input("\nNow what?\n\n")
  
  if action == "1":
    print(f"\n{red}You step onto the street...{reset}\n")
    time.sleep(1.7)
    print(f"You walk into a {yellow}Boba Shop{reset} and order {blue}Milk Tea With Boba{reset}")
    time.sleep(2.1)
    if random.randint(0,2) == 0:
      death("drank_fast")
    else:
      time.sleep(1)
      print(f"{red}+69{reset} HP!\n")
      time.sleep(1.7)
    progress["boba"] = True
  elif action == "2":
    print(f"\nYou walk forwards and step on the {yellow}poison grass{reset}\n")
    time.sleep(1.2)
    print(f"\n+{blue}Block{reset}\n")
    time.sleep(1)
  elif action == "3":
    death("blocking")
  clear()
  print(f"{blue}You have completed this level!{reset}")
  progress["lvl"] += 1
  time.sleep(2)
  clear()
  menu()

def lvl4():
  global progress
  print(f"{yellow}CUTSCENE 1{reset}\n")
  time.sleep(1.3)
  print(f"{blue}You Meet Villager!{reset}\n")
  time.sleep(1.7)
  start_time = time.time()
  action = input(f"1: {green}Do Nothing{reset}\n\n2: {blue}Block{reset}\n\n3: {yellow}Talk To Villager{reset}\n\n")
  response_time = time.time() - start_time
  time.sleep(0.8)
  if action == "1":
    print(f"\n{yellow}Villager:{reset} Is that you?")
    time.sleep(0.8)
    death("emotional_damage")
  elif action == "2":
    print(f"\n{yellow}Villager:{reset} Is that you?")
    time.sleep(0.4)
    if response_time < 2:
      print(f"\n+{blue}Block{reset}\n")
      time.sleep(1)
    else:
      time.sleep(0.4)
      death("emotional_damage")
    print(f"\n{yellow}Villager:{reset} Well, whatever. Take this {blue}Spear{reset} which will help\nyou defeat the {red}Main Character{reset}!\n")
    time.sleep(3)
    print(f"{yellow}Villager:{reset} {red}*chucks spear at you*{reset}\n")
    time.sleep(1.6)
    print(f"{red}-69{reset} Dmg!")
    time.sleep(1)
    if progress["boba"] == False:
      death("not_enough_hp")
    time.sleep(0.2)
    clear()
    print(f"{red}CHINESE Difficulty Unlocked!{reset}")
    db[username]["chinese"] = True
    db[username]["lvl"] = 5
    time.sleep(2.3)
    clear()
    progress["lvl"] += 1
    progress["chinese"] = True
    menu()
  elif action == "3":
    death("social_anxiety")

def lvl5():
  global progress
  print(f"{green}You have spawned.{reset}\n")
  time.sleep(1.3)
  print(f"{yellow}You Meet A Wandering Trader{reset}\n")
  time.sleep(1.7)
  start_time = time.time()
  action = input(f"2: {blue}Talk To Him{reset}\n\n1: {yellow}Block{reset}\n\n")
  response_time = time.time() - start_time
  if action == "2":
    death("social_anxiety")
  if action == "1":
    if response_time > 1.75:
      print(f"\n{yellow}Trader:{reset} For 10 Coins, you may buy this {blue}Potion{reset}")
      time.sleep(1.35)
      death("social_anxiety")
    else:
      print(f"\n{yellow}Trader:{reset} For 10 Coins, you may buy this {blue}Potion{reset}")
      time.sleep(1.2)
      print(f"\n+{blue}Block{reset}\n")
      time.sleep(1)
      action = input(f"\n1: {blue}Buy the Potion{reset}\n\n2: {yellow}Walk Away{reset}\n\n")
      if action == "1":
        death("coins")
      elif action == "2":
        if random.randint(0,1) == 0:
          clear()
          time.sleep(random.randint(18,33)*0.1)
          print(f"A {green}Leaf{reset} Falls!\n")
          start_time = time.time()
          action = input(f"1: {yellow}Walk Forward{reset}\n\n2: {blue}Block{reset}\n\n")
          response_time = time.time() - start_time
          if action == "1":
            death("branch")
          elif action == "2":
            if response_time < 2.1:
              print(f"\n+{blue}Block{reset}\n")
              time.sleep(1.4)
              clear()
            else:
              death("leaf")
          else:
            death("leaf")
          time.sleep(1)
      else:
        death("idk")
  else:
    print(f"\n{yellow}Trader:{reset} For 10 Coins, you may buy this {blue}Potion{reset}")
    time.sleep(1.35)
    death("social_anxiety")
  clear()
  print(f"{blue}You Have Passed The Warm-Up Level!")
  progress["lvl"] += 1
  time.sleep(1.7)
  clear()
  menu()

def lvl6():
  global progress
  print(f"{green}You have spawned.{reset}\n")
  time.sleep(1.3)
  print(f"{red}You Meet The Neighbor's Kid!{reset}\n")
  time.sleep(1.7)
  print(f"{red}Neighbor's Kid:{reset} Oh, hello {blue}"+username+reset+"! It seems we meet again.\n")
  time.sleep(2.5)
  print(f"{red}Neighbor's Kid:{reset} Remember when we used to be in {red}highschool{reset}?\n")
  time.sleep(1.4)
  start_time = time.time()
  action = input(f"1: {blue}Block{reset}\n\n")
  response_time = time.time() - start_time
  if response_time > 1.6:
    death("highschool_memories")
  else:
    if action != "1":
      death("idk")
    else:
      print(f"\n+{blue}Block{reset}")
      time.sleep(1)
      print(f"{red}-9000{reset} Dmg! (Highschool Memories)\n")
      time.sleep(1.8)
      clear()
      input(f"1: {green}School?{reset}\n\n2: {magenta}School?{reset}\n\n3: {red}School?{reset}\n\n4: {yellow}School?{reset}\n\n")
      print(f"\n{blue}{username}{reset}: Which college did you go to?\n")
      time.sleep(2)
      print(f"{red}Neighbor's Kid:{reset} Oh, I went to {red}Harvard{reset}.\n")
      time.sleep(0.7)
      start_time = time.time()
      action = input(f"1: {blue}Block{reset}\n\n")
      response_time = time.time() - start_time
      if response_time > 1.4:
        death("too_stupid")
      else:
        if action != "1":
          death("idk")
        time.sleep(0.6)
        print(f"\n+{blue}Block{reset}\n")
        time.sleep(1.8)
        clear()
        input(f"1: {yellow}Doctor?{reset}\n\n2: {blue}Doctor?{reset}\n\n3: {magenta}Doctor?{reset}\n\n4: {green}Doctor?{reset}\n\n")
        print(f"\n{blue}{username}{reset}: Oh, did you go to Med School?\n")
        time.sleep(1.8)
        print(f"{red}Neighbor's Kid:{reset} Oh, no. I went to {red}Law School{reset}.\n")
        time.sleep(1)
        start_time = time.time()
        action = input(f"1: {blue}Block{reset}\n\n")
        response_time = time.time() - start_time
        if response_time > 1.3:
          death("too_stupid")
        else:
          if action != "1":
            death("idk")
          time.sleep(0.6)
          print(f"\n+{blue}Block{reset}\n")
          time.sleep(1.8)
          clear()
  action = input(f"1: {red}Insult{reset}\n\n2: {blue}Block{reset}\n\n3: {red}Hit{reset} the Neighbor's Kid\n\n")
  if action == "1":
    insult = input(f"\nWhich Insult?\n\n1: I bet you play {red}Fortnite{reset} every day\n\n2: I went to {green}Hardvard{reset} (Harvard but harder)\n\n3: {magenta}Joe Mama{reset}\n\n4: {blue}I will send you to Jesus{reset}\n\n")
    if insult == "1":
      print(f"\n{red}Neighbor's Kid:{reset} I play {blue}Minecraft{reset}.")
      time.sleep(2)
      death("emotional_damage")
    elif insult == "2":
      print(f"\n{red}Neighbor's Kid:{reset} I haven't even heard of that school.")
      time.sleep(2)
      death("emotional_damage")
    elif insult == "3":
      print(f"\n{red}Neighbor's Kid:{reset} What a little kid.")
      time.sleep(2)
      death("emotional_damage")
    elif insult == "4":
      print(f"\n{red}-99999{reset} Dmg!")
      time.sleep(2)
      clear()
      print(f"{red}EMOTIONAL DAMAGE Difficulty Unlocked!{reset}")
      db[username]["emotional"] = True
      db[username]["lvl"] = 7
      progress["lvl"] += 1
      progress["emotional"] = True
      time.sleep(2)
      clear()
      menu()
    else:
      death("idk")
  elif action == "2":
    death("blocking")
  elif action == "3":
    death("hit_aunty")
  else:
    death("idk")

def lvl7():
  global progress
  print(f"{green}You have spawned.{reset}\n")
  time.sleep(random.randint(5,50)*0.1)
  print(f"{red}Guard:{reset} (Looks in your direction)\n")
  start_time = time.time()
  action = input(f"1: {yellow}Hide Behind {green}Tree{reset}\n\n2: {blue}Block{reset}\n\n")
  response_time = time.time() - start_time
  if action == "2":
    time.sleep(0.6)
    print(f"\n{red}Guard:{reset} Hey, um, HQ? I think there's an enemy standing there.\n")
    time.sleep(1.7)
    death("enemy_alerted")
  elif action == "1":
    time.sleep(random.randint(17,50)*0.1)
    random_move = random.randint(0,1)
    if random_move == 0:
      print(f"\n{red}Guard:{reset} (Looks to the left of the {green}tree{reset})\n")
    else:
      print(f"\n{red}Guard:{reset} (Looks to the right of the {green}tree{reset})\n")
    time.sleep(0.7)
    start_time = time.time()
  action = input(f"1: Turn to the {red}RIGHT{reset}\n\n2: Turn to the {blue}LEFT{reset}\n\n")
  if action != "1" and action != "2":
    death("enemy_alerted")
  if random_move == 0 and action == "2":
    death("enemy_alerted")
  elif random_move == 1 and action == "1":
    death("enemy_alerted")
  response_time = time.time() - start_time
  if response_time > random.randint(15,23)*0.1:
    death("enemy_alerted")
  time.sleep(1)
  clear()
  print(f"{red}Guard:{reset} Huuh. Not bad.\n")
  time.sleep(random.randint(17,50)*0.1)
  random_move = random.randint(0,1)
  if random_move == 0:
    print(f"\n{red}Guard:{reset} (Looks to the left of the {green}tree{reset})\n")
  else:
    print(f"\n{red}Guard:{reset} (Looks to the right of the {green}tree{reset})\n")
  time.sleep(1.3)
  start_time = time.time()
  action = input(f"1: Turn to the {red}LEFT{reset}\n\n2: Turn to the {blue}RIGHT{reset}\n\n")
  if action != "1" and action != "2":
    death("enemy_alerted")
  if random_move == 0 and action == "1":
    death("enemy_alerted")
  elif random_move == 1 and action == "2":
    death("enemy_alerted")
  response_time = time.time() - start_time
  if response_time > random.randint(15,23)*0.1:
    death("enemy_alerted")
  time.sleep(1)
  clear()
  time.sleep(2)
  print(f"{red}Guard:{reset} Well, I sure hope nobody's hiding behind THAT tree...\n")
  time.sleep(1.7)
  print(f"{red}Guard:{reset} Because if they did, they would have {red}NEGATIVE IQ{reset}\n")
  time.sleep(1.5)
  start_time = time.time()
  action = input(f"1: {blue}Block{reset}\n\n")
  response_time = time.time() - start_time
  if response_time > 1.2:
    death("emotional_damage")
  else:
    if action != "1":
      death("idk")
    time.sleep(0.6)
    print(f"\n+{blue}Block{reset}\n")
    time.sleep(1.8)
  clear()
  time.sleep(1)
  print(f"{blue}GET READY!{reset}\n")
  time.sleep(1)
  num1=random.randint(10,26)
  num2=random.randint(31,47)
  if random.randint(0,1) == 0:
    print(f"To shoot the {red}Guard{reset}, aim by solving this equation!\n")
    time.sleep(2.5)
    start_time = time.time()
    answer = input(f"{num1} + {num2} = ?\n\n")
    response_time = time.time() - start_time
    if response_time > 8:
      death("enemy_alerted")
    if int(answer) != num1+num2:
      print(f"{red}You MISSED!{reset}")
      time.sleep(1)
      death("enemy_alert")
  else:
    print(f"To shoot the {red}Guard{reset}, aim by solving this equation!\n")
    time.sleep(2.5)
    start_time = time.time()
    answer = input(f"{num2} - {num1} = ?\n\n")
    response_time = time.time() - start_time
    if response_time > 11:
      death("enemy_alerted")
    if int(answer) != num2-num1:
      print(f"{red}You MISSED!{reset}")
      time.sleep(1)
      death("enemy_alert")
  time.sleep(1)
  clear()
  time.sleep(0.65)
  print(f"{blue}Mission Success!{reset}\n")
  time.sleep(1.9)
  print(f"You have beaten {blue}Steven He's {red}ASIAN Difficulty{reset} Game!\n")
  time.sleep(2.1)
  print(f"{blue}Saving your score to the leaderboard...{reset}\n")
  try:
    leaderboard = json.loads(getDB())
    if username not in leaderboard:
      leaderboard[username] = (1, time.ctime())
      db[username]["win"] = {"win":(1, time.ctime())}
    else:
      leaderboard[username][0] += 1
      db[username]["win"][0] += 1
    postDB(leaderboard)
    print(f"{blue}Score saved!{reset} If you enjoyed this game, give us an {red}UPVOTE!{reset}\n")
  except:
    print(f"Due to {red}Replit{reset} being unstable lately, we are unable\nto save your score to the {blue}Online{reset} {yellow}Leaderboard{reset}.\n")
    time.sleep(2)
    print(f"{blue}Saving your score locally...{reset}\n")
    if "win" in db[username]:
      db[username]["win"][0] += 1
    else:
      db[username]["win"] = (1, time.ctime())
    print(f"{blue}Saved!{reset}\n")
    print(f"To save your score to the leaderboard, type 's'\nin the menu.\n")
  progress = {"lvl":1,"boba":False,"chinese":False,"emotional":False,"win":db[username]["win"]}
  db[username] = progress
  time.sleep(2)
  os._exit(0)

def us_event():
  clear()
  print(end='')
  time.sleep(1)
  print(f"{red}EVENT DIFFICULTY: {blue}A{reset}M{red}E{reset}R{blue}I{reset}C{red}A{reset}N\n")
  time.sleep(3.2)
  clear()
  print(f"{green}You have spawned.{reset}")
  time.sleep(2)
  answer = input(f"\n{red}Teacher:{reset} What is {blue}1 + 1{reset} ?\n\n")
  if answer != "11":
    time.sleep(0.7)
    death("adding")
  else:
    time.sleep(0.6)
    print(f"\n{red}Teacher:{reset} Good job. Have fun at {red}Recess!{reset}\n")
    time.sleep(1.8)
    clear()
    time.sleep(0.9)
  print(f"{red}Bully:{reset} Heheheha")
  time.sleep(1)
  print("")
  time.sleep(1)
  clear()
  menu()

def bsian_event(): # make this harder
  geography = False
  english = False
  clear()
  print(end='')
  time.sleep(1)
  print(f"{red}EVENT DIFFICULTY: {yellow}BSIAN{reset}\n")
  time.sleep(3.2)
  clear()
  print(f"{green}You have spawned.{reset}")
  time.sleep(2)
  clear()
  answer = input(f"{yellow}GEOGRAPHY TEST:{reset}\n\nWhat is the capital city of Bermuda?\n\n")
  if answer == "Hamilton" or answer == "hamilton":
    geography = True
  time.sleep(1)
  print("\n...\n")
  time.sleep(1)
  clear()
  answer = input(f"{blue}ENGLISH TEST:{reset}\n\nWhat is the definition of \n{red}supercalifragilisticexpialidocious{reset}?\n\n")
  if answer == "Extraordinarily good; wonderful" or answer == "Extraordinarily good" or answer == "Wonderful" or answer == "extraordinarily good; wonderful" or answer == "extraordinarily good" or answer == "wonderful":
    english = True
  time.sleep(1)
  print("\n...\n")
  time.sleep(1)
  clear()
  print(f"{blue}Your REPORT CARD:{reset}\n")
  time.sleep(1)
  if geography == False:
    print(f"{yellow}Geography{reset}: {red}B{reset}")
  else:
    print(f"{yellow}Geography{reset}: {blue}A{reset}")
  print()
  time.sleep(1)
  if english == False:
    print(f"{blue}English{reset}: {red}B{reset}")
  else:
    print(f"{blue}English{reset}: {blue}A{reset}")
  time.sleep(2)
  if geography == True and english == True:
    clear()
    print(f"{blue}You have beaten the BSIAN EVENT!{reset}")
  else:
    death("bsian")
  time.sleep(2)
  clear()
  menu()

def brand_event():
  clear()
  print(f"{red}EVENT DIFFICULTY: {red}OFF-BRAND{reset}\n")
  time.sleep(1)
  clear()
  time.sleep(1.5)
  print(f"{green}You walk into a store:{reset}\n")
  time.sleep(1.5)
  print(f"{blue}Manager:{reset} Welcome to our store, {blue}{username}{reset}.\n")
  time.sleep(1)
  print(f"{blue}Manager:{reset} Feel free to check out some of our items.\n")
  time.sleep(0.5)
  input(f"[{blue}ENTER{reset}]")
  clear()
  store_items = {
    "Mountain View":"Mountain Dew",
    "Crocodile Help":"Gatorade",
    "Pephere":"Pepsi",
    "Kitdog":"Kitkat",
    "Fire Milk":"Ice Cream",
    "Hehim":"Hershey",
    "Jacob Nuts":"Quaker Oats",
    "5 Hour Depression":"5 Hour Energy"
  }
  item_list = [store_items[i].lower() for i in store_items]
  print(f"\033[2m(Tip: Guess the real brand name!){reset}\n")
  time.sleep(2.3)
  answers = []
  for i in store_items:
    clear()
    answer = input(f"{blue}Manager:{reset} Would you like some {red}{i}{reset}?\n\n{blue}{username}:{reset} You mean {blue}")
    answers.append(answer.lower())
  for i in answers:
    if i not in item_list:
      death("brand")
  clear()
  print(f"{blue}You have beaten the OFF-BRAND EVENT!{reset}")
  time.sleep(2)
  clear()
  menu()

def buffet_event():
  clear()
  print(f"{red}EVENT DIFFICULTY: {yellow}BUFFET{reset}\n")
  time.sleep(1)
  clear()
  time.sleep(1.5)
  print(f"{green}You walk into the Steven Buffet...{reset}")
  time.sleep(1.5)
  buffet_map = f'''
  +[{blue}1{reset}]+++++++++++++++++++++[{blue}5{reset}]+
  ++++++++++++[{red}CRAB{reset}]+++++++++++
  +[{blue}2{reset}]+++++++++++++++++++++[{blue}6{reset}]+
  +++++++++++[{green}SALAD{reset}]+++++++++++
  +[{blue}3{reset}]+++++++++++++++++++++[{blue}7{reset}]+
  +++++++++++[{yellow}FRIED{reset}]+++++++++++
  +[{blue}4{reset}]+++++++++++++++++++++[{blue}8{reset}]+
  '''
  
  table = input(buffet_map+"\n\nChoose a table: ")
  if table == "5":
    points = 3
  elif table == "1":
    points = 2
  elif table == "6":
    points = 5
  elif table == "2":
    points = 4
  elif table == "7" or table =="3":
    points = -1
  else:
    points = -4

  health = 5
  cost = 0
  appetite = 1
  full = False
  fullness = 0
  dishes = 0
  
  print("\nGet Ready!")
  time.sleep(1.5)
  clear()
  
  buffet_menu = f''' {green}SALADS{reset}...          {blue}SEAFOODS{reset}...           {yellow}FRIED{reset}...
  1: Caesar Salad    4: Marinated Shrimp   7: Tempura Shrimp
  2: Greek Salad     5: Octopus Legs       8: Fried Chicken
  3: Chicken Salad   6: Alaskan King Crab  9: Seasoned Fries
  '''
  
  while full == False:
    if fullness <= 16*(appetite/2) and health > 0 and dishes < 4+round(points/2):
      print(buffet_menu)
      dish = input("Choose a dish: ")
      time.sleep(0.4)
      dishes += 1
      if dish == "1" or dish == "2":
        health += 2
        if table == "6" or table == "2":
          health += 1
        fullness += 1
        cost += 5
        print("Healthy Choice!")
      elif dish == "3":
        health += 1
        fullness += 2
        appetite += 1
        cost += 6
        print("Good Choice!")
      elif dish == "4":
        fullness += 2
        appetite += 1
        cost += 8
        if table == "5" or table == "1":
          fullness += 1
        print("Tasty!")
      elif dish == "5":
        fullness += 2
        appetite += 1
        cost += 8
        if table == "5" or table == "1":
          fullness += 1
        print("Very Unique!")
      elif dish == "6":
        fullness += 3
        appetite += 2
        cost += 14
        if table == "5" or table == "1":
          fullness += 1
        print("Nothing Beats King Crab!")
      elif dish == "7":
        fullness += 2
        health -= 1
        appetite += 3
        cost += 6
        print("Crunch, Crunch!")
      elif dish == "8":
        fullness += 3
        health -= 2
        appetite += 3
        cost += 6
        print("Good ol' Fried Chicken!")
      elif dish == "9":
        fullness += 2
        health -= 1
        appetite += 3
        cost += 3
        print("Very Flavorful!")
      time.sleep(1.2)
      clear()
    else:
      clear()
      print("You are full...")
      time.sleep(1)
      print(f"{red}Health: {health}{reset}")
      time.sleep(0.5)
      print(f"{green}Cost: {cost}{reset}")
      time.sleep(0.5)
      print(f"{yellow}Fullness: {fullness}{reset}")
      time.sleep(0.5)
      print(f"{blue}Dishes: {dishes}{reset}")
      time.sleep(2)
      if health <= 5:
        death("fat")
      elif cost < 69:
        death("money")
      clear()
      print(f"{blue}You have beaten the BUFFET Event!")
      time.sleep(1.8)
      clear()
      menu()

start_time = time.time()

def menu():
  day = time.ctime().split()[0]
  if day == "Mon":
    day = "Monday"
    event = "US"
    diff = "Medium"
  elif day == "Tue":
    day = "Tuesday"
    event = "Off Brand"
    diff = "Normal"
  elif day == "Wed":
    day = "Wednesday"
    event = "Bsian"
    diff = "Easy"
  elif day == "Thu":
    day = "Thursday"
    event = "Buffet"
    diff = "Normal Difficulty"
  elif day == "Fri":
    day = "Friday"
    event = "US"
    diff = "Medium"
  elif day == "Sat":
    day = "Saturday"
    event = "Off Brand"
    diff = "Normal"
  elif day == "Sun":
    day = "Sunday"
    event = "Bsian"
    diff = "Easy"
  
  
  # make sure to add level names!
  if progress["lvl"] == 1:
    if progress["chinese"] == True and progress["emotional"] == False:
      print(f"{yellow}LEVEL{reset}",5,"\n")
    elif progress["chinese"] == True and progress["emotional"] == True:
      print(f"{yellow}LEVEL{reset}",7,"\n")
    else:
      print(f"{yellow}LEVEL{reset}",progress["lvl"],"\n")
  else:
    print(f"{yellow}LEVEL{reset}",progress["lvl"],"\n")
  print(f"{blue}0: Leaderboard{reset}\n\n{magenta}s: Upload data to Leaderboard{reset}\n\n{red}e: Events{reset}\n")
  if progress["chinese"] == False:
    print(f"Choose a difficulty:\n\n{green}1: Easy\n\n{yellow}2: Normal\n\n{blue}3: Hard\n\n{red}4: ASIAN{reset}\n")
  elif progress["chinese"] == True and progress["emotional"] == False:
    print(f"Choose a difficulty:\n\n{green}1: Normal\n\n{yellow}2: Hard\n\n{blue}3: ASIAN\n\n{red}4: CHINESE{reset}\n")
  else:
    print(f"Choose a difficulty:\n\n{green}1: Hard\n\n{yellow}2: ASIAN\n\n{blue}3: CHINESE\n\n{red}4: EMOTIONAL DAMAGE{reset}\n")
    
  difficulty = input()

  if time.time() - start_time > 540:
    death("old_age")

  if difficulty == "e":
    clear()
    print(f"{blue}{day}{reset} {red} Events:{reset}\n")
    time.sleep(1.2)
    print(f"{red}{event}{reset} Event Ongoing!\n[{blue}{diff} Difficulty{reset}]\n\n\033[2m(Type {blue}{event.lower()}{reset} \033[2min the menu to try!){reset}\n")
    time.sleep(1)
    print(f"{blue}All Events{reset}:\nMonday........... U{blue}S{reset} Event\nTuesday... {green}Off Brand{reset} Event\nWednesday..... {yellow}Bsian{reset} Event\nThursday..... {red}Buffet{reset} Event\nFriday........... U{blue}S{reset} Event\nSaturday.. {green}Off Brand{reset} Event\nSunday........ {yellow}Bsian{reset} Event\n")
    time.sleep(0.5)
    input(f"[{blue}ENTER{reset}]")
    clear()
    menu()
  
  elif difficulty == "s":
    clear()
    if username not in db:
      print(f"You don't have any {blue}Game Saves{reset} yet!")
      time.sleep(2)
    else:
      print(f"{blue}Saving...\n")
      try:
        leaderboard = json.loads(getDB())
        leaderboard[username] = db[username]["win"].value
        postDB(leaderboard)
      except:
        print(f"Sorry, due to {red}Replit{reset} being {blue}unstable{reset} recently, we cannot\nsave your {blue}Score Online{reset}.\nPlease try again. (Works 50% of the time)\n")
        time.sleep(2.7)
    clear()
    menu()

  if difficulty == "0":
    clear()
    print(f"{blue}Loading...{reset}\n")
    try:
      leaderboard = json.loads(getDB())
    except:
      print(f"Sorry, due to {red}Replit{reset} being {blue}unstable{reset} recently, we cannot\nget the {blue}Online{reset} {yellow}Leaderboard{reset}. Please try again.\n")
      if username in db:
        leaderboard = {username:[db[username]["win"][0],db[username]["win"][1]],"Steven He":[1,time.ctime()],"5 Year Old In China":[1,time.ctime()]}
      else:
        leaderboard = {"Steven He":[1,time.ctime()],"5 Year Old In China":[1,time.ctime()]}
    leaderboard = sorted(leaderboard.items(), key = lambda kv:(kv[1], kv[0][0]), reverse = True)
    if len(leaderboard) == 0:
      print(f"{blue}No one has beaten the game yet!{reset} Who will be first?\n")
    else:
      clear()
      for i in leaderboard:
        time.sleep(0.5)
        print(f"[{blue}{i[0]}{reset}] - {red}{i[1][0]}{reset} Wins\n\033[2mBeat game on {yellow}{i[1][1]}{reset}")
    time.sleep(0.5)
    input(f"Press [{blue}ENTER{reset}] to return\n")
    clear()
    menu()

  if difficulty == "us":
    if day == "Monday" or day == "Friday":
      us_event()
      return
  elif difficulty == "bsian":
    if day == "Wednesday" or day == "Sunday":
      bsian_event()
      return
  elif difficulty == "off brand":
    if day == "Tuesday" or day == "Saturday":
      brand_event()
      return
  elif difficulty == "buffet":
    #if day == "Thursday":
    buffet_event()
    return
  
  try:
    if int(difficulty) < 4:
      death("level_choice")
  except:
    if difficulty != cheat:
      print("Unknown input.")
      time.sleep(1.3)
      clear()
      menu()
    else:
      time.sleep(0.7)
      clear()
      print(f"Woah, woah, woah! Is that a {red}cheat code?{reset}\n")
      time.sleep(2.3)
      print(f"Hmm, it seems like you're on the {red}wrong level{reset}!\n")
      time.sleep(2.5)
      print(f"Let's take you back to {green}Easy{reset} mode!")
      time.sleep(2)
      clear()
      time.sleep(0.9)
      death("cheating")
  
  clear()
  if progress["chinese"] == False:
    if progress["lvl"] == 1:
      lvl1()
    elif progress["lvl"] == 2:
      lvl2()
    elif progress["lvl"] == 3:
      lvl3()
    elif progress["lvl"] == 4:
      lvl4()
  if progress["chinese"] == True and progress["emotional"] == False:
    if progress["lvl"] == 5:
      lvl5()
    elif progress["lvl"] == 6:
      lvl6()
    else:
      progress["lvl"] = 5
      lvl5()
  if progress["emotional"] == True:
    lvl7()

menu()
