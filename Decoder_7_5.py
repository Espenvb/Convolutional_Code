import numpy as np

class Conv_7_5_dec:
    def __init__(self, T, S):
        self.T = T
        self.S = S
        self.prob = np.zeros((T, S))
        self.prev = np.zeros((T, S))

        self.states = np.array([0, 1, 2, 3])
        self.init_probs = np.array([1, 0, 0, 0])
        self.trans = np.array([
            [1, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 1, 0, 1]
        ])
        self.emit = np.array([
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0]
        ])

        self.input = np.array([
            [0, None, 1, None],
            [0, None, 1, None],
            [None, 0, None, 1],
            [None, 0, None, 1]
        ])

    def decode_symbol(self, symbol):
        self.prob.fill(0)
        self.prev.fill(0)

        for s in self.states:
            self.prob[0][s] = self.init_probs[s] * self.emit[s][symbol[0]]

        for t in range(1, self.T):
            for s in self.states:
                for r in self.states:
                    current_obs = symbol[t]
                    new_prob = self.prob[t-1][r] * self.trans[r][s] * self.emit[s][current_obs]
                    if new_prob > self.prob[t][s]:
                        self.prob[t][s] = new_prob
                        self.prev[t][s] = r

        path = np.zeros(self.T, dtype=int)
        values = np.zeros(self.T-2, dtype=int)
        path[self.T-1] = np.argmax(self.prob[self.T-1])
        for t in range (self.T-2, 0, -1):
            path[t] = self.prev[t+1][path[t+1]]

        for t in range(self.T-2):
            values[t] = self.input[path[t]][path[t+1]]

        return path, values