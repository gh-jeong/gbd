## Importing modules
try:
    import numpy as np
    import pandas as pd
except Exception as e:
    print("Module not present: ", e)

def gbd_retrieve(data, measure, location_name, age, metric, year, sex=3):
    data_t = data[(data['measure_id']==measure) & (data['location_name']==location_name) & (data['age_id']==age) & (data['sex_id']==sex) & (data['metric_id']==metric) & (data['year']==year)]
    value = str(round(data_t["val"].values[0],2)) + " (" + str(round(data_t["lower"].values[0],2)) + ", " + str(round(data_t["upper"].values[0],2)) + ")"
  return value # value includes val (95% UI)

def combine_val(val, lower, upper, n=2):
    '''
    :param val: effect size (type: float)
    :param lower, upper: lower and upper limit (float)
    :param n: number of maximum digits
    :return: es (lower, upper) (type: string)
    '''
    return str(round(val, n)) + " (" + str(lower, n)) + ", " + str(round(upper, n)) + ")"


def table_1(data, cause, measure, risk=None): #todo Table 1
    '''
    :param data: dataset (Data format: dataframe)
    :param cause: cause_id (see codebook) (Data format: List)
    :param risk: (if present) risk_id (Data format: int)
    :param measure: list of measures (Data format: List)
    :return: table (as dataframe)
    '''
    df = pd.DataFrame(index = measure, column = cause)    

    if not risk:
        for cause in cause:
            for measure in measure:
                value_t = gbd_retrieve(data, measure, "Global", age=22, metric=1, year=2019)
                df[cause, measure] = value_t # add value_t in the right site of the dataframe
        pass
    else:
        pass
    pass
