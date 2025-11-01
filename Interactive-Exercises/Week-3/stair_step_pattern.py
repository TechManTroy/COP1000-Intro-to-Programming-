# This prgram displays a STAIR-STEP pattern




def main():
    NUM_STEPS = 8


    for r in range (NUM_STEPS):
        for c in range(r):
            print(' ', end='')
        print('#')    
main()
