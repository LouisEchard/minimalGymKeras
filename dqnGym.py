import gym
import numpy as np
import pandas as pd
import random
import keras



class Agent:
    def __init__(self, state_size, action_size):

        self.gamma = 0.99
        self.explorationRate = 1.0 #to replace with expo
        self.decay = 0.99
        self.learning_rate = 0.03

