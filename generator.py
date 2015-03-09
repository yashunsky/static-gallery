#!/usr/bin/python
# -*- coding: utf8 -*-

'''Gallery generator. Creates linked html files with human-readable names
  and an index with previews from tab-separated INPUT'''

from os.path import join

INPUT = 'images.txt'
GALLEY_PAGE = 'gallery_page_template.html'
INDEX = 'index_template.html'
NAVIGATION = 'navigation_template.html'
OUTPUT_PATH = '../gallery'


def create_page(prev, this, next, template, navigation_template, output):
    '''Put all data into page template'''
    prev = '' if prev is None else navigation_template.format(side='left',
                                                              filename=prev['page'],
                                                              image='prev')
    next = '' if next is None else navigation_template.format(side='right',
                                                              filename=next['page'],
                                                              image='next')

    html = template.format(title=this['title'],
                           prev=prev, next=next,
                           filename=this['image'],
                           description=this['description'])
    with open(join(OUTPUT_PATH, this['page']), 'w') as html_file:
        html_file.write(html)

def create_index(images_list, template, output):
    images = ',\n'.join(['"%s"' % image['image'] for image in images_list[1:-1]])
    html = template.replace('{images}', images)
    with open(join(OUTPUT_PATH, 'index.html'), 'w') as html_file:
        html_file.write(html)    

if __name__ == '__main__':
    with open(GALLEY_PAGE, 'r') as template_file:
        gallery_page_template = template_file.read()

    with open(NAVIGATION, 'r') as template_file:
        navigation_template = template_file.read()

    with open(INDEX, 'r') as template_file:
        index_template = template_file.read()


    images = [None]
    with open(INPUT, 'r') as input_file:
        for line in input_file:
            print line.rstrip() # tor debug
            filename, title, description = line.rstrip().split('\t')
            images.append({'image': filename,
                           'page': filename.split('.')[0]+'.html',
                           'title': title,
                           'description': description})
    images.append(None)

    for prev, this, next in zip(images[:-2], images[1:-1], images[2:]):
        create_page(prev, this, next, 
                    gallery_page_template,
                    navigation_template,
                    OUTPUT_PATH)

    create_index(images, index_template, OUTPUT_PATH)
