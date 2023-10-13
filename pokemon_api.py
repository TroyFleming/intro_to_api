import requests, json

poke_List = ['metapod','weedle','charizard','blastoise','venusaur','hitmonchan','hitmonlee', 'caterpie','beedrill', \
             'rattata','meowth','sandshrew','diglett','gastly','haunter','jigglypuff','ninetales','geodude','onix', \
             'golem', 'zubat', 'pidgeot', 'butterfree', 'pikachu', 'raichu','hypno','abra']

def whos_That_Pokemon():

    '''
    This function collects the type, name, abilities, and weight of each Pokemen within poke_List,
    then creates a master dictionary of all the collected data. Each Pokemon has its own dictionary
    which houses abilities and weight.

    Pokemons are classified by type.
    '''
    
    # Dictionary of the types of Pokemon available for documentation
    poke_Type_Dict = {
                'normal':{},
                'fighting':{},
                'flying':{},
                'poison':{},
                'ground':{},
                'rock':{},
                'bug':{},
                'ghost':{},
                'steel':{},
                'fire':{},
                'water':{},
                'grass':{},
                'electric':{},
                'psychic':{},
                'ice':{},
                'dragon':{},
                'dark':{},
                'fairy':{},
                }

    # For loop for each Pokemon entered into poke_List to collect data
    for pokeMon in poke_List:

        # Call pokeapi
        pokeMon_Url = f'https://pokeapi.co/api/v2/pokemon/{pokeMon}'
        poke_Response = requests.get(pokeMon_Url).json()

        # Assigns Pokemon's type to variable 'pokeType'
        pokeType = poke_Response['types'][0]['type']['name']

        # Depending on how many abilities Pokemon has, will add the appropriate Key:Value pairs into
        # said Pokemon's personal dictionary
        if len(poke_Response['abilities']) == 3:
            pokeInfo = {
                'abilities':{poke_Response['abilities'][0]['ability']['name'],poke_Response['abilities'][1]['ability']['name'], \
                             poke_Response['abilities'][2]['ability']['name']},
                'weight':poke_Response['weight'],
            }
        elif len(poke_Response['abilities']) == 2:
            pokeInfo = {
                'abilities':{poke_Response['abilities'][0]['ability']['name'],poke_Response['abilities'][1]['ability']['name']},
                'weight':poke_Response['weight'],
            }
        else:
            pokeInfo = {
                'abilities':{poke_Response['abilities'][0]['ability']['name']},
                'weight':poke_Response['weight'],
            }

        # Dictionary for each Pokemon and its collected attributes is created
        pokeData = {pokeMon:pokeInfo}

        # Created dictionary for each Pokeman is added to the master Type dictionary
        poke_Type_Dict[pokeType].update(pokeData)

    print(poke_Type_Dict)

whos_That_Pokemon()