
# timed typing text function
import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.015)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

    

#introduction 
print("\n")
typingPrint("Welcome! You have recently opened your own bakery in an unknown suburb.\n")
time.sleep(1)
typingPrint("Business is not thriving yet because you have not made yourself known to the public.\n")
time.sleep(1)
typingPrint("Make choices for the business and create a prosperous bakery with lots of customers and a perfect five star ranking!\n")
time.sleep(1)
typingPrint("Beware, you may end up with a negative score if you make poor decisions!\n\n")
time.sleep(1)

customerCount = 0
stars = 0

print("But first? What's the name of your bakery?")
bakeryName = typingInput(">")
print(bakeryName,"Bakery? That's a lovely name!\n")
time.sleep(1)

typingPrint("You will start off with 0 customers and a 0 star ranking.\n")
time.sleep(1)
typingPrint("Build your way to success. Good luck!\n\n")
time.sleep(1)

print("Customers:",customerCount)
print("Star Ranking:",stars,"Stars\n\n")
time.sleep(1)

#endings
def ending1():
  global typingPrint
  global customerCount
  global stars

  print("\n")
  typingPrint("Business is booming, Everything's going great!\n")
  time.sleep(1)
  print(r"""                 ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ") """)
  time.sleep(1)
  typingPrint("???\n")
  typingPrint("The dead rat's family came to invade you after you killed its relative.\n")
  time.sleep(1)
  typingPrint("Your bakery became infested with rats.\n")
  time.sleep(1)
  typingPrint("Neighbouring cities have experienced an alarming surplus of rats and the blame has been put on you.\n")
  time.sleep(1)
  typingPrint("You became sad, packed your bags, and fled the country.\n")
  time.sleep(1)

  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)

