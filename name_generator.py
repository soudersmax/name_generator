# Import dependencies
import sys
import random

# Print title and intro
print("\nWelcome the definitive Benedict Cumberbatch name generator!\n")

first = ["Benedryl", "Bendydick", "Benneyboop", "Bendycat", "Breadmachine", "Cucumber", "Bumblebee","Engelbert",
         "Brendadirk", "Bumpercar", "Buttercup","Butterfried","Buttduck","Balladry", "Butterfree","Battlefield",
         "Butterdish","Britishman", "Burningman","Beatrix", "Beenadick", "Robotnik", "Benedoop", "Bendthatdick",
         "Bumberbimble","Bunsenburner", "Bumblesnuff","Babadook","Blenderdick","Blunderbuss","Bubblesnatch",
         "Scumblewonk","Bonobo", "Bend-a-brick", "Rumplestump","Dinglebat", "Bubblegum","Bentobox","Beelzebub",
         "Bodysnatch","Bumblesnuff", "Bangerang", "Booblebong"]
         
last = ["Cabbagepatch", "Hairysnatch", "Cumberbop", "Tennismatch","Cookiebatch", "Thundersnatch", "Custardbath", 
        "Crackerjack", "Bandersnatch", "Baggageclaim","Humperdink","Cramplesnatch", "Slumbercatch", "Crumplezone",
        "Candycrush", "Cobsalad","Cataract", "Caterwaul", "Catinhat", "Counterstrike","Crumblescone","Fancyname",
        "Cagematch", "LacksAnAss", "Upyourass","Rubbersnatch","Shoopdawhoop", "Cuminbitch","Cinderblock",
        "Coochierash", "Crimpysnitch", "Cameltoe","Carrotstick", "Cummysnatch", "Cabbagewank","Dinglebat","Clobbersmash",
        "Fistybars", "Cummergrundle", "Fischybuns", "Cukooclock", "Scoobysnack","Crumpetbat","Chumbawabumba"]

# Create a while loop to generate names each time the player continues
while True:

    # Use random.choice to select an entry from each list and store it as a variable
    firstName = random.choice(first)
    lastName = random.choice(last)

    # Print the results, formatted as red from the error formatting
    print("\n")
    print("{} {}".format(firstName,lastName),file=sys.stderr)
    print("\n")

    # Receive player input and set loop to replay or quit
    try_again = input("\nTry again? (Press enter to play again or q to quit)\n")
    if try_again.lower() == "q":
        break
    

