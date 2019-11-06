import gym

from qiskit import *
%matplotlib inline

from gym import error, spaces, utils . #Probably my own space
from gym.utils import seeding

import numpy as np
import math

from qiskit import(
  QuantumCircuit,
  execute,
  Aer)




class QiskitGameEnv(gym.Env):
  '''
  The game starts in state |+>|->|+>|->|+>|-> and the objective of each player is to measure as many 0 or 1 as possible
  '''
  metadata = {'render.modes': ['human']}

  def __init__(self):

        self.max_turns = 10
        self.qubits = 6
        self.turn = True
        self.objective = 1 #Assume 1 means that we want to measure 1
        self.adversary_objective = -self.objective
        
        self.gates = ['H','X','Z','CX',CZ','M']
        
        '''
        ACTIONS = { 'H':  000,
                    'M':  100,
                    'X':  200,
                    'Z':  300,
                    'CX': 400,
                    'CZ': 500,
        '''
        
        self.simulator = Aer.get_backend('qasm_simulator')
        self.circuit = QuantumCircuit(self.qubits,self.qubits) #self.qubit qubits and self.qubit bits to store the result

        self.viewer = None
        
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(self.low, self.high, dtype=np.float32)

        self.seed()
        
  def step(self, action):
  
    self.step_count += 1
    
    if action[0] not in self.gates:
      raise Exception('Not valid gate!')
    
    if action[0] = 'H':
      self.circuit.h(action[1]) #apply Hadamard to qubit action[1]
      
    elif action[0] = 'M':
      self.circuit.measure(action[1],action[1]) #measures qubit in action[1] and saves the result to bit action[1]
      
    elif action[0] = 'X':
      self.circuit.x(action[1]) #apply X to qubit action[1]
      
    elif action[0] = 'Z':
      self.circuit.z(action[1]) #apply Z to qubit action[1]

    elif action[0] = 'CX':
      self.circuit.cx(action[1],action[2]) #apply X to qubit action[1]
      
    elif action[0] = 'CZ':
      self.circuit.cz(action[1],action[2]) #apply Z to qubit action[1]

  def reset(self):
  
    self.circuit = QuantumCircuit(self.qubits,self.qubits)
    
    for qubit in self.qubits:
    
      if qubit % 2 == 1:
        self.circuit.x(qubit) #Apply X on the odd qubits
        
      self.circuit.h(qubit) #Apply H on all qubits
      
    return self.circuit # The initial state is |+>|->|+>|->|+>|->

    
  def render(self, mode='human'):
    return self.circuit.draw()
    
    
    
  def close(self):
  
