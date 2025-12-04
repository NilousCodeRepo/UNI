################################################################################
# Funzioni
################################################################################
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.
def cubic_root(n):
    pass

# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.
def check_date(d, m, y):
    pass


#Test funzioni
print_test(cubic_root, 8)
print_test(cubic_root, -1)
print_test(check_date, -1, 12, 2011)
print_test(check_date, 1, 14, 2011)
print_test(check_date, 1, 12, -1)
print_test(check_date, 31, 4, 2011)
print_test(check_date, 30, 4, 2011)

################################################################################
# Stringhe
################################################################################


# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    pass


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    pass


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    pass


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    pass


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    pass


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrf gzggf', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    pass


# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    pass


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    pass


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    pass


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e restituisce una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    pass
