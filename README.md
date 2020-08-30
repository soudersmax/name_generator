# Name Generator

## Objective

Randomly generate Benedict Cumberbatch meme names using Python code that conforms to established style guidelines



## Plan

1. Start with two lists - one for first name, one for last. 
2. Write a script that will generate tuples from the lists
3. Highlight the name in the interpreter window somehow so it stands out from command prompt
   1. print("whatever", file=sys.stderr) will print the output on the error channel in its standard red font
4. Ensure that code follows pythonic style recommendations



## Pseudocode

```
Load a list of first names
Load a list of surnames
Choose a first name at random
Assign name to variable
Choose a surname at random
Assign name to a variable
Print the names to the screen in order and in red font
Ask the user to quit or play again
if user plays again:
	repeat
if user quits
	end and exit
```

