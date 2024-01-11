import random

hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)

BACKSIDE = 'backside'

def getting_Bet(maximumbet):
    bet = input(f"How much do you want to bet? 1 - 500 or type quit : ")
    if bet == 'quit' or bet == 'QUIT':
        print("Thanks for playing")
        exit()
    if not bet.isdecimal() and bet > maximumbet:
        print("It should be a number between 1 - 500")
    bet = int(bet)
    return bet

def getting_deck():
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((str(rank), suit))
    random.shuffle(deck)
    return deck

def show_of_hands(players_hand, dealers_hand, show_dealers_hand):
    print()
    if show_dealers_hand:
        print('Dealer: ', get_hand_value(dealers_hand))
        display_cards(dealers_hand)
    else:
        print("DEALER: ???")
        display_cards([BACKSIDE] + dealers_hand[1:])
    
    print("PLAYER:", get_hand_value(players_hand))
    display_cards(players_hand)

def get_hand_value(cards):
    value = 0
    number_of_Aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_Aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    
    value += number_of_Aces
    for i in range(number_of_Aces):
        for i in range(number_of_Aces):
            if value + 10 <= 21:
                value += 10
    return value

def display_cards(cards):
    rows = ['','','','','']

    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)}  | '
            rows[2] += f'| {suit} | '
            rows[3] += '|__{}| '.format(rank.rjust(2, '_'))
    
    for row in rows:
        print(row)

def getting_move(player_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move
        

def main():
    money = 5000
    while True:  # Main game loop.
# Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            exit()

         # Let the player enter their bet for this round:
        print('Money:', money)
        bet = getting_Bet(money)

         # Give the dealer and player two cards from the deck each:
        deck = getting_deck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

         # Handle player actions:
        print('Bet:', bet)
        while True:  # Keep looping until player stands or busts.
            show_of_hands(playerHand, dealerHand, False)
            print()

             # Check if the player has bust:
            if get_hand_value(playerHand) > 21:
                break

             # Get the player's move, either H, S, or D:
            move = getting_move(playerHand, money - bet)
             # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getting_Bet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                 # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if get_hand_value(playerHand) > 21:
                   # The player has busted:
                    continue

            if move in ('S', 'D'):
               # Stand/doubling down stops the player's turn.
                break

         # Handle the dealer's actions:
        if get_hand_value(playerHand) <= 21:
            while get_hand_value(dealerHand) < 17:
                 # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                show_of_hands(playerHand, dealerHand, False)

                if get_hand_value(dealerHand) > 21:
                    break  # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

         # Show the final hands:
        show_of_hands(playerHand, dealerHand, True)
        playerValue = get_hand_value(playerHand)
        dealerValue = get_hand_value(dealerHand)
         # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')

if __name__ == '__main__':
    main()