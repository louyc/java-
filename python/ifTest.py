height = 1.70
weight =80.5
bmi = weight/(height*height)
if bmi>32:
	print('小明的bmi指数{0:.1f}%,严重肥胖'.format(bmi))
elif bmi>28:
	print('小明的bmi指数{0:.1f}%,肥胖'.format(bmi))
elif bmi>25:
	print('小明的bmi指数{0:.1f}%,过重'.format(bmi))
elif bmi>18.5:
	print('小明的bmi指数{0:.1f}%,正常'.format(bmi))
else:
	print('小明的bmi指数{0:.1f}%,过轻'.format(bmi))