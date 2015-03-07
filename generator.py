#!/usr/bin/python
# -*- coding: utf8 -*-

'''Gallery generator. Creates linked html files with human-readable names
  and an index with previews from tab-separated INPUT'''

from os.path import join

INPUT = 'images.txt'
GALLEY_PAGE = 'gallery_page_template.html'
OUTPUT_PATH = '../'

PREV_TEMPLATE = '''
   <div style="position: absolute; left: 0px; top: 0px; width:64px; padding: 20px;">
    <a href="{}" style="color: white;">
     <img src="techImages/prev.png" borger="0" width="64" height="64">
    </a>
   </div>
'''

NEXT_TEMPLATE = '''
   <div style="position: absolute; right: 0px; top: 0px; width:64px; padding: 20px;">
    <a href="{}" style="color: white;">
     <img src="techImages/next.png" borger="0" width="64" height="64">
    </a>
   </div>
'''

def create_page(prev, this, next, template, output=OUTPUT_PATH):
    '''Put all data into page template'''
    prev = '' if prev is None else PREV_TEMPLATE.format(prev['page'])
    next = '' if next is None else NEXT_TEMPLATE.format(next['page'])

    html = template.format(title=this['title'],
                           prev=prev, next=next,
                           filename=this['image'],
                           description=this['description'])
    with open(join(OUTPUT_PATH, this['page']), 'w') as html_file:
        html_file.write(html)


if __name__ == '__main__':
    with open(GALLEY_PAGE, 'r') as template_file:
        gallery_page_template = template_file.read()


    images = [None]
    with open(INPUT, 'r') as input_file:
        for line in input_file:
            filename, title, description = line.split('\t')
            images.append({'image': filename,
                           'page': filename.split('.')[0]+'.html',
                           'title': title,
                           'description': description})
    images.append(None)

    for prev, this, next in zip(images[:-2], images[1:-1], images[2:]):
        create_page(prev, this, next, gallery_page_template)
