import re

with open('input.txt', 'r') as input_file:
    input_string = input_file.read().strip() # Read the input string from input.txt and remove leading/trailing whitespaces

tag_list = input_string.split() # Split the input string by space
tag_list = [tag.replace('_', ' ') for tag in tag_list] # Replace underscores with spaces in each tag
tag_list = [re.sub(r'(\d)([a-zA-Z])', r'\1 \2', tag) for tag in tag_list] # Insert space between digits and letters in each tag
tagging_system_2 = ", ".join(tag_list) # Join the list of tags with commas and spaces

with open('output.txt', 'w') as output_file:
    output_file.write(tagging_system_2) # Write the output string to output.txt
