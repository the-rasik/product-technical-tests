# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:55:16 2020

@author: Rasik
"""

#Primarily using the pandas library for this cleansing demo
import pandas as pd

#First, reading the JSON file generated from the Mongo Seed (this was done with an external file modification to Parse JSON)
#Storing this to a Pandas Dataframe
df = pd.read_json(r'sizes_json.json')

#Getting a list of all the labels in that column
all_labels = df['label'].tolist()

#Creating new columns to store cleaned data demoed in this script
df['cleanItemDescription'] = ''
df['cleanItemSize'] = ''