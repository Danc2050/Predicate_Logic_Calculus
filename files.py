# https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
# Grant Hulegaard's answer.

def find_file(rel_path):
    import os
    script_dir = os.path.dirname(os.path.abspath(rel_path))
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

def open_file(location, x):
    if(x == 1): location = find_file("Quantifiers and Variables.txt")
    if (x == 2): location = find_file("Predicates and Names.txt")
    if (x == 3): location = find_file("Formation Rules")
    if (x == 4): location = find_file("Refutation Trees.txt")
    if (x == 5): location = find_file("Identity.txt")
    if (x == 7): return()
    f = open(location, 'r')
    for line in f: print(line)

def open_filePC(location, x):
    print(x)
    if (x == 0): location = find_file("Intro PredC")
    if (x == 1): location = find_file("Inference Rules - Universal")
    if (x == 2): location = find_file("Inference Rules - Existential")
    if (x == 3): location = find_file("Inference Rules - Identity")
    if (x == 4): location = find_file("Theorems")
    if (x == 5): return()
    print(location)
    f = open(location, 'r')
    for line in f: print(line)