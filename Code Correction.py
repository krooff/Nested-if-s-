# Task 1: Buggy Code

place = input("Choose a place: forest or cave? ")

# Added = on lines "4,6,8,10"
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
              #changed else to elif statement)
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
# Task 2" Setting the Scene    
    action = input("Light a Torch? or Proceed in the dark?")
    
if action == ("yes"):
    print("You find a hidden treasure!")
elif:
    print("Stumble and Leave in Embarasment")
    
else:
        print("Invalid choice.")
        pass  # Placeholder for invalid actions
    else:
        print("Invalid place selected.")
    pass  # Placeholder for invalid places: