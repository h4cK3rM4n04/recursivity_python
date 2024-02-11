#coding;utf-8
#https://www.youtube.com/watch?v=txyZbIVoOy4
#Lumière avec aimant
#comme si t'étais un mini Rubiks cube sexy...il a du mal à résoudre le mystère que t'es mais il s'amuse beaucoup à essayer

def count_down(n):
	print(n)
	if n > 0:
		count_down(n-1)
	else:
		return 0
count_down(3)

print("=========================================================")

def count_up(n):
	#Faire l'inverse de la première fonction
	raise NotImplementedError()

print("==========================INCOMPLET CODE=====================")
print("=========================================================")


#faire la somme d'un nombre n+n-1+n-2+n-3...
def somme(n):
	res = 0
	for x in range(n+1):#la dernière valeur ne rentre jamais de la vie
		res = res + x
	return res
print(somme(100))

print("================================")

def somme_recursi(n):
	if n > 0:
		return n + somme_recursi(n-1)
	else:
		return 0
print(somme_recursi(3))


print("=========================================================")


def compres_som_recursi(n):
	return n + somme_recursi(n-1) if n > 0 else 0
print(compres_som_recursi(100))

def longueur(ch):
	if not ch:
		return 0
	else:
		return 1+longueur(ch[1:])
print(longueur("Manoa"))

x = 5
if not x > 10:
	print("False")
else:
	print("True")



def compte(chaine, a):
	if chaine == "":
		return 0
	else:
		if chaine[0] == a:
			return 1 + compte(chaine[1:], a)
		else:
			return compte(chaine[1:], a)

def next_ligne(L):
    t = [1]
    for x in range(len(L)-1):
        t.append(L[x] + L[x+1])
    t.append(1)
    return t

def pascal_it(n):
    ligne = [1]
    for x in range(1, n+1):
        ligne = next_ligne(ligne)
        print(ligne)
pascal_it(21)



#  LINK:	https://www.bouticoupe.fr/couteau-papillon-albainox-02211lame-97-cm-c2x39270985 == balisong
#12,84 = 62951,55

def tri_bulles(liste = [1,65,0,78,9,3,1,2,56,4,5,89,65,478,23]):
	for y in range(len(liste)-1):
		for x in range(len(liste)-1):
			if liste[x] > liste[x + 1]:
				b = liste[x]
				liste[x] = liste[x + 1]
				liste[x + 1] = b
	return liste
print(tri_bulles())