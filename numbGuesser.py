import random

border = '================'



def main():
    while True:
        print(border)
        print("Guess the Number!")
        randNumb = random.randint(1,100)
        guesses = 0
        
        while guesses < 5:
            print(border)
            
            try:
                
                guess = int(input("try: "))
                
                if guess == randNumb:
                    print("YOU WIN!!!")
                    break
                elif guess < randNumb:
                    print("TOO LOW!!!")
                    guesses += 1
                    print(f"tries left:{5-guesses}")
                else:
                    print("TOO HIGH!!!")
                    
                    guesses += 1
                    print(f"tries left:{5-guesses}")
            except:
                print("GIVE A NUMBER")
            
        if guesses >= 5:
            print("AWW, TOO MANY TRIES!!!")
            print(f"The number was {randNumb}")
            
        tryagain = input(str("TRY AGAIN??? (y/n)"))
        if tryagain == 'n':
            break

main()