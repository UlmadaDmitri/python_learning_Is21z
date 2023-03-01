#1-2 nr
import pandas as pd
my_list = ['sand', 'cement', 'gravel', 'gypsum', 'drywall', 'steel ropes', 'cladding materials']
my_index = [1, 2, 3, 4, 5, 6, 7]
my_series1 = pd.Series(my_list, index=my_index)
print(my_series1)
#3 nr
import pandas as pd
my_dict = {1: 'sand', 2: 'cement', 3: 'gravel', 4: 'gypsum', 5: 'drywall', 6: 'steel ropes', 7: 'cladding materials'}
my_series2 = pd.Series(my_dict)
print(my_series2)
#nr 4