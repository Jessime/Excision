# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 02:18:10 2016

@author: jessime

"""

def split(infile):
    """
    Notes
    -----
    Read down the code as your reading through the file. It's chronological.
    """
    
    sections = {}

    current_section_title = ''
    
    current_section_data = ''
    
    with open(infile) as infile:
        for i, line in enumerate(infile):
            if i == 0:
                sections['title'] = line
            elif i == 3:
                sections['subtitle'] = line
            elif i == 6:
                sections['img'] = line

            #Story
            elif i == 8:
                current_section_title = 'story'
                current_section_data += line
            elif current_section_title == 'story' and line != '---\n':
                current_section_data += line
            elif current_section_title == 'story' and line == '---\n':
                sections['story'] = current_section_data
                current_section_data = ''
                current_section_title = 'task1'
                current_section_data += line
            
            #Task & Hint 1
            elif current_section_title == 'task1' and not line.startswith('**Hint:**'):
                current_section_data += line
            elif current_section_title == 'task1' and line.startswith('**Hint:**'):
                sections['task1'] = current_section_data
                current_section_data = ''
                current_section_title = 'hint1'
                current_section_data += line
            elif current_section_title == 'hint1' and line != '---\n':
                current_section_data += line
            elif current_section_title == 'hint1' and line == '---\n':
                sections['hint1'] = current_section_data
                current_section_data = ''
                current_section_title = 'task2'
                current_section_data += line

            #Task & Hint 2
            elif current_section_title == 'task2' and not line.startswith('**Hint:**'):
                current_section_data += line
            elif current_section_title == 'task2' and line.startswith('**Hint:**'):
                sections['task2'] = current_section_data
                current_section_data = ''
                current_section_title = 'hint2'
                current_section_data += line
            elif current_section_title == 'hint2' and line != '---\n':
                current_section_data += line
            elif current_section_title == 'hint2' and line == '---\n':
                sections['hint2'] = current_section_data
                current_section_data = ''
                current_section_title = 'task3'
                current_section_data += line

            #Task & Hint 3
            elif current_section_title == 'task3' and not line.startswith('**Hint:**'):
                current_section_data += line
            elif current_section_title == 'task3' and line.startswith('**Hint:**'):
                sections['task3'] = current_section_data
                current_section_data = ''
                current_section_title = 'hint3'
                current_section_data += line
            elif current_section_title == 'hint3' and line != '---\n':
                current_section_data += line
            elif current_section_title == 'hint3' and line == '---\n':
                sections['hint3'] = current_section_data
                current_section_data = ''
                current_section_title = 'problem'
                current_section_data += line
            
            #Problem
            elif current_section_title == 'problem':
                current_section_data += line
        sections['problem'] = current_section_data

    return sections
    
def cat():
    pass