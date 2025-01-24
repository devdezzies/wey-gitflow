import sys 

def fizzBuzz(int: to):
    for i in range(to):
        if (i%3==0 && i%5==0):
            print("FizzBuzz")
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("Buzz")

def main():
    print("Hello world")

if __name__ == "__main__":
    main()
