def split_string(string: str, characters: str = '') -> list[str]:
    list(string)

    new_string = []
    nuovo_inizio = 0

    if characters in string:
        for i in range(len(string)):
            if string[i] == characters:
                new_string.append(string[nuovo_inizio:i])
                nuovo_inizio = i+1'''arrivo a cia e mi fermo, quindi ricomincio da " s" vedo la o e mi fermo e così via'''
    else:
        print(f"no {characters} in {string}")

    return new_string

print(split_string("ciao sono", "o"))
