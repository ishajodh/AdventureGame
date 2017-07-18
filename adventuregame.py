import time
while True:
    print ("Welcome to my Adventure Game! You are lost in the middle of a forest, when you hear a tiger growling and getting closer to you. What do you do to escape the tiger and find your way out of the forest?")
    direction = input ("Do you turn left or right? ")
    if direction == "left":
        print ("After turning left, you see the tiger directly in front of you. What do you do now?")
        time.sleep (1.9)
        print ("Freeze and hope the tiger goes away")
        print ("Run away from the tiger")
        print ("Try to fight off the tiger")
        print ("Try to hide from the tiger")
        choice = input ("Type your decision: ")
        if choice == "Freeze and hope the tiger goes away":
            print ("The tiger does not go away, instead deciding to pounce on you. You die.")
        if choice == "Run away from the tiger":
            print ("You can't outrun the tiger, and it quickly catches up to you and you die a painful death.")
        if choice == "Try to fight off the tiger":
            print ("You manage to fight it off and escape the forest. You survived!!!")
        if choice == "Try to hide from the tiger":
            print ("The tiger is smart and sees you. It sneaks up behind you and jumps on your back before you even know it is there. You die.")
    elif direction == "right":
        print ("The growling gets quieter and quieter, so you have successfully gone away from the tiger. However, there is now a raging river in front of you. What do you do now?")
        time.sleep (1.9)
        print ("Build a raft to cross the river in")
        print ("Go back into the forest in the same way you just came from")
        print ("Sit down, wait, and hope the river becomes calm enough to cross")
        print ("Try to swim across the river")
        decision = input ("Type your decision: ")
        if decision == "Build a raft to cross the river in":
            print ("You waste too much time building the raft and it becomes night. You die from freezing in the cold.")
        if decision == "Go back into the forest in the same way you just came from":
            print ("Luckily, the tiger has moved on and is no longer there. You manage to find your way out of the forest and survive.")
        if decision == "Sit down, wait, and hope the river becomes calm enough to cross":
            print ("Unfortunately for you, the river does not calm down and you die from sitting in the cold.")
        if decision == "Try to swim across the river":
            print ("You manage to swim across the river, but the water was so cold that you suffered some damage. You are now paralyzed and almost brain dead. At least you're alive though. Hang in there.")

    print ("Would you like to play the game again?")
    answer = input ("Yes or No? ")
    if answer == "No":
        print ("Goodbye!")
        break
