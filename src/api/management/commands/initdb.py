from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Запуск действий команды. """

        try:
            User.objects.get(username='admin')
            print('Администратор уже создан.')
        except:
            User.objects.create_superuser('admin', 'admin@admin.com', '123')
