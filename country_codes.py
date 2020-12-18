from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Return the Pygal 2-digit country code for the given country.'''

    names = []
    codes = []
    indices = []
    count = 0
    for code, name in COUNTRIES.items():
        if name.strip() == country_name.strip():
            names.append(name)
            indices.append(count)
            codes.append(code)
            count += 1

    for i in indices:
        if country_name == names[i]:
            return codes[i]

    if country_name == 'Arab World':
        return 'arb'
    elif country_name == 'Venezuela, RB':
        return 'ven'
    elif country_name == 'Yemen, Rep.':
        return 'yem'
    elif country_name == 'West Bank and Gaza':
        return 'pse'
    elif country_name == 'Bolivia':
        return 'bol'

    print('Error - ' + country_name)
    return None

    # If the country wasn't found, retun None.


# print(get_country_code('Afghanistan'))
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))

# def get_country_code(country_name):
#     '''Return the Pygal 2-digit country code for the given country.'''
#
#     for code, name in COUNTRIES.items():
#         if name.strip() == country_name.strip():
#             return code
#
#         else:
#             return None
#
#
#
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
# print(get_country_code('Zimbabwe'))
