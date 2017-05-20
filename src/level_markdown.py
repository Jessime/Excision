# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 02:18:10 2016

@author: jessime

"""
import os

def _head(data):
    line_map = {0: 'title', 3: 'subtitle', 6: 'img'}
    data = data.split('\n')
    sections = {v:data[k] for k,v in line_map.items()}
    sections['story'] = '\n'.join(data[8:])
    return sections

def _task(sections, data, i):
    splitter = '#### Hint\n'
    task_hint = data.split(splitter)
    sections['task{}'.format(i)] = task_hint[0]
    sections['hint{}'.format(i)] = splitter + task_hint[1].strip()
    return sections

def parse(infile):
    with open(infile) as infile:
        data = infile.read()
    intermediate_names = ['head', 'problem', 'task1', 'task2', 'task3']
    intermediate_sections = data.split('\n---\n')
    intermediate_sections = dict(zip(intermediate_names, intermediate_sections))
    sections = _head(intermediate_sections['head'])
    sections['problem'] = intermediate_sections['problem'].strip()
    for i in range(1, 4):
        sections = _task(sections, intermediate_sections['task{}'.format(i)], i)
    return sections

def cat_story():
    level_files = [f for f in os.listdir('static/story/') if f.startswith('level')]

    with open('static/story/full_story.md', 'w') as outfile:
        for lf in sorted(level_files):
            sections = parse(os.path.join('static/story', lf))
            outfile.write('{}'.format(sections['title']))
            outfile.write('=====\n\n')
            outfile.write('{}'.format(sections['subtitle']))
            outfile.write('-----\n\n')
            outfile.write('{}\n'.format(sections['story']))
