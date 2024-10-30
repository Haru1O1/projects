def brute_DLP(alpha, beta, p):
	table = {}
	alpha_pow = 1
	for x in range(p - 1):
		table[alpha_pow] = x
		alpha_pow = (alpha_pow * alpha) % p
	alpha_inv = pow(alpha, p - 2, p)

	beta_x_alpha_pow = beta
	for x in range(p - 1):
		if beta_x_alpha_pow in table:
			return (x * (p - 1) + table[beta_x_alpha_pow]) % (p - 1)
		beta_x_alpha_pow = (beta_x_alpha_pow * alpha_inv) % p
	return None

print(brute_DLP(41, 12959645, 100000081))
