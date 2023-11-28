import random



attempts_list = []

attempts = 0

def showing_results():
    if not attempts_list:
        print("There is no score now")
    else:
        print(f"Your score is {min(attempts_list)} attempts")    

random_number = random.randint(1,10)

userName = input("What's your name? ")



wanna_play = input(f"Hi {userName}, would you want to play ?"
                   "(Yes, No) "
                   ).lower()

if wanna_play != "yes":
    print("Thanks !")    
    exit()
else:
    showing_results()
    while True:
        try:
            guess = int(input("Please enter number range between 1 and 10 "))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess number range between 1 and 10")
            
            attempts+=1
            

            if (random_number == guess):
                attempts_list.append(attempts)
                print("Awesome! You got it")
                print(f"It took {attempts} attempts")
                wanna_play = input(f"Hi {userName}, would you want to play ?"
                   "(Yes, No) "
                   ).lower()
                if wanna_play == "no":
                    print("Thanks , hope you have a good day!")
                    showing_results()
                    exit()
                else:
                    attempts=0
                    random_number = random.randint(1,10)    
                    showing_results()
                    continue
            elif guess > random_number:
                print("It's lower")    
            else:
                print("It's heigher")    


        except ValueError as err:
            print(err)    


