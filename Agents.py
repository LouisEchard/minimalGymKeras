import numpy as np
import pandas as pd
import random
import keras

class KerasAgent:
    def __init__(self,aExplorationFunction):

        self.gamma = 0.99
        self.explorationRate = 1.0 #to replace with expo
        self.decay = 0.99
        self.learning_rate = 0.03
        self.model = self.initializeNetwork()
        self.targetModel = self.initializeNetwork()
        self.simulationNumber = 500
        self.explorationFunction = aExplorationFunction
        self.memory = list()
        self.updateTarget()

    def ownLoss(self, aTarget, aPreds):
        myError = aPreds - aTarget

        return myError

    def updateTarget(self):

        # copy weights from model to target_model
        self.targetModel.set_weights(self.model.get_weights())


    def initializeNetwork(self):
        myModel = keras.models.Sequential()
        myModel.add(keras.layers.Dense(24, input_dim=self.state_size, activation='relu'))
        myModel.add(keras.layers.Dense(24, activation= 'relu'))
        myModel.add(keras.layers.Dense(self.outputSize, activation='linear'))
        myModel.compile(loss=self.ownLoss, optimizer=keras.optimizers.Adam(lr=self.learning_rate))

        return myModel

    def act(self, state):
        if np.random.rand() < self.explorationFunction.getExplorationChance():
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0]) # returns action