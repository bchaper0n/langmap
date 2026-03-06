"""
fetching and parsing country info taken from https://github.com/samayo/country-json/
"""
from git import Repo # pip install gitpython
import json
import os
from pathlib import Path
import shutil
import stat
import fix_countries_data as fix

update = False
repo_url = "https://github.com/samayo/country-json/"
repo_download_path = "country-json"
countries_filename = "countries.json"
data_path = "data"
api_data_path = "../db/load-sh/data"

country_property_info = [
    {   "name": "country",
        "input_name": "country",
        "path": "country-by-name.json",
        "func": fix.fix_countries_data},
    {   "name": "capital",
        "input_name": "city",
        "path": "country-by-capital-city.json",
        "func": fix.fix_capitals_data},
    {   "name": "abbreviation",
        "input_name": "abbreviation",
        "path": "country-by-abbreviation.json",
        "func": fix.fix_abbrvs_data},
    {   "name": "continent",
        "input_name": "continent",
        "path": "country-by-continent.json",
        "func": fix.fix_continents_data},
    {   "name": "flag",
        "input_name": "flag_base64",
        "path": "country-by-flag.json",
        "func": fix.fix_flags_data},
    {   "name": "languages",
        "input_name": "languages",
        "path": "country-by-languages.json",
        "func": fix.fix_languages_data}
]
#"coordinates": "country-by-geo-coordinates.json",

def main():

    if update:
        get_country_data()

    countries_json = []
    temp_info_json = []
    # for each country property, fetch json and save to combined json
    for i in range(len(country_property_info)):
        property = country_property_info[i]
        with open(os.path.join(data_path, property["path"]), encoding='utf-8') as f:
            if i == 0: # load country data first
                countries_json = json.load(f)
                countries_json = property["func"](countries_json) # fix data for countries
            else: # add data for country property
                temp_info_json = json.load(f)
                temp_info_json = property["func"](temp_info_json) # fix data for current property
            
                # search for each country's property
                for j in range(len(countries_json)):
                    for k in range(len(temp_info_json)):
                        if countries_json[j]["country"] == temp_info_json[k]["country"]: # if prop for country found
                            countries_json[j].update({property["name"]: temp_info_json[k][property["input_name"]]}) # save to json
                            temp_info_json.pop(k) # delete from temp
                            break
                    
                    if property["name"] not in countries_json[j]: # if prop not found for current country, fail
                        print(f"\t{property["name"]} from {countries_json[j]["country"]} missing")
                        break

    # check if api has directory for json
    if not Path(api_data_path).is_dir():
        os.mkdir(api_data_path)

    # save json to api directory
    with open(f"{api_data_path}/{countries_filename}", 'w', encoding='utf-8') as f:
        json.dump(countries_json, f, ensure_ascii=False, indent=4)
        

# get country data from repo and delete unneeded files
def get_country_data():

    # if directory exists, clone github repo
    if not Path(f"./{repo_download_path}").is_dir():
        Repo.clone_from(repo_url, f"./{repo_download_path}")

    #keep req files
    if not Path(data_path).is_dir():
        os.mkdir(data_path)

    # save desired country properties
    for filename in country_property_info:
        shutil.copyfile(f"./{repo_download_path}/src/{filename}", f"./{data_path}/{filename}")

    # delete everything else from cloned repo
    if Path(f"./{repo_download_path}").is_dir():
        for root, dirs, files in os.walk(repo_download_path):  
            for dir in dirs:
                os.chmod(os.path.join(root, dir), stat.S_IRWXU)
            for file in files:
                os.chmod(os.path.join(root, file), stat.S_IRWXU)
        shutil.rmtree(repo_download_path)

if __name__ == '__main__':
    main()
