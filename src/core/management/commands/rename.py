import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # bit of logic to rename project
        # current projects name is stored in settings.PROJECT_NAME
        # open file read data and user replace method to alter file
        files_to_rename = [settings.PROJECT_NAME+'/settings/base.py', settings.PROJECT_NAME+'/wsgi.py', 'manage.py']
        folder_to_rename = settings.PROJECT_NAME

        for f in files_to_rename:
            with open(f, 'r') as file:
                file_data = file.read()

            file_data = file_data.replace(settings.PROJECT_NAME, new_project_name)

            with open(f, 'w') as file:
                file.write(file_data)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))
