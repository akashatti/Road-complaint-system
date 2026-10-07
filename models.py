from django.db import models


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    problem = models.CharField(max_length=100)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Reported', 'Reported'),
        ('In Progress', 'In Progress'),
        ('Fixed', 'Fixed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Reported'
    )

    def __str__(self):
        return self.location