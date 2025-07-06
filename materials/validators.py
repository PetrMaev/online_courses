from rest_framework import serializers


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'youtube.com' not in tmp_val:
            raise serializers.ValidationError(
                'Запрещено прикреплять в материалы ссылки на сторонние образовательные платформы или личные сайты'
            )
