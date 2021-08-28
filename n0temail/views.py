import logging

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import EmailSerializer
from .models import RequestLog, Email

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "email/index.html")


def address(request, email_name):
    return render(
        request, "email/address.html", {"email_name": email_name.replace("@", "._.")}
    )


@csrf_exempt
def SendgridWebhookView(request: HttpRequest):
    ret = {"status": "success", "message": "ok"}

    RequestLog(
        data=request.POST, path=request.path, method=request.method, query=request.GET
    ).save()

    if request.method == "POST":
        p = request.POST
        email = Email(
            spf=p.get("SPF"),
            dkim=p.get("dkim"),
            html=p.get("html"),
            text=p.get("text"),
            subject=p.get("subject"),
            headers=p.get("headers"),
            content=p.get("content"),
            to_email=p.get("to"),
            charsets=p.get("charsets"),
            envelope=p.get("envelope"),
            sender_ip=p.get("sender_ip"),
            spam_score=p.get("spam_score"),
            from_email=p.get("from"),
            spam_report=p.get("spam_report"),
        )
        email.save()

        if p.get("attachments"):
            pass

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            p.get("to").replace("@", "._."), {"email": email.pk}
        )

        # ret.update({"post": request.POST, "files": [str(f) for f in request.FILES]})

    logger.debug(ret)
    return JsonResponse(ret)


class EmailViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows emails to be viewed or edited.
    """

    queryset = Email.objects.all().order_by("-created_at")
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]
