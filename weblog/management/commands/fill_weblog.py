import json

from django.core.management import BaseCommand

from weblog.models import WeBlog
from config.settings import BASE_DIR


class Command(BaseCommand):
    weblog_file = f'{BASE_DIR}/weblog_data.json'

    @staticmethod
    def json_read_weblog():
        with open(Command.weblog_file, 'r', encoding='windows-1251') as f:
            weblog_list = json.load(f)
        return weblog_list

    def handle(self, *args, **options):
        WeBlog.objects.all().delete()
        weblog_for_create = []

        for weblog in Command.json_read_weblog():
            weblog_for_create.append(
                WeBlog(title=weblog['fields']['title'],
                       slug=weblog['fields']['slug'],
                       text=weblog['fields']['text'],
                       blog_img=weblog['fields']['blog_img'],
                       date_of_creation=weblog['fields']['date_of_creation'],
                       is_published=weblog['fields']['is_published'],
                       count_of_views=weblog['fields']['count_of_views'])
            )

        WeBlog.objects.bulk_create(weblog_for_create)
