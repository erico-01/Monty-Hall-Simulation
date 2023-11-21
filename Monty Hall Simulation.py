import random

selected_door = 0
prizes = ["car", "goat", "goat"]
revealed_door = 0
wins = 0


def pick_a_door():
    global selected_door
    selected_door = random.randint(0, 2)

def reveal_goat():
    global prizes
    global selected_door
    global revealed_door
    for i in range(3):
        if i == selected_door:
            continue
        if prizes[i] == 'goat':
            revealed_door = i
            break

def shuffle_prizes():
    random.shuffle(prizes)

def switch_door():
    global selected_door
    for i in range(3):
        if i != selected_door and i != revealed_door:
            selected_door = i
            break
            
def count_wins():
    global wins
    global prizes
    if prizes[selected_door] == "car":
        wins += 1


def reset_game():
    global selected_door
    global prizes
    global revealed_door
    global wins

    selected_door = 0
    prizes = ["car", "goat", "goat"]
    revealed_door = 0
    wins = 0
                         
if __name__ == "__main__":
    test_cases = int(input("Input number of test cases: "))
    for _ in range(test_cases):
        shuffle_prizes()
        pick_a_door()
        reveal_goat()
        count_wins()
    print(f"Total number of winning games without switching: {wins}")
    print(f"Percentage of games won: {round((wins/test_cases)*100, 2)}%")
    reset_game()
    print("With switching")
    for _ in range(test_cases):
        shuffle_prizes()
        pick_a_door()
        reveal_goat()
        switch_door()
        count_wins()
    print(f"Total number of winning games with switching: {wins}")
    print(f"Percentage of games won: {round((wins/test_cases)*100, 2)}%")