def ending2():
  global typingPrint
  global customerCount
  global stars

  print("\n")
  typingPrint("Your business failed. You had to close down due to your poor reputation.\n")
  time.sleep(1)
  typingPrint("???\n")
  typingPrint("The health inspector's rats came to haunt you.\n\n")
  time.sleep(1)
  print(r"""   
    ( (^)-~-(^)
__,-.\_( 6 6 )__,-.___
  'M'   \   /   'M'
hjw      >o< 

""")
  time.sleep(1)
  typingPrint("You live in fear every night.\n")
  time.sleep(1)
  typingPrint("What a sad life.\n")
  time.sleep(1)

  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'  
   
    """)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending3():
  global customerCount
  global typingPrint
  global stars

  print("\n")
  typingPrint("Congratulations! You have reached the highest level of success.\n")
  time.sleep(1)
  typingPrint("Local citizens are amused by this shocking collaboration between you and your rat friends.\n\n")
  time.sleep(1)
  print(r"""
       _ _
  (\  (c)_)_
   \\  )  ee\_
    )) \ \___=D=
   ((  / _ / \_
    \\/ (/|  |\)
     \    /_ |)
     ""''''''''
  
   """)
  time.sleep(1)
  typingPrint("You have been named the 'local trendsetter' and have gained global recognition!\n")
  time.sleep(1)
  typingPrint("Nice work!\n")
  time.sleep(1)
  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'  
   
    """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending4():
  global customerCount
  global stars
  global typingPrint

  print("\n")
  typingPrint("Congratulations on a successful start to your bakery!\n")
  time.sleep(1)
  typingPrint("You ended up training the rats to hunt for money.\n")
  time.sleep(1)
  typingPrint("They are now your main source of revenue!\n\n")
  time.sleep(1)
  print(r"""
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
   """)
  time.sleep(1)
  typingPrint("The bakery is doing splendid with your newly accumulated assets.\n")
  time.sleep(1)
  typingPrint("Good job!\n")
  time.sleep(1)
  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending5():
  global customerCount
  global bakeryName
  global stars
  global typingPrint

  print("\n")
  time.sleep(1)
  typingPrint("Congrats! You became a walking meme!\n")
  time.sleep(1)
  typingPrint("How iconic!\n")
  time.sleep(1)
  print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⡴⠞⠛⠉⢙⡛⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⢰⠁⠀⠀⠉⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠜⢹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡶⠶⠮⠭⠵⢖⠒⠿⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡶⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣄⡀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠚⠿⡷⣄⣀⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠪⣻⣄⠀⠀⠀⣀⣀⠤⠴⠒⠚⢋⣭⣟⣯⣍⠉⠓⠒⠦⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡝⣧⠔⠋⠁⠀⣀⠤⠔⣶⣿⡿⠿⠿⠿⠍⠉⠒⠢⢤⣀⠈⠑⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡦⠤⢤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣞⣧⠤⠒⠉⠀⠀⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢲⣴⣾⣷⢤⡀⠀⠀⠀⠀⠀⠀⠀
⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⢿⣿⣧⠙⢦⠀⠀⠀⠀⠀⠀
⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⣄⡀⠀⠐⢄⠀⠀⠀⢻⡇⠀⠀⠀⠀⡠⢊⣭⣬⣭⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡀⠀⠑⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠑⢄⣀⢿⠇⠀⠀⠀⡜⣼⠟⠁⠀⠀⠉⢿⡄⠀⠀⠀⠀⣠⠤⠤⠤⣀⡀⠈⠙⡄⠀⠈⢆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣝⢦⡀⠀⣠⡞⠢⢄⠀⡜⣼⠁⣠⣴⣶⢦⡀⠀⢻⠀⠀⢀⣎⡴⠟⠛⠛⠶⣝⢦⠀⠘⡄⠀⠈⢧⠀⠀
⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⢻⡾⠋⠀⣀⣀⠁⠁⡇⢰⢿⣄⣿⣎⢷⠀⢸⡇⠀⢸⡝⢀⣤⣄⡀⠀⠙⢷⡀⠀⢱⠀⠀⠈⡇⠀
⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠈⠙⣳⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣧⠀⢀⣀⣀⡉⠱⣿⣼⣆⢿⠻⣯⡞⠀⢸⡇⠀⢸⣷⣏⢙⣿⡻⡆⠀⠀⢳⠀⠀⠀⠀⠀⢸⡀
⠀⢳⡀⠀⠀⠀⠀⠀⠉⠚⠁⠀⠀⠀⠀⠀⠉⠻⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠈⠁⠀⠀⠉⠢⠈⠛⢻⣿⠿⠛⠁⢀⣿⠇⠀⠈⣿⣿⢿⡟⣧⡷⠀⠀⢸⡄⠀⠀⠀⠀⠈⡇
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⢧⡀⠀⠀⠀⠢⠤⠔⡽⠁⠚⠉⠉⠉⢗⢷⣄⡠⣀⢻⣆⣀⣠⡿⠋⠀⠀⠀⠈⢿⡷⠿⠟⠁⠀⠀⣼⠀⠀⠀⠀⠀⠀⢱
⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠻⡄⠀⢀⣀⡤⠞⠁⠀⠀⠀⠀⠀⠘⢦⡈⠁⠀⠀⠸⡟⠉⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣤⡶⠟⠉⠙⠒⠀⠀⠀⠀⢘
⠀⠀⠀⠀⠈⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⡇⣿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣤⡀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠍⠠⠤⠒⠂⢄⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠈⠙⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⣽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣉⡿⠓⠲⠄⠀⠀⠀⠀⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣤⣄⣀⣠⣤⡤⠶⠛⣿⡀⠀⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣄⠀⠀⠉⠙⠒⠲⠤⠤⠤⣤⣤⡤⠖⠚⠁⠀⠀⠀⠀⠀⠀⠀⢰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣦⣄⡀⠀⠀⠀⢀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⡀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡱⡀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣔⢹⡉⢻⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣥⣠⣹⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣕⢄⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⠌⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⡦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠺⢕⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠤⢄⣀⣀⣀⣀⣀⣀⣠⠤⠴⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


  """)
  print(bakeryName,"Bakery is now a household name.\n\n")
  time.sleep(1)
  typingPrint("People across the world travel just to meet you and the amazing kid you hired.\n")
  time.sleep(1)
  typingPrint("Your bakery is a massive success!\n")
  time.sleep(1)
  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending6():  
  global customerCount
  global stars
  global typingPrint

  print("\n")
  time.sleep(1)
  typingPrint("...\n")
  time.sleep(1)
  typingPrint("Your bakery went instantly bankrupt.\n")
  time.sleep(1)
  typingPrint("You suffered from nightly embarrassment.\n\n")
  time.sleep(1)
  typingPrint("The random kid you hired somehow got out of the situation by befriending the bloggers.\n")
  time.sleep(1)
  typingPrint("He's the real winner in this situation.\n\n")
  time.sleep(1)

  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending7():
  global customerCount
  global stars
  global typingPrint

  print("\n")
  time.sleep(1)
  typingPrint("...\n")
  time.sleep(1)
  typingPrint("Turns out the random kid you rejected was behind all of this.\n")
  time.sleep(1)
  typingPrint("You sit in silence as you regret all your life choices.")
  time.sleep(1)
  print(r"""⠀⠀⠀⠀
                ⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠚⠉⠁⠀⠀⠉⠙⠒⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀
⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄
⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘
⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⡄⠀⠀⠀⠀⠀⢀⣶⡆⠀⢠⠇
⠀⠀⠀⠀⠀⠀⣣⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠈⠛⠁⡰⠃⠀
⠀⠀⠀⠀⢠⠞⠋⢳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀
⠀⠀⠀⣰⠋⠀⠀⠀⢷⠙⠲⢤⣀⡀⠀⠀⠀⠀⠴⠴⣆⠴⠚⠁⠀⠀⠀⠀
⠀⠀⣰⠃⠀⠀⠀⠀⠘⡇⠀⣀⣀⡉⠙⠒⠒⠒⡎⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠃⠀⠀⢶⠀⠀⠀⢳⠋⠁⠀⠙⢳⡠⠖⠚⠑⠲⡀⠀⠀⠀⠀⠀⠀⠀
⠀⡎⠀⠀⠀⠘⣆⠀⠀⠈⢧⣀⣠⠔⡺⣧⠀⡴⡖⠦⠟⢣⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⢈⡷⣄⡀⠀⠀⠀⠀⠉⢹⣾⠁⠁⠀⣠⠎⠀⠀⠀⠀⠀⠀
⠈⠀⠀⠀⠀⠀⡼⠆⠀⠉⢉⡝⠓⠦⠤⢾⠈⠓⠖⠚⢹⠀⠀⠀⠀⠀⠀⠀
⢰⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⢸⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠳⡀⠀⠀⠀⠀⠀⠀⣀⢾⠀⠀⠀⠀⣾⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠐⠢⠤⠤⠔⠚⠁⠘⣆⠀⠀⢠⠋⢧⣀⣀⡼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠁⠀⠀⠀⠁⠀⠀⠀⠀

""")
  time.sleep(1)

  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")

def ending8():
  global customerCount
  global stars
  global typingPrint

  print("\n")
  time.sleep(1)
  typingPrint("...\n")
  time.sleep(1)
  typingPrint("The random kid you rejected stops by.\n")
  time.sleep(1)
  typingPrint("He laughs at you and leaves.\n")
  time.sleep(1)
  typingPrint("You wonder what would happen if hired him.\n")
  time.sleep(1)
  print(r""" 

.-') _    ('-. .-.   ('-.           ('-.       .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)        _(  OO)     ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      (,------.,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'       |  .---'|   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |           |  |    |    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       (|  '--. |  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'        |  .--' |  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.       |  `---.|  | \   |   |  '--'  / 
   `--'   `--' `--' `------'       `------'`--'  `--'   `-------'   
   
   """)
  time.sleep(1)

  typingPrint("ENDING STATS\n")
  print("Customers:",customerCount)
  print("Star Ranking:",stars,"Star\n\n")


#first interaction
def firstcustomer():
  global customerCount
  global stars
  global bakeryName
  global typingPrint

  time.sleep(1)
  typingPrint("Wow! You got your first customer.\n")
  time.sleep(1)
  print("Customer: 'Hey, I've never seen", bakeryName,"Bakery before!" , "Can I try one of your specialty items?\n\n")

  print("What do you give them?")
  print("1. Donut")
  print("2. Croissant")
  choice = input(">")

  if choice == "1":
    print(r""" ⠀⠀⠀⠀⠀⠀⠀
        ⢀⡠⠤⠄⠀⠒⠂⢀⡤⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠔⢈⠀⠀⡿⠀⢀⣤⡄⠈⠋⢁⣀⠀⢈⡒⢄⠀⠀⠀⠀
⠀⠀⣠⠊⣁⡀⠉⠋⠀⣦⠀⠀⠁⢀⠀⠀⠀⠛⠀⠘⠃⣄⠑⢄⠀⠀
⠀⡔⡁⠀⠉⢁⣄⠄⠀⠈⠀⣶⠀⠈⠛⠀⣠⠄⠶⠦⠀⠑⠀⢬⣧⠀
⡐⠀⠿⢠⢄⠀⣀⠀⠀⡠⠄⠠⠔⠉⠢⡀⠉⠀⠀⢀⣴⠆⠀⠈⠁⢣
⠃⣤⠄⠀⢁⣄⠙⠀⠘⠀⡠⠒⠉⠉⠒⢄⠉⢢⠀⠀⢀⡀⠟⠃⢴⡤
⡀⠀⢔⡀⠈⠋⠠⢄⠰⡜⠀⠀⠀⠀⠀⠀⠱⡜⢠⡤⠈⠛⠁⢀⣄⢀
⡇⠀⣀⡀⠀⠀⠀⠉⠀⠘⠢⣀⠀⠀⠀⡠⠊⢀⠈⠀⠀⢸⡄⠈⠁⢸
⠰⡌⠋⠀⠰⣂⠛⠃⠀⢰⣆⠀⠈⣯⡁⢀⡀⠈⠋⠀⣔⠆⠀⠸⢆⡎
⠀⠸⡐⠂⠤⢀⠀⢶⠀⠀⣈⡀⠀⢈⡅⠈⠘⡁⠀⠶⠅⡀⠠⠒⡙⠀
⠀⠀⠐⡄⠀⠀⠱⡀⠀⠀⠉⢁⡠⢏⠁⠀⠚⠁⠀⢠⠊⠀⢀⠜⠀⠀
⠀⠀⠀⠈⠢⠀⠀⠈⠒⠀⠂⠁⠀⠀⠉⠂⠤⠤⠐⠁⢀⠴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠑⠠⢄⡀⠀⠀⠀⠀⠀⠀⣀⡠⠄⠂⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  """)
    typingPrint("Customer: 'Thank you! I'm excited to try it out!'\n")
    time.sleep(1)
    typingPrint("Customer: 'This is the worst donut I've ever tasted. What an absolute monstrosity. You should change up your recipe.'\n")
    time.sleep(1)
    typingPrint("Your first impression was so bad. But there's always a chance to improve, right? \n\n")
    time.sleep(1)

    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    secondcustomer()

    
  elif choice == "2":
    print(r"""                                                                                        
                                    
                                              ██████                                    
                                  ████████████░░░░░░██                                  
                                ██░░░░░░░░░░░░██░░░░░░██████                            
                              ██░░░░░░░░░░░░░░██░░░░░░██░░░░██                          
                            ██░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░██                        
                            ██░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░██                        
                            ██░░░░░░░░░░░░░░░░░░░░██░░████████                          
                          ██░░████░░░░░░░░░░░░░░░░██░░██                                
                          ██░░░░░░████░░░░░░░░░░░░████                                  
                        ██░░░░░░░░░░░░████░░░░░░░░██                                    
                        ██░░░░░░░░░░░░░░░░██░░░░██                                      
                          ██░░░░░░░░░░░░░░██████                                        
                        ██░░████████░░░░░░██                                            
                        ██░░░░░░░░░░██████                                              
                          ██░░░░░░░░░░██                                                
                        ██░░██████████                                                  
                        ██░░░░░░░░██                                                    
                          ██░░░░██                                                      
                            ████                                                        

                                                                                         """)
    typingPrint("Customer: 'Thank you! I'm excited to try it out'\n")
    time.sleep(1)
    typingPrint("Customer: 'This is the best croissant I've ever tasted! I'm gonna tell my friends to come here.'\n")
    time.sleep(1)
    typingPrint("Amazing! What a fresh start to your bakery. You've gained a new regular! (+10 customers)(+1 star)\n\n")
    time.sleep(1)

    customerCount += 10
    stars += 1
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n\n")
    secondcustomer()
  
  else:
      print("Invalid input. Please try again.")
      firstcustomer()


#second interaction
def secondcustomer():
  global customerCount
  global stars
  
  time.sleep(1)
  typingPrint("A week has passed...\n")
  time.sleep(1)
  typingPrint("Business is slow as usual\n\n")
  time.sleep(1)
  typingPrint("You notice that one of your bags of flour has a hole.\n")
  time.sleep(1)
  typingPrint("It seems like you might need to inspect the area for any strange creatures...\n\n")
  time.sleep(1)
  typingPrint("Oh wait look, a family of customers arrived!\n")
  time.sleep(1)
  typingPrint("The child looks a bit angry though.\n\n")
  print(r""" (╯°□°）╯︵ ┻━┻ """)

  time.sleep(1)
  typingPrint("Oh no, They're going to break your furniture! But what about the flour bag with a hole? You can't just leave it there!\n\n")

  print("What do you do?")
  print("1. Inspect flour bag ")
  print("2. Give free food to child to calm them down")
  choice = input(">")

  if choice == "1":
    print("\n")
    typingPrint("You ignore the chaotic scene in front of you and check out the flour bag.\n")
    time.sleep(1)
    typingPrint("You discover a path of crumbs and follow it\n")
    time.sleep(1)
    typingPrint("Oh look! There's a rat. Luckily you found out about this.\n")

    print(r"""
 ()()         ____
 (..)        /|o  |
 /\/\       /o|  o|
c\db/o...  /o_|_o_| """)
    time.sleep(1)
    typingPrint("But what about the child? \n\n")
    time.sleep(1)
    typingPrint("The child broke all your furniture and other customers were shocked by your failure to deeescalate the situation.\n")
    time.sleep(1)
    typingPrint("Your reputation is in shambles. (-10 customers)(-1 star)\n\n")
    time.sleep(1)

    customerCount -= 10
    stars -= 1
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    ratroute()

  elif choice == "2":
    print("\n")
    time.sleep(1)
    typingPrint("It worked surprisingly well.\n")
    time.sleep(1)
    typingPrint("The child gave you a lovely review and your reputation is saved.\n")
    time.sleep(1)
    typingPrint("Don't worry about the flour bag. It was probably nothing.\n")
    time.sleep(1)
    typingPrint("Great choice! (+50 customers)(+1 star)\n\n")
    time.sleep(1)

    customerCount += 50
    stars += 1
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    normalroute()

  else:
      print("Invalid input. Please try again.")
      secondcustomer()

#route number 1
def ratroute():
  global customerCount
  global stars
  global bakeryName
  global typingPrint
  
  typingPrint("Your bakery is not doing the best right now, but let's figure out what to do with the rat.\n")
  typingPrint("There's a health inspection tomorrow.\n\n")
  print(bakeryName, "Bakery could be at risk of shutting down!\n")

  print("What do you do?")
  print("1. Set up mouse traps")
  print("2. Befriend the rat")
  choice = input(">")

  if choice == "1":
    print("\n")
    time.sleep(1)
    typingPrint("I guess it's better to be safe than sorry right?\n")
    time.sleep(1)
    typingPrint("You set up a few mouse traps. \n\n")
    time.sleep(1)
    print (r"""
    
        ,--..._
      .'  .-.  `""--.
   _./`-. `-'     __/|
  F `"--i_       `. \|========/`"\--------------------------------/
  `-.     `"--.__.'`|J       /   /SSSSSSSSSSSSSSSSSSSSSSssss.._ /  |
   _/  _     ()  |  !       {._ /                             YS   |
  !__./ \        | /       /.-.\SSSssSSsssSSSSSssSSSSSSSSS__.=P    |
 /       `""--.__!'        :| |:`"""""""  \                   |   /
 --------------------------------------------------------------  /
|_____________________________________________________________| /
                 

    """)
    time.sleep(1)
    typingPrint("The next day...\n")
    time.sleep(1)
    typingPrint("Yay! You caught a rat\n")
    time.sleep(1)
    typingPrint("Phew, you passed the health inspection.\n\n")
    time.sleep(1)
    typingPrint("Your business is bouncing back! (+50 customers)(+1 star)\n\n")
    time.sleep(1)

    customerCount += 50
    stars += 1
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")

    #FIRST ENDING
    ending1()


  elif choice == "2":
    print("\n")
    time.sleep(1)
    typingPrint("You give the rat some food to befriend it.\n")
    time.sleep(1)
    typingPrint("It leads you to its house.\n")
    time.sleep(1)
    typingPrint("...\n\n")
    time.sleep(1)

    typingPrint("You find a massive family of rats!\n")
    time.sleep(1)
    typingPrint("Wow, they even know how to bake!!\n")
    time.sleep(1)
    typingPrint("Wait! But it's time for the health inspection\n\n")
    time.sleep(1)
    typingPrint("The health inspector arrives...\n")
    time.sleep(1)
    typingPrint("He discovers rat droppings and finds the rat house!\n\n")
    time.sleep(1)
    ratroute2()
  
  else:
    print("Invalid input. Please try again.")
    ratroute()

def ratroute2():
  global customerCount
  global stars
  global typingPrint

  print("Hurry! What do you do to cover it up?")
  print("1. Say that it's your pet rat")
  print("2. Let your rat friend attack the health inspector")
  choice2 = input(">")

  if choice2 == "1":
    print("\n")
    time.sleep(1)
    typingPrint("You tell him it's your pet rat.\n")
    time.sleep(1)
    typingPrint("...\n")
    time.sleep(1)
    typingPrint("The health inspector symphasizes with your situation!\n\n")
    time.sleep(1)

    typingPrint("Health Inspector: 'Oh cool! I used to have a pet rat too. But he ran away...'\n")
    time.sleep(1)
    typingPrint("He goes on a sad rant and then leaves.\n\n")
    time.sleep(1)

    typingPrint("The results of the health inspection came back...\n")
    time.sleep(1)
    typingPrint("Phew, you passed the health inspection.\n\n")
    time.sleep(1)
    typingPrint("Your business is bouncing back! (+100 customers)(+2 star)\n\n")
    time.sleep(1)

    customerCount += 100
    stars += 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    ratroute3()
      
  elif choice2 == "2":
    print("\n")
    time.sleep(1)
    typingPrint("!!!!!!\n")
    time.sleep(1)
    typingPrint("You allowed your rat friend to attack the health inspector!\n")
    time.sleep(1)
    typingPrint("What a great way to cover up the situation.\n\n")
    time.sleep(1)
    typingPrint("Health Inspector: 'Ow!'\n")
    time.sleep(1)
    typingPrint("Health Inspector: 'Huh? Wait, isn't this my pet rat??'\n")
    time.sleep(1)
    typingPrint("Health Inspector: 'I've been looking for him everywhere! Did you steal him???'\n\n")
    time.sleep(1)
    typingPrint("The rat starts to attack you.\n")
    time.sleep(1)
    typingPrint("!!!\n\n")
    time.sleep(1)
    typingPrint("You return your rat friend to the health inspector.\n")
    time.sleep(1)
    typingPrint("You feel mixed emotions.\n\n")
    time.sleep(1)

    typingPrint("The results of the health inspection came back...\n")
    time.sleep(1)
    typingPrint("Uh oh, you didn't pass :(\n\n")
    time.sleep(1)
    typingPrint("News of your failed health inspection spreads and citizens are disgusted by your rat scandal (-100 customers)(-1 star)\n\n")
    time.sleep(1)

    customerCount -= 100
    stars -= 1
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    ending2()

  else:
    print("Invalid input. Please try again.")
    ratroute2()

#further gameplay of route number 1
def ratroute3():
  global typingPrint
  global customerCount
  global stars

  typingPrint("Hooray! Good job.\n")
  time.sleep(1)
  typingPrint("Now that you passed the health inspection, you think about what you want to do with your pet rats.\n\n")
  time.sleep(1)

  print("What do you do with the rats?")
  print("1. Train them")
  print("2. Bring them home")
  choice = input(">")

  if choice == "1":
    print("\n")
    typingPrint("You trained the rats and employed them.\n")
    time.sleep(1)
    typingPrint("The rats are naturally talented bakers and helped you gain popularity.\n\n")
    time.sleep(1)
    typingPrint("Great choice! (+100K customers)(+3 stars)\n\n")
    time.sleep(1)

    customerCount += 100000
    stars += 3
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")

    ending3()

  elif choice == "2":
    print("\n")
    typingPrint("You bring the rats home and they explore your house\n")
    time.sleep(1)
    typingPrint("They magically find a stack of money that you never knew you had!\n")
    time.sleep(1)
    typingPrint("what a genius family of rats.\n\n")
    time.sleep(1)
    typingPrint("You use the cash to slowly grow your business.\n")
    time.sleep(1)
    typingPrint("Amazing choice! (+50K customers)(+2 stars)\n\n")
    time.sleep(1)

    customerCount += 50000
    stars += 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star")

    ending4()

  else:
    print("Invalid input. Please try again.")
    ratroute3()


#route number 2
def normalroute():
  global typingPrint
  global customerCount
  global stars
  
  time.sleep(1)
  typingPrint("Another fresh day begins!\n")
  time.sleep(1)
  typingPrint("...\n")
  time.sleep(1)
  typingPrint("A random kid walks into your bakery.\n\n")
  time.sleep(1)

  typingPrint("Kid: 'Hey, can I get a job here?'\n")
  time.sleep(1)
  typingPrint("Kid: 'You will regret it if you don't hire me.'\n\n")
  time.sleep(1)

  print("What do you say?")
  print("1. Sure")
  print("2. No, go away")
  choice = input(">")

  if choice == "1":
    print("\n")
    time.sleep(1)
    typingPrint("You hire the 'responsible' kid.\n")
    time.sleep(1)
    typingPrint("...\n\n")
    time.sleep(1)
    typingPrint("The kid was a great investment!\n")
    time.sleep(1)
    typingPrint("He's naturally skilled and charismatic!\n")
    time.sleep(1)
    typingPrint("His mere prescence singlehandedly led to an increase in customers and popularity!\n\n")
    time.sleep(1)
    typingPrint("Spectacular choice! (+1K customers)(+2 stars)\n\n")
    time.sleep(1)

    customerCount += 1000
    stars += 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")

    employee()

  elif choice == "2":
    print("\n")
    time.sleep(1)
    typingPrint("You reject the kid and tell him to go away.\n")
    time.sleep(1)
    typingPrint("He was probably useless anyways.\n\n")
    time.sleep(1)
    typingPrint("One day later...\n")
    time.sleep(1)
    typingPrint("You notice that the kid left a bad review of your bakery!\n")
    time.sleep(1)
    typingPrint("You are now under fire for rude behaviour :(\n\n")
    time.sleep(1)

    typingPrint("Kid: 'I know you regret your decisions ;)' (-1K customers)(-2 stars)\n\n")
    time.sleep(1)

    customerCount -= 1000
    stars -= 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")

    magicalman()

  else:
    print("Invalid input. Please try again.")
    normalroute()

def employee():
  global customerCount
  global typingPrint
  global stars

  time.sleep(1)
  typingPrint("Amazing! Your bakery should be stable now with a valuable employee.\n")
  time.sleep(1)
  typingPrint("Let's keep up the momentum and think of a marketing strategy!\n")
  time.sleep(1)
  typingPrint("Perfect! Your trusty employee came up with two ideas for you.\n\n")
  time.sleep(1)

  print("Choose one:")
  print("1. Walk around in a croissant costume")
  print("2. Host a party with famous food bloggers")
  choice = input(">")

  if choice == "1":
    print("\n")
    time.sleep(1)
    typingPrint("You order a cheap croissant costume.\n")
    time.sleep(1)
    typingPrint("It looks tacky, but it'll probably do...\n")
    time.sleep(1)
    typingPrint("You begin to rethink your choice, but you still do it anyways.\n")
    time.sleep(1)
    typingPrint("...\n\n")
    time.sleep(1)
    typingPrint("People begin to take videos and pictures of you and post it online!\n\n")
    time.sleep(1)
    typingPrint("You turn into a viral sensation!! (+100K customers)(+3 stars)\n\n")
    time.sleep(1)

    customerCount += 100000
    stars += 3
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")

    ending5()

  elif choice == "2":
    print("\n")
    time.sleep(1)
    typingPrint("The kid you hired went and invited 50 famous food bloggers.\n")
    time.sleep(1)
    typingPrint("What a dedicated employee!\n")
    time.sleep(1)
    typingPrint("To your surprise, all 50 food bloggers showed up to your bakery!!!\n\n")
    time.sleep(1)
    typingPrint("You make food for them.\n")
    time.sleep(1)
    typingPrint("...\n")
    time.sleep(1)
    typingPrint("They all hated your food!\n")
    time.sleep(1)
    typingPrint("They stormed out of your bakery, breaking all your furniture.\n")
    time.sleep(1)
    typingPrint("They made sure to leave bad reviews and attack you online\n\n.")
    time.sleep(1)
    typingPrint("What a shame :( (-100K customers)(-2 stars)\n\n")

    customerCount -= 100000
    stars -= 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n")
    
    ending6()

  else:
    print("Invalid input. Please try again.")
    employee()

def magicalman():
  global typingPrint
  global customerCount
  global stars

  typingPrint("One week later...\n")
  time.sleep(1)
  typingPrint("A magical man pays you a visit!\n\n")
  time.sleep(1)
  typingPrint("Magic Man: 'Hello there. I'm here to offer you some assistance!'\n")
  time.sleep(1)
  typingPrint("Magic Man: 'I'll help revive your bakery's reputation!!'\n")
  time.sleep(1)
  typingPrint("Magic Man: 'All of my services are free of charge!'\n\n")
  time.sleep(1)

  print("So, what do you say?")
  print("1. YES")
  print("2. NO")
  choice = input(">")

  if choice == "1":
    time.sleep(1)
    typingPrint("Magic Man: 'Yay!'\n\n")
    time.sleep(1)
    print(r"""
                                      .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
jgs     *
        *

    
    
     """)
    time.sleep(1)
    typingPrint("???\n")
    time.sleep(1)
    typingPrint("Your entire bakery disappeared along with the magic man.\n")
    time.sleep(1)
    typingPrint("That's pretty unfortunate. Maybe you should've not trusted him.\n\n")
    time.sleep(1)
    typingPrint("Well, I guess there's nothing much you can do. (-1200 customers)(-2 stars)\n\n")

    customerCount -= 1200
    stars -= 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n") 

    ending7()

  elif choice == "2":
    print("\n")
    time.sleep(1)
    typingPrint("Magic Man: 'OK. It's your choice after all!'\n")
    time.sleep(1)
    typingPrint("...\n")
    time.sleep(1)
    typingPrint("Nothing happened to your bakery after that.\n\n")
    time.sleep(1)
    typingPrint("...A few weeks later\n")
    time.sleep(1)
    typingPrint("You notice business is a bit slow.\n")
    time.sleep(1)
    typingPrint("You start getting 0 customers a day.\n")
    time.sleep(1)
    typingPrint("You begin to wonder if the magic man was responsible for this\n\n")
    time.sleep(1)
    typingPrint("You lost everything :( (-1200 customers)(-2 stars)")

    customerCount -= 1200
    stars -= 2
    print("Stats:")
    print("Customers:",customerCount)
    print("Star Ranking:",stars,"Star\n") 

    ending8()

  else:
    print("Invalid input. Please try again.")
    magicalman()


firstcustomer()











