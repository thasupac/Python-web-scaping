data_list = [
    '\nvirtusaconsultingservicespvt.ltd.\n\n',
    '\n\ndataanalysis,communication,problemsolving,microsoftoffice,visualizationtools,dataanalytics,dataanalyst,sql,tableau,writtencommunication\n\n',
    'Posted few days ago'
]

# Initialize an empty list to hold the results
split_data_list = []

# Iterate through each item in the original list
for item in data_list:
    # Split the item by '\n' and extend the result list with the split lines
    lines = item.split('\n')
    split_data_list.extend(lines)

# Remove empty strings that may result from splitting
split_data_list = [line for line in split_data_list if line.strip()]

# Print the final list with each line as a separate element
print(split_data_list[0])