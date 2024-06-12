import random

import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     


def play_again(balance):
  play_or_not = input(
    "\nDo you want to play again? Type 'yes' or 'no': ").lower()

  if play_or_not == "yes":
    if balance > 0:
      restart(balance)
    else:
      print("You don't have enough money to play again.")
      money_choice = input("\nDo you deposit more money? Type 'yes' or 'no': ").lower()

      if money_choice == "yes":
        restart(int(input("Amount you want to deposit: Rs.")))

      else:
        print("Thank you for playing.")
        

  else:
    print("\nThank you for playing.")

def restart(balance):
  os.system('clear')
  print(logo)

  print(f"Your balance is Rs.{balance}")
  while True:
    user_bet = int(input("Place your bet: Rs."))
    if user_bet > balance:
      print("You don't have enough balance to place this bet.")
    else:
      break

  balance -= user_bet
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_card = random.sample(cards, 2)

  print(f"Your cards:{user_card},Your current score:{sum(user_card)}")
  computer_card = random.sample(cards, 2)
  print(f"Computer's first card:{computer_card[0]}")
  
  while sum(user_card) <= 21:
    user_choice = input(
        "\nType 'hit' to get another card or type 'stand' to pass: ").lower()

    if user_choice == "hit":
      user_new_card = random.choice(cards)
      user_card.append(user_new_card)

      if user_new_card == 11 and sum(user_card ) > 21:
        user_card.pop()
        user_card.append(1)

      print(f"\tYour cards:{user_card},Your current score:{sum(user_card)}")

      if sum(user_card) > 21:
        print("Busted! You loose.")
        play_again(balance)
        break

    else:
      print(f"\nYour final hand:{user_card}, Your final score:{sum(user_card)}")
      while sum(computer_card) <= 16:
        comp_new_card = random.choice(cards)
        computer_card.append(comp_new_card)
        
        if comp_new_card == 11 and sum(computer_card ) > 21:
          computer_card.pop()
          computer_card.append(1)
        
      print(f"Computer's final hand:{computer_card}, Computer's final score:{sum(computer_card)} ")

      if sum(computer_card) > 21:
        print("Computer busted! You win.")
        balance += user_bet * 2
        print(f"Your balance is Rs.{balance}")
        play_again(balance)
        break

      else:
        if sum(user_card) > sum(computer_card):
          print("\nYou win.")
          balance += user_bet * 2
          print(f"Your balance is Rs.{balance}")
          play_again(balance)
          break

        elif sum(user_card) == sum(computer_card):
          print("\nIts a draw.")
          balance += user_bet
          print(f"Your balance is Rs.{balance}")
          play_again(balance)
          break
        
        else:
          print("\nYou loose.")
          play_again(balance)
          break

print(logo)
          
restart(int(input("Amount you want to deposit: Rs.")))
