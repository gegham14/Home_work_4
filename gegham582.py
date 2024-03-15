

def game_with_pc(arr):
    gamers_score = []
    i = 0
    while i < len(arr):
        if arr[i:i+6].count('b') == 6:
            arr = arr[i + 6:]
            gamers_score.append('b')
            i = 0
        elif arr[i:i+6].count('a') == 6:
            arr = arr[i + 6:]
            gamers_score.append('a')
            i = 0
        else:
            i += 1
    if gamers_score.count('b') == gamers_score.count('a'):
        return "Gexam"
    return 'PC Wins' if gamers_score.count('b') > gamers_score.count('a') else 'I Win'


results = ['b', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
print(game_with_pc(results))


def game_with_pc(arr):
    text = ''.join(arr)
    return 'PC Wins' if text.count('bbbbbb') > text.count('aaaaaa') else 'I Win'

results = ['b', 'a', 'a', 'a', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'b', 'b', 'b', 'b','b', 'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
print(game_with_pc(results))


