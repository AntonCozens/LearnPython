from importlib.resources import read_text
from pkgutil import read_code


wikiSource = open('./wiki/templates/lesson_1.template.mediawiki', 'r')
wikiLines = wikiSource.readlines()

for line in wikiLines:
    print(('Line: ' + line)[:-1])