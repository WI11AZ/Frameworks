from django.db import models

# Create your models here.
def get_cat_dict(self):
    return {
        'knowledge': list(self.knowledge_set.all()),
        'skills': list(self.skill_set.all()),
        'abilities': list(self.ability_set.all()),
        'tasks': list(self.task_set.all()),
    }