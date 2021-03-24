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