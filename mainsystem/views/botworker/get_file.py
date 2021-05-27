from django.http import FileResponse
from jbs_system import settings


def send_file(response):
    print(response.GET["name"])
    img = open(str(settings.BASE_DIR) + '/media/' + response.GET["name"], 'rb')

    response = FileResponse(img)

    return response
