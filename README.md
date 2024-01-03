# Pacman AI Agent

## Overview

This project aims to implement an intelligent agent capable of performing in the Pacman game environment and achieving the highest score possible.
## Environment

In this phase of the project, we use the Pacman environment provided by UC Berkeley. The agent navigates through a maze, consuming small dots and avoiding ghosts. The objective is to eat the dots while avoiding collisions with ghosts. Eating large dots temporarily allows the agent to eat ghosts and score more points.

### Project Structure

```plaintext
multiagent.zip
├── multiAgents.py
├── pacman.py
├── game.py
└── util.py
```
### Getting Started

## Getting Started

To run the game, open the terminal in the game environment directory and execute the following command. Use arrow keys or the specified keyboard keys for agent movement.

```bash
python pacman.py -k 1
```
### Possible Actions

- Left: 'a'
- Right: 'd'
- Up: 'w'
- Down: 's'
- Stop: 'q'

## Actions

The agent can choose actions such as North, South, East, West, and Stop, provided the movement is legal. Actions are deterministic.
## Game Completion

The game ends under the following conditions:

- The agent collides with a ghost.
- All dots within the environment are consumed.
## Implementation

Each game state is defined by a `GameState`. Functions defined for this class allow you to retrieve the current game state and legal actions.

- `gameState.getLegalActions(agentIndex)`: Returns a list of legal actions for an agent.
- `gameState.generateSuccessor(agentIndex, action)`: Returns the successor game state after an agent takes an action.

The code should expand the game tree up to the specified depth, and leaf nodes in the Minimax tree should be scored using `self.evaluationFunction`.

## Testing

To test your algorithm, open the terminal in the game environment directory and execute the following command:

```bash
python pacman.py -p AIAgent -k 1 -a depth=4
```
