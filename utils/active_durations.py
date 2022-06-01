
import numpy as np
import pandas as pd

def convert_timestamps2minutes(tstamps: pd.Series):
    try:
        return tstamps / np.timedelta64(1, 'm')

    except Exception as e:
        print("Exception raised in generating convert_timestamps2minutes() method = ", e)
    
    
def get_activities(df, target_appliance=None, threshold=None, index_name='time'):
    """
    This method will return the durations or events of the active appliance in the dataframe
    
    Parameters 
    ----------
    df : pandas.DataFrame
            contains power consumption in float values with timestamps as index (may contain multiple columns)
    target_appliance : string
            name of the target appliance (may be the name of the column targeted)
    threshold : float
            value of threshold for raw samples of power consumption 
    index_name: string
            name of the index (index_name was set to 'time' while loading)
        
    returns: pandas.DataFrame 
            {
                'Activity_Start': pandas._libs.tslibs.timestamps.Timestamp
                    start of the duration/event 
                'Activity_End': pandas._libs.tslibs.timestamps.Timestamp 
                    end of the duration/event
                'Duration': float
                    minutes of active appliance (using the method = convert_timestamps2minutes to convert timestamps to minutes)
            }
    """
    
    try:
        duration_start = []
        duration_end = []
        duration_size = []
        
        if target_appliance is None:
            target_appliance = df.columns[-1]
        
        if threshold is None:
            threshold = 0.0

        df_tmp = df[[target_appliance]].copy()
        mask = df[target_appliance] > threshold
        df_tmp['mask'] = (mask)
        df_tmp['cum_sum'] = (~mask).cumsum()
        df_tmp = df_tmp[df_tmp['mask'] == True]
        df_tmp = df_tmp.groupby(['cum_sum', index_name]).first()

        for x in df_tmp.index.unique(level='cum_sum'):
            d = df_tmp.loc[(x)].reset_index()
            duration_start.append(d.iloc[0]['time'])
            duration_end.append(d.iloc[-1]['time'])
            duration_size.append(duration_end[-1] - duration_start[-1])
    
        return pd.DataFrame({'Activity_Start': duration_start, 'Activity_End': duration_end, 'Duration': convert_timestamps2minutes(pd.Series(duration_size))})

    except Exception as e:
        print("Exception raised in get_activities() method = ", e)