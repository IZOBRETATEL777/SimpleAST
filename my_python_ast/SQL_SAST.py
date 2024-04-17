import re

def SQLi_SAST(file_path):
    pattern = re.compile(r"SELECT|UPDATE|DELETE|INSERT.*\+.*'|'.*\+.*SELECT|UPDATE|DELETE|INSERT")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line_no, line in enumerate(lines, 1):
        if pattern.search(line):
            print(f"Potential SQLi vulnerability detected in {file_path} at line {line_no}")


file_to_scan = input("Enter path: ")
SQLi_SAST(file_to_scan)

