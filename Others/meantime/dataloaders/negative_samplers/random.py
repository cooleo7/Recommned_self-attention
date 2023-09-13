from .base import AbstractNegativeSampler

from tqdm import trange

import numpy as np


class RandomNegativeSampler(AbstractNegativeSampler):
    @classmethod
    def code(cls):
        return 'random'

    def generate_negative_samples(self):
        assert self.seed is not None, 'Specify seed for random sampling'
        np.random.seed(self.seed)
        items = np.arange(self.item_count) + 1
        prob = np.ones_like(items)
        #print("prob!!!", prob)
        prob = prob / prob.sum()
        assert prob.sum() - 1e-9 <= 1.0

        negative_samples = {}
        print('Sampling negative items')
        for user in trange(1, self.user_count+1):
            seen = set(self.user2dict[user]['items'])

            zeros = np.array(list(seen)) - 1  # items start from 1
            p = prob.copy()
            p[zeros] = 0.0
            #print("P!!!", p)
            #if p.sum() == 0 or p == 0:  #로직추가
            #if p == NaN or p.sum() == 0:  #로직추가
            #    continue      #로직추가
            
            print("P1!!!", p)
            if p.sum() == 0:
                for i in range(len(p)):
                    if i %2 == 0:
                        p[i] = 0.00001
                    else:
                        p[i] = 0
                p = p / p.sum()
            else:
                p = p / p.sum()
            #for i in range(len(p)):
            #    if p[i] == 'nan':
            #        p[i] = 0
            
            print("P2!!!", p)
            print("!!!!!", items)
            print("?????", self.sample_size)

            #samples = np.random.choice(items, self.sample_size, replace=False, p=p)  #삭제
            samples = np.random.choice(items, self.sample_size, p=p)  #수정
            negative_samples[user] = samples.tolist()
        return negative_samples
