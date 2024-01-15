import pip
import sys
import os

"""
SECLIST in:
https://github.com/danielmiessler/SecLists/tree/master
"""

try:
    import requests
except ImportError:
    print('install libraries...')
    pip.main(['install', 'requests', '--quiet'])

site_directories_small = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/raft-small-directories.txt'
site_directories_small_list = []
r_list_dir = requests.get(site_directories_small)

if r_list_dir.status_code == 200:
    site_directories_small_list = r_list_dir.text.split('\n')
else:
    print('Something is wrong here...')

target_success = []
target_fail = []
target_list_len =  len(site_directories_small_list)
text_decorator = '-='

print(f'The total list have {target_list_len} URLs.')
list_analyser = (input('Prees <enter> to analyse the FULL list or enter any number: '))

if list_analyser == '' or list_analyser.isnumeric:
    if list_analyser == '':
        list_analyser = target_list_len
    for i in range (0,int(list_analyser)):

        try:
            domain = 'https://' + sys.argv[1] + '/' + site_directories_small_list[i]
            r = requests.get(domain)
            #verbose mode
            print(f'{i + 1} / {list_analyser}| {text_decorator * 3} {site_directories_small_list[i]} {text_decorator * 3}')
            #print(domain)

            if r.status_code == 200:
                target_success.append(domain)
        except requests.exceptions.ConnectTimeout:
            target_fail.append(domain)

print(f'''
{len(target_success)} urls found.
{len(target_fail)} urls failed.
These sites are successfuly in request:''')

for domain in target_success:
    print(domain)

temp_dir = os.path.join('temp', 'target_fail.txt')

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

with open(temp_dir, 'w') as file:
    # Escrevendo cada elemento da lista em uma nova linha do arquivo
    for line in target_fail:
        file.write(f"{line}\n")

print('Great powers, great responsabilies')