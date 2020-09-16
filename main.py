import os
from datetime import datetime

tournament_number = input("Les rives masquées #?: ")
video_file = input("Video file: ") or (tournament_number + ".mp4")
batching = True

while (batching):
    time_start = input("Starting time: ")

    player1 = input("Player 1: ")
    player1_characters = input("Player 1 Characters: ")

    player2 = input("Player 2: ")
    player2_characters = input("Player 2 Characters: ")

    bracket = input("Bracket: ")

    result = "LRM #{} - {} ({}) vs {} ({}) - {}".format(tournament_number, player1, player1_characters, player2, player2_characters, bracket)

    time_end = input("Ending time: ")

    time_startobject = datetime.strptime(time_start, '%H:%M:%S')
    time_endobject = datetime.strptime(time_end, '%H:%M:%S')

    time_difference = time_endobject - time_startobject

    os.system("ffmpeg -ss {} -i {} -to {} -avoid_negative_ts make_zero -c:v copy -c:a copy \"{}.mp4\"".format(
        time_start, video_file, time_difference, result))

    ask = input("Keep going?")

    if ask == "y":
        pass
    else:
        batching = False
