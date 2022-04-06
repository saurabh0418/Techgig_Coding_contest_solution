import sys
import os


for i in range(int(input())):
    n=int(input())
    g=int(input())
    prices=list(map(int,input().split()))
    prices.sort()
    print(sum(prices[:n]))
