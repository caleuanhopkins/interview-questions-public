from django.db import models
from listings.models import Listing

class Assignment(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        help_text="The listing that this assignment relates to",
        related_name="assignments",
    )
