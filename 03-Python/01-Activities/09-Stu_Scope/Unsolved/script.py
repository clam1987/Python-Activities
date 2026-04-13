# TODO: Declare variable 'shout' with the value 'Shout' so it's available to `justShout` and `shoutItAllOut` functions
def justShout():
    print(shout + ", " + shout)
    return

def shoutItAllOut():
    print(shout + " it all out! ")
    return

justShout()
shoutItAllOut()

# TODO: Declare variable 'animal' with the value 'Tigers' so it is only available to the 'sayTigers' function
def sayLions():
    animal = "Lions"
    print(animal)
    return

def sayTigers():
    print("and " + animal + " and ")
    return

# TODO: The variable 'bears' should only declared once and 'sayBears' should return "Bears! OH MY!". 
bears = "Bears"

def sayBears():
    bears = "Pandas"
    print(bears + "! OH MY!")
    return

sayLions();
sayTigers();
sayBears();

# TODO: The variable 'sing' should be declared once in the local scope.
sing = "Sing"; 

def singAlong():
    print(sing + ",")
    def singASong():
        print(sing + " a Song.")
    singASong()

singAlong();
