from functools import reduce

#Ejercicio N° 1 - Calculadora de descuentos

def calculadorDescuentos(precio:float, descuento:float)-> float:
	"""
	Args:
			precio (float): recibe precio original del producto/servicio _
			descuento (float): recibe en porcentaje (sin el simbolo) 
   			del descuento a aplicar

	Returns:
			float:retorna el precio final del producto,
   		una vez aplicado el descuento
	"""
	
	precio_final=0.00;
	desc = descuento/100;
	precio_final= precio - precio*desc;
 
	return  precio_final;

precio_final=calculadorDescuentos(500.00, 1);
# print(f'El precio final del producto es de {precio_final} pesos')


#Ejercicio N° 2 - Conversion de temperaturas

def conversorTemperatura(temp: float, unidadOrigen: str, unidadDestino: str) -> float:
	"""Conversor de unidades Celsius a Fahrenheit o viceversa

	Args:
			temp (float): Recibe un valor que representa la temperatura
			unidadOrigen (str): Recibe un Caracter que representa la unidad de origen
			unidadDestino (str): Recibe un Caracter que representa la unidad de destino

	Raises:
			ValueError: lanza una validacion personalizada que asegura recibir los valores  

	Returns:
			float: retorna un valor que surge de aplicar una formula de conversion
	"""
	result=0;
	# Validar las unidades de origen y destino
	if unidadOrigen not in ['C', 'F'] or unidadDestino not in ['C', 'F']:
			raise ValueError("Las unidades deben ser 'C' para Celsius o 'F' para Fahrenheit.")

	# Conversión de Celsius a Fahrenheit
	if unidadOrigen == 'C' and unidadDestino == 'F':
				result=	(temp * 9/5) + 32
				return F'RESULTADO :{result}-{unidadDestino}°';

	# Conversión de Fahrenheit a Celsius
	elif unidadOrigen == 'F' and unidadDestino == 'C':
				result=	(temp - 32) * 5/9
				return F'RESULTADO :{result}-{unidadDestino}°';

	# Si las unidades de origen y destino son las mismas, no se necesita conversión
	return F'RESULTADO :{temp}-{unidadDestino}°';


primerUso = conversorTemperatura(20, 'F', 'C')

# print(primerUso)

#Ejercicio N° 3 - Verificacion de palindromos

def esPalindromo(cadena:str)->bool:
	"""determina si una cadena es palindromo

	Args:
			cadena (str): recibe una cadena de caracteres a evaluar

	Returns:
			bool: retorna un booleano como respuesta a la consulta de 
   si una cadena es o no palindromo
	"""

	palabra= cadena.replace(" ", "").lower();
	nuevaPalabra=palabra[::-1].replace(" ","").lower();
	
	if palabra==nuevaPalabra:
			return True;
	else:
			return False;
 
# prueba=esPalindromo('Neuquen');

# print(prueba)



#Ejercicio N° 4 - Analisis de texto.-

def contarCaracteres(cadena:str)->dict:
		"""funcion contadora de caracteres

		Args:
				cadena (str):recibe una cadena de caracteres

		Returns:
				dict: la funcion retorna un diccionario  

		"""
		cantidadCaracteres=0;
		cadenaModificada = cadena.replace(" ","").lower();
		for i in cadenaModificada:
			cantidadCaracteres+=1;
		return {"cantidad de caracteres":cantidadCaracteres};

def contarPalabras(cadena:str)->dict:
	"""funcion contadora de palabras

	Args:
			cadena (str):recibe una cadena de caracteres

	Returns:
			dict: la funcion retorna un diccionario  

	"""
	cadena_nueva=cadena.split();
	cantidadPalabras=0;
	for p in cadena_nueva:
		cantidadPalabras+=1;
	return {"cantidad de palabras":cantidadPalabras};
    
    
    
def analisisTexto(cadena:str)->dict:
		"""la funcion arma un diccionario que tiene como elementos
	la cantidad de caracteres de una cadena y la cantidad de 
	palabras de la misma

		Args:
				cadena (str): recibe una cadena de caracteres

		Returns:
				dict: la funcion retorna un diccionario cuyos elmentos 
    son la cantidad de palabras de la cadena y la cantidad de caracteres
    de la misma.
		"""
		elemento1=contarCaracteres(cadena);
		elemento2=contarPalabras(cadena);

		return dict(**elemento1,**elemento2)    

