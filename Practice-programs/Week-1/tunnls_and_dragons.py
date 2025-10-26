# Adventure Game Troy Edmonds
print("You are lost underground in a maze of tunnels.")
# Variable to generate random number between 1 and 2 
import random 
dangerTunnel = random.randint(1,2)
treasureTunnel = random.randint(1,2)
#print("Dragon in tunnel", dangerTunnel)
print("Treasure in tunnel", treasureTunnel)
tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 2: 
    
# Ask players to choose a tunnel 
    tunnelChoice = int(input("Choose tunnel 1 or tunnel 2:"))
# Compare choice to tunnel with dragon, safe or not 
print("You chose tunnel", tunnelChoice)
if tunnelChoice == dangerTunnel:
     print("You entered a tunnel with a dragon. Game Over!")
else:
     print("You entered an empty tunnel. You are safe for now.")

# Compare choice to tunnel with treasure, collect or not 
#print("You chose tunnel", tunnelChoice)
if tunnelChoice == treasureTunnel:
     print("You entered a tunnel with a treasure collect it!, if dragon is present Game Over!")
else:
     print("You entered an empty tunnel. with no treasure")


#Next tunnel 
