from django.db import models


class Tag(models):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    creation_time = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{Tag.name} : {self.content}"
