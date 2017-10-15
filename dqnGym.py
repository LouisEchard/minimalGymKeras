import gym

import Agents
import functions
import numpy as np


if __name__ == "__main__":
    myExploration = functions.getExplorationFunction(functions.explorationFunctions.fixed)

    myEnv = gym.make('CartPole-v1')
    myStateSize = myEnv.observation_space.shape[0]
    myActionSize = myEnv.action_space.n
    myAgent = Agents(myExploration, myStateSize, myActionSize)
    isDone = False
    batchSize = 32
    simulations = 500

    for sim in range(myAgent.simulationNumber):
        myState = myEnv.reset()
        myState = np.reshape(myState, [1, myStateSize])
        for time in range(100):
            myAction = myAgent.runner()
            myNextState, myReward, done, _ = myEnv.step(myAction)
            myReward = myReward if not done else -10
            myNextState = np.reshape(myNextState, [1, myStateSize])
            myAgent.remember(myState, myAction, myReward, next_state, isDone)
            myState = myNextState
            if done:
                myAgent.update_target_model()
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(sim, 500, time, myAgent.explorationRate))
                break
        if len(myAgent.memory) > batchSize:
            myAgent.replay(batchSize)