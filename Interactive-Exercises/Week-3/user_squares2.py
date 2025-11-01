# This proram uses a loop to display a
# table of numbers and their squares.

def main():
   # Get the ending limit.
   print('This program displays a list of numbers')
   print('and their squares.')
   start = int(input('Enter the starting number? '))

   # Get the ending limit
   end = int(input('How high should i go? '))
   

   # Print table headings
   print()
   print('Number\tSquare')
   print('--------------')

   for number in range(start, end + 1):
       square = number ** 2
       print(f'{number}\t{square}')
    


main()
