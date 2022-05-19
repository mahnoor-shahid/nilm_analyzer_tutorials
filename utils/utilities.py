
import re
from configs.configuration import general_config


def refit_parser(readme_file):
    """
    
    """
    try:
        display(f'Parsing the readme file specified: {readme_file}')
        with open(readme_file) as f:
            content = f.readlines()
        ls = {}
        for i, s in enumerate(content):
            if 'House' in s.capitalize():
                keys, appliances = [], []
                house = s.split()[1]
                for indx in range(1, 6):
                    if content[i+indx] == '\t!NOTES\n':
                        break
                    else:
                        target = [value.split('.') for value in [value for value in content[i+indx].split(',') if value != '\n']]
                        for t in target:
                            if len(t) > 2: ##### one comma missing caused issue
                                appliances.append(t[1])
                                appliances.append(t[2])
                            else:
                                appliances.append(t[1])
                ls.update({house: [item.split('\n')[0] for item in appliances]})
        return ls
    
    except Exception as e:
        display("Error occured in parser method due to ", e)