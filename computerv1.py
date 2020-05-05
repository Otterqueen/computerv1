import re
import sys
#fonction racine carée
def sqrt(nb):
	i = 0.00001
	while((i*i) < nb):
		i = i + 0.00001
	return float("%.5f" % i)

def resoudre(eq):
	a = eq[2]
	b = eq[1]
	c = eq[0]
	delta = (b*b) - (4*a*c)
	#print("delta = " + str(delta))
	if delta > 0 :
		print("Delta est positif.\nSoit 2 solutions telles que : ")
		x1 = (-b - sqrt(delta))/(2*a)
		x2 = (-b + sqrt(delta))/(2*a)
		print("x1 = " + str(x1) + "\nx2 = "+str(x2))
		sys.exit()
	if delta == 0:
		print("Delta est nul.\nSoit 1 solution telle que : ")
		x0 = -b / (2*a)
		print("x0 = " + str(x0))
		sys.exit()
	if delta < 0 :
		print("Delta est negatif.\nSoit 2 solutions complexes telles que : ")
		r = sqrt(-delta)
		z1 = str(-b) + " - i * " + str(r) + "/ " + str(2*a)
		z2 = str(-b) + " + i * " + str(r) + "/ " + str(2*a)
		print("z1 = " + z1 + "\nz2 = "+z2)
		sys.exit()

#parser l'entree
if len(sys.argv) == 2:
	string_test = sys.argv[1]
else:
	print("Missing argument\n[usage:] ./computerv1.py  \"expression d'un polynome sous la forme n * X^0 + m * X^1 + o * X^2 = p * X^0 + q * X^1 + r * X^2\" ")
	sys.exit()
#string_test = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
pattern = r"(\+ |\- |\= )*(\d+\.*\d*) \* \w\^(\d)"
result = re.findall(pattern, string_test, re.I | re.U)

#verifier les cas d'erreur 
add = 0
eq = [0,0,0,0,0,0]
for res in result:
	if res[0] == '= ':
		add = 3
	if res[2] == '0':
		eq[0 + add] = float(eq[0 + add]) + float(('-'  if res[0] == '- ' else '')+ res[1])
	elif res[2] == '1':
		eq[1 + add] = float(eq[1 + add]) + float(('-'  if res[0] == '- ' else '')+ res[1])
	elif res[2] == '2':
		eq[2 + add] = float(eq[2 + add]) + float(('-'  if res[0] == '- ' else '')+ res[1])
	else:
		print("Erreur : degré trop élevé")
		sys.exit()

#mettre sous forme simplifiee (=0)
eq[0] = eq[0] - eq[3]
eq[1] = eq[1] - eq[4]
eq[2] = eq[2] - eq[5]

#afficher forme simplifiee
a = (str(eq[2])+"x² + ") if eq[2] != 0 else ''
b = (str(eq[1])+"x + ") if eq[1] != 0 else ''
c = (str(eq[0])+" = 0") if eq[0] != 0 else ''
print(("Equation simplifiée  = "+ a + b + c) if a+b+c != '' else '')
#chercher le degré le plus elevé
if eq[2] != 0:
	deg = 2
	print ("Polynome du second degré")
	resoudre(eq)
elif eq[1] != 0:
	deg = 1
	print ("Polynome du premier degré")
	print("Solution : x = "+ str(-eq[0]/eq[1]))
	sys.exit()
elif int(eq[0]) != 0:
	print ("Erreur, équation impossible")
	sys.exit()
else:
	print("Good job you have the proof of  0 = 0")
	sys.exit()