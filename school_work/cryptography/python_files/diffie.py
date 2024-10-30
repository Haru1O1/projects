def diffieHel(p, alpha, a, b):
	common = 0
	public_keyA = (alpha ** a) % p
	public_keyB = (alpha ** b) % p
	commonkeyA = (public_keyB ** a) % p
	commonkeyB = (public_keyA ** b) % p
	if commonkeyA == commonkeyB:
		return commonkeyA
	else:
		return None

def diffie_run(p, alpha, a, b):
	res = diffieHel(p, alpha, a, b)
	if res != None:
		print("The common key is ", res, sep="")
	else:
		print("something went wrong")

def main():
	p = 17
	alpha = 2
	a = 6
	b = 4
	res = diffieHel(p, alpha, a, b)
	if res != None:
		print("common key is ", res, sep="")
	else:
		print("something went wrong")

main()
