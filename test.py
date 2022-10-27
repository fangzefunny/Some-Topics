import numpy as np

class DDM:
    name = 'standard, DDM'

    def __init__(self, params):
        self._load_params(params)

    def _load_params(self, params):
        self.nu  = params[0] # drift rate mean, ν
        self.eta = params[1] # drift rate sd, η
        self.b   = params[2] # bound b
        self.z   = params[3] # prior z
        self.t0  = params[4] # non-decison time t0

    def decide(self, N, T, rng):
        '''Make a decision

        Args: 
            N: Total number of trials
            T: Terminated timesteps
        
        Outputs:
            RT:   reaction time
            act:  action (-1, 0, 1)
            traj: evidence trace
        '''
        # init storages
        RT   = np.zeros([N,]) + np.nan
        act  = np.zeros([N,])
        traj = np.zeros([N, T]) 

        DV = self.z 
        for t in range(T):

            # δ = ν + ηε, ε ~ N(0, 1)
            delta = self.nu + self.eta*rng.randn(N)
            # add increment after nondecision time 
            DV += delta*(t-self.t0 >= 0)

            # collect data 
            RT[(DV > self.b) * (act==0)] = t
            RT[(DV < 0) * (act==0)] = t
            act[(DV > self.b) * (act==0)] = 1
            act[(DV > self.b) * (act==0)] = -1
            traj[:, t] = DV
            traj[act==1, t] = self.b
            traj[act==-1, t] = 0

        return RT, act, traj

if __name__ == '__main__':

    params = [1, 10, 500, .5, 0]
model = DDM(params)
model.decide(100, 1000, rng=np.random.RandomState(123))