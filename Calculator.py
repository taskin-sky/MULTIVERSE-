#                       [STRING]
def string(): 
    print("STRING CLASS")
    
    name = input("What's your name? ").strip().title()
    print(f"hello, {name}")

    """
    # Reomve whitespace feom str
    name = name.strip()

    # Capitalize user's name
    name = name.capitalize()

    #Title 
    name = name.title()

    # Split user's name into first name and last name 
    first, last = name.split(" ")
    print(f"hello, {last}")
    
    #print("hello,", name)
    #print(*name, sep=' ', end='\n', file=None, flush=False)
    #print("hello,", name, sep=" ")
    """
#------------- String End -----------------





#                     [INTEGER]
def integer():
    print("INTRGER CLASS")
    
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    # How many digit after point(.)
    #print(round(x,2))

    #z = x + y
    #print(f"sum {z:,}")

    z = x / y
    print(f"sum {z:.2f}")
#----------- Integer End -------------





#                  [FUNCTION]

def mainString():
    name = input("What's your name? ")
    hello(name)
    
def hello(to = "World"):
    print("Hello,", to)
    
    
#twoDegitCalculator
def twoDegitCalculator():
    def main():
        type = input("Oparations \n1. Sum \n2. Sub \n3. Mul \n4. Div \n5. Squ \n6. Root \nSelect a number of oparation type \n") 
        x = float(input("x = "))
        y = float(input("y = "))
        
        if (type == "1"):
            print(f"{x} plus {y} is {round(summation(x, y),2)}")
            
        elif (type == "2"):
            print(f"{x} minus {y} is {round(substract(x, y),2)}")

        elif (type == "3"):
            print(f"{x} multiply {y} is {round(multiply(x, y),2)}")
            
        elif (type == "4"):
            if (y == 0):
                print ("Math Error")
            else:
                print(f"{x} devided {y} is {round(devided(x, y),2)}")
        
        elif (type == "5"):
            print(f"{x} to the power {y} is {round(power(x, y),2)}")
            
        elif (type == "6"):
            print(f"{x} rootOver {y} is {round(rootOver(x, y),2)}")
        

    def summation(n, m):
        return (n + m)

    def substract(n, m):
        return(n - m)

    def multiply(n, m):
        return (n * m)

    def devided(n, m):
        return(n / m)
    
    def power(n, m):
        return pow(n, m)

    def rootOver(n, m):
        return((n**(1 / m)))
    main()

twoDegitCalculator()

#--------------- Function End ---------------