import sys
import os

args = sys.argv[1:] # Almacena los argumentos de la terminal de forma conveniente.

# Comprueba si el usuario solicita una explicación del método de uso o si los argumentos están en un formato correcto.
for arg in args:
    if arg == "-h" or arg == "--h" or arg == "-help" or arg == "--help" or len(args)!=2 or not isinstance(arg, str):
        print("Método de uso: python criptfrec.py \"textoEncriptado.txt\" \"textoDesencriptado.txt\"")
        print("¡Se recomienda ejecutar el programa en pantalla completa!")
        exit()

'''
Si creemos que "A" es "E", pero ya hay "E" en el texto encriptado no podemos cambiar la "A" directamente.
Esto haría que luego no podamos cambiar las "E"s encriptadas sin cambiar las "A"s ya correctas.
Para solucionar esto cambiamos primero las "E"s encriptadas a un símbolo que no se va a utilizar más que de placeholder.
'''
placeholders = ["*","-","+","/","<",">","#","$","~","%","&","(",")","@"]
# El alfabeto español tiene 27 letras, por lo que con 14 placeholders cubrimos cada caso posible.

# Alfabeto ordenado según la frecuencia de uso de las letras.
frec_esp=[
    "E",    "A",    "O",    "L",    "S",    "N",    "D",
    "R",    "U",    "I",    "T",    "C",    "P",    "M",
    "Y",    "Q",    "B",    "H",    "G",    "F",    "V",
    "J",    "Ñ",    "Z",    "X",    "K",    "W"
]

# Determina si la letra dada por el usuario está dada en un formato correcto:
def valid(ch):
    if ch.isalpha() or ch in placeholders:return True
    else: return False

# Código que actualiza la terminal con el formato correcto:
def act_terminal(encr_txt,prog_txt,rec_txt,reg_c):
    os.system('clear')
    print('Asistente de criptoanálisis mediante estadística:\n')
    print(140*'-' + "\n")
    print('TEXTO ENCRIPTADO:\n')
    print(encr_txt)
    print(140*'-' + "\n")
    print('PROGRESO DE DESENCRIPTADO:\n')
    print(prog_txt)
    print(140*'-' + "\n")
    print('RECOMENDACIONES:\n')
    print(rec_txt)
    print(140*'-' + "\n")
    print("REGISTRO DE CAMBIOS:\n")
    print(reg_c+"\n")
    print(140*'-' + "\n")

# Generar las recomendaciones estadísticas:
def frec(txt):
    contador = {}

    for ch in txt.strip():
        if ch.isalpha():
            ch = ch.upper()
            if ch in contador: contador[ch]+=1
            else: contador[ch] = 1

    return sorted(contador, key=contador.get, reverse=True)        

# Leer el archivo con el texto encriptado:
with open(args[0],"r") as txt:
    encr = txt.read()
    decr = encr.upper()

# Genera las recomendaciones:
frec_txt = frec(encr)
rec=""
for ch in range(len(frec_txt)):
    rec += frec_txt[ch] + "->" + frec_esp[ch] + "\t"

#Ejecución principal:
reg_c = ""
while True:
    err = False
    act_terminal(encr,decr,rec,reg_c)

    acc=input("Inserte la letra a cambiar:\t\t(Inserte \"º\" para salir del programa)\n")
    if acc == 'º': break

    if valid(acc):
        c=acc.upper()
        acc2=input("Inserte la letra que sustituirá a " + "\"" + c + "\"" + ":\t(Inserte \"º\" para salir del programa)\n")
        if acc2 == 'º':break
        if valid(acc2):
            s=acc2.upper()
            if s in decr:
                i = 0
                for ph in placeholders:
                    if ph in decr:
                        i+=1
                    else:
                        decr = decr.replace(s,placeholders[i])
                        if reg_c != "": reg_c += ", " + s + "->" + placeholders[i]
                        else: reg_c += s + "->" + placeholders[i]
                        break
            decr = decr.replace(c,s)
            if reg_c != "": reg_c += ", " + c + "->" + s
            else: reg_c += c + "->" + s
        else:
            print("\"" + acc2.upper() + "\"" + " no es una letra.")
            err = True
    else:
        print("\"" + acc.upper() + "\"" + " no es una letra.")
        err = True

    if not err: act_terminal(encr,decr,rec,reg_c)

    decision=input("\n¿Continuar?[Y/N/R] (R = restart)")
    
    if decision.upper() =="Y":continue
    elif decision.upper() == "R":
        decr = encr
        reg_c = ""
    else: 
        with open(args[1],"w") as wr:
            wr.write(decr)
        break

