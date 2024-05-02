# These two functions will help determine if two numbers are coprimes #
# Returns the greatest common denominator for two numbers
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p
# Determines if two numbers are coprime. Returns True or False
def is_coprime(x, y):
    return gcd(x, y) == 1

# Returns a list of all the prime numbers from 2 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes

print("All primes less than 1,000:\n"+str(primes_less_than(1000)))

p = 823
q = 251
def calculate_N(p,q):
	return p*q
def calculate_T(p,q):
	return (p-1)*(q-1)

def pick_e_d(p,q):
	t = calculate_T(p,q)
	n = calculate_N(p,q)
	e=0
	d=0
	e_value = 0
	print(t)
	for e in range(t):
		if(is_coprime(e,t) and is_coprime(e,n)):
			e_value = e
	print(str(e_value))
	for d in range(e_value):
		if((e_value * d) % t) == 1:
			print("d found")
			return [e_value,d]
def encrypt(n, e, letter):
	pass

def encrypt_message(n, e, message):
	pass
def decrypt(n, d, enc):
	pass

def decrypt_message(n,d,list):
	pass
print(str(pick_e_d(p,q)))