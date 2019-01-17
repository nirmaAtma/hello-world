"""test program"""
def main():
    print('Guess my number between 1 and 100')
    randomNumber = 44
    random = 55
    userGuess = input("Your Guess number: ")
    if (float(userGuess) == randomNumber+random):
        print ("YESS")
    else:
        print ("NOOO")
    
        
if __name__ == "__main__":
    main()
