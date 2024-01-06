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
import math 



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
            return self.evaluationFunction(game_state) , None
        
        
        legal_actions = game_state.getLegalActions(agent_indx)  # index 0 is pacman and else are ghosts

        #========================
        #       max player
        #========================
        

        if agent_indx == 0:  #pacman
            action_scores = []
            max_indices = []
            
            max_eval = float('-inf')
            for action in legal_actions:
                successor_state = game_state.generateSuccessor(agent_indx, action)
                eval , _ = self.minimax_alpha_beta(successor_state, depth , alpha, beta, (agent_indx + 1) % game_state.getNumAgents())
                print(f'eval is: {eval}')
                action_scores.append(eval)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
            for index in range(len(action_scores)):
                if action_scores[index] == max_eval:
                    max_indices.append(index)
            chosenIndex = random.choice(max_indices)
            print(f'legal is : {legal_actions}\naction score is: {action_scores}')
            return max_eval , legal_actions[chosenIndex]

        #========================
        #       min player
        #========================
    
        else:
            minEval = float('inf')
            if (agent_indx % game_state.getNumAgents()) == game_state.getNumAgents() - 1:
                depth -= 1 
            
            for action in legal_actions:
                successor_state = game_state.generateSuccessor(agent_indx, action)
                eval , _ = self.minimax_alpha_beta(successor_state, depth, alpha, beta, (agent_indx + 1) % game_state.getNumAgents())
                minEval = min(minEval, eval)
                beta = min(beta, minEval)
                if beta <= alpha:
                    break  # Alpha cut-off

            return minEval , None


    def getAction(self, gameState: GameState):
        
        # print(f'issssssss {self.evaluationFunction(gameState)}')
        initialAlpha = float('-inf')
        initialBeta = float('inf')


        possibleActions = gameState.getLegalActions(0)
        # action_scores = []

        # for action in possibleActions:
        #     action_scores.append(self.minimax_alpha_beta(gameState.generateSuccessor(0, action), self.depth,initialAlpha, initialBeta ,0 ))

        # max_action = max(action_scores)
        # max_indices = []
        # for index in range(len(action_scores)):
        #     if action_scores[index] == max_action:
        #         max_indices.append(index)
        
        # chosenIndex = random.choice(max_indices)
        # print(f'choosen is : {possibleActions[chosenIndex]}')
        _, action = self.minimax_alpha_beta(gameState, self.depth,initialAlpha, initialBeta ,0 )
        print(f'action: {action}')
        return action


        # TODO: Your code goes here
        # util.raiseNotDefined()