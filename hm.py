numlist=[]
zerolist=[]
with open("号段.txt","r") as f:
    for i in f:
        with open('res.txt', "a") as pp:
            for s in range(0,10000):
                pp.write(i.strip() + str(s).zfill(4) + "\n")
                print("写入了:", i.strip() + str(s).zfill(4))
# for i in range(0000,10000):
#     zerolist.append(str(i).zfill(4))

