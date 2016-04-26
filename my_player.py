
# bring in base classes

import blackjack_base as bj
import blackjack_base_players as bj_players

# define my player class

class MyPlayer(bj_players.ProtoPlayer):
    
    def __init__(self, name='Andy'):
        bj_players.ProtoPlayer.__init__(self, name)
        self.hands_won = 0

    def bet(self, current_funds, minimum_bet, maximum_bet):
        if self.hands_won > 10:
            return maximum_bet
        else:
            return minimum_bet
            
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
                pass
            else:
                self.hands_won += 1
        elif my_score == 'bust':
            pass
        else:
            if dealer_score == 'blackjack':
                pass
            elif dealer_score == 'bust':
                self.hands_won += 1
            else:
                if my_score > dealer_score:
                    self.hands_won += 1
                elif my_score < dealer_score:
                    pass
                else:
                    pass
                
