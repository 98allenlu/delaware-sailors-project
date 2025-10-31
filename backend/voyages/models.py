from django.db import models

class Voyage(models.Model):
    # We will use the 'voyageid' from the CSV as the primary key
    voyageid = models.IntegerField(primary_key=True, help_text="Unique ID from the CSV")
    
    shipname = models.CharField(max_length=255, null=True, blank=True)
    captain = models.CharField(max_length=255, null=True, blank=True)
    
    # Using DateField for the date
    date = models.DateField(null=True, blank=True)
    
    origin_port = models.CharField(max_length=255, null=True, blank=True)
    destination_port = models.CharField(max_length=255, null=True, blank=True)
    ship_type = models.CharField(max_length=100, null=True, blank=True)
    
    # Using TextField for potentially long cargo descriptions
    cargo_summary = models.TextField(null=True, blank=True)
    
    source_database = models.CharField(max_length=255, null=True, blank=True, db_column='Source_Database')

    class Meta:
        db_table = 'voyage'  # Explicitly name the table 'voyage'
        ordering = ['date']  # Order records by date by default

    def __str__(self):
        return f"Voyage {self.voyageid} - {self.shipname} ({self.date})"

