# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 02:18:10 2016

@author: jessime

"""
import os
import json

from os.path import join

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
    with open(infile, encoding='utf-8') as infile:
        data = infile.read()
    intermediate_names = ['head', 'problem', 'task1', 'task2', 'task3']
    intermediate_sections = data.split('\n---\n')
    intermediate_sections = dict(zip(intermediate_names, intermediate_sections))
    sections = _head(intermediate_sections['head'])
    sections['problem'] = intermediate_sections['problem'].strip()
    for i in range(1, 4):
        sections = _task(sections, intermediate_sections['task{}'.format(i)], i)
    return sections

def change_log():
    #HACK This is pretty inflexible right now. CHANGELOG may develop

    log = '../CHANGELOG.md'
    with open(log, encoding='utf-8') as log:
        changes = log.read()

    sections = {}
    current_changes = changes.split('\n---\n')[1]
    version, rest = current_changes.split('### Added')
    sections['version'] = version.strip('\n## ')
    sections['added'], sections['fixed'] = rest.split('### Fixed')
    sections = {k:v.strip() for k, v in sections.items()}
    return sections


class Cat():

    def __init__(self):
        self.level_files = [f for f in os.listdir('static/story/') if f.startswith('level')]
        self.outpath_base = 'static/story/{}.md'

    def concatenate(self, section_names, outfile):
        """Concatenates all levels of specific sections of the game into a single file.

        Parameters
        ----------
        section_names : [str]
            Keys for sections to store from each level markdown file.
        outfile : str
            Location of new markdown file.
        """
        with open(self.outpath_base.format(outfile), 'w', encoding='utf-8') as outfile:
            for lf in sorted(self.level_files):
                sections = parse(join('static/story', lf))
                outfile.write('{}'.format(sections['title']) + '\n=====\n\n')
                outfile.write('{}'.format(sections['subtitle'])+ '\n-----\n\n')
                for sn in section_names:
                    outfile.write('{}\n'.format(sections[sn]))

    def story(self, outfile='full_story'):
        self.concatenate(['story'], outfile)

    def tasks(self, outfile='all_tasks'):
        self.concatenate(['task1', 'task2', 'task3'], outfile)

    def problems(self, outfile='all_problems'):
        self.concatenate(['problem'], outfile)

    def titles(self, outfile='all_titles'):
        t_ls = [parse(join('static/story', lf))['title'] for lf in self.level_files]
        json.dump(t_ls, open(self.outpath_base.format(outfile), 'w', encoding='utf-8'))
