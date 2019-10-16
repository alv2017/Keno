import datetime
import random

# Game Parameters
N = 80
M = 20
K = 10
# Payouts
payout_table = [0, 0, 0, 0, 0, 3, 15, 100, 1000, 25000, 2500000]

def c(n, k):
    """
        Computes the number of all possible combinations 
        of k elements out of n.  
    """
    high = max(k, n-k)
    it = n
    s1 = 1
    s2 = 1
    while it > high:
        s1 *= it
        s2 *= (n - it + 1)
        it -= 1
    return round(s1/s2)

denom = c(N, K)
expected_game_return = -1
prob_test = 0

# probabilities and decimal odds
for i in range(K+1):
    numerator = c(M, i) * c(N-M, K-i)
    p = numerator / denom
    prob_test += p
    expected_game_return += p * payout_table[i]
    
# Expected game return
print("Expected game return: ", round(expected_game_return,4))
    
    