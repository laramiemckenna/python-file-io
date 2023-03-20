import re

def origin_words(file_path, regex_pattern):

    """
    This function is built to find all occurrences of words 
    in a file that match the inputed regex pattern.

    Inputs:
    file_path (str): The path to the file to search for words, 
    thus allowing any file to be used, not just origin.txt
    regex_pattern (str): The pattern that will be searched

    Returns: a list of tuples, which are ordered and unchangeable. 
    """

    with open(file_path, 'r') as file:
        herit_instances = []
        for line_number, line in enumerate(file, start=1):
            for match in re.finditer(regex_pattern, line):
                word = match.group(0)
                herit_instances.append((line_number, word))
    return herit_instances

def make_a_file(file_path, herit_instances):

    """
    This function writes all of the instances of the unit "herit" 
    and their unique line numbers to a file.

    Inputs:
    file_path (str): The path to the file to write the found words to.
    herit_instances (list): a list of tuples, which are ordered and unchangeable. 

    """

    with open(file_path, 'w') as file:
        for line_number, word in herit_instances:
            file.write(f"{line_number}\t{word}\n")

#A Note on the Regex Expression: I was unsure exactly how many forms of heritable, inherit, and inheritance 
#there were in origin.txt, but to reproduce those top ten words, I needed to use the unit "herit,"
# which is what I chose for the regular expression.


if __name__ == '__main__':
    origin_file_path = 'origin.txt'
    output_file = 'instances.txt'
    regex_pattern = re.compile(r'\b\w*herit\w*\b', re.IGNORECASE)
    herit_instances = origin_words(origin_file_path, regex_pattern)
    make_a_file(output_file, herit_instances)
