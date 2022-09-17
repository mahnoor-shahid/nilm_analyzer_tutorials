
from utils.configuration import get_config_from_json
from utils.parser import refit_parser
import dask.dataframe as dd
import utils.time_utils as t
from utils.validations import check_house_availability, check_list_validations, check_correct_datatype
        

    
class _Loader:
    """
    Interface that loads all the data into the memory
    """

    def __init__(self):
        try:
            pass
            
        except Exception as e:
            print("Error occured in initialization of _Loader interface due to ", e)
                
        finally:
            pass
        
    @staticmethod
    def _load_file():
        raise NotImplementedError    


        
class CSV_Loader(_Loader):
    """
    
    """
    def __init__(self):
        try:
            super().__init__()
        
        except Exception as e:
            print("Error occured in initialization of CSV_Loader class due to ", e)
                
        finally:
            pass
        
    @staticmethod
    def _load_file(csv_file_path,
                   index_column_name=None,
                   _nrows=None,
                   _iterator=True,
                   _chunksize=100000):
        try:
            tp = pd.read_csv(csv_file_path, nrows=_nrows, index_col=index_column_name, iterator=_iterator, chunksize=_chunksize) ## loading data in chunks reduces 90 percent execution time 
            df = pd.concat(tp, ignore_index=False)
            df.info(verbose=False, memory_usage="deep")
            return df  
        
        except Exception as e:
            print("Error occured in _load_file method of CSV_Loader class due to ", e)
    
    @staticmethod
    def _load_files_via_dask(_data_folder,
                             _files_format,
                             _buildings):
        try:
            ls = {}
            print(f"\nLoading specified buildings: {_buildings}")
            for i in _buildings:
                ls.update({i: dd.read_csv(f"{_data_folder}{i}{_files_format}")})
            return ls
        
        except Exception as e:
            print("Error occured in _load_file_via_dask method of CSV_Loader class due to ", e)
    

    
class REFIT_Loader(CSV_Loader):
    """
    
    """
    def __init__(self):
        try:
            super().__init__()
        
        except Exception as e:
            print("Error occured in initialization of REFIT_Loader class due to ", e)
                
        finally:
            config = get_config_from_json(description="general configuration", config_file="./config.json")
            self.collective_dataset = CSV_Loader._load_files_via_dask(_data_folder=config['DATA_FOLDER']+'House_',
                                                                _files_format=config['DATA_TYPE'],
                                                                _buildings=config['REFIT_HOUSES'])
            self.keys_of_appliances = refit_parser(config['README_FILE'])
            for house_number in self.collective_dataset:
                cols = [header.lower() for header in self.keys_of_appliances[str(house_number)]]
                self.collective_dataset[house_number] = self.collective_dataset[house_number].rename(columns={"Time": "time", "Unix": "unix", "Aggregate": cols[0], "Appliance1":cols[1], "Appliance2":cols[2],
                                                                                                      "Appliance3":cols[3], "Appliance4":cols[4], "Appliance5":cols[5],"Appliance6":cols[6], "Appliance7":cols[7],
                                                                                                      "Appliance8":cols[8], "Appliance9":cols[9]})
                self.collective_dataset[house_number].index = self.collective_dataset[house_number]['time']
                self.collective_dataset[house_number] = self.collective_dataset[house_number].drop('time', axis=1)
                
    def get_appliance_names(self, house: int):
        """
        
        """
        try:
            if check_correct_datatype(arg_name='house', arg_value=house, target_datatype=int):
                if check_house_availability(arg_name='House Number', arg_value=house, collection=self.collective_dataset.keys()):
                    print(f"Fetching appliances for house = {house}")
                    return [name for name in self.collective_dataset[house].columns]
        except Exception as e:
            print("Error occured in get_appliance_names method of REFIT_Loader due to ", e)
                
    def get_house_data(self, house: int):
        """
        
        """
        try:                
            if check_correct_datatype(arg_name='house', arg_value=house, target_datatype=int):
                if check_house_availability(arg_name='House Number', arg_value=house, collection=self.collective_dataset.keys()):
                    print(f"Loading data for house = {house}")
                    return self.collective_dataset[house].compute() 
        
        except Exception as e:
            print("Error occured in get_house_data method of REFIT_Loader due to ", e)
    
    def get_appliance_data(self, appliance, houses=None):
        """
        
        """
        try:
            self.data = {}
            if check_correct_datatype(arg_name='appliance', arg_value=appliance, target_datatype=str):
                target_appliance = appliance.lower()
            if houses == None:
                houses=list(self.collective_dataset.keys())
                
            print(f"Loading data for appliance {target_appliance.upper()} ...")
            if check_list_validations(arg_name='houses', arg_value=houses, member_datatype='int'):
                for house_number in houses:
                    if check_house_availability(arg_name='House Number', arg_value=house_number, collection=self.collective_dataset.keys()):
                        if target_appliance in self.collective_dataset[house_number].columns:
                            print(f"Fetching {target_appliance.upper()} data for House {house_number}")
                            data = self.collective_dataset[house_number][['aggregate', target_appliance]].compute()
                            data.index = t.convert_object2timestamps(data.index)
                            self.data.update({house_number: data})
                        else:
                            print(f"Appliance '{target_appliance.upper()}' does not exist in house {house_number}. Hint: Check the availability of the appliance by using 'get_appliance_names' method")

            return RefitData(self.data, self.collective_dataset.keys())
                
        except Exception as e:
            print("Error occured in get_appliance_data method of REFIT_Loader due to ", e)


class RefitData():
    """
    
    """
    def __init__(self, data, available_houses):
        try:
            self.data = data
            self.available_houses = available_houses
        
        except Exception as e:
            print("Error occured in initialization of RefitData class due to ", e)
                
        finally:
            pass
    
    def resample(self, house=None, sampling_period='8s', fill_value=0.0, window_limit=3.0):
        """
        
        """
        try:
            self.sampling_period = sampling_period
            self.fill_value = fill_value
            self.window_limit= int(window_limit*60)
            
            if house == None:
                ls = {}
                for house_number in self.data.keys():
                    print(f"Resampling for house number: ", house_number)
#                     target_appliance = self.data[house_number].columns[-1]
                    appliance_data = self.data[house_number]
#                     appliance_data = appliance_data.resample('1s').mean().dropna()
                    appliance_data = appliance_data.resample('1s').asfreq()
                    appliance_data.fillna(method='ffill', axis=0, inplace=True, limit=self.window_limit)
                    appliance_data.fillna(axis=0, inplace=True, value=self.fill_value)
                    appliance_data = appliance_data.resample(self.sampling_period).median()
                    ls.update({house_number: appliance_data})
                self.data = ls

        except Exception as e:
            print("Error occured in resample method of REFIT_Loader due to ", e) 

    