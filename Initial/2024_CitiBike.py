#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import gc
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


# del df_final_2024

# gc.collect()


# In[6]:


def get_excel_files_from_monthly_folders(base_path):
    
    column_mapping = {'Trip Duration': 'tripduration',
    'Start Time': 'starttime',
    'Stop Time': 'stoptime',
    'Start Station ID': 'start station id',
    'Start Station Name': 'start station name',
    'Start Station Latitude': 'start station latitude',
    'Start Station Longitude': 'start station longitude',
    'End Station ID': 'end station id',
    'End Station Name': 'end station name',
    'End Station Latitude': 'end station latitude',
    'End Station Longitude': 'end station longitude',
    'Bike ID': 'bikeid',
    'User Type': 'usertype',
    'Birth Year': 'birth year',
    'Gender': 'gender'}

    if not os.path.exists(base_path):
        print(f"Error: The base path '{base_path}' does not exist.")
        return []

    all_dataframes = []
    
    for month_folder in os.listdir(base_path):
        month_path = os.path.join(base_path, month_folder)
        
        if os.path.isdir(month_path):
            for file in os.listdir(month_path):
                if file.endswith(".csv"):
                    file_path = os.path.join(month_path, file)                  
                    try:
                        df = pd.read_csv(file_path)
                        all_dataframes.append(df)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    
    return all_dataframes


# In[4]:


def combine_dataframes(dataframes):
    combined_df = pd.concat(dataframes, ignore_index = True)
    combined_df[['member_casual','rideable_type','started_at','ended_at']]
    return combined_df


def save_combined_dataframe(df, output_path):
    try:
        df.to_excel(output_path, index=False)
        print(f"Combined Excel file saved to: {output_path}")
    except Exception as e:
        print(f"Error saving combined Excel file: {e}")


# In[7]:


base_path = r"Downloads\CitiBike\2024-citibike-tripdata\2024-citibike-tripdata"  
excel_files = get_excel_files_from_monthly_folders(base_path)
df_final_2024 = combine_dataframes(excel_files)


# In[ ]:


base_path = r"Downloads\CitiBike\2023-citibike-tripdata\2023-citibike-tripdata"  
excel_files = get_excel_files_from_monthly_folders(base_path)
df_final_2023 = combine_dataframes(excel_files)


# In[1]:


df_final_2023


# In[8]:


df_final_2024.drop(columns = 'ride_id',inplace = True)


# In[9]:


df_final_2024['started_at'] = pd.to_datetime(df_final_2024['started_at'])
df_final_2024['Month'] = df_final_2024['started_at'].dt.month


# In[10]:


df_final_2024.groupby(['Month'])['started_at'].count()


# In[11]:


df_final_2024.head()


# In[46]:


df_final_2024.groupby(df_final_2024['member_casual'])['rideable_type'].value_counts()


# In[14]:


ride_cnt_2024 = df_final_2024['rideable_type'].value_counts().reset_index()


# In[27]:


df_final_2024[df_final_2024['rideable_type']=='electric_bike']['rideable_type'].count()/df_final_2024['rideable_type'].count()*100


# 56.19 % of rides are electric 

# In[20]:


from collections import Counter

df_same_station = df_final_2024[df_final_2024['start_station_name'] == df_final_2024['end_station_name']]
df_diff_station = df_final_2024[df_final_2024['start_station_name'] != df_final_2024['end_station_name']]

pair_1 = list(zip(df_same_station['start_station_name'], df_same_station['end_station_name']))
pair_2 = list(zip(df_diff_station['start_station_name'], df_diff_station['end_station_name']))

# pair_counts_same = Counter(pair_1)
# pair_counts_same.most_common()


# In[19]:


# pair_counts_diff = Counter(pair_2)
# pair_counts_diff.most_common()


# In[ ]:




