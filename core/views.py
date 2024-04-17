from django.http import HttpResponse


def api_status(request):
    return HttpResponse("API is up and running. Visit /admin to manage your data or use Postman to interact with the API.")
