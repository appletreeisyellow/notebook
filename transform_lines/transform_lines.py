# Open the input file
input_file = open("list.txt", 'r')
input_content = input_file.readlines()

for row in input_content:
    print("\'{}\',".format(row.strip()))  # e.g. SELECT --> 'SELECT',

# Close the input file
input_file.close()
