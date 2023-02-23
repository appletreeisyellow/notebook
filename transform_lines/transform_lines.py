# Open the input file
input_file = open("list.txt", 'r')
input_content = input_file.readlines()


def add_quotation(string):
    # e.g. `SELECT` --> `'SELECT',`
    print("\'{}\',".format(row.strip()))


def add_quotation_before_comment(string):
    # e.g. `ADD   // +` --> `'ADD', // +`
    line = row.strip().split('//')
    if len(line) > 1:
        print("\'{}\', //{}".format(line[0].strip(), line[1]))


# Main block
for row in input_content:
    # add_quotation(row)
    add_quotation_before_comment(row)


# Close the input file
input_file.close()
