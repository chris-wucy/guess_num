import random

r = random.randint(1, 100)
while True:
	num = input('請猜猜數字(1~100):')
	num = int(num)
	if num == r:
		print('答對囉！')
		break
	elif num > r:
		print('小一點！')
	else:
		print('大一點！')