tagging_system_1 = ""
tag_list = tagging_system_1.split() # Split the input string by space
tag_list = [tag.replace('_', ' ') for tag in tag_list] # Replace underscores with spaces in each tag
tagging_system_2 = ", ".join(tag_list) # Join the list of tags with commas and spaces
print(tagging_system_2) # Output: "tag 1, tag 2, tag 3"
