def split_string(string: str, characters: str = '') -> list[str]:
    list(string)
    new_string = []
    if characters in string:
        for i in range(len(string)):
            if string[i] in characters:
                new_string = string[:i] #TODO: enable multiple words + 
                                        #add new_string[i] in some way
    else:
        print(f"no {characters} in {string}")
    print(new_string)

#print(string.split("o")) desired output:['cia', ' c', 'me va?']

split_string("ciao", "o")
