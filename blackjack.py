import random

class card(): #this class is to deal with ind. cards and their format of display:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

class deck():
  def __init__(self): 
    self.cards = []
    suits = ["heart", "spade", "diamond", "club"]
    ranks = [{"rank": "A","value": 11}, 
             {"rank": "2","value": 2}, 
             {"rank": "3","value": 3}, 
             {"rank": "4","value": 4},
             {"rank": "5","value": 5},
             {"rank": "6","value": 6},
             {"rank": "7","value": 7},
             {"rank": "8","value": 8},
             {"rank": "9","value": 9},
             {"rank": "10","value": 10},
             {"rank": "J","value": 10},
             {"rank": "Q","value": 10},
             {"rank": "K","value": 10}]
    for suit in suits:
      for rank in ranks:
        self.cards.append(card(suit,rank))
  
  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)
 
  def deal(self, number):
    cards_dealt = []
    if len(self.cards) > 0:
      for i in range(0, number):
        card = self.cards.pop()
        cards_dealt.append(card)
      return cards_dealt

class hand():
  def __init__(self, dealer = False): #handling to make a dealer
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value = 0
    is_ace = False

    for card in self.cards:
      card_value = int(card.rank['value'])
      self.value += card_value
      if card.rank['rank'] == "A":
        is_ace = True

    if is_ace and self.value > 21:
      self.value -= 10  #updating the value of A will to 1 instead of 11

  def get_value(self):
    self.calculate_value() #to run another function
    return self.value

  def is_blackjack(self):
    return self.get_value == 21 

  def display(self, show_all_cards = False):
    print("Dealer\'s hand:") if self.dealer else print("Your hand:")
    for index,card in enumerate(self.cards):
      if index == 0 and self.dealer and not show_all_cards \
      and not self.is_blackjack(): #the if condition is for dealer only
        print("Hidden")
      else:
        print(card)

    if not self.dealer:
      print("Value: ", self.get_value())
    print()

class game():
  def __init(self):
    pass

  def play(self):
    self.game_number = 0
    self.games_to_play = 0

    while self.games_to_play <= 0 :
      try:
        self.games_to_play = int(input("Enter the number of games: "))
      except ValueError:
        print("Input has to be an integer.")
        
    while self.game_number < self.games_to_play:
      self.game_number += 1

      deck1 = deck()
      deck1.shuffle()

      player_hand = hand()
      dealer_hand = hand(dealer = True) #dealer was by default false.

      for i in range(2):
        player_hand.add_card(deck1.deal(1))
        dealer_hand.add_card(deck1.deal(1))

      print()
      print("* " * 30)
      print(f"{self.game_number} of {self.games_to_play}")
      print("* " * 30)
      
      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("stand or hit? (s/h): ").lower() #asking for the choice 1st time
        print()
        while choice not in ["h", "s", "stand", "hit"]: #if user inputs anything except for these elements, the choice will be asked again.
          choice = input("stand or hit? (s/h): ").lower()
          print()
        if choice == "hit" or choice == "h":   
          player_hand.add_card(deck1.deal(1))
          player_hand.display()


      #this entire code is for the stand choice:
      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck1.deal(1))
        dealer_hand_value = dealer_hand.get_value() 

      dealer_hand.display(show_all_cards = True) #to show the hidden card as well

      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final results: ")
      print("Your hand: ",player_hand_value)
      print("Dealer's hand: ",dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True) #this marks the end of the game.

    print("\nThanks for playing!")
          
  def check_winner(self, player_hand, dealer_hand, game_over = False):
    if not game_over: #this case is for hit i.e. the player is asking for more cards for higher value
      if dealer_hand.get_value() > 21:
        print("Dealer busted. You win!")
        return True
      elif player_hand.get_value() > 21:
        print("You busted. Dealer wins!")
        return True
      elif player_hand.is_blackjack():
        print("You win!")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer wins!")
        return True
      elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
        print("Both have blackjacks. It's a tie!")
        return True
    else: #this case is for stand i.e. the players do not ask for any more cards
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win!")
      elif player_hand.get_value() == dealer_hand.get_value():
        print("It's a tie!")
      else:
        print("Dealer wins!")
      return True
    return False
      
game1 = game()
game1.play()
