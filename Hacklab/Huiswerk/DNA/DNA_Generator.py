# DNA Generator

import random

def DNA_Gen(lengte):
    karakters = ['C', 'G', 'A', 'T']
    return ''.join(random.choice(karakters) for _ in range(lengte))