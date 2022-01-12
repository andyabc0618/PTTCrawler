from datetime import datetime
import pandas as pd

def date_compare(date):
    now  = datetime.now()
    if now.month < date.month:
        # last year
        date = date.replace(year= sub_years(now, 1))
    else:
        # this year
        date = date.replace( year = now.year)

    return date

def sub_years( date, years):
    return date.replace(year = date.year - years).year


def dictlist_to_dataframe( dictlist, attributes):
    dict_ = {}
    attribute_keys = list(attributes.keys())
    for i in range( 0, len(dictlist), 1):
        entry = dictlist[i]
        for j in range( 0, len(attribute_keys), 1):
            key     = attribute_keys[j]
            keyname = attributes[key]
            value   = entry[key]
            if keyname not in dict_:
                dict_[keyname] = []
            dict_[keyname].append(value)
    
    df = pd.DataFrame(dict_)


    return df   


