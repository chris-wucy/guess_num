import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜猜數字(1~100):')
	num = int(num)
	if num == r:
		print('答對囉！')
		print ('猜第', count, '次！')
		break
	elif num > r:
		print('小一點！')
	else:
		print('大一點！')
	print ('猜第', count, '次囉！')