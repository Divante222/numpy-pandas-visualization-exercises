
import numpy as np
import pandas as pd
the_dict = {'A': [1, 9], 'B': [4, 5, 6]}
new_value = []
for key, value in the_dict.items():
    if len(the_dict[key]) < 3:
        for i in range(0, (len(value)+1)):
            if i + 1 == len(value)+1:
                new_value.append(np.nan)
            else:
                new_value.append(value[i]) 
        if new_value != []:
            the_dict[key] = new_value
    
    
    new_value = []
    

print(the_dict)
the_dataframe = pd.DataFrame(the_dict)

print(the_dataframe)