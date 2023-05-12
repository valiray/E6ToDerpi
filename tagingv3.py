import os

# Check if input file exists, otherwise create it
if not os.path.exists('input.txt'):
    with open('input.txt', 'w') as f:
        pass

# Open input file
with open('input.txt', 'r') as input_file:
    # Read the input from input file
    tagging_system_1 = input_file.read()

    # Split the input string by space
    tag_list = tagging_system_1.split()

    # Replace underscores with spaces in each tag
    tag_list = [tag.replace('_', ' ') for tag in tag_list]

    # Join the list of tags with commas and spaces
    tagging_system_2 = ", ".join(tag_list)

# Open output file
with open('output.txt', 'w') as output_file:
    # Write the output to output file
    output_file.write(tagging_system_2)

# Print confirmation message
print('Output written to output.txt')
