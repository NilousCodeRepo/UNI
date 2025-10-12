# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> list[str]:
    list(string)
    for (index,char) in enumerate(string):
        print(string[index])
        if char == characters:
            print(string)

split_string("ciao", "o")
