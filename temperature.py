# this is a practice
choose = input('請問要轉換？1.華氏轉為攝氏；2.攝氏轉為華氏')
if choose == '1':
	F = input('現在是華氏幾度呢？')
	C = (float(F) - 32) * 5/9
	print(C)
if choose == '2':
	C = input('現在是攝氏幾度呢？')
	F = float(C) * 9/5 + 32
	print(F)