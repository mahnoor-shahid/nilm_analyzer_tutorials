
from utils.configuration import get_config_from_json
from utils.parser import refit_parser
import dask.dataframe as dd


class _Loader:
    """
    Interface that loads all the data into the memory
    """

    def __init__(self):
        try:
            pass
            
        except Exception as e:
            display("Error occured in initialization of _Loader interface due to ", e)
                
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
            display("Error occured in initialization of CSV_Loader class due to ", e)
                
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
            display("Error occured in _load_file method of CSV_Loader class due to ", e)
    
    @staticmethod
    def _load_files_via_dask(_data_folder,
                             _files_format,
                             _buildings):
        try:
            ls = {}
            display(f"Loading specified buildings: {_buildings}")
            for i in _buildings:
                ls.update({i: dd.read_csv(f"{_data_folder}{i}{_files_format}")})
            return ls
        
        except Exception as e:
            display("Error occured in _load_file_via_dask method of CSV_Loader class due to ", e)

            
class REFIT_Loader(CSV_Loader):
    """
    
    """
    def __init__(self):
        try:
            super().__init__()
        
        except Exception as e:
            display("Error occured in initialization of REFIT_Loader class due to ", e)
                
        finally:
            config = get_config_from_json(description="general configuration", config_file="./configs/general_config.json")
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
                
    def get_house_data(self, house_number):
        """
        
        """
        try:
            display(f"Fetching data for house = {house_number}")
            return self.collective_dataset[house_number].compute()
        
        except Exception as e:
            display("Error occured in get_house_data method of REFIT_Loader due to ", e)
    
    def get_appliance_data(self, target_appliance, houses='all_houses'):
        """
        
        """
        try:
            ls = {}
            target_appliance = target_appliance.lower()
            display(f"Fetching data for appliance = {target_appliance}")
            if houses == 'all_houses':
                for house_number in self.collective_dataset.keys():
                    print(self.collective_dataset[house_number].columns)
                    if target_appliance in self.collective_dataset[house_number].columns:
                        display(f"Fetching data for House {house_number}")
                        data = self.collective_dataset[house_number][['aggregate', target_appliance]].compute()
                        ls.update({house_number: data})
            elif type(houses) == list and len(houses)!=0:
                for house_number in houses:
                    print(self.collective_dataset[house_number].columns)
                    if target_appliance not in self.collective_dataset[house_number].columns:
                        display(f"House {house_number} does not have {target_appliance}")
                    else:
                        display(f"Fetching data for House {house_number}")
                        data = self.collective_dataset[house_number][['aggregate', target_appliance]].compute()
                        ls.update({house_number: data})
            else:
                raise Exception("Argument 'houses' is by default set to 'all_houses'. Argument 'houses' should not be an empty list. Argument values must be a list of valid house numbers.")
            return ls
                
        except Exception as e:
            display("Error occured in get_appliance_data method of REFIT_Loader due to ", e)

    