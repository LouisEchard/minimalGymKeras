import gym
import numpy as np
import pandas as pd
import random
import keras



class Agent:
    def __init__(self):

        self.gamma = 0.99
        self.explorationRate = 1.0 #to replace with expo
        self.decay = 0.99
        self.learning_rate = 0.03
        self.initializeNetwork()

    def initializeNetwork(self):
        myModel = keras.models.Sequential()

        return myModel


if __name__ == "__main__":
    myAgent = Agent()