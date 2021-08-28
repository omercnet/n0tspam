from .models import Email
from rest_framework import serializers


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = [
            "html",
            "text",
            "subject",
            "content",
            "to_email",
            "from_email",
            "created_at",
            "spam_report",
        ]
