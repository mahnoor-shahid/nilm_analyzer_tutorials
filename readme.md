
# REFIT Analyzer
> This project uses refit_loader as a submodule which has taken the advantage of **Dask Dataframes** to ease and fasten the process of loading all the data of REFIT dataset and also provides some functionalities. This project demonstrates how refit_loader can be used to do different transformations (e.g, resampling) and manipulate the REFIT dataset for statistical analysis purpose. 


## REFIT dataset
An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study. Sci Data 4, 160122 (2017). <br />
Murray, D., Stankovic, L. & Stankovic, V.  <br />

### Links
For more detail information, visit the following links: <br />
http://dx.doi.org/10.1038/sdata.2016.122 <br />
https://rdcu.be/cMD9F <br />


## Dependencies
Ensure that the following dependencies are satisfied either in your current environment 
```
  - python=3.9.2
  - numpy=1.20.3
  - pandas=1.2.4
  - dask=2021.06.2
  - json=2.0.9
```
or create a new environment using 'environment.yml'
```
conda create env --file=environment.yml
conda activate refit_loader_env
```


## Steps to implement this project
1) Use refit_loader as a submodule and clone it into your target source project
```
git submodule add https://github.com/mahnoor-shahid/refit_loader.git
```

2) Make sure the 'config.json' file of refit_loader has the correct DATA_FOLDER path; [Download] the dataset and it should be located in this data folder.
```
{ 
    "DATA_FOLDER" : "data/refit/",
    "DATA_TYPE" : ".csv",
    "README_FILE" : "refit_loader/REFIT_Readme.txt",
    "REFIT_HOUSES" : [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21]
}
```

3) Use the notebooks "geting_started.ipynb" and "resampling.ipynb" to know the instructions on how to use the refit loader

Reference Repository: <br />
[Refit Loader](https://github.com/mahnoor-shahid/refit_loader) = REFIT loader is a simple, fast and handy data loader for REFIT dataset to explore the data at convenience, provided with basic transformations like resampling and extract activities by thresholding.

### Repo Structure:
This repository follows the below structure format:
```
|
|  
├── refit_loader
|  └── data_loader.py
|  └── utilities
|   |  └── configuration.py
|   |  └── parser.py
|   |  └── time_utils.py
|   |  └── validations.py
|  └── config.json
|  └── environment.yml
|  └── REFIT_README.txt
|  └── readme.md
|
|
├── data
|  └── refit
|  |  └── REFIT_Readme.txt
|  |  └── House_1.csv
|  |  └── House_2.csv
|  |  └── House_3.csv
|  |  └── House_4.csv
|  |  └── House_5.csv
|  |  └── House_6.csv
|  |  └── House_7.csv
|  |  └── House_8.csv
|  |  └── House_9.csv
|  |  └── House_10.csv
|  |  └── House_11.csv
|  |  └── House_12.csv
|  |  └── House_13.csv
|  |  └── House_15.csv
|  |  └── House_16.csv
|  |  └── House_17.csv
|  |  └── House_18.csv
|  |  └── House_19.csv
|  |  └── House_20.csv
|
|
├── 01_getting_started.ipynb
|
├── 02_resampling.ipynb
|
├── 03_extract_durations.ipynb
|
├── environment.yml
|
├── readme.md
```

## From where to download the dataset 
The REFIT Smart Home dataset is a publicly available dataset of Smart Home data. <br />
Dataset - https://pureportal.strath.ac.uk/files/52873459/Processed_Data_CSV.7z <br />
Main Page - https://pureportal.strath.ac.uk/en/datasets/refit-electrical-load-measurements-cleaned


## Citation
```
Murray, D., Stankovic, L. & Stankovic, V. An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study. Sci Data 4, 160122 (2017). https://doi.org/10.1038/sdata.2016.122
```

