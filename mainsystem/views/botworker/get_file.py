from django.http import FileResponse
from jbs_system import settings


def send_file(response):
    print(response.GET["name"])
    data = open(str(settings.BASE_DIR) + response.GET["name"], 'rb')
    response = FileResponse(data)

    return response
