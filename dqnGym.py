import gym

import Agent
import functions



if __name__ == "__main__":
    myAgent = Agent()
    myEnv = gym.make('CartPole-v1')
    myStateSize = myEnv.observation_space.shape[0]
    myActionSize = myEnv.action_space.n
    isDone = False
    myExploration = functions.getExplorationFunction(functions.explorationFunctions.fixed)

    for sim in range(myAgent.simulationNumber):
        myState = myEnv.reset()

        for time in range(100):
            myAction = myAgent.runner()
