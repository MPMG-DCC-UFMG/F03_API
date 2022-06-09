from src.modules.charts.charts_operations import ChartsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session

from sqlalchemy import and_
from collections import defaultdict
from datetime import datetime
import numpy as np


class ChartsRepository:

    def get_aggregate(params: ChartsQueryParams):
        # filters = params.filters

        # if params.description:
        #     filters.append(ItemModel.original.__eq__(params.description))
            
        # print(params.description)

        # if params.unit_measure:
        #     filters.append(
        #         ItemModel.dsc_unidade_medida.__eq__(params.unit_measure))

        # result = db_session.query(ItemModel) \
        #                    .filter(and_(*filters)) \
        #                    .offset(params.offset) \
        #                    .limit(params.limit)

        # dict_list = [row.__dict__ for row in result]

        # pivot = defaultdict(list)
        # pivot2 = defaultdict(list)
        # for item in dict_list:
        #     item['data'] = item['mes'] + '/' + item['ano']          
        #     pivot2[item['data']].append(item['preco'])
        #     pivot[item['data']].append(item['qtde_item'])
        
        # dict_x = [{'data': k, 'qtde_item': sum(values)} for k, values in pivot.items()]
        # dict_y = [{'data': k, 'mean_preco': round(np.mean(values), 2), 'median_preco': round(np.median(values),2)} for k, values in pivot2.items()]
        
        # res = [{**dx, **dy} for dx, dy in zip(dict_x, dict_y)]
        # for item in res:
        #     data = datetime.strptime(item['data'], '%m/%Y')
        #     item['mes'] = data.strftime('%m')
        #     item['ano'] = data.strftime('%Y')
        
        return [
            {
                "data": "01/2014",
                "qtde_item": 17516173,
                "mean_preco": 9936.87,
                "median_preco": 3.12,
                "mes": "01",
                "ano": "2014"
            },
            {
                "data": "02/2014",
                "qtde_item": 7446975.82,
                "mean_preco": 10671.47,
                "median_preco": 3.09,
                "mes": "02",
                "ano": "2014"
            },
            {
                "data": "03/2014",
                "qtde_item": 4128370.82,
                "mean_preco": 8797.05,
                "median_preco": 3.12,
                "mes": "03",
                "ano": "2014"
            },
            {
                "data": "04/2014",
                "qtde_item": 3255744,
                "mean_preco": 3.12,
                "median_preco": 3.12,
                "mes": "04",
                "ano": "2014"
            },
            {
                "data": "05/2014",
                "qtde_item": 1544500,
                "mean_preco": 4.57,
                "median_preco": 3.15,
                "mes": "05",
                "ano": "2014"
            },
            {
                "data": "06/2014",
                "qtde_item": 911000,
                "mean_preco": 3.07,
                "median_preco": 3.08,
                "mes": "06",
                "ano": "2014"
            },
            {
                "data": "07/2014",
                "qtde_item": 2560871.46,
                "mean_preco": 3.13,
                "median_preco": 3.12,
                "mes": "07",
                "ano": "2014"
            },
            {
                "data": "08/2014",
                "qtde_item": 954495.92,
                "mean_preco": 3.03,
                "median_preco": 3.06,
                "mes": "08",
                "ano": "2014"
            },
            {
                "data": "09/2014",
                "qtde_item": 704767.6699999999,
                "mean_preco": 3.13,
                "median_preco": 3.2,
                "mes": "09",
                "ano": "2014"
            },
            {
                "data": "10/2014",
                "qtde_item": 983000,
                "mean_preco": 3.09,
                "median_preco": 3.05,
                "mes": "10",
                "ano": "2014"
            },
            {
                "data": "11/2014",
                "qtde_item": 1245600,
                "mean_preco": 3.09,
                "median_preco": 3.15,
                "mes": "11",
                "ano": "2014"
            },
            {
                "data": "12/2014",
                "qtde_item": 5157447,
                "mean_preco": 3.11,
                "median_preco": 3.17,
                "mes": "12",
                "ano": "2014"
            },
            {
                "data": "01/2015",
                "qtde_item": 16004336.41,
                "mean_preco": 3737.03,
                "median_preco": 3.2,
                "mes": "01",
                "ano": "2015"
            },
            {
                "data": "02/2015",
                "qtde_item": 5678348,
                "mean_preco": 13759.84,
                "median_preco": 3.4,
                "mes": "02",
                "ano": "2015"
            },
            {
                "data": "03/2015",
                "qtde_item": 4730612.6,
                "mean_preco": 3.46,
                "median_preco": 3.48,
                "mes": "03",
                "ano": "2015"
            },
            {
                "data": "04/2015",
                "qtde_item": 3260263,
                "mean_preco": 473.76,
                "median_preco": 3.5,
                "mes": "04",
                "ano": "2015"
            },
            {
                "data": "05/2015",
                "qtde_item": 1381062,
                "mean_preco": 3.92,
                "median_preco": 3.58,
                "mes": "05",
                "ano": "2015"
            },
            {
                "data": "06/2015",
                "qtde_item": 918615,
                "mean_preco": 588.15,
                "median_preco": 3.53,
                "mes": "06",
                "ano": "2015"
            },
            {
                "data": "07/2015",
                "qtde_item": 1430451.28,
                "mean_preco": 3.53,
                "median_preco": 3.55,
                "mes": "07",
                "ano": "2015"
            },
            {
                "data": "08/2015",
                "qtde_item": 608565,
                "mean_preco": 3.44,
                "median_preco": 3.38,
                "mes": "08",
                "ano": "2015"
            },
            {
                "data": "09/2015",
                "qtde_item": 1359020,
                "mean_preco": 3.57,
                "median_preco": 3.54,
                "mes": "09",
                "ano": "2015"
            },
            {
                "data": "10/2015",
                "qtde_item": 1345008,
                "mean_preco": 3.68,
                "median_preco": 3.62,
                "mes": "10",
                "ano": "2015"
            },
            {
                "data": "11/2015",
                "qtde_item": 730760,
                "mean_preco": 3.7,
                "median_preco": 3.72,
                "mes": "11",
                "ano": "2015"
            },
            {
                "data": "12/2015",
                "qtde_item": 5915088.02,
                "mean_preco": 3.84,
                "median_preco": 3.84,
                "mes": "12",
                "ano": "2015"
            },
            {
                "data": "01/2016",
                "qtde_item": 14009301.8,
                "mean_preco": 1252.17,
                "median_preco": 3.89,
                "mes": "01",
                "ano": "2016"
            },
            {
                "data": "02/2016",
                "qtde_item": 5681632,
                "mean_preco": 18294.13,
                "median_preco": 3.93,
                "mes": "02",
                "ano": "2016"
            },
            {
                "data": "03/2016",
                "qtde_item": 6018424.609999999,
                "mean_preco": 3.82,
                "median_preco": 3.9,
                "mes": "03",
                "ano": "2016"
            },
            {
                "data": "04/2016",
                "qtde_item": 3068283,
                "mean_preco": 3.83,
                "median_preco": 3.9,
                "mes": "04",
                "ano": "2016"
            },
            {
                "data": "05/2016",
                "qtde_item": 1848675,
                "mean_preco": 3.91,
                "median_preco": 3.93,
                "mes": "05",
                "ano": "2016"
            },
            {
                "data": "06/2016",
                "qtde_item": 1103800,
                "mean_preco": 1342.74,
                "median_preco": 4,
                "mes": "06",
                "ano": "2016"
            },
            {
                "data": "07/2016",
                "qtde_item": 887008,
                "mean_preco": 3.81,
                "median_preco": 3.83,
                "mes": "07",
                "ano": "2016"
            },
            {
                "data": "08/2016",
                "qtde_item": 448655,
                "mean_preco": 5.8,
                "median_preco": 4.05,
                "mes": "08",
                "ano": "2016"
            },
            {
                "data": "09/2016",
                "qtde_item": 1147152.44,
                "mean_preco": 3.97,
                "median_preco": 3.9,
                "mes": "09",
                "ano": "2016"
            },
            {
                "data": "10/2016",
                "qtde_item": 816568,
                "mean_preco": 3.86,
                "median_preco": 3.89,
                "mes": "10",
                "ano": "2016"
            },
            {
                "data": "11/2016",
                "qtde_item": 519700,
                "mean_preco": 3.94,
                "median_preco": 3.96,
                "mes": "11",
                "ano": "2016"
            },
            {
                "data": "12/2016",
                "qtde_item": 4207986,
                "mean_preco": 10353.83,
                "median_preco": 3.95,
                "mes": "12",
                "ano": "2016"
            },
            {
                "data": "01/2017",
                "qtde_item": 12748687.04,
                "mean_preco": 775.3,
                "median_preco": 4.03,
                "mes": "01",
                "ano": "2017"
            },
            {
                "data": "02/2017",
                "qtde_item": 8245554,
                "mean_preco": 4,
                "median_preco": 4.03,
                "mes": "02",
                "ano": "2017"
            },
            {
                "data": "03/2017",
                "qtde_item": 6896816.87,
                "mean_preco": 3.87,
                "median_preco": 3.92,
                "mes": "03",
                "ano": "2017"
            },
            {
                "data": "04/2017",
                "qtde_item": 3514775,
                "mean_preco": 3.89,
                "median_preco": 3.9,
                "mes": "04",
                "ano": "2017"
            },
            {
                "data": "05/2017",
                "qtde_item": 2226097,
                "mean_preco": 3.85,
                "median_preco": 3.88,
                "mes": "05",
                "ano": "2017"
            },
            {
                "data": "06/2017",
                "qtde_item": 982545,
                "mean_preco": 1422.69,
                "median_preco": 3.73,
                "mes": "06",
                "ano": "2017"
            },
            {
                "data": "07/2017",
                "qtde_item": 1249501,
                "mean_preco": 3.88,
                "median_preco": 3.94,
                "mes": "07",
                "ano": "2017"
            },
            {
                "data": "08/2017",
                "qtde_item": 1158093,
                "mean_preco": 5.36,
                "median_preco": 4.22,
                "mes": "08",
                "ano": "2017"
            },
            {
                "data": "09/2017",
                "qtde_item": 1860690,
                "mean_preco": 4.61,
                "median_preco": 4.15,
                "mes": "09",
                "ano": "2017"
            },
            {
                "data": "10/2017",
                "qtde_item": 816100,
                "mean_preco": 4.15,
                "median_preco": 4.13,
                "mes": "10",
                "ano": "2017"
            },
            {
                "data": "11/2017",
                "qtde_item": 1511690,
                "mean_preco": 4.36,
                "median_preco": 4.37,
                "mes": "11",
                "ano": "2017"
            },
            {
                "data": "12/2017",
                "qtde_item": 4556470,
                "mean_preco": 34148.67,
                "median_preco": 4.38,
                "mes": "12",
                "ano": "2017"
            },
            {
                "data": "01/2018",
                "qtde_item": 12745551.69,
                "mean_preco": 4.51,
                "median_preco": 4.53,
                "mes": "01",
                "ano": "2018"
            },
            {
                "data": "02/2018",
                "qtde_item": 5592977,
                "mean_preco": 130.92,
                "median_preco": 4.58,
                "mes": "02",
                "ano": "2018"
            },
            {
                "data": "03/2018",
                "qtde_item": 5384134.05,
                "mean_preco": 4.55,
                "median_preco": 4.62,
                "mes": "03",
                "ano": "2018"
            },
            {
                "data": "04/2018",
                "qtde_item": 2100150,
                "mean_preco": 4.55,
                "median_preco": 4.7,
                "mes": "04",
                "ano": "2018"
            },
            {
                "data": "05/2018",
                "qtde_item": 1642200,
                "mean_preco": 4.61,
                "median_preco": 4.78,
                "mes": "05",
                "ano": "2018"
            },
            {
                "data": "06/2018",
                "qtde_item": 1882459,
                "mean_preco": 4.66,
                "median_preco": 4.88,
                "mes": "06",
                "ano": "2018"
            },
            {
                "data": "07/2018",
                "qtde_item": 2166390,
                "mean_preco": 4.83,
                "median_preco": 4.88,
                "mes": "07",
                "ano": "2018"
            },
            {
                "data": "08/2018",
                "qtde_item": 1298374,
                "mean_preco": 4.91,
                "median_preco": 4.89,
                "mes": "08",
                "ano": "2018"
            },
            {
                "data": "09/2018",
                "qtde_item": 795436,
                "mean_preco": 5.12,
                "median_preco": 5.16,
                "mes": "09",
                "ano": "2018"
            },
            {
                "data": "10/2018",
                "qtde_item": 1268760,
                "mean_preco": 5.13,
                "median_preco": 5.14,
                "mes": "10",
                "ano": "2018"
            },
            {
                "data": "11/2018",
                "qtde_item": 1537520,
                "mean_preco": 4.62,
                "median_preco": 5,
                "mes": "11",
                "ano": "2018"
            },
            {
                "data": "12/2018",
                "qtde_item": 5613710,
                "mean_preco": 4.67,
                "median_preco": 4.8,
                "mes": "12",
                "ano": "2018"
            },
            {
                "data": "01/2019",
                "qtde_item": 9042532.3,
                "mean_preco": 4.77,
                "median_preco": 4.78,
                "mes": "01",
                "ano": "2019"
            },
            {
                "data": "02/2019",
                "qtde_item": 5642962,
                "mean_preco": 9978.72,
                "median_preco": 4.69,
                "mes": "02",
                "ano": "2019"
            },
            {
                "data": "03/2019",
                "qtde_item": 3749179,
                "mean_preco": 667.46,
                "median_preco": 4.8,
                "mes": "03",
                "ano": "2019"
            },
            {
                "data": "04/2019",
                "qtde_item": 2715150,
                "mean_preco": 4.95,
                "median_preco": 4.94,
                "mes": "04",
                "ano": "2019"
            },
            {
                "data": "05/2019",
                "qtde_item": 1917500,
                "mean_preco": 4.76,
                "median_preco": 4.96,
                "mes": "05",
                "ano": "2019"
            },
            {
                "data": "06/2019",
                "qtde_item": 1496820,
                "mean_preco": 4.82,
                "median_preco": 4.9,
                "mes": "06",
                "ano": "2019"
            },
            {
                "data": "07/2019",
                "qtde_item": 1668780,
                "mean_preco": 4.88,
                "median_preco": 4.88,
                "mes": "07",
                "ano": "2019"
            },
            {
                "data": "08/2019",
                "qtde_item": 1289600,
                "mean_preco": 4.7,
                "median_preco": 4.72,
                "mes": "08",
                "ano": "2019"
            },
            {
                "data": "09/2019",
                "qtde_item": 1498300,
                "mean_preco": 4.86,
                "median_preco": 4.81,
                "mes": "09",
                "ano": "2019"
            },
            {
                "data": "10/2019",
                "qtde_item": 730300,
                "mean_preco": 4.91,
                "median_preco": 4.93,
                "mes": "10",
                "ano": "2019"
            },
            {
                "data": "11/2019",
                "qtde_item": 1669000,
                "mean_preco": 4.9,
                "median_preco": 4.86,
                "mes": "11",
                "ano": "2019"
            },
            {
                "data": "12/2019",
                "qtde_item": 4283853,
                "mean_preco": 4.83,
                "median_preco": 4.95,
                "mes": "12",
                "ano": "2019"
            },
            {
                "data": "01/2020",
                "qtde_item": 10424031,
                "mean_preco": 4.96,
                "median_preco": 4.95,
                "mes": "01",
                "ano": "2020"
            },
            {
                "data": "02/2020",
                "qtde_item": 6799121,
                "mean_preco": 11260.9,
                "median_preco": 4.99,
                "mes": "02",
                "ano": "2020"
            },
            {
                "data": "03/2020",
                "qtde_item": 4209984,
                "mean_preco": 4.86,
                "median_preco": 4.89,
                "mes": "03",
                "ano": "2020"
            },
            {
                "data": "04/2020",
                "qtde_item": 2019080,
                "mean_preco": 4.55,
                "median_preco": 4.54,
                "mes": "04",
                "ano": "2020"
            },
            {
                "data": "05/2020",
                "qtde_item": 2234800,
                "mean_preco": 4.24,
                "median_preco": 4.2,
                "mes": "05",
                "ano": "2020"
            },
            {
                "data": "06/2020",
                "qtde_item": 1115300,
                "mean_preco": 4.27,
                "median_preco": 4.23,
                "mes": "06",
                "ano": "2020"
            },
            {
                "data": "07/2020",
                "qtde_item": 1075980,
                "mean_preco": 4.55,
                "median_preco": 4.45,
                "mes": "07",
                "ano": "2020"
            },
            {
                "data": "08/2020",
                "qtde_item": 943167,
                "mean_preco": 4.65,
                "median_preco": 4.61,
                "mes": "08",
                "ano": "2020"
            },
            {
                "data": "09/2020",
                "qtde_item": 1477200,
                "mean_preco": 4.68,
                "median_preco": 4.7,
                "mes": "09",
                "ano": "2020"
            },
            {
                "data": "10/2020",
                "qtde_item": 1892609,
                "mean_preco": 4.85,
                "median_preco": 4.89,
                "mes": "10",
                "ano": "2020"
            },
            {
                "data": "11/2020",
                "qtde_item": 1433040,
                "mean_preco": 4.75,
                "median_preco": 4.74,
                "mes": "11",
                "ano": "2020"
            },
            {
                "data": "12/2020",
                "qtde_item": 3742110,
                "mean_preco": 4.91,
                "median_preco": 4.87,
                "mes": "12",
                "ano": "2020"
            },
            {
                "data": "01/2021",
                "qtde_item": 7327832.3,
                "mean_preco": 4.93,
                "median_preco": 4.94,
                "mes": "01",
                "ano": "2021"
            },
            {
                "data": "02/2021",
                "qtde_item": 5917810,
                "mean_preco": 5.19,
                "median_preco": 5.16,
                "mes": "02",
                "ano": "2021"
            },
            {
                "data": "03/2021",
                "qtde_item": 4927939,
                "mean_preco": 5.78,
                "median_preco": 5.78,
                "mes": "03",
                "ano": "2021"
            },
            {
                "data": "04/2021",
                "qtde_item": 2888908,
                "mean_preco": 5.9,
                "median_preco": 5.96,
                "mes": "04",
                "ano": "2021"
            },
            {
                "data": "05/2021",
                "qtde_item": 2056881,
                "mean_preco": 6.12,
                "median_preco": 6.05,
                "mes": "05",
                "ano": "2021"
            },
            {
                "data": "06/2021",
                "qtde_item": 1430600,
                "mean_preco": 6.12,
                "median_preco": 6.2,
                "mes": "06",
                "ano": "2021"
            }
        ]
        # return sorted(res, key=lambda d: datetime.strptime(d['data'], '%m/%Y'))
