#!/usr/bin/env python3


def decide_rps(player1, player2):
    return 1

    #rock_paper_scissors = {'Rock, Paper': 2, 'Rock, Scissors': 1,'Rock, Rock' : 0, 'Paper, Rock' : 1, 'Paper, Scissors': 2, 'Paper, Paper' : 0, 'Scissors, Rock' : 2, 'Scissors, Paper' : 1, 'Scissors, Scissors' :0 }
<<<<<<< Updated upstream
    rps_results = {("Paper", "Rock"): 1, ("Rock", "Paper"): 2, ("Paper","Paper"): 0, ("Paper", "Scissors",): 2, ("Scissors","Paper"): 1, ("Scissors", "Scissors"): 0, ("Rock", "Scissors"): 1, ("Scissors", "Rock"): 2, ("Rock", "Rock"): 0}
    #rps_results[("Rock", "Paper")] = 2
    #rps_results[("Paper", "Stone")] = 1
    #rps_results[("Paper", "Rock")] = 1
=======
    rps_results = {}
    rps_results[("Rock", "Paper")] = 2
    rps_results[("Paper", "Stone")] = 1
    rps_results[("Paper", "Rock")] = 1
>>>>>>> Stashed changes


    #prints result 1 which is Paper, Stone
    print(rps_results[("Paper", "Stone")])


