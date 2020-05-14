
import numpy as np
import matplotlib.pyplot as plt

cash_initial = 100
prob_win = 0.5
reward = 5
penalty = -5
num_iterations = 1000

busted = False
busted_iteration = 0
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
    rng_values.append(rng)
    cash_positions.append(cash)
    iterations.append(ctr)

print('\nStarting Cash = $', cash_initial)
print('Number of Iterations =', num_iterations, '\n')
if busted:
    print('Busted!')
    print('Ending Cash = $ 0')
else:
    print('Ending Cash = $', cash_positions[num_iterations])

plt.plot(iterations, cash_positions, color='green')
plt.axhline(cash_initial, color='blue')
plt.axhline(0, color='red')
if busted:
    plt.axvline(busted_iteration, color='orange')
plt.xlabel('Iteration')
plt.ylabel('Cash Position')
plt.title('Cash Positions Over Time')
if busted:
    plt.legend(['Cash Positions', 'Starting Cash', 'No Cash', 'Busted Iteration = ' + str(busted_iteration)])
else:
    plt.legend(['Cash Positions', 'Starting Cash', 'No Cash'])
plt.show()
