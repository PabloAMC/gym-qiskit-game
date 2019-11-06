from gym.envs.registration import register

register(
    id='qiskit-game-v0',
    entry_point='gym_qiskit-game.envs:QiskitGameEnv',
)
register(
    id='qiskit-game-extrahard-v0',
    entry_point='gym_qiskit-game.envs:QiskitGameExtraHardEnv',
)
