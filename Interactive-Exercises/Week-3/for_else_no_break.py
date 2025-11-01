# This program demonstrates a loop with an else clause. In
# this example, the break statement is executed.

def main():

    for n in range(3):
        if n == 5:
            print('Breaking out of loop.')
            break
        print(n)
    else:
        print(f'After the loop, n is {n}.')

     
  
main()
