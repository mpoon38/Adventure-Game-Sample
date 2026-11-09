from time import sleep

#Introduction
sleep (2)
print("Hello Dr. Smolder Bravestone, welcome to Jumanji!")
sleep(2)
print("I will be your personal tour guide!")
sleep(2)
print("Before we start our fun adventure in the Jungle.")
sleep(2)
print("Let us see your stregths and weaknesses Dr. Smolder Bravestone")


def name():
 while True:
  choice = input("Please type in Dr. Smolder Bravestone to see stregths and weaknesses (dr. smolder bravestone):")

  if choice.lower() == "dr. smolder bravestone": 
    intro()
    break

  else:
    print("Invalid choice. Try again.")
    name()
    break

#Scene 1
def intro():
  print("Dr. smolder Bravestone")
  sleep(2)
  print("Strengths: strong, confident archaeologist and explorer with no weakness.")
  sleep(2)
  print("Welcome Dr.Smolder Bravestone,")
  sleep(2)
  print("In order to complete the game.")
  sleep(2)
  print("You must return the gem to the jaguar statue and call out,'Jumanji' for you to win the game.")
  sleep(2)
  print("But the gem is kept in the Linlants Hollows")
  sleep(2)
  print("you must go through a series of obstacles in order to achieve the gem.")
  sleep(2)
  print("Some of these obstacles might result to death.")

  

  while True:
    choice = input("Are you ready Dr. Smolder Bravestone? (yes):")
    if choice.lower() =='yes':
      ob()
      break

    else:
     print("Invalid choice. Try again.")
     intro()
     break

#Scene 2
def ob():

  sleep(3)
  print("Fantastic Dr. Smolder Bravestone! Let's head in the jungle to find the gem.")
  sleep(3)
  print("Looks like we have arrived at our first obstacle. Heridwell Falls.")
  sleep(3)
  print(r"""  
                      _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
Lester||||AMC       --------/     '     '   '

    """)


  sleep(3)
  print("wait what's that in the water......")
  sleep(3)
  print("is that...an alligator?")
  sleep(3)
  print(r"""

                / \/ \-._   _.-'^'^^'^^'^^"^^'-.
    .OO.----'\o/\o/   `-'                /^  ^^-._
   (    `                 \             |    _    ^^-._
    VvvvvvvVvv`___...)_/  /_/_/_/_/_/_/_/\  (__________^^-.
jgs  `^^^^^^^^`       /  /                >  >        _`)  )
                     (((`                (((`        `'--'^
    
    
    """)
  sleep(3)
  print("We have to go across Heridwell Falls to get to the Linlants Hollows.")
  sleep(3)
  print("Looks like we have to sneak past the alligator")
  sleep(3)


  while True:
   choice = input("should we run or walk past the alligator? (run/walk)")
   if choice.lower() =='run':
    run()
    break
   elif choice.lower() =='walk':
    walk()
    break
   else:
    print("Invalid choice.")
    ob()




def run():
        sleep(3)
        print("Lets trying running.")
        sleep(3)
        print("3...2...1..RUN!!")
        sleep(3)
        print(" DR. SMOLDER BRAVESTONE IT'S RUNNING BEHIND YOU")
        sleep(3)
        print("RUN FASTER DR. SMOLDER BRAVESTONE, ONE OF YOUR STRENGTHS WAS THAT YOUR STRONG, SO RUN FASTER.")
        sleep(3)
        print("OH NO DR. SMOLDER BRAVESTONE, LOOKOUT!!!! ")
        sleep(3)
        print("Dr. Smolder Bravestone has been killed by an alligator.")
        sleep(1.5)

        print(r'''            ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#                

''') 

#Scene 3
def walk():
  sleep(2)
  print("Well done Dr. Smolder Bravestone! Looks like we made it pass the alligator!")
  sleep(2)
  print("We are one step closer to the gem.")
        
  print(r'''
         (              ````                                            
;`             ;;                                               
 ;;  -""-.   ;;                 -;'  -.                         
   ""     ``                      `.   `.                       
                                    ;    `                      
           `;                  -          ;         -.        ;`
             `-  `.         .'`  .-'             .--`  ;     ;  
              ;    `-.   ;    `-'             .;`     ;       `.
              .        ``                                       
               `            .--------.             .'           
             ...        .--'``````````'--.        ;.            
            `      . .-' .``          ``. '-. .      `.         
          ;-.;  .  .' .`                  `. '.  .    ;         
              .' .' .`                      `. '. '.    .       
_____/'.-..___________________________ mvn,, ___________________
                             )\     nMmIEFooPTn                 
                            ( (    Li1iiJl1ItTIjp               
                             ) \  i i_BP_LWmKK`  J  `           
`                .          /  (   i1 LL 1I`L            .      
             ..             \   \  i   X  Y o1                  
                        .    )   )  `   l   p      ..           
;                           /   (,      l(@) l                ..
  q      ` .  '            (     \.     i    p   R          .;  
   \  t            ;        )     \`   j,.. ,.q,/Pqoj          `
    \/            `       ./       \`;     `'     `          .. 
  '-     \;            -'.'    ;    \ `                     `. `
.--.`.; ,-.. ,.-, ;' `.-'       `    `.'.   .--.""-._        .; 
    `............---""     ;_.         )   (  '=    /         `-
 ~                                    /     `------'     .      
                 ~                  ,'  \|//            `'      
                ~           ~       ; `. ""                   ..
                                     `.  )     \"       .--"""
        
         ''')

  print("Look Dr. Smolder Bravestone.")
  sleep(2)
  print("It's elephants!!!!")
  sleep(2)
  print(r'''
                       .---'-    \
      .-----------/           \
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\).
    ''')
  sleep(2)

  while True:
    choice = input("What should we do Dr. Smolder Bravestone? (approach it/leave it)")

    if choice.lower()=='approach it':
      approach()
    
 
    elif choice.lower() =='leave it':
      leave()
      break

    else:
      print("Invalid choice.")
      walk()

 
