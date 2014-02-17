from django.db import models

ATT_VALUES = (
        ('STR', 'Strength'),
        ('CON', 'Constitution'),
        ('DEX', 'Dexterity'),
        ('INT', 'Intelligence'),
        ('WIS', 'Wisdom'),
        ('CHA', 'Charisma'),
)

SIZE_VALUES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
)


class ClassChassis(models.Model):
    BAB_VALUES = (
        ('G', 'Good'),
        ('P', 'Poor'),
    )

    name = models.CharField(max_length=200)
    hp_per_level = models.SmallIntegerField(default=0)
    base_attack_bonus = models.CharField(max_length=1, choices=BAB_VALUES, default='P')
    kom = models.CharField(max_length=3, choices=ATT_VALUES, default='STR')
    kdm = models.CharField(max_length=3, choices=ATT_VALUES, default='STR')
    num_skills = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=1, choices=SIZE_VALUES, default='M')

    def __str__(self):
        return self.name


class Character(models.Model):
    cname = models.CharField(max_length=200)
    pname = models.CharField(max_length=200)
    class_chassis = models.ForeignKey(ClassChassis)
    race = models.ForeignKey(Race)

    str = models.SmallIntegerField(default=10)
    con = models.SmallIntegerField(default=10)
    dex = models.SmallIntegerField(default=10)
    int = models.SmallIntegerField(default=10)
    wis = models.SmallIntegerField(default=10)
    cha = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.cname
