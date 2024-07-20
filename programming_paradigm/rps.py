import random

done = False

wins, losses, ties = 0, 0, 0

names = {"R": "rock", "P": "paper", "S": "scissors"}
loses = {'R': 'P', 'P': 'S', 'S': 'R'}
while not done:
    choice = input('Please choose your next move (R, P , S)(Q to quit): ').upper()
    cpu_choice = random.choice(['R', 'P', 'S'])
    if choice == cpu_choice:
        print(f"It's a tie you both chose {names[choice]}")
        ties += 1
    elif choice in ['R','P','S']:
        if cpu_choice == loses[choice]:
            print(f'Cpu wins its chose {names[cpu_choice]},and you chose {names[choice]}')
            losses += 1
        else:
            print(f'you win you chose {names[choice]},and the cpu chose {names[cpu_choice]}')
            wins += 1

    elif choice == 'Q':
        done = True
    else:
        print('invalid command')

    print(f'current stats: {wins} wins, {losses} losses, {ties} ties')