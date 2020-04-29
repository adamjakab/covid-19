# COVID-19

## Visualizations

Thevisualizations are based on the public official datasets prepared by:
 
 - [OWID](https://ourworldindata.org/) and in the specific on the datasets from [this repository](https://github.com/owid/covid-19-data/tree/master/public/data). 
 - The World Bank - https://databank.worldbank.org/home.aspx
 - Italy: Istat - https://www.istat.it/it/dati-analisi-e-prodotti and http://demo.istat.it/
 - Italy: Protezione Civile - 

For more information about the accuracy of the data please refer to: https://ourworldindata.org/what-can-data-on-testing-tell-us-about-the-pandemic

Wherever possible the notebooks are connected to on-line resources so on each execution they will fetch the updated datasets.








```python
# Country codes (c19df['iso_code'].unique())
#['ABW', 'AFG', 'AGO', 'AIA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM',
#'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BES', 'BFA',
#'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL',
#'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHL',
#'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'CPV', 'CRI', 'CUB',
#'CUW', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM',
#'DZA', 'ECU', 'EGY', 'ERI', 'ESH', 'ESP', 'EST', 'ETH', 'FIN',
#'FJI', 'FLK', 'FRA', 'FRO', 'GAB', 'GBR', 'GEO', 'GGY', 'GHA',
#'GIB', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM',
#'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN',
#'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JEY',
#'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KNA', 'KOR', 'KWT',
#'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LTU', 'LUX',
#'LVA', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MKD', 'MLI',
#'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MUS',
#'MWI', 'MYS', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NLD', 'NOR',
#'NPL', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PNG', 'POL',
#'PRI', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'RKS', 'ROU', 'RUS',
#'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLE', 'SLV', 'SMR', 'SOM',
#'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM',
#'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TLS', 'TTO', 'TUN',
#'TUR', 'TWN', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VAT',
#'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'YEM', 'ZAF', 'ZMB', 'ZWE',]
```