def approach():
  print("I'll stay over here Dr.Smolder Bravestone")
  sleep(2)
  print("woah there...be careful")
  sleep(2)
  print("Dr. Smolder Bravestone?")
  sleep(2)
  print("OH NO! The elephant took Dr. Smolder Bravestone!")
  sleep(2)
  print(r'''
                 /eeeeeeeeeee\ 
   /RRRRRRRRRR\ /eeeeeeeeeeeee\ /RRRRRRRRRR\ 
  /RRRRRRRRRRRR\|eeeeeeeeeeeee|/RRRRRRRRRRRR\ 
 /RRRRRRRRRRRRRR +++++++++++++ RRRRRRRRRRRRRR\ 
|RRRRRRRRRRRRRR ############### RRRRRRRRRRRRRR| 
|RRRRRRRRRRRRR ######### ####### RRRRRRRRRRRRR| 
 \RRRRRRRRRRR ######### ######### RRRRRRRRRR/ 
   |RRRRRRRRR ########## ######## RRRRRRRR| 
  |RRRRRRRRRR ################### RRRRRRRRR| 
               ######     ###### 
               #####       ##### 
               #nnn#       #nnn#
      ''')

#Scene 4
def leave():
  print("Good Idea.")
  sleep(2)
  print("I heard elephants is on the top 10 list for most dangerous animals")
  sleep(2)
  print("wouldn't want to get to close.")

  sleep(2)
  print("Look over there! I think those are mountains!")
  sleep(2)
  print(r'''
                _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/jgs     `.  / /       `.~-^=-=~=^=.-'      '-._ `._
        ''')

  sleep(2)    
  print("That means we are close to Linlants Hollows")
  sleep(2)
  print("LOOK OVER THERE DR. SMOLDER BRAVESTONE ITS THE LINLANTS HOLLOWS!!!")
  sleep(2)
  #Scene 5
  print(r'''
                  ^
                 / \
            ^   _|.|_   ^
          _|I|  |I .|  |.|_
          \II||~~| |~~||  /
           ~\~|~~~~~~~|~/~
             \|II I ..|/
        /\    |II.    |    /\
       /  \  _|III .  |_  /  \
       |-~| /(|I.I I  |)\ |~-|
     _/(I | +-----------+ |. )\_
     \~-----/____-~-____\-----~/
      |I.III|  /(===)\  |  .. |
      /~~~-----_________---~~~\
     `##########!\-#####%!!!!!| |\
    _/###########!!\~~-_##%!!!\_/|
    \##############!!!!!/~~-_%!!!!\
     ~)#################!!!!!/~~--\_
  __ /#####################%%!!!!/ /
  \,~\-_____##############%%%!!!!\/
  /!!!!\ \ \~-_###########%%%!!!!\
 /#####!!!!!!!\~-_#######%%%!!!!!!\_
/#############!!!\#########%%%!!!!!!\
    ''')
  sleep(2)
  print("Dr, Smolder Bravestone we have to sneak in cafefully.")
  sleep(2)
  print("I am pretty sure that people are gaurding this place.")
  sleep(2)
# Scene 6
  print("Shhhhhh..... there is someone over there.")
  sleep(2)
  print(r'''
      ////^\\\\
      | ^   ^ |
     @ (o) (o) @
      |   <   |
      |  ___  |
       \_____/
     ____|  |____
    /    \__/    \
   /              \
  /\_/|        |\_/\
 / /  |        |  \ \
( <   |        |   > )
 \ \  |        |  / /
  \ \ |________| / /
   \ \|
    ''')
  sleep(2)

  while True:
   choice = input("What should we do? (attack/hide)")
   if choice.lower()=='attack':
    attack()
    break

   elif choice.lower() =='hide':
    hide()
    break
   else:
    print("Invalid choice.")
    leave()

#Scene 7
def attack():
  print("Dr. Smolder Bravestone use your strengths, you have no weaknesses!")
  sleep(2)
  print("Ouch...sorry guard...")
  sleep(2)
  print("Looks like you knocked out the guard Dr. Smolder Bravestone.")
  sleep(2)
  print("is that.....")
  sleep(2)
  print("that's the gem!!!!!")
  sleep(2)
  print(r'''
          ,
   \  :  /
`. __/ \__ .'
_ _\     /_ _
   /_   _\
 .'  \ /  `.
   /  :  \    hjw
      '
    ''')
  sleep(2)
  print("Let's grab it and get out of here and head to the jaguar statue!")
  sleep(2)
  print("Looks like our advebture has come to an end.")
  sleep(2)
  print("Just yell out Jumanji.")
  sleep(2)
  print("then you can completed the game!")
  sleep(2)
  print("Jumanji")

  

  choice = input("Just yell out Jumanji to complete the game!(Jumanji):")

  while True:

    if choice.lower() == "Jumanji": 
      end()
      break

    else:
      print("Invalid choice. Try again.")
      attack()
      break

def end():
  sleep(2)
  print("So long Dr. Smolder Bravestone!")
  sleep(2)
  print("Game Completed")

  
def hide():
  print("Seriously Dr. Smolder Bravestone??????")
  sleep(2)
  print("You are like one of the most strongest charcters.")
  sleep(2)
  print("and you chose to HIDE??")
  sleep(2)
  print("I guess we have to wait and hide for awhile.")

  sleep(0.5)
  print("Game crashed")
  sleep(0.5)
  print("Please restart the game")
  

  
  


      
name()