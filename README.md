# gym-qiskit-game
Use a combination of qiskit and OpenAI's gym to create a game. This 2-player game consists, starting from a 6-qubit circuit initialized at |+>|->|+>|->|+>|-> to measure as many |0> or |1> depending on which player you are. One is allowed to use H, X, Z, and the controlled version of this last two gates to achieve that goal.
This game can be easily played using the IBM Q experience, so the aim of this repository is to create an AlphaZero like agent that is able to play this game.
