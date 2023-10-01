import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import copy
import pickle
from Helper_Class import Game, QPlayer, RandomPlayer  # Import necessary classes

root = tk.Tk()
epsilon = 0.9
Q = pickle.load(open("Q_Values_Episodes_200000.p", "rb"))
player1 = QPlayer(mark="X", epsilon=0)
player2 = RandomPlayer(mark="O")
game = Game(root, player1, player2, Q=Q)

N_episodes = 10000
results = {'X': 0, 'O': 0, 'Draw': 0}  # Dictionary to keep track of results

for episode in range(N_episodes):
    print(f'Episode {episode + 1}/{N_episodes}')
    game.play()
    
    # Get the winner or 'Draw' after each episode
    winner = game.get_winner()
    results[winner] += 1
    
    game.reset()


# Plot the results after all episodes
labels = results.keys()
values = results.values()

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(f"Results of QPlayer vs RandomPlayer after {N_episodes} episodes")
plt.show()
