from flask import request
from . import routes
from models import Country, CountryQueries

import pandas as pd

@routes.route('/import', methods=['POST'], endpoint='import')
def import_csv():
    universities_ranking = pd.read_csv(request.files.get("world_university_ranking"), delimiter=',')
    countries_ranking_by_pib = pd.read_csv(request.files.get("countries_ranking_by_pib"), delimiter=',')

    df = countries_ranking_by_pib.sort_values(by="2022", ascending=False)
    index = 0

    for _, country in df.iterrows():
        index += 1
        country_code = country['Country Code'][0:2]
        country_name = country['Country Name']
        country_universities = universities_ranking[universities_ranking['location'] == country_name]

        country_model = Country(
            code=country_code,
            name=country_name,
            ranking_pos=index,
            pib=country['2022'],
            universities_on_world_ranking=len(country_universities)
        )

        CountryQueries.insert(country_model)

    return '', 200
