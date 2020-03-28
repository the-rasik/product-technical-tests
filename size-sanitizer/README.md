# Data Engineer Test: Sizes & Variants (Trouva)

## Files

##### trouva_cleanse_demo.py
Main Python File that runs the cleasing scripts for this test.
##### sizes_json.json
The JSON file generated from the sizes Mongo Data Seed (for this test).
##### clean_sizes_json.csv
The final CSV results file generated from the main python script - this demos clean data columns.

## Instructions

- Run the main python file using *python trouva_cleanse_demo.py*

The python file generates the sample CSV File (*clean_sizes_json.csv*) - this demos clean data columns.

## Test Questions / Notes

##### Identify core issues

The main issue here appears to be around uneven labelling - different types of value appear in different keys. This may or may not be currently handled in the front-end - but this non-standardised value set will definitely result in incorrect analytics (for example, mixing age groups with sizes and description).

1. Uneven ‘label’ key in dataset. Examples:

- "label": "6 - 12 months"
- "label": "24"
- "label": "Sand"
- "label": "N"
- "label": "21 / UK 4.5"

2. Uneven ‘filter_label’ key in dataset. Examples:

- "filter_label": "0-1 years"
- "filter_label": "M"

Sometimes filter_label doesn’t appear in a dictionary (this might be on purpose, not sure?):

*{
  "_id": {
    "$oid": "557abe8565950003006ff06c"
  },
  "updated_at": {
    "$date": "2015-06-12T11:12:05.586Z"
  },
  "label": "Teal",
  "created_at": {
    "$date": "2015-06-12T11:12:05.303Z"
  },
  "old_label": [
    "Teal"
  ],
  "__v": 0
}*

##### Outline the strategy you would propose to cleanse the data

1. Discuss these priorities within the Data Team and with other teams (Marketing, Engineering) to decide what the top priority is, by providing this suggestion and seeing if it lines up with what is genuinely needed in the immediate future. Data analysts will play a key role here in providing input, on what they find difficult to analyse and why (e.g. distinguishing between sizes, materials, colours etc.)

2. Look at the current analytical database model to see how data is stored, and re-design it (if necessary) to include any extra fields, modify existing ones (type for example) or remove redundant ones.

3. Decide cleansing priority and assign Data Engineering resources to members of the team to fix them, in an achievable (and fast as possible) timeline.

4. Start the data cleansing process with progress recorded in a Daily Data ‘Stand Up’.

##### Perform a data cleansing operation

For this test exercise, I will be going with looking at the “label” key cleansing for demonstration purposes.

- The first will be a ‘Item Description’ cleanse.
- The second will be a ‘Alphabetical Size’ cleanse for known values.



