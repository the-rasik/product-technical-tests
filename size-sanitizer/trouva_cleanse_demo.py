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

#Our first cleansing function to populate the cleanItemDescription column
def itemDescriptionCleanse():
    
    #This sets loop variables - the current row and the total dataframe row count
    dfRowLoop = 0
    dfRowCount = len(df.index)
    
    #Iterate over each dataframe row
    while dfRowLoop < dfRowCount:
        
        #Get the current 'label' column value for that row
        #Convert this to lowercase - this is to help filtering
        currentRowLabel = all_labels[dfRowLoop].lower()
        
        #Check if the current row value for 'label' is alphabetical
        #>1 character (labels like 'A','B','L','S' etc...is this is an item classification, as well as size? To be checked)
        if currentRowLabel.isalpha() and len(currentRowLabel) > 1:
            
            #This is a list of confidently known sizes (based on unique search of label column)
            #Note: I'm not sure if 'xss' amd 'xx' which were found are sizes or descriptions, left out for now
            itemSizes = ['small', 'xsmall', 'xxsmall', 'xs', 'xxs', 
                         'medium', 
                         'large', 'xlarge', 'xxlarge', 'xl', 'xxl', 'xxxl']
            
            #Remove confidently known size values
            if currentRowLabel not in itemSizes:
            
                #If it meets above conditions, populate new column with this after capitalising first letter
                df.loc[dfRowLoop,"cleanItemDescription"] = currentRowLabel.title()
            
        #Loop + 1 to go to the next row
        dfRowLoop+=1

#Our second cleansing function to populate the cleanItemSize column
def itemSizeCleanse():
    
    #This sets loop variables - the current row and the total dataframe row count
    dfRowLoop = 0
    dfRowCount = len(df.index)
    
    #Iterate over each dataframe row
    while dfRowLoop < dfRowCount:
        
        #Get the current 'label' column value for that row
        #Convert this to lowercase - this is to help filtering
        currentRowLabel = all_labels[dfRowLoop].lower()
        
        #Check if the current row value for 'label' is alphabetical
        if currentRowLabel.isalpha():
            
            #This is a list of confidently known sizes (based on unique search of label column)
            #Note: I'm not sure if 'xss' amd 'xx' which were found are sizes or descriptions, left out for now
            itemSizes = ['small', 'xsmall', 'xxsmall', 'xs', 'xxs', 
                         'medium', 
                         'large', 'xlarge', 'xxlarge', 'xl', 'xxl', 'xxxl']
            
            #Keep confidently known size values
            if currentRowLabel in itemSizes:
            
                #If it meets above conditions, populate new column with this after capitalising all letters
                df.loc[dfRowLoop,"cleanItemSize"] = currentRowLabel.upper()
            
        #Loop + 1 to go to the next row
        dfRowLoop+=1
        
#This is a simple test to check the DataFrame is not empty
#Multiple tests can be written for a full version
def test_dfsize():
    assert len(df.index) > 0, "DataFrame is Empty. Test Failed"

#Run it all, does so if tests pass
if __name__ == "__main__":
    
    test_dfsize()
    print("DataFrame has "+str(len(df.index))+" rows. Test passed.")
    
    print("Cleansing Item Description data...")
    
    #Call the first cleanse (Item Description)
    itemDescriptionCleanse()
    
    print("Cleansing Item Size data...")
    #Call the second cleanse (Item Size)
    itemSizeCleanse()
    
    print("Generating demo CSV file for this technical test...")
    
    #Generating a CSV for this test - to show the results      
    csvFilename = 'clean_sizes_json.csv'
    df.to_csv(csvFilename, index_label = 'rownum' )
    
    print("Success! Check '"+csvFilename+"' for test results (the cleanItemDescription and cleanItemSize columns).")
