from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from .models import RequestLog, Email


@csrf_exempt
def SendgridWebhookView(request: HttpRequest):
    ret = {"status": "success", "message": "ok"}

    RequestLog(
        data=request.POST, path=request.path, method=request.method, query=request.GET
    ).save()

    if request.method == "POST":
        p = request.POST
        Email(
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
        ).save()

        ret.update({"post": request.POST, "files": request.FILES})

    return JsonResponse(ret)
