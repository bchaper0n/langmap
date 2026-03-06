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
        "path": "country-by-name.json"},
    {   "name": "capital",
        "input_name": "city",
        "path": "country-by-capital-city.json"},
    {   "name": "abbreviation",
        "input_name": "abbreviation",
        "path": "country-by-abbreviation.json"},
    {   "name": "continent",
        "input_name": "continent",
        "path": "country-by-continent.json"},
    {   "name": "flag",
        "input_name": "flag_base64",
        "path": "country-by-flag.json"},
    {   "name": "languages",
        "input_name": "languages",
        "path": "country-by-languages.json"}
]
#"coordinates": "country-by-geo-coordinates.json",

country_data_funcs = [fix.fix_countries_data, fix.fix_capitals_data, fix.fix_abbrvs_data, fix.fix_continents_data, fix.fix_flags_data, fix.fix_languages_data]

def main():

    if update:
        get_country_data()

    countries_json = []
    temp_info_json = []
    for i in range(len(country_property_info)):
        property = country_property_info[i]
        with open(os.path.join(data_path, property["path"]), encoding='utf-8') as f:
            if i == 0: # load country data first
                countries_json = json.load(f)
                countries_json = country_data_funcs[i](countries_json) # fix data for countries
            else:
                temp_info_json = json.load(f)
                temp_info_json = country_data_funcs[i](temp_info_json) # fix data for current property
            
                # add data for country property
                for j in range(len(countries_json)):
                    for k in range(len(temp_info_json)):
                        if countries_json[j]["country"] == temp_info_json[k]["country"]:
                            countries_json[j].update({property["name"]: temp_info_json[k][property["input_name"]]})
                            temp_info_json.pop(k)
                            break
                    
                    if property["name"] not in countries_json[j]:
                        print(f"\t{property["name"]} from {countries_json[j]["country"]} missing")
                        break

    # copy json to api directory
    if not Path(api_data_path).is_dir():
        os.mkdir(api_data_path)

    with open(f"{api_data_path}/{countries_filename}", 'w', encoding='utf-8') as f:
        json.dump(countries_json, f, ensure_ascii=False, indent=4)
        

# get country data from repo and delete unneeded files
def get_country_data():

    if not Path(f"./{repo_download_path}").is_dir():
        Repo.clone_from(repo_url, f"./{repo_download_path}")

    #keep req files
    if not Path(data_path).is_dir():
        os.mkdir(data_path)

    for filename in country_property_info:
        shutil.copyfile(f"./{repo_download_path}/src/{filename}", f"./{data_path}/{filename}")

    # delete repo
    if Path(f"./{repo_download_path}").is_dir():
        for root, dirs, files in os.walk(repo_download_path):  
            for dir in dirs:
                os.chmod(os.path.join(root, dir), stat.S_IRWXU)
            for file in files:
                os.chmod(os.path.join(root, file), stat.S_IRWXU)
        shutil.rmtree(repo_download_path)

if __name__ == '__main__':
    main()
