# This proram uses a loop to display a
# table of numbers and their squares.

def main():
   # Get the ending limit.
   print('This program displays a list of numbers')
   print('(starting at 1) and their squares.')
   end = int(input('How high should I go? '))

   # Print table headings
   print('Number\tSquare')
   print('--------------')

   for number in range(1, end + 1):
       square = number ** 2
       print(f'{number}\t{square}')
    


main()
