import sys
import os
h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
for i in range(1,((h2*60)+m2)+1):
    m1=m1+1
    if m1>59:
        m1=0
        h1+=1
        if h1>23:
            h1=0
print(f"{h1:02d}",f"{m1:02d}")


