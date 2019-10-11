import random
with open("email.txt","w") as f:
    for i in range(1000001):
        f.write(''.join(str(random.choice(range(10))) for _ in range(10))+"@qq.com"+"\n")