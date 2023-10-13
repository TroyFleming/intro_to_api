import requests, json

poke_List = ['metapod','weedle','charizard','blastoise','venusaur','hitmonchan','hitmonlee', 'caterpie','beedrill', \
             'rattata','meowth','sandshrew','diglett','gastly','haunter','jigglypuff','ninetales','geodude','onix', \
             'golem', 'zubat', 'pidgeot', 'butterfree', 'pikachu', 'raichu','hypno','abra']

def whos_That_Pokemon():
    
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

    for pokeMon in poke_List:

        pokeMon_Url = f'https://pokeapi.co/api/v2/pokemon/{pokeMon}'
        poke_Response = requests.get(pokeMon_Url).json()

        pokeType = poke_Response['types'][0]['type']['name']

        if len(poke_Response['abilities']) == 3:
            pokeInfo = {
                'abilities':{poke_Response['abilities'][0]['ability']['name'],poke_Response['abilities'][1]['ability']['name'],poke_Response['abilities'][2]['ability']['name']},
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

        pokeData = {pokeMon:pokeInfo}

        poke_Type_Dict[pokeType].update(pokeData)

    print(poke_Type_Dict)

whos_That_Pokemon()