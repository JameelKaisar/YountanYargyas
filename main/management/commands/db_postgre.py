from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from pathlib import Path

from dotenv import load_dotenv
from os import getenv

class Command(BaseCommand):
    help = "Change Database to PostgreSQL."

    def add_arguments(self, parser):
        parser.add_argument('--name', required=True)
        parser.add_argument('--user', required=True)
        parser.add_argument('--pass', required=True)
        parser.add_argument('--host', default="localhost")
        parser.add_argument('--port', default="")

    def handle(self, *args, **options):
        try:
            # Taking Backup of Existing Database
            backup_time = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
            backup_file_name = "database_backup_" + backup_time + ".json"
            backup_file_path = "backup/partial/" + backup_file_name
            Path("backup/partial/").mkdir(parents=True, exist_ok=True)
            call_command("dumpdata_utf8", output=backup_file_path)

            # Changing Database to PostgreSQL
            load_dotenv()
            SECRET_KEY = str(getenv('SECRET_KEY'))
            with open(".env", "w") as file:
                file.write(f"SECRET_KEY={SECRET_KEY}\nDATABASE_CODE=1\nDATABASE_NAME={options['name']}\nDATABASE_USER={options['user']}\nDATABASE_PASS={options['pass']}\nDATABASE_HOST={options['host']}\nDATABASE_PORT={options['port']}\n")

            # Saving backup_file_path to .tmp file
            with open(".tmp", "w") as file:
                file.write(backup_file_path)
        except Exception as err:
            self.stdout.write("")
            if hasattr(err, '__iter__'):
                for e in err:
                    self.stdout.write(f"{err.__class__.__name__}: {str(e)}")
            else:
                self.stdout.write(f"{err.__class__.__name__}: {str(err)}")
