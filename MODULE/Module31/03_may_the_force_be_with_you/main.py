import requests
import json

dict_info = {}

my_req = requests.get('https://swapi.dev/api/starships/10/')  # общий запрос с API
data = json.loads(my_req.text)


for key, value in data.items():
    if key == "name":
        dict_info[key] = value
    elif key == "starship_class":
        dict_info[key] = value
    elif key == "max_atmosphering_speed":
        dict_info[key] = value

    elif key == "pilots":
        all_pilot = []
        for p_url in value:
            pilot_req = requests.get(p_url)  # запрос api каждого пилота
            data_pilot = json.loads(pilot_req.text)
            i_pilot = {}

            for p_key, p_value in data_pilot.items():
                if p_key == 'name':
                    i_pilot[p_key] = p_value
                elif p_key == 'height':
                    i_pilot[p_key] = p_value
                elif p_key == 'mass':
                    i_pilot[p_key] = p_value

                elif p_key == 'homeworld':
                    homeworld_req = requests.get(p_value)  # запрос api планеты
                    data_home = json.loads(homeworld_req.text)

                    for home_key, home_value in data_home.items():
                        if home_key == 'name':
                            i_pilot[p_key] = home_value
                        elif home_key == 'url':
                            i_pilot['homeworld_url'] = home_value

            all_pilot.append(i_pilot)

        dict_info[key] = all_pilot

with open('falcon_file.json', 'w') as file:
    json.dump(dict_info, file, indent=4)

with open('falcon_file.json', 'r') as file:
    data = json.load(file)
    print(data)
