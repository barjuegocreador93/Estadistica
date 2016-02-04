#Autor: Camilo Barbosa
#pedir la poblacion:
poblacion=input("Entre el numero de poblacion: ")

#encontrar las muestras en una poblacion
muestra=[]
i=0
while i<poblacion:
	txt="Entre la muesta "+str(i+1)+": "
	x=input(txt)
	muestra.append(x)
	i+=1

#media geometrica 1:

g=1
i=0
while i<poblacion:
	g *= pow(muestra[i],1/poblacion)
	i+=1

print "La media geometrica 1: ",g

#media geometrica 2:
mulmP=1
i=0
while i<poblacion:
	mulmP = mulmP * pow(muestra[i],poblacion)
	i+=1
g=pow(mulmP,1/poblacion)

print "La media geometrica 2: ",g


#media aritmetica 1:
mx = 0.0
i=0
while i<poblacion:
	mx += muestra[i]
	i+=1

mx = mx / poblacion 

print "La media aritmetica es 1: ", mx

#media aritmetica 2:
mx = 0.0
i=0
while i<poblacion:
	mx += muestra[i] * poblacion
	i+=1

mx = mx / poblacion 

print "La media aritmetica es 2: ", mx


# medica Cuadratica 1: 

sumc=0.0
i=0
while i<poblacion:
	sumc += pow(muestra[i],2)
	i+=1

mc=pow(sumc/poblacion,0.5)

print "La media cuadrada es 1: ", mc

# medica Cuadratica 2: 

sumc=0.0
i=0
while i<poblacion:
	sumc += pow(muestra[i],2) * poblacion
	i+=1

mc=pow(sumc/poblacion,0.5)

print "La media cuadrada es 2: ", mc


#mediana:
me=0.0
if(poblacion % 2==0):
	sumc=0.0
	i=0
	while i<poblacion:
		sumc += (muestra[i/2]) + (muestra[(i/2)+ 1]) 
		i+=1
	me=sumc/2
else:
	sumc=0.0
	i=0
	while i<poblacion:
		sumc += muestra[(i+1)/2]  
		i+=1
	me=sumc/2

print "la mediana es: ", mc

