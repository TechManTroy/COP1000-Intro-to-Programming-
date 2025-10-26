#Wacky Word Game program
#Part 1: Request the input words.
first_name = input("Type your name, and select enter: ")
print("")
print("Hello " + first_name + ". Let's play a game.")
print("")
adjective1 = input("Tell me an adjective, and select enter. red ")
noun1 = input("Tell me a noun (plural), and select enter. cars ")
noun2 = input("Tell me another noun (plural), and select enter. clous ")
adjective2 = input("Tell me another adjective, and select enter. speedy ")

#Part 2: Print the poem.
print(first_name + "'s Wacky Word Game")
print("")
print("Roses are " + adjective1)
print(noun1 + " are blue")
print(noun2 + " are " + adjective2)
print("And so are you!")