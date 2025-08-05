import random
print("*" * 130)
print("Welcome to the Guess the Number Game!👋😍🎮😊✨🤗")
print("=" * 130)
while True:  # This is outer loop that will help to play the game again or exit.
    rand_num = random.randint(1, 150) # Randomly generate a number between 1 and 150
    guess = 0
    n = None
    while(n!= rand_num):
        try:
            n = int(input("Enter your guess(between 1-150): ")) # Input from user
            guess += 1
        except ValueError: # Handle the case where user enters a non-integer value.
                print("Invalid input! Please enter a integer, not anything else, for trying this game!")
                continue
        if n > rand_num:
            print("Please! Try a lower number.")
        elif n < rand_num:
            print("Please! Try a higher number.")
        else:
            if guess <= 10:
                print("=" * 130) # This is the average level of attempts, when the game is over in this range of attempts.
                print("Congratulation!✌️✅ 🎀 You passed the average level successfully!")
                print(f"\nYou passed the average score in {guess} attempts:  {rand_num}!")
                print("<" * 130)
            elif guess <= 5:
                print("=" * 130) # This is the good level of attempts, when the game is over in this range of attempts.
                print("Congratulation!🎁✨🎉 You passed the intermediate level successfully!")
                print(f"\nYou passed the intermediate score in {guess} attempts:  {rand_num}!")
                print("<" * 130)
            elif guess <= 3:
                print("" * 130) # This is the genius level of attempts, when the game is over in this range of attempts.
                print("Congratulation! 🏆 🥇 😎 You passed the genius level successfully!")
                print(f"\nCongratualation! You passed the genius score in {guess} attempts:  {rand_num}!")
                print("<" * 130)
            elif guess <= 1:
                print("=" * 130) # This is the expert level of attempts, when the game is over in just one shot or attempt.
                print("Wow! Gorgeous! You passed the expert level successfully! 🥳🎊")
                print(f"\nYou passed the expert score in {guess} attempts:  {rand_num}!")
                print("<" * 130)
            else:  # This is the case when the user has guessed the number but not in above mentioned levels.
                print("<" * 130) # This is the case when the user has guessed the number but not in above mentioned levels.
                print(f"\nYou guessed the number {rand_num} in {guess} attempts, but you can do better next time!")
                print("=" *130)
                print("Congratulations!👏 You guessed the number correctly!") # This is the feedback to give motivation to user to try different attempts and make himself better.
            
            
            
    print("*" * 130)
    while True:
            
        Play_again = input("Do you want to play again? (yes/no): ") # Input from user to play again or exit the game, to prevent them from boring.
        if Play_again.lower() == 'yes': # If user wants to play again, then the game will start again.
            print("*" * 130)
            print("Welcome again 👋😍🎮 to the Guess the Number Game!")
            print("Great! Let's play again!")
            print("*" * 130)
            break
        elif Play_again.lower() == 'no': # If user wants to exit the game, then the game will exit.
            print("*" * 130)
            print("Thank you for playing the Guess the Number Game!")
            print("We hope you had fun! Goodbye!")
            print("=" * 130)
            exit()
        else:
            print("Invalid input! Please enter 'yes' or 'no'.") # This is the case, when user enters anything other than 'yes' or 'no'.
        
        
    
print("*" * 130) # These are the sepcified levels of attempts that are mentioned in the game, for the user to know about the levels of attempts.
print("Levels of attempts:\n")
print("<" * 130)
print("Average level attempts:  10 ")
print("Good level attempts: 5 ") 
print("Genius level attempts: 3 ")  
print("Expert level attempts: 1 ")
print("=" * 130)
    