# cadena1="hola como estas"
# prueba = analisisTexto(cadena1)

# print(prueba)
  
#Ejercicio N° 5 - Generador de numeros primos.- 
# 
def es_primo(n:int)->bool:
	"""Verificacion de si un numero es primo

	Args:
			n (int): recibe un numero entero a evaluar

	Returns:
			bool: la funcion retorna un booleano como respuesta 
   a la verificacion de si un numero es primo
	"""
	if n <= 1:
			return False
	if n == 2:
			return True
	if n % 2 == 0:
			return False
	for i in range(3, int(n**0.5) + 1,2):
			if n % i == 0:
					return False
	return True



def generadorNumerosPrimos(numero:int)->list:
	"""Funcion generador de numeros primos
 
 Un número primo se define como un número natural mayor que 1 
 que tiene exactamente dos divisores: 1 y el propio número
	Args:
			numero (int): la funcion recibe un numero entero positivo

	Returns:
			list: la funcion retorna una lista que contiene los numeros primos 
   desde 2 hasta el numero que recibe como parametro
	"""
	primos=[];
	i=2;
	while i < numero: 
			if es_primo(i):
				primos.append(i);
				# print(primos)					
			i+=1;	
	return primos

# numero= generadorNumerosPrimos(30);
# print(numero)

  
#Ejercicio N° 6 - Gestion de inventarios.- 

productos={'p1':0,'p2':0,'p3':0}


def gestionInventario(inventario:dict, producto:str, cantidad:int)->dict:
	"""Funcion para actualizar el inventario 

	Args:
			inventario (dict): recibe un diccionario con los productos
			producto (str): recibe el producto a inventariar
			cantidad (int): recibe la cantidad del producto a agregar/disminuir 

	Returns:
			dict: retorna el inventario actualizado
   
  
		actualizarInventario = gestionInventario(productos,'p2',100);
		actualizarInventario1 = gestionInventario(productos,'p1',1000);
		actualizarInventario2 = gestionInventario(productos,'p3',10);
		print(productos)
	"""
	
	if producto in inventario:
		inventario[producto]+=cantidad;
	else:
			inventario[producto]=cantidad;
   
	if inventario[producto]<0:
			inventario[producto]=0;	
	return inventario;
  
  
#Ejercicio N° 7 - Validacion de contraseñas.-

def validarContrasenia(lista:list)->list:
	"""funcion que recibe una lista de cadenas y retorna una lista 
 con sublistas que contienen caracteres

	Args:
			lista (list): recibe una lista de cadenas de caracteres

	Returns:
			list: la funcion retorna una lista de listas de caracteres
	"""
 
	nuevaLista= list(map(list,lista))
	return nuevaLista;
	
# print(validarContrasenia(['hola','como','estas']))


#Ejercicio N° 8 - Calculo de estadisticas.-

def calcularModa(lista):
	contador={};
	for num in lista:
		if num in contador:
			contador[num]+=1;
		else:
			contador[num]=1;
	if contador[num]==1:
		moda=0
	else:       
		moda= max(contador,key=contador.get);  
	return moda;     
        
def calcularMediana(lista):
		lista_ordenada = sorted(lista)
		n = len(lista_ordenada)
		if n % 2 == 1:  
				mediana = lista_ordenada[n // 2]
		else:  
				mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

		return mediana

def calculoEstadisticas(lista:list)->dict:
	"""Funcion que retorna un conjunto de estadisticas 
 dada una lista

	Args:
			lista (list): recibe una lista de numeros

	Returns:
			dict: retorna un conjunto de estadisticas 
	"""
	suma= reduce(lambda x,y:x+y, lista);
	media=suma//len(lista);
	mediana = calcularMediana(lista);
	moda=calcularModa(lista);
	estadistica={'media':media,'mediana':mediana,'moda':moda}
	return estadistica;




estadisticas= calculoEstadisticas([2,5,5,3,8,5,8]);
estadisticas1= calculoEstadisticas([1,2,3,4,5,6,7,7]);

print(estadisticas1)