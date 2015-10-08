
# coding: utf-8

# In[2]:

import numpy as np
import json 
msg3 = 'C:\Users\jim.kleinert.HNETNT\Desktop\msg3.txt'
file1 = open(msg3, mode = 'U')
data = file1.read()
msg3_text = open(msg3, mode = 'U')
segment_list = []

for row in msg3_text: 
    segment = row.strip('\n')
    segment_list.append(segment)
segment_list[0]
fields_list = []
for segment in segment_list:
    fields = segment.split("|")
    fields_list.append(fields)
field_components = []
for fields in fields_list:
    for field in fields:
        if '^' in field:
            component = field.replace('^', ',')
        else:
            component = field
        field_components.append(component)
field_components[0:12]
dict_list = [] # Each segment has a list of dictionaries as a dictionary
for fields in fields_list:
    dict_name = {}
    key = fields[0]
    value = fields[1:]
    dict_name[key] = value
    dict_list.append(dict_name) 
dict_list
json_msg3 = json.dumps(dict_list, indent=2)
print(json_msg3)



# In[ ]:



