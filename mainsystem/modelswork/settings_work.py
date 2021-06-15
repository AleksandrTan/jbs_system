from mainsystem.models import Settings


class SettingsWork:

    @staticmethod
    def is_update_proxy():
        record = Settings.objects.filter(alias="proxy_update").values("is_active")
        return record[0]["is_active"]

    @staticmethod
    def update_active(record_id):
        data = dict()
        record = Settings.objects.get(pk=record_id)
        if record.is_active:
            record.is_active = False
            data["color"] = "red"
            data["text"] = "False"
        else:
            record.is_active = True
            data["color"] = "green"
            data["text"] = "True"
        record.save()

        return data
