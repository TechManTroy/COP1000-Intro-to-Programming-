# This program reads and displays the contents
# of the philoso[hers.txt file

def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read the files contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(file_contents)




# Call the main function
if __name__ == "__main__":
    main()
    
    
