import random

start = input('請決定隨機範圍, 開始值： ')
end = input('請決定隨機範圍, 結束值： ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜猜數字(1~100):')
	num = int(num)
	if num == r:
		print('答對囉！')
		print ('這是你猜的第', count, '次！')
		break
	elif num > r:
		print('小一點！')
	else:
		print('大一點！')
	print ('猜第', count, '次囉！')