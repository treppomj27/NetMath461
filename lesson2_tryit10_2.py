
import numpy as np

cash_initial = 20
prob_win = 0.51
reward = 1
penalty = -1
num_iterations = 1000
num_experiments = 1000

num_busted = 0
outcomes = []
for i in range(0, num_experiments):

    busted = False
    cash = cash_initial
    cash_positions = [cash]
    iterations = [0]
    rng_values = [np.random.uniform(low=0.0, high=1.0)]
    for ctr in range(1, num_iterations + 1):
        rng = np.random.uniform(low=0.0, high=1.0)
        if rng < prob_win:
            cash += reward
        else:
            cash += penalty
        if not busted and cash <= 0:
            busted = True
            busted_iteration = ctr
        cash_positions.append(cash)
        iterations.append(ctr)

    if busted:
        outcomes.append(0)
        num_busted += 1
    else:
        outcomes.append(cash_positions[num_iterations])

num_losses = 0
num_wins = 0
num_ties = 0
for i in range(0, len(outcomes)):
    if outcomes[i] < cash_initial:
        num_losses += 1
    elif outcomes[i] > cash_initial:
        num_wins += 1
    else:
        num_ties += 1

print()
print('     Number of Losses =', num_losses)
print('  ( Number Driven Out =', num_busted, ')')
print('       Number of Wins =', num_wins)
print('       Number of Ties =', num_ties)
print('--------------------------------')
print('Number of Experiments =', num_experiments, '\n')

print('       Losses / Total =', round(num_losses / num_experiments * 100, 2), '%')
print(' ( Driven Out / Total =', round(num_busted / num_experiments * 100, 2), '%', ')')
print('         Wins / Total =', round(num_wins / num_experiments * 100, 2), '%')
print('         Ties / Total =', round(num_ties / num_experiments * 100, 2), '%')
print('--------------------------------')
print('                      = 100.00%')

print()
print('Avg. Ending Cash Position = $', np.round(np.mean(outcomes), 2), '\n')
