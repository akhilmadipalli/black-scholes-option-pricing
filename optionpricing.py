"""
Black-Scholes-Merton Option Pricing Model

Calculates theoretical value of an option based on five variables: stock price (S), strike price (K), time to expiration (T), risk-free interest rate (R), and volatility (sigma).
"""

import math
from scipy.stats import norm

# Define the variables
S = 42  # Current stock price
K = 40  # Strike price
T = 0.5  # Time to expiration (years)
r = 0.037  # Risk-free interest rate (10 year Treasury bond yield 9-6-2024)
vol = 0.2  # Volatility (standard deviation of returns)


# Calculate d1 and d2
def black_scholes(S, K, T, r, vol):
    d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)

    # Calculate the Call Option Price (C)
    C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

    # Calculate the Put Option Price (P)
    P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return d1, d2, C, P


print("The value of d1 is {:.4f}".format(black_scholes(S, K, T, r, vol)[0]))
print("The value of d2 is {:.4f}".format(black_scholes(S, K, T, r, vol)[1]))
print(
    "The value of the Call Option is {:.4f}".format(black_scholes(S, K, T, r, vol)[2])
)
print("The value of the Put Option is {:.4f}".format(black_scholes(S, K, T, r, vol)[3]))
