#!/usr/bin/env python

import json
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'legendgen.settings'
from cgen.models import ClassChassis, Race

def main():
    with open('classes.txt') as f:
        classes = json.load(f)['classes']

    for i in classes:
        cc = ClassChassis(name=i['Name'],
                          hp_per_level=i['HP/level'],
                          base_attack_bonus=i['BAB'].title(),
                          kom=i['KOM'].upper(),
                          kdm=i['KDM'].upper(),
                          num_skills=i['Skills'])
        cc.save()

    with open('races.txt') as f:
        races = json.load(f)['races']

    for i in races:
        race = Race(name=i['Name'],
                    size=i['Size'][0].upper())
        race.save()

if __name__ == '__main__':
    main()