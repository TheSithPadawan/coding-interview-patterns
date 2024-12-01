# https://www.1point3acres.com/bbs/thread-774866-1-1.html
"""

card game
2 players, deck of 52 cards [1…52] unique integers
deal out cards
each player will take out the first card on the top of their stack of cards
whichever one has the highest value card wins that round
they will get those 2 points (one for each card)
continue until cards run out
winner has the highest score
print out who is the winner + score, loser + score

Game:
1. Deal card to two players deal()
2. Each player now has 26 cards
3. Start Game: each player take turns to get the first card, game score is being kept 
for each plyer
4. Aggregate results

Extension

want to play with N players, input is list of strings (len N) with their names
deck has M cards of distinct integers (1-M)
M=56 cards
3 players
18 cards per player
2 cards leftover
print out who is the winner + score, losers + scores

"""

from collections import defaultdict
import random


class Game:
    def __init__(self, num_players, M) -> None:
        # might need to remove some number of cards for even distribution
        if M % num_players != 0:
            self.num_cards = M - (M % num_players)
            print('Effective number of cards', self.num_cards)
        else:
            self.num_cards = M            
        self.reset_game(num_players)
    
    def deal_cards(self):
        count = 0
        while self.cards:
            index = random.randint(0, len(self.cards) - 1)
            self.cards[index], self.cards[-1] = self.cards[-1], self.cards[index]
            card = self.cards.pop()
            player_id = count % self.num_players
            self.players[player_id].append(card)
            count += 1

    def start_game(self):
        self.deal_cards()
        round = 0
        while round < self.num_cards // self.num_players:
            highest = 0
            highest_player = 0
            for i in range(self.num_players):
                current_player = i
                current_card = self.players[current_player].pop()
                if current_card > highest:
                    highest = current_card
                    highest_player = current_player
            # record score for winner for current round
            # print(f'round {round}: winner {highest_player}')
            self.scores[highest_player] += 2
            round += 1
            

    def get_winner(self):
        winner = 0
        maxscore = 0
        print('---- Score Board ----')
        for playerId, score in self.scores.items():
            print(f'PlayerId: {playerId}, Score: {score}')
            if score > maxscore:
                maxscore = score
                winner = playerId
        print('Winner of current game:', winner, 'Score:', maxscore)
    
    def reset_game(self, num_players):
        self.cards = [i for i in range(1, self.num_cards + 1)]
        self.scores = defaultdict(int)
        self.num_players = num_players
        self.players = dict()
        for i in range(num_players):
            self.players[i] = []

if __name__ == '__main__':
    game = Game(2, 52)
    game.start_game()
    game.get_winner()

    # test another game configuration
    game = Game(3, 56)
    game.start_game()
    game.get_winner()