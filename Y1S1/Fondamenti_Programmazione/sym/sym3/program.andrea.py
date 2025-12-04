#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la simulazione e' necessario ottenere il punteggio 18 o più.
(15 per studenti con DSA)

Il voto finale e' la somma dei punteggi dei problemi risolti.
"""
nome       = "A"
cognome    = "S"
matricola  = "42"

################################################################################
################################################################################
################################################################################
# ---------------------------- DEBUG SUGGESTIONS ----------------------------- #
# To run only some of the tests, you can comment the entries with which the
# 'tests' list is assigned at the end of grade.py
################################################################################


#%% ---------------------------- FUNC 1 ---------------------------- #

'''
Func 1: 8 punti
Si definisca la funzione func1(png_input) che riceve come argomento:
- png_input:  il percorso di una inmagine PNG

Il file png_input contiene una immagine a sfondo nero, contenente stelline,
ovvero crocette di dimensione 3x3 pixel in diagonale di colori qualsiasi.
Esempio:
.x.x....
..xo.o..
.x.xo...
...o.o..
........

Nell'esempio sono presenti una stellina di colore 'x' ed una di colore 'o'.

Assumete che due qualsiasi stelline dello stesso colore siano separate da almeno un pixel
e quindi non si toccano nè in orizzontale/verticale nè in diagonale.
Assumete che i pixel della immagine siano solo stelline o sfondo nero.

La funzione deve contare il numero di stelline presenti, per ciascun colore
e tornare un dizionario che ha come chiavi i colori delle stelline presenti nell'immagine
e come valori il numero di stelline di quel colore.

Esempio:
Se l'immagine è 'func1/in_2.png' il risultato sarà il dizionario
{(150, 200, 150): 3, (200, 150, 125): 4, (125, 175, 200): 2,
(125, 100, 125): 3, (125, 175, 125): 4, (200, 100, 150): 2}

'''

import images

def func1(png_input):
    pass
    img = images.load(png_input)
    W,H = len(img[0]), len(img)
    result = {}
    for y,row in enumerate(img):
        for x,px in enumerate(row):
            if px != (0,0,0):
                if 0<y<H-1 and 0<x<W-1:
                    if px == img[y-1][x-1] == img[y+1][x+1] == img[y-1][x+1] == img[y+1][x-1]:
                        if px not in result:
                            result[px] = 0
                        result[px] += 1
    return result

# %% ----------------------------------- FUNC2 ------------------------- #
'''
Func 2: 10 punti
Si definisca la funzione func2(txt_input, width, height, png_output) che riceve come argomenti

- txt_input:  il percorso di un file che contiene un elenco di figure da disegnare
- width:      larghezza in pixel dell'immagine da creare
- height:     altezza in pixel dell'immagine da creare
- png_output: il percorso di una immagine PNG che dovete creare, contenente le figure

La funzione deve creare una immagine a sfondo nero e disegnarci sopra
tutte le figure indicate nel file 'txt_input', nell'ordine in cui
appaiono nel file.

Il file txt_file contiene, una per riga, separate da spazi:
- una parola che indica il tipo di figura da disegnare
- le tre componenti R G B del colore da usare
- le coordinate e gli altri parametri necessari a definire la figura

Possono essre presenti 2 tipi di figura:
- diagonale discendente di un quadrato (in direzione -45°)
    diagonalDOWN R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in BASSO a destra, ed è lunga L pixel
- diagonale ascendente di un quadrato (in direzione +45°)
    diagonalUP R G B x y L
    La diagonale inizia nel punto (x,y), si dirige in ALTO a destra, ed è lunga L pixel

Quindi deve salvare l'immagine ottenuta nel file 'png_output' usando la funzione images.save.
Inoltre deve ritornare il numero di diagonali disegnate dei due tipi
come tupla dei due valori (DIAGUP,DIAGDOWN)

NOTA: va gestito correttamente lo sbordare delle figure dalla
immagine, infatti sono ammesse anche coordinate negative, e dimensioni
o parametro L tali da far sbordare la figura dalla immagine

Esempio: se il file func2/in_1.txt contiene le 3 righe
diagonalDOWN 0 255 0 -30 -40 110
diagonalUP 255 0 0 20 100 200
diagonalUP 0 0 255 10 120 50

l'esecuzione della funzione func2('func2/in_1.txt', 50, 100, 'func2/your_image_1.png')
produrrà una figura uguale al file 'func2/expected_1.png'
e tornerà la coppia (2, 1)
'''

def func2(txt_input, width, height, png_output):
    pass
    DOWN = UP = 0
    img = [[(0, 0, 0)] * width for _ in range(height)]
    with open(txt_input) as FIN:
        for linea in FIN:
            F, *valori = linea.split()
            R, G, B, x, y, L = map(int, valori)
            if F == 'diagonalDOWN':
                dy = 1
                DOWN += 1
            else:
                dy = -1
                UP += 1
            for i in range(L):
                X, Y = x + i, y + (i * dy)
                if 0 <= X < width and 0 <= Y < height:
                    img[Y][X] = R, G, B
    images.save(img, png_output)
    return UP, DOWN

# print(func2('func2/in_1.txt', 50, 100, 'func2/out_1.png'))

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 points
Si scriva una funzione func3(imagefile, output_imagefile, color) che prende
in ingresso due stringhe che rappresentano due nomi di file di immagini PNG.
L'immagine nel file 'imagefile' contiene esclusivamente segmenti orizzontali
bianchi su uno sfondo nero. Ogni riga ha al più un segmento bianco.
La funzione deve creare una nuova immagine in cui sono presenti gli stessi
segmenti dell'immagine in ingresso e modificare il colore dei segmenti con
lunghezza massima utilizzando il colore color preso in ingresso.

L'immagine così ottuenuta deve essere salvata in formato PNG nel file con
percorso output_imagefile.

La funzione ritorna il numero di segmenti colorati nell'immagine in output.
"""
import images
def func3(imagefile, output_imagefile, color):
    # Inserisci qui il tuo codice
    white = 255,255,255
    black = 0,0,0
    img = images.load(imagefile)
    segmenti = {}
    for y,riga in enumerate(img):
        minx=maxx=None
        for x,c in enumerate(riga):
            if c == white:
                if minx is None:
                    minx = x
                if maxx is None:
                    maxx = x
                elif x > maxx:
                    maxx = x
        if minx is not None:
            segmenti[y] = minx, maxx
    lunghezze = [ maxx-minx for minx,maxx in segmenti.values() ]
    maxlen    = max(lunghezze)
    N = 0
    for y,[minx,maxx] in segmenti.items():
        if maxx-minx == maxlen:
            N += 1
            for x in range(minx,maxx+1):
                img[y][x] = color
    images.save(img,output_imagefile)
    return N

