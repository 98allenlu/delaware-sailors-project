import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from voyages.models import Voyage

class Command(BaseCommand):
    help = 'Loads voyage data from delaware_voyage_records.csv'

    def handle(self, *args, **options):
        # The tutorial states the CSV will be in the 'backend' folder, which is settings.BASE_DIR
        file_path = os.path.join(settings.BASE_DIR, 'delaware_voyage_records.csv')
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found at: {file_path}'))
            self.stdout.write(self.style.ERROR('Please place "delaware_voyage_records.csv" in your "backend" folder (the same folder as manage.py).'))
            return

        self.stdout.write(f'Opening file: {file_path}')
        
        # Clear existing data to avoid duplicates on re-runs
        Voyage.objects.all().delete()
        self.stdout.write('Cleared existing voyage data.')

        count = 0
        # 'utf-8-sig' handles the BOM (Byte Order Mark) that Excel sometimes adds
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Helper function to convert empty strings to None
                def clean(value):
                    return value if value else None

                # Parse date
                date_obj = None
                date_str = clean(row.get('date'))
                if date_str:
                    try:
                        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Could not parse date '{date_str}' for voyageid {row.get('voyageid')}. Skipping date."))
                
                # Handle voyageid - it must exist and be an integer
                voyage_id_str = row.get('voyageid')
                if not voyage_id_str:
                    self.stdout.write(self.style.WARNING(f"Skipping row with empty voyageid."))
                    continue
                try:
                    voyage_id = int(voyage_id_str)
                except ValueError:
                    self.stdout.write(self.style.WARNING(f"Skipping row with invalid voyageid: {voyage_id_str}"))
                    continue

                # Prepare data for the model
                # Note the mapping of 'Source/Database' from the CSV to 'source_database' in the model
                row_data = {
                    'voyageid': voyage_id,
                    'shipname': clean(row.get('shipname')),
                    'captain': clean(row.get('captain')),
                    'date': date_obj,
                    'origin_port': clean(row.get('origin_port')),
                    'destination_port': clean(row.get('destination_port')),
                    'ship_type': clean(row.get('ship_type')),
                    'cargo_summary': clean(row.get('cargo_summary')),
                    'source_database': clean(row.get('Source/Database')), # CSV header mapping
                }

                # Use update_or_create to safely add or update records based on the primary key
                try:
                    obj, created = Voyage.objects.update_or_create(
                        voyageid=row_data['voyageid'],
                        defaults=row_data
                    )
                    if created:
                        count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creating record for voyageid {row_data['voyageid']}: {e}"))

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {count} voyage records.'))

