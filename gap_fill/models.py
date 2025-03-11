from django.db import models

class GapFillText(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text

class GapFillOption(models.Model):
    gap_fill_parent = models.ForeignKey(GapFillText, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=40)
    valid_positions_str = models.CharField(max_length=100)
    def __str__(self):
        return self.option_text