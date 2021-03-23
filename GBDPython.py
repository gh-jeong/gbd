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


def measure_index(measure):
    '''
    :param measure: measure_id (type: list)
    '''
    for i in len(measure):
        if measure[i] == 1:
            measure[i] = 'Deaths'
        elif measure[i] == 2:
            measure[i] = 'DALYs'
        elif measure[i] == 3:
            measure[i] = 'YLDs'
        elif measure[i] == 4:
            measure[i] = 'YLLs'
        elif measure[i] == 5:
            measure[i] = 'Prevalence'
        elif measure[i] == 6:
            measure[i] = 'Incidence'
        elif measure[i] == 25:
            measure[i] = 'Maternal mortality ratio'
        elif measure[i] == 26:
            measure[i] = 'Life expectancy'
        elif measure[i] == 28:
            measure[i] = 'HALE (Healthy life expectancy)'
        elif measure[i] == 29:
            measure[i] = 'Summary exposure value'
        else:
            measure[i] = 'UNKNOWNED MEASURE VARIABLE!!!'
    return measure

def table_1(data, cause, measure, risk=None): #todo Table 1
    '''
    :param data: dataset (Data format: dataframe)
    :param cause: cause_id (see codebook) (Data format: List)
    :param risk: (if present) risk_id (Data format: int)
    :param measure: list of measures (Data format: List)
    :return: table (as dataframe)
    '''
    
    df_t = pd.DataFrame(columns=["Measure"] + cause)

    if not risk:
        for cause in cause:
            for measure in measure:
                data_t = data[(data['cause_name']==cause) & (data['measure_id']==measure) & (data['location_id']==1) & (data['age_id']==22) & (data['sex_id']==3) & (data['metric_id']==1) & (data['year']==2019)]
                value_t = combine_val(data_t['val'], data_t['lower'], data_t['upper'])
                
                pass
            pass
        pass
    else:
        pass
    pass
