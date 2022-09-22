# REFIT Loader
> This project uses **Dask Dataframes** to ease and fasten the process of loading all the data of REFIT and provides functionalities to transform and maniuplate the REFIT dataset for statistical analysis purpose.


## REFIT dataset
An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study. Sci Data 4, 160122 (2017). <br />
Murray, D., Stankovic, L. & Stankovic, V.  <br />


### Links
For more detail information, visit the following links: <br />
http://dx.doi.org/10.1038/sdata.2016.122 <br />
https://rdcu.be/cMD9F <br />


## Steps to implement this project
1) Clone this repository to the target source project.
2) Download the REFIT dataset using the [download links](#downloads) below 
3) Unzip the data in the **data/refit/** folder
4) Make sure to download the "REFIT_Readme.txt" and save it in the **data/refit/** folder
5) Use the notebooks "geting_started.ipynb" and "resampling.ipynb" to know the instructions on how to use the loader


## Downloads
The REFIT Smart Home dataset is a publicly available dataset of Smart Home data. <br />
Dataset - https://pureportal.strath.ac.uk/files/52873459/Processed_Data_CSV.7z <br />
Readme File - <br />
Main Page - https://pureportal.strath.ac.uk/en/datasets/refit-electrical-load-measurements-cleaned


### Repo Structure:
This repository follows the below structure format:
```
|
|── loader
|  └── __init__.py
|  └── data_loader.py
|
|
├── utils
|  └── configuration.py
|  └── parser.py
|  └── time_utils.py
|  └── validations.py
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
├── config.json
|
├── 01_getting_started.ipynb
|
├── 02_resampling.ipynb
|
├── environment.yml
|
├── readme.md
```

## Dependencies:
```
  - python=3.9.2
  - numpy=1.20.3
  - pandas=1.2.4
  - dask=2021.06.2
  - json=2.0.9
```

# Citation:
```
Murray, D., Stankovic, L. & Stankovic, V. An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study. Sci Data 4, 160122 (2017). https://doi.org/10.1038/sdata.2016.122
```

## Future Work:
- data downloading from source to repository

