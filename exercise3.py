#!/usr/bin/env python3
"""
    Assignment 1, Exercise 3, INF1340 Fall 2014
    This module decides the result of a rock, paper, scissors game. The rules of
    the game are:
    Scissors beats Paper;
    Paper beats Rock;
    Rock beats Scissors;
    Other results are ties.
"""

_author__ = "Zhao Hu"
__email__ = "zhao.hu@mail.utoronto.ca"


def decide_rps(player1, player2):
    """
    Returns result of a rock, paper, scissors game
    :param:
        player1 (string):  rock, paper, scissors
        player1 (string):  rock, paper, scissors

    :return:
        integer: result of a rock, paper, scissors game
        Value is 0, 1, 2
    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is not rock, paper or scissors
    """
    #Defines different scenarios for Rock, Paper, Scissors
    rps_input = ("Paper", "Rock", "Scissors")
    input_player1 = ""
    input_player2 = ""
    rps_results = {("Paper", "Rock"): 1, ("Paper", "Scissors",): 2,
                   ("Paper", "Paper"): 0, ("Rock", "Paper"): 2,
                   ("Rock", "Scissors"): 1, ("Rock", "Rock"): 0,
                   ("Scissors", "Paper"): 1, ("Scissors", "Rock"): 2,
                   ("Scissors", "Scissors"): 0}
    # Check if both player1
    #  and player2 are string
    # Check if player1 is a correct input
    # Assign player1 to input_player1
    # Check if player2 is a correct input
    # Assign player1 to input_player1
    # Check if both input_player1
    # and input_player2 are not blank
    if type(player1) is str and type(player2) is str:
        for item in rps_input:
            if player1 == item:
                input_player1 = player1
            if player2 == item:
                input_player2 = player2
        if input_player1 and input_player2:
            return rps_results[(input_player1, input_player2)]
        else:
            raise ValueError("Invalid value passed as parameter")
    else:
        raise TypeError("Invalid type passed as parameter")
