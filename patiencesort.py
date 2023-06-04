import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def merge_piles(piles: list[int]) -> list[int]:
	num = []
	while (True):
		minu = float("inf")
		index = -1
		for i in range(len(piles)):
			if (minu > piles[i][-1]):
				minu = piles[i][-1]
				index = i
		num.append(minu)
		piles[index].pop()
		if (not piles[index]):
			piles.pop(index)
		if (not piles):
			break
	return num

def patiencesort(num: list[int]) -> list[int]:
	piles = []
	for i in range(len(num)):
		if (not piles):
			temp = []
			temp.append(num[i])
			piles.append(temp)
		else:
			flag = True
			for j in range(len(piles)):
				if (comp(piles[j][-1], num[i]) == 1):
					piles[j].append(num[i])
					flag = False
					break
			if (flag):
				temp = []
				temp.append(num[i])
				piles.append(temp)
	ans = []
	ans = merge_piles(piles)
	return ans