# print(func3('func3/image01.png', 'func3/your_image01.png', (255,0,0)))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 6 points
Si definisca la funzione func4(L, A, sfondo, file_rettangoli, imagefile_out) 
che riceve come argomenti:
    - la larghezza L, altezza A e colore di sfondo di una immagine da creare
    - il path di un file che contiene, su ciascuna riga, i parametri di un rettangolo
    - il path imagefile_out in cui salvere l'immagine ottenuta
Il file dei rettangoli contiene su ciascuna riga 7 valori
    - x, y, larghezza, altezza, R, G, B
    dove x, y sono le coordinate dell'angolo in alto a sinistra del rettangolo.    
    NOTA: i rettangoli potrebbero sbordare dall'immagine
La funzione deve:
    - disegnare nell'ordine i rettangoli pieni per la parte contenuta nella immagine
    - sommare il numero di pixel di ciascun rettangolo che sono stati disegnati
        nell'immagine (anche se successivamente sovrascritti, ed escludendo quelli 
        esterni all'immagine)
    - restituire tale somma
"""
import images
def func4(L : int, A : int, sfondo : tuple[int,int,int], file_rettangoli : str, imagefile_out : str) -> int:
    pass
    # Inserisci qui il tuo codice
    area = 0
    img = [ [sfondo for x in range(L)] for y in range(A)]
    with open(file_rettangoli, encoding='utf8') as FIN:
        for line in FIN:
            x, y, w, h, R, G, B = list(map(int,line.split()))
            area += draw_rectangle(x,y,w,h,(R,G,B),img,L,A)
    images.save(img, imagefile_out)
    return area

def bound(X,m,M):
    return max(min(X,M),m)

def draw_rectangle1(x,y,w,h,c,img,L,A):
    minx = bound(x,  0,L-1)
    miny = bound(y,  0,A-1)
    maxx = bound(x+w,0,L-1)
    maxy = bound(y+h,0,A-1)
    area = (maxx-minx+1)*(maxy-miny+1)
    N = 0
    for X in range(minx, maxx+1):
        for Y in range(miny,maxy+1):
            img[Y][X] = c
            N += 1
    assert area==N
    return area

def draw_rectangle(x,y,w,h,c,img,L,A):
    N = 0
    for X in range(x, x+w):
        if 0 <= X < L:
            for Y in range(y,y+h):
                if 0 <= Y < A:
                    img[Y][X] = c
                    N += 1
    return N

    
# print(func4(50,50,(0,255,0),'func4/rect_01.txt', 'func4/out_01.png'))    # 67
def genera_rect(N,ID,W,H):
    from random import randint
    with open(f'func4/rect_0{ID}.txt','w') as FOUT:
        for _ in range(N):
            x = randint(-50, W)
            y = randint(-50, H)
            w = randint(1, W//4)
            h = randint(1, H//4)
            R = randint(0,255)
            G = randint(0,255)
            B = randint(0,255)
            print(x,y,w,h,R,G,B,file=FOUT)
#genera_rect(55,4,500,200)
