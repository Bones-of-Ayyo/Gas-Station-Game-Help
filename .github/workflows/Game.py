location = "outside"
lever = "down"
switch = "middle"

while True:
    while location == "outside":#starting area of the game/title screen. The "one way portal" is located here in the form of the "front door"
        answer = input("Would you like to play the game? (yes/no)").lower().strip()#these two functions here error check the input incase of capitalization or quotations.
        if answer == "yes":
            
            answer = input("You stumble upon an abandoned gas station during your morning run. It is off the main road, and there are no people in sight. You see the front door slightly open. Do you wish to take a look inside? (yes/no): ").lower().strip()
            if answer == "yes":
                print("You open the front door and walk inside.")
                print("The front door slams shut and locks behind you! You're trapped!")
                location = "main room"
            
            elif answer == "no":
                print("You decide it's not worth the risk and continue on with your morning run. Alternative victory achieved!")
                quit()
            
            else:
                print("I don't understand your answer. HINT: Look at the brackets for possible answers")
        
        elif answer == "no":
            print("Ok. Quiting game :(")
            quit()
        
        else:
            print("I don't understand your answer. HINT: Look at the brackets for possible answers")
   
    while location == "main room":#this is the main room where you select your desired location and check the status of the locked door
        print("You are in the main room. There is a garage to your left and a janitor's closet to your right. On the other side of the room is the back door to the gas station, your way out!")
        answer = input("Where do you want to go? (front door/back door/garage/closet)").lower().strip()
        
        if answer == "front door":
            print("The front door locked behind you, remember?")
        
        elif answer == "back door":
            if (switch == "right") and (lever == "up"):
                print("The back door swings open!")
                location = "escaped"
            
            else:
                print("The back door is electronically locked. You'll need to turn on the power to open it. Try looking in the rooms.")
            
        elif answer == "garage":
            print("You enter the garage.")
            location = "garage"
        
        elif answer == "closet":
            print("You squeeze into the closet.")
            location = "closet"
        
        else:
            print("I don't understand your answer. HINT: Look at the brackets for possible answers")
    
    while location == "garage":#the garage features a red lever in place of the silver lock. It will have to be moved to the correct position to win the game. 
        print("You are in the garage. It smells like stale gasoline. You see a grey power box with a red lever.")
        print("The red lever can be set to the up position, middle position, or the down position. It is currently in the {} position".format(lever))
        answer = input("What position would you like to set the red lever to? Alternatively, you can leave the garage. (up/middle/down/leave)").lower().strip()
        
        if answer == "up":
            print("You set the red lever to the up position and hear a whirring noise!")
            lever = "up"
        
        elif answer == "down":
            print("You set the red lever to the down position. Nothing happens...")
            lever = "down"
            
        elif answer == "middle":
            print("You set the red lever to the middle position. Nothing happens...")
            lever = "middle"
            
        elif answer == "leave":
            print("You return to the main room.")
            location = "main room"
            
        else:
            print("I don't understand your answer. HINT: Look at the brackets for possible answers")
            
    while location == "closet":#the closet features a blue switch in place of the gold lock. same situation as the garage
        print("You've squeezed into the dusty janitor's closet. There is a fuse box with many switches. The blue switch stands out to you.")
        print("The blue switch can be set to the left, middle, and right position. It is currently in the {} position".format(switch))
        answer = input("What position would you like to set the blue switch to? Alternatively, you can leave the closet. (left/middle/right/leave)").lower().strip()
        
        if answer == "right":
            print("You set the blue switch to the right position and hear a sparking noise!")
            switch = "right"
        
        elif answer == "left":
            print("You set the blue switch to the left position. Nothing happens...")
            switch = "left"
            
        elif answer == "middle":
            print("You set the blue switch to the middle position. Nothing happens...")
            switch = "middle"
            
        elif answer == "leave":
            print("You return to the main room.")
            location = "main room"
            
        else:
            print("I don't understand your answer. HINT: Look at the brackets for possible answers")
            
    while location == "escaped":#winning area when both the red lever and the blue switch are successfully positioned
        print("You've escaped the abandoned gas station! Congratulations!")
        print("Created by Bones_of_Ayyo circ. 2021!")
        quit()
