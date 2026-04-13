# Assignment Code
from pyscript import dom, when

generateBtn = dom["#generate"][0]

# Write password to the #password input and add event listener to generate button
@when("click", "#generate")
def writePassword():
    password = generatePassword()
    passwordText = dom["#password"][0]
    passwordText.value = password

