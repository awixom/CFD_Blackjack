
# bring in base classes

import blackjack_base as bj
import blackjack_base_players as bj_players
import numpy as np

# define a "hot streak" player class that bets based on how much they've been
# winning

class HotStreakPlayer(bj_players.DealerRulesPlayer):

    def __init__(self, name='Andy'):
        bj_players.DealerRulesPlayer.__init__(self, name)
        self.num_prev_hands = 10
        self.prev_hand_count = 0
        self.previous_hands = np.zeros(self.num_prev_hands)

    def bet(self, current_funds, minimum_bet, maximum_bet):

        # determine bet as a function of how many previous hands won

        avg_wins = self.previous_hands.mean()
        scaled_bet = minimum_bet + (maximum_bet-minimum_bet)*avg_wins

        return scaled_bet

    def final_look(self, final_table):

        # recreate my hand

        my_cards = final_table[self.name]
        my_hand = bj.Hand(list(my_cards))

        # recreate dealer hand

        dealer_cards = final_table['Dealer']
        dealer_hand = bj.Hand(list(dealer_cards))

        # compare scores

        my_score = my_hand.best_score()
        dealer_score = dealer_hand.best_score()

        if my_score == 'blackjack':
            if dealer_score == 'blackjack':
                self.previous_hands[self.prev_hand_count] = 0
            else:
                self.previous_hands[self.prev_hand_count] = 1
        elif my_score == 'bust':
            self.previous_hands[self.prev_hand_count] = 0
        else:
            if dealer_score == 'blackjack':
                self.previous_hands[self.prev_hand_count] = 0
            elif dealer_score == 'bust':
                self.previous_hands[self.prev_hand_count] = 1
            else:
                if my_score > dealer_score:
                    self.previous_hands[self.prev_hand_count] = 1
                elif my_score < dealer_score:
                    self.previous_hands[self.prev_hand_count] = 0
                else:
                    self.previous_hands[self.prev_hand_count] = 0

        # iterate prev_hand counter (mod num previous hands)

        self.prev_hand_count += 1
        self.prev_hand_count = self.prev_hand_count % self.num_prev_hands


