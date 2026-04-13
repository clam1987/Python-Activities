chosenPet = "Lulu"

def sendMessage():
    print("Email us at meetafreind@waywardpets.com to make an appointment to meet your new friend.")
    return

shelter = {
  "dogs": ["Mackie", "Bernice", "Cookie Monster", "Spot"],
  "cats": ["Astrid", "Lulu", "Fluffy", "Mouser"],
  "apptMessage": sendMessage
}

# Debug the code below 
def dogMessage():
  print("Congrats! " + chosenPet + ", a great dog, is available for adoption!");
  apptMessage();

def catMessage():
  print("Congrats! " + chosenPet + ", an awesome cat, is available for adoption!");
  apptMessage();


if (dogs.includes(chosenPet)):
  dogMessage()
elif (cats.includes(chosenPet)):
  catMessage() 
else:
    print("It looks like the pet is not available.")
    print("Check out our featured dog, " + shelter[0] + ". or our featured cat, " + cat.shelter[1])

