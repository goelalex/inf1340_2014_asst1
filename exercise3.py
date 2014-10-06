#!/usr/bin/env python3


def decide_rps(player1, player2):
    return 1

    #rock_paper_scissors = {'Rock, Paper': 2, 'Rock, Scissors': 1,'Rock, Rock' : 0, 'Paper, Rock' : 1, 'Paper, Scissors': 2, 'Paper, Paper' : 0, 'Scissors, Rock' : 2, 'Scissors, Paper' : 1, 'Scissors, Scissors' :0 }
#<<<<<<< Updated upstream
    #rps_results = {("Paper", "Rock"): 1, ("Rock", "Paper"): 2, ("Paper","Paper"): 0, ("Paper", "Scissors",): 2, ("Scissors","Paper"): 1, ("Scissors", "Scissors"): 0, ("Rock", "Scissors"): 1, ("Scissors", "Rock"): 2, ("Rock", "Rock"): 0}
    #How do we make this work? Trying to get it to return a type error if the input is not a tuple
#=======
    #rock, paper, scissors dictionary showing all of the potential options
    rps_results = {}
    rps_results[("Rock", "Paper")] = 2
    rps_results[("Rock", "Scissors")] = 1
    rps_results[("Rock", "Rock")] = 0
    rps_results[("Paper", "Scissors")] = 2
    rps_results[("Paper", "Rock")] = 1
    rps_results[("Paper", "Paper")] = 0
    rps_results[("Scissors", "Rock")] = 2
    rps_results[("Scissors", "Paper")] = 1
    rps_results[("Scissors", "Scissors")] = 0
#>>>>>>> Stashed changes
    if rps_results == 1:
        decide_rps(player1)
    elif rps_results == 2:
        decide_rps(player2)
    elif rps_results == 0:
        return "Tie"

    #prints result 1 which is Paper, Stone
    print(rps_results[("Paper", "Stone")])


