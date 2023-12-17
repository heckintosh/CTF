# i can send you the modified script that finds the LSB of dp, all you have to do is dp = dp*2**512+LSB, and then i will send you the script that calculates Phi and d


"""
This code finds unknown :SBs of dp, dq
when MSBs of dp & dq are known using our idea. It will reproduce Table 2 and Table 3 of our paper.

"""

m_1 = 4 #Parameter for 1st Lattice
m_2 = 9 #Parameter for 2nd Lattice
t_2 = 5 #Parameter for 2nd Lattice


# n is the size of primes, alpha is the size of e. dSize is bit size of dp & dq. Number of unknown bits of dp & dq is Unknown_LSB.

n = 1024
dSize = 1024
alpha = 227
Unknown_LSB = 512

#TWO_POWER is the left shift of 2. This value corresponds  to the knowledge of LSBs
TWO_POWER = 2^(dSize - Unknown_LSB)



l = 42502139446458622306081586167054806136995197007043648854665402570827
k = 62804256897977191309864388517988900324056730772228494118350161761418
dp = 54985370501257484461170850934100119105983084123923951902062416502028481080054200885835466435491679692553388732973503386191838349138543898963367742883636104109005115065576783550495631556396431820346746006312528871336758614747404840407265945738285591089547739839964805791459891062760386211539242209478622696951
N = 0x78fb80151a498704541b888b9ca21b9f159a45069b99b04befcb0e0403178dc243a66492771f057b28262332caecc673a2c68fd63e7c850dc534a74c705f865841c0b5af1e0791b8b5cc55ad3b04e25f20dedc15c36db46c328a61f3a10872d47d9426584f410fde4c8c2ebfaccc8d6a6bd1c067e5e8d8f107b56bf86ac06cd8a20661af832019de6e00ae6be24a946fe229476541b04b9a808375739681efd1888e44d41196e396af66f91f992383955f5faef0fc1fc7b5175135ab3ed62867a84843c49bdf83d0497b255e35432b332705cd09f01670815ce167aa35f7a454f8b26b6d6fd9a0006194ad2f8f33160c13c08c81fe8f74e13e84e9cdf6566d2f
e = 0x4b3393c9fe2e50e0c76920e1f34e0c86417f9a9ef8b5a3fa41b381355
c = 0x17f2b5a46e4122ff819807a9d92b6225c483cf93c9804381098ecd6b81f4670e94d8930001b760f1d26bc7aa7dda48c9e12809d20b33fdb4c4dd9190b105b7dab42e932b99aaff54023873381e7387f1b2b18b355d4476b664d44c40413d82a10635fe6e7322543943aed2dcfbe49764b8da70edeb88d6f63ee47f025be5f2f38319611ab74cd5db6f90f60870ecbb57a884f821d873db06aadf0e61ff74cc7d4c8fc1e527dba9b205220c6707f750822c675c530f8ad6956e41ab80911da49c3d6a7d27e93c44ba5968f2f47a9c5a2694c9d6da245ceffe9cab66b6043774f446b1b08ee4739d3cc716b87c8225a84d3c4ea2fdf68143d09f062c880a870554
MSB_dp = 0x59a2219560ee56e7c35f310a4d101061aa61e0ae4eae7605eb63784209ad488b4ed161e780811edd61bf593e2d385beccfd255b459382d8a9029943781b540e7




"""
From here 2nd step starts. After 1st step we know k. Now we try to find unknown
MSBs of dp

"""
R.<x>=QQ[]


f = (e*MSB_dp*TWO_POWER-1+k)
IN_k = (e).inverse_mod(k*N)

f = x+IN_k*f                # Make f monic by inverting the coefficient of x
X = 2^Unknown_LSB


#Generate shift polynomials and store these polynomials in F. Store monomials of shift polynomials in S
F = []
S = []
for i in range(m_2+1):
    h = f^i*k^(m_2-i)*N^(max(0,t_2-i))
    F.append(h)
    S.append(x^i)

 
"""
Form a matrix MAT. Entries of MAT are coming from the coefficient
vector from shift polynomials which are stored in F
"""

print('2nd lattice dimension', len(F))


MAT = Matrix(ZZ, len(F))

for i in range(len(F)):
  f = F[i]
  f = f(x*X)

  coeffs = (f.coefficients(sparse=False))
  for j in range(len(coeffs), len(F)):
      coeffs.append(0)
  coeffs = vector(coeffs)
  MAT[i] = coeffs

A = []
print(len(F))

from time import process_time
TIME_Start = process_time()
tt = cputime()
MAT = MAT.LLL()
TIME_Stop = process_time()
print('2nd LLL time', TIME_Stop-TIME_Start)

#After reduction identify polynomials which have root MSB_dp over integer and store them in a set A.


for j in range(len(F)):
  f = 0
  for i in range(len(S)):
    cij = MAT[j,i]
    cij = cij/S[i](X)
    cj = ZZ(cij)
    f = f + cj*S[i]
  if(j<=8 ):
    print(j)
    A.append(f)   
  else:
    break

I = ideal(A)
tt = cputime()
B = I.groebner_basis()

print('x - LSB', B)