import pandas as pd
import utils.time_utils as t


class Data():
    """
    
    """
    def __init__(self, data):
        try:
            self.data = data
        
        except Exception as e:
            print("Error occured in initialization of Data_Transformations class due to ", e)
                
        finally:
            pass

    def resample(self, sampling_period='8s', fill_value=0.0, window_limit=3.0):
        """
        
        """
        try:
            self.sampling_period = sampling_period
            self.fill_value = fill_value
            self.window_limit= int(window_limit*60)
            ls = {}

            for house_number in self.data.keys():
                print(f"Resampling for house number: ", house_number)
                target_appliance = self.data[house_number].columns[-1]
                appliance_data = self.data[house_number]
                appliance_data.index = t.convert_object2timestamps(appliance_data.index)
#                 appliance_data = appliance_data.resample('1s').mean().dropna()
                appliance_data = appliance_data.resample('1s').asfreq()
                appliance_data.fillna(method='ffill', axis=0, inplace=True, limit=self.window_limit)
                appliance_data.fillna(axis=0, inplace=True, value=self.fill_value)
                appliance_data = appliance_data.resample(self.sampling_period).median()
                ls.update({house_number: appliance_data})
            
            self.data = ls

        except Exception as e:
            print("Error occured in resample method of REFIT_Loader due to ", e)