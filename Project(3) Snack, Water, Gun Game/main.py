import random

youDic = {"s":1, "w":-1, "g":0} # Values are assinged to each letter for indicating the characters mentioned in the game.
reverseDic = {1:"Snake",0:"Gun",-1:"Water"}

print("=" * 130)
print("Welcome to the Snack-Water-Gun game!👋😍🎮")
print(">" * 130)

while True: # This is the outer loop control the flow of all program.
    Computer = random.choice([1,0,-1])

    while True: # This is the inner loop that address the user's input.
      youstr = input("Enter your choice: [s] for Snack, [w] for Water and [g] for gun.🛒🧐✍: \n")
      if youstr in youDic: # If the input of the user is  correct then loop break and program proceed.
        you = youDic[youstr] 
        break
      else: # If the users's input is incorrect then this condition will tell him for entering the correct input.
        print("*" *130) 
        print("Enter the valid input to proceed the process!")
        print("*" *130)
  
    you = youDic[youstr]
    print(f"Computer Chose: {reverseDic[Computer]}\nYou chose: {reverseDic[you]}") # It will print the choices of both user and Computer.
        

    if Computer == you:
        print("Game drew") # The game will drew, if both the input of user and Computer become same!
    else: # Following are the conditions for winning and losing in the game.
        if(Computer==1 and you==0):
            print("You won!🏆 🥇")
        elif(Computer==1 and you==-1):
            print("You lose!😥")
        elif(Computer==0 and you==1):
            print("You lose!😥")
        elif(Computer==0 and you==-1):
            print("You won!🏆 🥇")
        elif(Computer==-1 and you==0):
            print("You lose!😥")
        elif(Computer==-1 and you==1):
            print("You won!🏆 🥇")
        else:
            print("Choose a valid option between s, w, g")

    while True: # This loop control the restarting of the game, whether the user want to restart the game or not.
        play_again = input("Do you want to play again?💭📢 (yes/no): ")
        if play_again.lower() == "yes":
            print("=" *130)
            print("Welcome agin to Snack-Water-Gun game!😊✨🤗")
            print("Great! Let's play again!")
            print("=" *130)
            break
            
        elif play_again.lower() == "no":
            print("*" * 130)
            print("Thanks for playing the game! Goodbye👋💖✨✈️")
            print(">" * 130)
            exit() # If the user don't want to restart the game and enter no then the program will exit.
        else:
            print("*" * 130)
            print("Please enter a valid option (yes/no) to play again or exit the game.🚫✅")
            print(">" * 130) # This is the last condition, when the user enters something unexpected or something wrong instead yes or no.
             
        
 