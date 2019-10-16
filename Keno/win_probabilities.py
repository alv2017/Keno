import datetime
import random
from unicodedata import decimal

# Game Parameters
N = 80
M = 20
K = 10

# Payouts
payout_table = [0, 0, 0, 0, 0, 3, 15, 100, 1000, 25000, 2500000]
alt_weight = [0, 0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

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

probabilities = [0] * (K+1)
decimal_odds = [0] * (K+1)
alt_pay = [0] * (K+1)
denom = c(N, K)
prob_test = 0


# probabilities and decimal odds
for i in range(K+1):
    numerator = c(M, i) * c(N-M, K-i)
    p = numerator / denom
    prob_test += p
    probabilities[i] = p
    decimal_odds[i] = 1/p
    alt_pay[i] = alt_weight[i] * decimal_odds[i]
    
# printing summary
print("\nKeno Game Probabilities\n")
for i in range(K+1):
    print("{:<2}:".format(i), 
          "p: {:<12}".format(round(probabilities[i], 10)),
          "do: {:<12}".format(round(decimal_odds[i],2)),
          "pay: {:<10}".format(payout_table[i]),
          "alt_pay: {:<10}".format(round(alt_pay[i],2)),
          )
print("---------------------------")
print("Sum of Probabilities: ", round(prob_test, 4))


        