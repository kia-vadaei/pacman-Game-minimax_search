# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState




def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn="scoreEvaluationFunction", depth="2", time_limit="6"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.time_limit = int(time_limit)


class AIAgent(MultiAgentSearchAgent):
    
    def minimax_alpha_beta(self, game_state : GameState, depth, alpha, beta, agent_indx):
        if depth == 0 or game_state.isWin() or game_state.isLose():
            return self.evaluationFunction()
        
        legal_actions = game_state.getLegalActions(agent_indx)  # 0 is pacman and else are ghosts
        
        #========================
        #       max player
        #========================

        if legal_actions == 0:  #pacman
            max_eval = - float('inf')
            for action in legal_actions:
                successor_state = game_state.generateSuccessor(agent_indx, action)
                eval = self.minimax_alpha_beta(successor_state, depth-1, alpha, beta, (agent_indx + 1) % 2)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
                return max_eval

        # # Min player (Agent minimizing the utility)
        else:
            minEval = float('inf')
            for action in legal_actions:
                successorState = game_state.generateSuccessor(agent_indx, action)
                eval = self.minimax_alpha_beta(successorState, depth - 1, alpha, beta, (agent_indx + 1) % game_state.getNumAgents())
                minEval = min(minEval, eval)
                beta = min(beta, minEval)
                if beta <= alpha:
                    break  # Alpha cut-off
            return minEval


    def getAction(self, gameState: GameState):
        """
        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

        # TODO: Your code goes here
        # util.raiseNotDefined()
