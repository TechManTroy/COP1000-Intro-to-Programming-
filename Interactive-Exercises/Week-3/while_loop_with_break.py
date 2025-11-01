# This prgram demonstrates the break statement with a while loop

def main():
    n = 0
    while n < 100:
        print(n)
        if n == 5:
            break
        n += 1


    print(f'The loop stopped and n is {n}')
            
        
main()
