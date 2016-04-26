# try to create a basic blackjack game

import blackjack_base as bj
import blackjack_base_players as bj_player
from my_player import MyPlayer

# create the players

player1 = bj_player.ProtoPlayer(name='Steve')
player2 = bj_player.ProtoPlayer(name='Jenny')
player3 = bj_player.DealerRulesPlayer(name='David')
player4 = bj_player.DealerRulesPlayer(name='Lauren')
player5 = MyPlayer(name='Andy')
player_list = [player1, player2, player3, player5]

# set table minimum and maximum and the starting funds for each player

table_minimum = 5.0
table_maximum = 100.0
starting_funds = 100.0

# initialize game

game = bj.Game(player_list, table_minimum, table_maximum, starting_funds)

# play a round

game.ask_for_bets()
game.deal_starting_cards()
for player in player_list:
    game.play_hand(player)
game.dealer_play_hand()
game.settle_bets()
game.final_look_at_table()

