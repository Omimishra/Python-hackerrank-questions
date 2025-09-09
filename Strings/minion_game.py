# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Both players are given the same string,S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S .

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
def minion_game(string):
    # your code goes here
    kevin_score = stuart_score = 0
    length = len(string)
    count = 0
    for c in string:
        if c in 'AEIOU':
            kevin_score += (length - count)
        else:
            stuart_score += (length - count)
        # string = string[1:]
        count += 1

    if (kevin_score > stuart_score):
        print(f'Kevin {kevin_score}')
    elif (stuart_score > kevin_score):
        print(f'Stuart {stuart_score}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)