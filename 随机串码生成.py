import random


def randomstr(lenth):
	str1='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	str2=''
	for i in range(lenth):
		str2+= str1[random.randint(0, 35)]
	return str2


if __name__=='__main__':
	with open("./code.txt", 'w', encoding='UTF-8') as f:
		for i in range(1000000):
			f.write(randomstr(8)+'\n')