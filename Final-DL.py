L = []

print("CHAPTER 1: The year is 2122, and you are the captain of an elite space force.  Your mission is to assemble your crew and venture to space to retrieve a star crystal.  This crystal will provide energy for the entire planet, the future of planet Earth depends on you!")

print("You venture to the space station and see several potential crewmates.")

def Chapter1():
    CH1 = input("Would you like to... speak to Sam (A), speak to Nicholas (B), speak to Thomas (C), or leave for space (D)?: ")

    if CH1 == "A":
        L.append(CH1)
        fuel = input("Sam is the navigator and agrees to join your team.  She suggests that you check the ships' fuel before leaving. Would you like to check the fuel (yes, no)?: ")
        if fuel == "yes":
            L.append(fuel)
            print("The ship is low on fuel, and you ask Sam to fill the tanks.")
            Chapter1()
        elif fuel == "no":
            L.append(fuel)
            print("This can't go wrong..")
            Chapter1()
            
    elif CH1 == "B":
        L.append(CH1)
        print("Nicholas is a weapons specialist and will be a valuable addition to your team!")
        Chapter1()
        
    elif CH1 == "C":
        L.append(CH1)
        print("Thomas is a scientist and expert in star crystals,  he agrees to join your team!")
        Chapter1()
        
    elif CH1 == "D":
        print("You venture off to space!")
    
    else:
        print("Please enter a valid option.")
        Chapter1()

Chapter1()

print("CHAPTER 2: You begin your journey enter outer space.")

print("As the captain of the ship, you must decide which direction your ship will travel.")

def Chapter2():
    CH2 = input("Would you like to... speak to Sam (A), travel towards the Sun (B), travel away from the Sun (C), or travel perpendicular to the Sun(D)?: ")

    if CH2 == "A":
        if "A" in L:
            print("Based on energy reports, Sam suggests that you travel perpendicular to the Sun.")
            Chapter2()
        else:
            print("You did not recruit Sam on this mission...")
            Chapter2()
            
    elif CH2 == "B":
        print("Your ship travels rapidly towards the Sun.  Once reaching the Suns' atmosphere, your ship begins to melt!  You and your crew perish in space.  GAME OVER.")
        quit()
        
    elif CH2 == "C":
        print("Your ship travels away from the Sun.  After venturing for months you realize you've miscalculated the amount of fuel left.  You and your crew are stranded in space.  GAME OVER.")
        quit()
        
    elif CH2 == "D":
        print("You make the decision to travel perpendicular from the Sun. You have a good feeling about this choice!")
    
    else:
        print("Please enter a valid option.")
        Chapter2()
        
Chapter2()
if "yes" not in L:
    print("You forgot to fuel the ship before leaving... You and your crew are now stranded in space.  GAME OVER.")
    quit()

print("CHAPTER 3: Months go by, and you and your crew begin to become discouraged.  Far in the distance you see an object that appears to be coming towards your ship!")

print("After checking with your radar, you determine that the object is in fact another ship!")

def Chapter3():
    CH3 = input("Would you like to... speak to Nicholas (A), continue traveling towards the ship (B), open fire on the ship (C), or send a communication request to the ship(D)?: ")

    if CH3 == "A":
        if "B" in L:
            print("From the direction the other ship is coming, it is safe to say it is not a human ship.  Nicholas recommends destroying the ship immediately.")
            Chapter3()
        else:
            print("You did not recruit Nicholas on this mission...")
            Chapter3()
            
    elif CH3 == "B":
        print("You continue on your path towards the foreign ship.  As your near the ship, it speeds up and slices straight through your ship. GAME OVER.")
        quit()
        
    elif CH3 == "C":
        print("You make the executive decision to not risk interacting with the other space craft.  You fire up the ships' laser and destroy the other spacecraft instantly!")
        
    elif CH3 == "D":
        print("You decide on attempting to communicate with the other ship.  The aliens now realize your postition and release a space monster that swallows your ship whole.  GAME OVER.")
        quit()
        
    else:
        print("Please enter a valid option.")
        Chapter3()
        
Chapter3()

print("CHAPTER 4: You have successfully destroyed the aliens and fly towards its remains.")

print("As the captain, you decide to exit the ship to closely inspect the debris... While swimming through the remains you come upon a large chest, made from some unknown metal.")

def Chapter4():
    CH4 = input("Would you like to... radio Thomas (A), wait for your crew (B), open the chest (C), or bring the chest back to your ship(D)?: ")

    if CH4 == "A":
        if "C" in L:
            print("You inform Thomas that you've found a mysterious chest in this pile of rubble.  He suggests not doing anything until he arrives to inspect it.")
            Chapter4()
        else:
            print("You did not recruit Thomas on this mission...")
            Chapter4()
            
    elif CH4 == "B":
        print("You decide to play it safe and wait for you crewmates to arrive.")
        
    elif CH4 == "C":
        print("You've waited far too long not to see what the contents of the chest are!  You open the chest and the extreme radiation of the star crystal kills you immediately.  GAME OVER.")
        quit()
        
    elif CH4 == "D":
        print("You attempt to bring the giant chest to the ship yourself.  After a couple minutes, you realize that you are quickly depleting your oxygen and return to the ship empty-handed.")
        Chapter4()
        
    else:
        print("Please enter a valid option.")
        Chapter4()
        
Chapter4()

print("CHAPTER 5: There is an ominous energy surrounding this mysterious chest, it was probably for the best that you chose to wait. You've waited months for this moment!")

print("After what seems like an eternity, Thomas arrives to your location.  He scans the chest and confirms that it does in fact contain a star crystal!!")

def Chapter5():
    CH5 = input("Would you like to... push the chest back to the ship with Thomas and load it onboard (A), leave the chest (B), or bring your ship to carry the chest with its' grappling gun(C)?: ")

    if CH5 == "A":
        print("You manage to bring the chest back onto the ship with Thomas' help.  As you and your crew make your way back to earth, you begin spitting up blood.  The extreme radiation from the star crystal has taken its toll on you... GAME OVER.") 
        quit()
        
    elif CH5 == "B":
        print("You decide to leave the star crystal where it is.  You determine its' power is too great for humans to handle.  THE END.")
        
    elif CH5 == "C":
        print("You choose the safest option of dragging the chest back to Earth.  When you arrive to Earth a group of scientists are able to harness the power of the star crystal, saving the planet from impending doom!  YOU WIN!!!!!")

    else:
        print("Please enter a valid option.")
        Chapter5()
        
Chapter5()