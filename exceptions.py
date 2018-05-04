
#try is how to test for exceptions
#try says that all the code you're about to write can throw an exception
#if you're using try you should use except
#if try blows up except will handle it
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Your input is not correct!")
except ZeroDivisionError:
    print("you are dividing by 0")
#last except is kind of like else.
except:
    print("Something happened I don't know!")
#have to use try if using except
#have to use except if using try
#finally is like the clean up. If you have a file open for instance, 
#   when the tests are done finally closes the folder or does some similar actions
finally:
    print("I am always executed no matter what!")