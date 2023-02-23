# Open the input file
input_file = open("list.txt", 'r')
input_content = input_file.readlines()


def add_quotation(string: str):
    # e.g. `SELECT` --> `'SELECT',`
    print("\'{}\',".format(string.strip()))


def add_quotation_before_comment(string: str):
    # e.g. `ADD   // +` --> `'ADD', // +`
    line = string.strip().split('//')
    if len(line) > 1:
        print("\'{}\', //{}".format(line[0].strip(), line[1]))


def add_quotation_remove_parenthesis(string: str):
    # e.g. `COUNT()` --> `'COUNT',`
    stripped_str = string.strip()
    if stripped_str[-2::] == '()':
        print("\'{}\',".format(stripped_str[:-2]))


# Main block
for row in input_content:
    # add_quotation(row)
    # add_quotation_before_comment(row)
    add_quotation_remove_parenthesis(row)


# Close the input file
input_file.close()
