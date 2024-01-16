import pip
import sys

"""
insert info and docstrings (ver obsidian personal notes)

"""

try:
    import whois11
except ImportError:
    print('install lybraries...')
    pip.main(['install', 'whois11', '--quiet'])


domain = sys.argv[1]

print(whois11.whois(domain))

