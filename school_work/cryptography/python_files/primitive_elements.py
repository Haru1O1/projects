def primitive_elm(n):
	prim = []
	for i in range (2, n):
		ones = 0
		for j in range (2, n):
			res = i ** j % n
			if res == 1:
				print("i: ", i, " j: ", j, " res: ", res, sep="")
				ones += 1
				continue
		if ones == 1:
			prim.append(i)
	return prim

def main():
	n = 13
	print("primitive elments are ", primitive_elm(n), sep="")

if __name__ == "__main__":
	main()
