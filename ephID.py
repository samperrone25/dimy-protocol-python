# Code for task 1
from ecdsa import SigningKey, SECP128r1
from ecdsa.util import randrange
# This is an easy-to-use implementation of ECC 

# Code sample from document
# which generates a 16 ephID
# using the curve as the paper discribed
def gen_ephID():
	curve = SECP128r1
	secexp = randrange(curve.order)
	sk = SigningKey.from_secret_exponent(secexp, curve)
	ephid = sk.to_string()

	return secexp, ephid

if __name__ == "__main__":
    result = gen_ephID()
    print("\n element 0: " + str(result[0]) + "\n")
    print("\n element 1: " + str(result[1]) + "\n")