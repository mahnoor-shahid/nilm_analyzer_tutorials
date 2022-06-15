
import pandas as pd
import utils.time_utils as t


def generate_activity_report(df, target_appliance, threshold, index_name='time'):
    """
    
    """
    try: 
        duration_start = []
        duration_end = []
        duration_size = []

        if isinstance(df.index, object):
            df.index = t.convert_objects2timestamps(df.index)

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
        return pd.DataFrame({'Activity_Start': duration_start, 'Activity_End': duration_end, 'Duration': t.convert_timestamps2minutes(pd.Series(duration_size))})
    
    except Exception as e:
        print("Exception raised in generate_activity_report() method = ", e)


def get_activities(data, target_appliance=None, threshold=None):
    """
    This method will return the durations or events of the active appliance in the dataframe
    
    Parameters 
    ----------
    data : dict OR pandas.core.frame.DataFrame
                dictionary = contains dataframes of multiple houses where key represents the house number (int) and value represents (pandas.core.frame.DataFrame)
                             dataframe may include the aggregate consumption and power consumption of a specific appliance in float values
                             with timestamps as index
                dataframe =  of a specific house with multiple appliances that includes the aggregate consumption and power consumption of appliances in float values
                             with timestamps as index
    target_appliance : string
            name of the target appliance (may be the name of the column targeted)
    threshold : float
            value of threshold for raw samples of power consumption 
    index_name: string
            name of the index (index_name was set to 'time' while loading)
        
    returns: dict
            contains dataframes of multiple houses where key represents the house number (int) and value represents (pandas.core.frame.DataFrame)
            dataframe is of the following format            
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
        if threshold is None:
                threshold = 0.0
                
        if isinstance(data, dict):
            print('ditionary')
            house_activities = {}
            for key, df in data.items():
                if target_appliance is None:
                    target_appliance = df.columns[-1]
                print(f"Estimating active durations of House {key}: {target_appliance}")
                house_activities.update({key: generate_activity_report(df, target_appliance, threshold)})
            return house_activities
    
        elif isinstance(data, pd.DataFrame):
            print('dfdfdf')
            house_activities = {}
            if target_appliance is None:
                for col in data.columns[2:-1]:
                    target_appliance = col
                    print(f"Estimating active durations of {target_appliance}")
                    house_activities.update({key: generate_activity_report(data, target_appliance, threshold)})
                return house_activities
            else:
                print(f"Estimating active durations of {target_appliance}")
                house_activities.update({target_appliance: generate_activity_report(data, target_appliance, threshold)})
                return house_activities
                
        else:
            print('This method only accepts data as a "dictionary" with keys indicating house number and values indicating their corresponding dataframe or a "single dataframe" of specific house with multiple appliances')

    except Exception as e:
        print("Exception raised in get_activities() method = ", e)