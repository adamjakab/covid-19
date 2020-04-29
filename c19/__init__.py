# Utilities

from urllib.request import urlopen
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

url_tpl_wb = "https://api.worldbank.org/v2/en/country/" \
             "{cc}/indicator/{ic}?format=json&per_page=100"



def get_df_for_wb_countries_indicators(countries, indicators, jointype='inner'):
    wbdf = None
    for indicator_code in indicators:
        idf = get_df_for_wb_countries_indicator(countries, indicator_code)
        idf["CY"] = idf["country"] + "-" + idf["year"]
        idf.set_index('CY', inplace=True)
        if wbdf is None:
            wbdf = idf
        else:
            idf.drop(columns=['country', 'year'], axis=1, inplace=True)
            wbdf = wbdf.join(idf, how=jointype, on='CY', lsuffix='_left')

    return wbdf

def get_df_for_wb_countries_indicator(countries, indicator_code):
    wbdf = pd.DataFrame()

    for country_code in countries:
        wbdf = wbdf.append(
            get_df_for_wb_country_indicator(country_code, indicator_code))

    return wbdf

def get_df_for_wb_country_indicator(country_code, indicator_code):
    col_names = ['country', 'year', indicator_code]
    response = urlopen(url_tpl_wb.format(cc=country_code, ic=indicator_code))
    data = json.loads(response.read())
    rows = []
    for item in data[1]:
        rows.append([item["countryiso3code"], item["date"], item["value"]])

    return pd.DataFrame(np.array(rows), columns=col_names)
