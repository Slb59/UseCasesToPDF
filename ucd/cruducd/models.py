from django.db import models


class Functionality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Story(models.Model):
    description = models.CharField(max_length=300)
    functionality = models.ForeignKey(
        Functionality, blank=True, null=True, on_delete=models.CASCADE
        )

    def __str__(self) -> str:
        return self.description


class Scenario(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    story = models.ForeignKey(
        Story, blank=True, null=True, on_delete=models.CASCADE
        )

    def __str__(self) -> str:
        return self.title
