"""You're given a string of words. 
You need to find the word "Nemo", and return a string like this: 
I found Nemo at [the order of the word you find nemo]!.

If you can't find Nemo, return I can't find Nemo :(."""

def FindNemo(prase):
    palabras = prase.split()
    posicion = -1
    if "Nemo" in palabras:      
        posicion = palabras.index("Nemo")
    if posicion != -1:
        print(f"I found Nemo at {posicion+1}")
    else:
        print("I can't find Nemo :(")
    
FindNemo("I am otra palabra extra Nemo")