#!/usr/bin/python
# -*- coding: utf8 -*-

'''It looks like I've lost all previous source generator, and I don't want to rewrite
the text from all files even if it would be faster, then writing this script :)'''

from os import listdir
from os.path import isfile, join

import re

PATH = 'previously_generated'
OUTPUT = 'images.txt'

if __name__ == '__main__':
    with open(OUTPUT, 'w') as txt_file:
        for filename in listdir(PATH):
            full_name = join(PATH, filename)
            if (isfile(full_name) and 
                filename.endswith('html') and
                not filename in ['index.html', 'scripts.html']):
                with open(full_name) as html_file:

                    html = html_file.read().decode('cp1251').encode('utf8')
                    p = re.compile('<title>([^<]+)</title>')
                    title = p.findall(html)[0].lstrip().rstrip()

                    p = re.compile('src="images/original/([^<]+)">')
                    filename = p.findall(html)[0].lstrip().rstrip()

                    p = re.compile('<br>([^<]+)</p>')
                    description = p.findall(html)[0].lstrip().rstrip()
                    txt_file.write('%s\t%s\t%s\n' % (filename, title, description))

                