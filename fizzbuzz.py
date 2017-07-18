number = int (input("Enter a number to play the game FizzBuzz"))
if number%3==0 and number%5==0:
    print ("FizzBuzz")
elif number%3==0:
    print ("Fizz")
elif number%5==0:
    print ("Buzz")
#elif number%3==0 and number%5==0:
    #print ("FizzBuzz")
else:
    print ("Bad Number")
