# This prgram displays a retangluar pattern
# of asterisks



def main():
    rows = int(input('How many rows? '))
    cols = int(input('How many columns? '))


    for r in range (rows):
        for c in range (cols):
            print('*', end='')
        print()    
main()

