from django.core.management.base import BaseCommand
from blogapp.models import IletisimModel

class Command(BaseCommand):
    help = 'Verilen email adresine göre verilen mesajları sil.'

    def add_arguments(self, parser):
        parser.add_argument('--email', help='email adresi giriniz.')
    
    def handle(self, **options):
        if options.get('email') is None:
            IletisimModel.objects.all().delete()
            self.stdout.write("Tüm mesajlar silindi")

        else:
            IletisimModel.objects.filter(email=options.get('email')).delete()
            self.stdout.write('Mesajları silindi:' + options.get('email'))

