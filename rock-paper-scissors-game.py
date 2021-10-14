import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0 for Rock, 1 for paper and 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed invalid number, you loose!")  
else:   
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print (f"computer choose {computer_choice}")
  print (game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You wins!")

  elif user_choice == 2 and computer_choice == 0:
    print("You loose")  
  elif computer_choice > user_choice:
    print("You loose!")
  elif user_choice > computer_choice:
    print("You Win")  
  elif computer_choice == user_choice:
    print("It's a Draw!")  
  else:
    print("You typed an invalid number, you lose!")
