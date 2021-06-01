from django.http import FileResponse
from jbs_system import settings


def send_file(response):
    print(response.GET["file_url"])
    data = open(str(settings.BASE_DIR) + response.GET["file_url"], 'rb')
    response = FileResponse(data)

    return response
