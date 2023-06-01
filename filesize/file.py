import os
import subprocess
from tabulate import tabulate

def get_folder_sizes():
    command = 'du -h --max-depth=1 /'  
    result = subprocess.run(command.split(), capture_output=True, text=True)
    

    folders = []
    for line in result.stdout.strip().split('\n'):
        size, folder = line.split('\t')
        folders.append((size, folder))
    

    folders.sort(reverse=True)
    
    return folders

def format_size(size):
    if size.endswith('G'):
        return f'\033[91m{size}\033[0m'  
    elif size.endswith('M'):
        return f'\033[93m{size}\033[0m'  
    elif size.endswith('K'):
        return f'\033[92m{size}\033[0m' 
    else:
        return size

def main():

    folders = get_folder_sizes()
    
    headers = ['Size', 'Folder']
    table = [[format_size(size), folder] for size, folder in folders[:10]]
    print(tabulate(table, headers, tablefmt='fancy_grid'))

if __name__ == '__main__':
    main()
