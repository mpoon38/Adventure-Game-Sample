import random
import time

# default invalid input function
def impactDetected():
    print("INVALID COMMAND ENTERED, ATTEMPTING RECOVERY...REQUEST FAILED")
    time.sleep(3.5)
    print(random.choice([
        "MICROMETORITE IMPACT",
        "COSMIC RAY DETECTED"
    ]))
    print("MISSION FAILURE")
    
# intro instructions
print("You are a Mars Exploration Rover...SENDING COMMUNICATIONS TO EARTH...")
time.sleep(7)
print("Touchdown confirmed, we're safe on Mars!")
time.sleep(1)
print("\nInstructions from JPL \n")
print("Mission objective: Astrobiology, find evidence of past lifeforms")

# select a b or c from input for first choice
def chooseFirstObjective():
    print("SELECTING NEW OBJECTIVE")
    option = input("· (a) IMAGE PATH\n· (b) EXPLORE LANDING ZONE\n· (c) COLLECT SAMPLE\nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        imagePath()
    elif option == "b":
        exploreLandingZone()
    elif option == "c":
        collectSoilSample()
    else:
        # crash if invalid
        impactDetected()

# selecting a, b or c for first path
def imagePath():
    print("TAKING PANORAMIC IMAGE...SENDING DATA DUMP")
    time.sleep(2)
    print("SELECTING NEXT TARGET")
    option = input("· (a) IMAGE MARTIAN ECLPISE\n· (b) USE SPECTROMETER \n· (c) XYZZY SECRET \nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        print("ACTIVATING CAMERA...")
        time.sleep(2)
        # 60% chance of failure
        if random.random() < 0.6:
            print("CAMERA SENSOR DAMAGED ")
            print("MISSION FAILURE")
        else:
            print(r'''     |
     \    |    /
 `.   \   |   /   .'
   `.  \  |  /  .'
`-.  `. \d8b/ .'  .-'
   `-. do0o88b .-'
<~~~~ 8o0O0o888 ~~~~> 
<~~~~ 8o00o8888 ~~~~>
   _-' qoo888p '-_   
,-'  ,' /q8p\ `.  `-.   
   ,'  /  |  \  `.
 ,'   /   |   \   `.
     /    |    \
          |
            ''')
            print("MISSION COMPLETE!")

    elif option == "b":
        print("ANALYZING ATMOSPHERE...")
        time.sleep(2)
        print("95% CO2, 2.6% N2, 9.1% Ar")
        print("MISSION COMPLETE!")
    elif option == "c":
        XYZZY()
    else:
        impactDetected()

# secret password code (CAVE GAME)
def XYZZY():
    print("BEGINNING OVERRIDE PROCEDURE...")
    time.sleep(3)
    password = input("WHAT WAS THE NAME OF THE FIRST MARS ROVER MISSION? ")
    password=password.lower().lstrip().rstrip()
    if password == "pathfinder":
        PATHFINDER()
    else:
        impactDetected()

# choose a, b or c for second path
def exploreLandingZone():
    print("ACTIVATING AUTONOMOUS DRIVE FUNCTION...")
    time.sleep(2)
    WHEEL_INTERGRITY_FAILING=True
    for i in range(7):
        # you can drive seven times before crashing
        print("DETERMINING NEXT DIRECTON")
        # select two unique choices randomly
        choices=random.sample(["ENTER CRATOR", "CLIMB SAND DUNE", "TRAVERSE ICE PLANE"],2)
        option = input(f"· (a) {choices[0]}\n· (b) {choices[1]}\n· (c) CONTINUE DRIVING\nENTER LETTER: ")
        option=option.lower().lstrip().rstrip()
        if option == "a":
            if choices[0] == "ENTER CRATOR":
                enterCrator()            
            elif choices[0] == "CLIMB SAND DUNE":
                climbSandDune()
            elif choices[0] == "TRAVERSE ICE PLANE":
                traverseIcePlane()
            else:
                impactDetected()
            WHEEL_INTERGRITY_FAILING=False
            break

        elif option == "b":
            if choices[1] == "ENTER CRATOR":
                enterCrator()
            elif choices[1] == "CLIMB SAND DUNE":
                climbSandDune()
            elif choices[1] == "TRAVERSE ICE PLANE":
                traverseIcePlane()
            else:
                impactDetected()
            WHEEL_INTERGRITY_FAILING=False
            break

        elif option == "c":
            print("CONTIUING CURRENT TRAJECTORY...ETA TO TARGET 10 SECCONDS")
            time.sleep(10)
        else:
            impactDetected()
            WHEEL_INTERGRITY_FAILING=False
            break
    if WHEEL_INTERGRITY_FAILING:
        # crash if driven 7 times
        print("WHEEL INTEGRITY FAILING...ENTERING SAFE MODE")
        print("MISSION FAILURE")

# choose a or b for crator
def enterCrator():
    print("DRIVING TOWARDS OBJECTIVE...")
    time.sleep(2)
    option = input("· (a) RELEASE PAYLOAD\n· (b) EXPLORE RIVER BASIN \nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        print("RELEASING MARS HELICOPTER...")
        time.sleep(2)
        print("RETRIEVING HELICOPTER IMAGE DATA")
        print(r'''  
        ________/--\____<>______.______
        ''')
        print("MISSION COMPLETE!")

    elif option == "b":
        print("ANALYZING RIVER BASIN COMPOSITION...")
        time.sleep(2)
        print("ERROR: SENSOR DAMAGED")
        print("MISSION FAILURE")
    else:
        impactDetected()

# choose a or b for sand dune
def climbSandDune():
    print("DRIVING TOWARDS OBJECTIVE...")
    time.sleep(2)
    print("WARNING... WHEEL TRACTION FAILING...")
    option = input("· (a) CONTINUE DRIVING\n· (b) ANGLE SOLAR ARRAYS \nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        print("ATTEMPTING RECOVERY SEQUENCE...")
        time.sleep(5)
        print("ROVER IMMOBLIZED...")
        print("MISSION FAILURE")
    elif option == "b":
        print("TRACKING SUNLIGHT...")
        time.sleep(2)
        print("POWER LEVEL OPTIMAL")
        print("MISSION RECLASSIICATION: STATIONARY MISSION")
        print(r'''                                               _
                 ___                          (_)
               _/XXX\
_             /XXXXXX\_                                    __
X\__    __   /X XXXX XX\                          _       /XX\__      ___
    \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\
  \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/
 ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____//
/  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/
__/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______
                                  /|\
                                 / | \
                                /  |  \
                               /   |   \
                              /    |    \
                             /     |     \
                            /      |      \
                           /       |       \
                          /        |        \
                         /         |         \
''')
    else:
        impactDetected()

# ice plane path
def traverseIcePlane():
    print("DRIVING TOWARDS OBJECTIVE...")
    time.sleep(2)
    print("MATERIAL ABRASION IN PROGRESS...")
    time.sleep(2)
    print("ANALYSIS COMPLETE... PRESERVED BACTERIA SAMPLE DETECTED... MISSION SUCESSFUL!")
    
# choose a or b for third path
def collectSoilSample():
    print("COLLECTING SOIL SAMPLE...")
    time.sleep(5)
    print("DRILLING IN PROGRESS...")
    option = input("· (a) STORE SAMPLE TUBE ON BOARD\n· (b) DROP SAMPLE TUBE \nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        print("CALIBRATING SAMPLE HOLDER...")
        time.sleep(2)
        print("ERROR: ALIGNMENT FAILED")
        print("INSTRUMENTATION FAILURE")
    elif option == "b":
        dropSampleTube()
    else:
        impactDetected()

# choose a or b for drop soil sample       
def dropSampleTube():
    print("SCANNING SURFACE FOR SAMPLE TUBE DEPOT...")
    time.sleep(2)
    print(r'''.         _  .          .          .    +     .          .          .      .
        .(_)          .            .            .            .       :
        .   .      .    .     .     .    .      .   .      . .  .  -+-        .
          .           .   .        .           .          /         :  .
    . .        .  .      /.   .      .    .     .     .  / .      . ' .
        .  +       .    /     .          .          .   /      .
       .            .  /         .            .        *   .         .     .
      .   .      .    *     .     .    .      .   .       .  .
          .           .           .           .           .         +  .
  . .        .  .       .   .      .    .     .     .    .      .   .

 .   +      .          ___/\_._/~~\_...__/\__.._._/~\        .         .   .
       .          _.--'                              `--./\          .   .
           /~~\/~\                                         `-/~\_            .
 .      .-'                                                      `-/\_
  _/\.-'                                                          __/~\/\-.__
.'                                                                           `.dp''')
    print("DROP SUCESSFUL!")
    option = input("· (a) GO TO NEXT DRILLING LOCATION\n· (b) ANALYZE CHEMICAL COMPOSTION OF MARS REGOLITH \nENTER LETTER: ")
    option=option.lower().lstrip().rstrip()
    if option == "a":
        time.sleep(2)
        print("ORGANIC MOLECULES DETECTED")
        print(r'''     ,,,,,,,,
           ,|||````||||
     ,,,,|||||       ||,
  ,||||```````       `||
,|||`                 |||,
||`     ....,          `|||
||     ::::::::          |||,
||     :::::::'     ||    ``|||,
||,     :::::'               `|||
`||,                           |||
 `|||,       ||          ||    ,||
   `||                        |||`
    ||                   ,,,||||
    ||              ,||||||```
   ,||         ,,|||||`
  ,||`   ||   |||`
 |||`         ||
,||           ||
||`           ||
|||,         |||
 `|||,,    ,|||
   ``||||||||`''')
        print("MISSION COMPLETE!")
    elif option == "b":
        print("BEGINNING ANALYSIS...")
        time.sleep(2)
        print("ERROR: CAMERA SENSOR DAMAGED")
        print("INSTRUMENTATION FAILURE")
    else:
        impactDetected()
    
# pathfinder minigame
def PATHFINDER():
    print("OBJECIVE: YOU ARE REMOTELY OPERATING THE MARS RECONNAISSANCE ORBITER. YOU NEED TO TAKE 25 IMAGES OF THE LANDING ZONE FOR THE THE MARS SAMPLE RETURN MISSION.")
    time.sleep(6.5)
    orbitsize=40
    up=True
    distanceToTarget=12
    asteroids = []
    thetime=time.time()
    imagestaken = 0
    while True:
        # every seven seconds, add new asteroid
        if time.time() > thetime+7:
            # an asteroid is an up down position, location in orbit, and shape.
            asteroids.append((random.choice([True, False]), orbitsize-1, random.choice(["@","&","*","O"])))
            thetime=time.time()
        spaceup = [" "]*orbitsize
        spacedown = [" "]*orbitsize
        for asteroid in asteroids:
            # drawing the asteroids
            upasteroid=asteroid[0]
            if upasteroid==True:
                spaceup[asteroid[1]]=asteroid[2]
            else:
                spacedown[asteroid[1]]=asteroid[2]    
        # draw orbiter in up or down position    
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if up == True:
            print("      <-    " + " "*orbitsize)
            print("        |   " + " "*orbitsize)   
            print("     //---//" + "".join(spaceup))
            print("            " + " "*orbitsize)
            print("            " + " "*orbitsize)   
            print("            " + "".join(spacedown))
        else:
            print("            " + " "*orbitsize)
            print("            " + " "*orbitsize)   
            print("            " + "".join(spaceup))
            print("      <-    " + " "*orbitsize)
            print("        |   " + " "*orbitsize)   
            print("     //---//" + "".join(spacedown))
        for asteroid in asteroids.copy():
            # move the asteroids closer to the orbiter
            asteroids.remove(asteroid)
            position = asteroid[1]-1
            if position >= 0:
                # keep the asteroid if it did not reach the end
                asteroids.append((asteroid[0], position, asteroid[2]))
            else:
                # if the asteroid did not hit the orbiter, the asteroid is already deleted
                if asteroid[0] == up:
                    # if the asteroid hit the orbiter, crash
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    if up == True:
                        print("       -    " + " "*orbitsize)
                        print("     <  |   " + " "*orbitsize)   
                        print("     \/--\_|" + "".join(spaceup))
                        print("            " + " "*orbitsize)
                        print("            " + " "*orbitsize)   
                        print("            " + "".join(spacedown))
                    else:
                        print("            " + " "*orbitsize)
                        print("            " + " "*orbitsize)   
                        print("            " + "".join(spaceup))
                        print("       -    " + " "*orbitsize)
                        print("     <  |   " + " "*orbitsize)   
                        print("     \/--\_|" + "".join(spacedown))
                    print("L.O.S.")
                    return
        # update the distance to the next imaging target
        distanceToTarget -= 1
        if distanceToTarget == 0:
            # if the orbiter has arrived, collect user input
            distanceToTarget=7
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            if up == True:
                # orbiter is in the up position 
                print("      <-    " + " "*orbitsize)
                print("        |   " + " "*orbitsize)   
                print("     //---//" + "".join(spaceup))
                print("            " + " "*orbitsize)
                print("            " + " "*orbitsize)   
                print("            " + "".join(spacedown))
                command=input(f"a=down,b=take image; {imagestaken} images taken. enter letter: ")
                command=command.lower().lstrip().rstrip()
                if command=="a":
                    # move the orbiter down
                    up=False
                elif command == "b":
                    # take an image, but do not move the orbiter
                    imagestaken+=1
                    if imagestaken == 25:
                        # all images collected, end game
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("      <-    " + " "*orbitsize)
                        print("        |   " + " "*orbitsize)   
                        print("     //---//" + "".join(spaceup))
                        print("            " + " "*orbitsize)
                        print("            " + " "*orbitsize)   
                        print("            " + "".join(spacedown))
                        print("MISSION SUCESSFUL! SECRET COOKIE UNLOCKED! 🍪")
                        return
                else:
                    # invalid command, deorbiting orbiter
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("       -    " + " "*orbitsize)
                    print("     <  |   " + " "*orbitsize)   
                    print("     \/--\_|" + "".join(spaceup))
                    print("            " + " "*orbitsize)
                    print("            " + " "*orbitsize)   
                    print("            " + "".join(spacedown))
                    print("L.O.S.")
                    return
            else: 
                # orbiter is in the down position
                print("            " + " "*orbitsize)
                print("            " + " "*orbitsize)   
                print("            " + "".join(spaceup))
                print("      <-    " + " "*orbitsize)
                print("        |   " + " "*orbitsize)   
                print("     //---//" + "".join(spacedown))
                command=input(f"a=up,b=take image; {imagestaken} images taken. enter letter: ")
                command=command.lower().lstrip().rstrip()
                if command=="a":
                    # move the orbiter up
                    up=True
                elif command == "b":
                    # take image 
                    imagestaken+=1
                    if imagestaken == 25:
                        # end game if all images collected
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("            " + " "*orbitsize)
                        print("            " + " "*orbitsize)   
                        print("            " + "".join(spaceup))
                        print("      <-    " + " "*orbitsize)
                        print("        |   " + " "*orbitsize)   
                        print("     //---//" + "".join(spacedown))
                        print("MISSION SUCESSFUL! SECRET COOKIE UNLOCKED! 🍪")
                        return
                else:
                    # invalid command, de-orbiting orbiter
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("            " + " "*orbitsize)
                    print("            " + " "*orbitsize)   
                    print("            " + "".join(spaceup))
                    print("       -    " + " "*orbitsize)
                    print("     <  |   " + " "*orbitsize)   
                    print("     \/--\_|" + "".join(spacedown))
                    print("L.O.S.")
                    return

        # update all positions every half second    
        time.sleep(0.5)

# prompt the first choice 
chooseFirstObjective()
