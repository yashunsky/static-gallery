#!/usr/bin/python
# -*- coding: utf8 -*-

'''Gallery generator. Creates linked html files with human-readable names
  and an index with previews from tab-separated INPUT'''

from os.path import join

INPUT = 'images.txt'
GALLEY_PAGE = 'gallery_page_template.html'
NAVIGATION = 'navigation_template.html'
OUTPUT_PATH = '../'


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


if __name__ == '__main__':
    with open(GALLEY_PAGE, 'r') as template_file:
        gallery_page_template = template_file.read()

    with open(NAVIGATION, 'r') as template_file:
        navigation_template = template_file.read()


    images = [None]
    with open(INPUT, 'r') as input_file:
        for line in input_file:
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
