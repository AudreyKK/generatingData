import json
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.maps.world import World
from country_codes import get_country_code


filename = 'gdp_json.json'

with open(filename) as f:
    gdp_data = json.load(f)


# Build a dictionary of GDP data
country_gdp = {}
# Print the GDP for 2015 for each country
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2015:
        country_name = gdp_dict['Country Name']
        gdp = int(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            country_gdp[code] = gdp

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'GDP by Country in 2015'
wm.add('gdp', country_gdp)


wm.render_to_file('world_gdp.svg')
