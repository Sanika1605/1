x=2
lr=0.01
precision=0.000001
previous_step_size=1
max_iter=10000
iters=0
gf=lambda x: (x+3)**2

gd=[]
while precision<previous_step_size and iters<max_iter:
    prev=x
    x=x-lr*gf(prev)
    previous_step_size=abs(x-prev)`
    iters+=1
    gd.append(x)
    print("Iteration: ", iters," Value: ",x)

print("Local Minima:",x)

import matplotlib.pyplot as plt
plt.plot(gd)