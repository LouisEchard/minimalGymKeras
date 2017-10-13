import numpy as np
import pandas as pd
import random
import keras

class KerasAgent:
    def __init__(self):

        self.gamma = 0.99
        self.explorationRate = 1.0 #to replace with expo
        self.decay = 0.99
        self.learning_rate = 0.03
        self.model = self.initializeNetwork()
        self.simulationNumber = 500



    def initializeNetwork(self):
        myModel = keras.models.Sequential()

        return myModel

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0]) # returns action