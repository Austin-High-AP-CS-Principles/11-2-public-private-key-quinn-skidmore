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

#print("All primes less than 1,000:\n"+str(primes_less_than(1000)))


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
	for e in range(t):
		if(is_coprime(e,t) and is_coprime(e,n)):
			e_value = e
	for d in range(400000, 100000000):
		if((e_value * d) % t) == 1:
			return [e_value,d]
		
def encrypt(n, e, letter):
	v = ord(letter)
	enc = (v**e) % n
	return enc

def encrypt_message(n, e, message):
	enc_message = []
	for letter in message:
		enc_message.append(encrypt(n, e ,letter))
	return enc_message
def decrypt(n, d, enc):
	dec = (enc**d)%n
	return chr(dec)

def decrypt_message(n,d,list):
	dec_message = ""
	for letter in list:
		dec_message += decrypt(n,d,letter)
	return dec_message
	
p = 823
q = 251
n = calculate_N(p,q)
ed = pick_e_d(p,q)
decryped_message = "Quinn Quake - 'Unleashing seismic power, reshaping the earth.'"
encrypted_message = [17852, 75920, 114107, 118310, 118310, 174296, 17852, 75920, 44722, 173753, 36815, 174296, 197392, 174296, 21187, 116653, 118310, 13389, 36815, 44722, 193999, 85410, 114107, 118310, 174484, 174296, 193999, 36815, 114107, 193999, 11371, 114107, 108503, 174296, 197351, 102356, 112834, 36815, 164896, 89202, 174296, 164896, 36815, 193999, 85410, 44722, 197351, 114107, 118310, 174484, 174296, 197669, 85410, 36815, 174296, 36815, 44722, 164896, 197669, 85410, 175138, 21187]

print(encrypt_message(n,ed[0],decryped_message))
print(decrypt_message(n,ed[1],encrypted_message))