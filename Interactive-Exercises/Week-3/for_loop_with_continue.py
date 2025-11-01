# This prgram demonstrates the continue statement with a for loop.

def main():
     
    for n in range (1, 11):
        
        if n % 3 == 0:
            continue
        print(n)
        
main()
