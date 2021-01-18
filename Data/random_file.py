import random
x = "mohit"
len_r=random.choice(range(0,40))
r="".join(random.choice(x) for i in range(len_r))
print(r)