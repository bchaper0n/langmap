import os
flags_path = "flags"

def fix_countries_data(countries):
    # Ivory Coast wrong place
    ivory_coast = countries.pop(52)
    countries.insert(109, ivory_coast)

    # England wrong place
    england = countries.pop(63)
    countries.insert(64, england)

    # DRC wrong place and add 2nd "the"
    drc = countries.pop(49)
    drc["country"] = "The Democratic Republic of the Congo"
    countries.insert(218, drc)

    # Montserrat wrong place
    montserrat = countries.pop(145)
    countries.insert(146, montserrat)

    #remove Holy See and add Vatican City
    vc = countries.pop(95)
    vc["country"] = "Vatican City"
    countries.insert(237, vc)

    # Israel wrong order
    isr = countries.pop(104)
    countries.insert(105, isr)

    return countries

def fix_capitals_data(capitals):

    # DRC add 2nd "the"
    capitals[215]["country"] = "The Democratic Republic of the Congo"

    #remove Holy See and add Vatican City
    capitals[94]["country"] = "Vatican City"

    # missing British Indian Ocean Territory capital
    capitals[30]["city"] = "Diego Garcia"

    # missing South Georgia and the South Sandwich Islands capitald
    capitals[201]["city"] = "King Edward Point"

    capitals.append({"country": "Guernsey", "city": "Saint Peter Port"})
    capitals.append({"country": "Isle of Man", "city": "Douglas"})
    capitals.append({"country": "Jersey", "city": "St Helier"})
    capitals.append({"country": "Timor-Leste", "city": "Dili"})

    return capitals

def fix_abbrvs_data(abbrvs):
    # DRC add 2nd "the"
    abbrvs[216]["country"] = "The Democratic Republic of the Congo"

    # change Holy See to Vatican City
    abbrvs[94]["country"] = "Vatican City"

    # missing England, Scotland, and Wales abbrv
    abbrvs.append({"country": "England", "abbreviation": "GB"})
    abbrvs.append({"country": "Scotland", "abbreviation": "GB"})
    abbrvs.append({"country": "Wales", "abbreviation": "GB"})

    return abbrvs

def fix_continents_data(continents):

    # DRC wrong place and add 2nd "the"
    continents[215]["country"] = "The Democratic Republic of the Congo"

    # change Holy See to Vatican City
    continents[94]["country"] = "Vatican City"

    continents.append({"country": "Guernsey", "continent": "Europe"})
    continents.append({"country": "Isle of Man", "continent": "Europe"})
    continents.append({"country": "Jersey", "continent": "Europe"})
    continents.append({"country": "Timor-Leste", "continent": "Asia"})
    
    return continents

def fix_flags_data(flags):

    # DRC wrong place and add 2nd "the"
    flags[216]["country"] = "The Democratic Republic of the Congo"

    #remove Holy See and add Vatican City
    flags[95]["country"] = "Vatican City"

    # missing South Georgia and the South Sandwich Islands flag
    with open(os.path.join(flags_path, "south_georgia.txt"), encoding='utf-8') as f:
        base64_str = f.read()
        flags[202]["flag_base64"] = base64_str

    # missing Jersey flag
    with open(os.path.join(flags_path, "jersey.txt"), encoding='utf-8') as f:
        base64_str = f.read()
        flags.append({"country": "Jersey", "flag_base64": base64_str})

    # missing Montenegro flag
    with open(os.path.join(flags_path, "montenegro.txt"), encoding='utf-8') as f:
        base64_str = f.read()
        flags.append({"country": "Montenegro", "flag_base64": base64_str})

    # missing Timor-Leste flag
    with open(os.path.join(flags_path, "timor-leste.txt"), encoding='utf-8') as f:
        base64_str = f.read()
        flags.append({"country": "Timor-Leste", "flag_base64": base64_str})

    return flags

def fix_languages_data(languages):

    languages[41]["country"] = "The Democratic Republic of the Congo"

    languages.append({"country": "Antarctica", "languages": None})
    languages.append({"country": "Bouvet Island", "languages": ["Norwegian"]})
    languages.append({"country": "British Indian Ocean Territory", "languages": ["English"]})
    languages.append({"country": "England", "languages": ["English"]})
    languages.append({"country": "French Southern territories", "languages": ["French"]})
    languages.append({"country": "Guernsey", "languages": ["English", "Sercquiais", "Auregnais"]})
    languages.append({"country": "Heard Island and McDonald Islands", "languages": ["English"]})
    languages.append({"country": "Isle of Man", "languages": ["English", "Manx"]})
    languages.append({"country": "Jersey", "languages": ["English", "Jèrriais", "Jersey Legal French"]})
    languages.append({"country": "Vatican City", "languages": ["Latin", "Italian"]})
    languages.append({"country": "Wales", "languages": ["English", "Welsh"]})
    languages.append({"country": "Montenegro", "languages": ["Montenegrin", "Albanian", "Bosnian", "Croatian", "Serbian"]})
    languages.append({"country": "Northern Ireland", "languages": ["English", "Irish", "Ulster Scots"]})
    languages.append({"country": "Scotland", "languages": ["English", "Scots", "Scottish Gaelic"]})
    languages.append({"country": "South Georgia and the South Sandwich Islands", "languages": ["English"]})
    languages.append({"country": "South Sudan", "languages": ["English"]})
    languages.append({"country": "North Macedonia", "languages": ["Macedonian", "Albanian", "Turkish", "Romani", "Serbian", "Bosnian", "Aromanian"]})
    languages.append({"country": "South Sudan", "languages": ["English", "Dinka", "Juba Arabic", "Nuer", "Bari", "Murle", "Luo", "Ma'di", "Otuho", "Zande", "Murle", "Shilluk"]})
    languages.append({"country": "Timor-Leste", "languages": ["Portuguese", "Tetum", "Atauru", "Baikeno", "Bekais", "Bunak", "Fataluku", "Galoli", "Habun", "Idalaka", "Kawaimina", "Kemak", "Makalero", "Makasae", "Makuva", "Mambai", "Tokodede", "English", "Indonesian" ]})

    return languages
