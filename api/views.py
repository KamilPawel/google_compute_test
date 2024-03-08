from django.conf import settings
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from api.helpers import send_email
from django.http import Http404
import jwt
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from api.serializers import ContactSerializer

from rest_framework.response import Response


class UserAuthView(APIView):
    def get(self, request):
        send_email("balhamboxframes@gmail.com")
        raise Http404()


class ContactAPIView(APIView):
    serializer_class = ContactSerializer

    def post(self, request):
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        return Response(
            {
                "message": "Thank you for your query, we will get back to you as quickly as possible"
            }
        )


class UserAuthVerifyView(APIView):
    def get(self, request, jwt_token=""):
        try:
            decoded_token = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms="HS256"
            )
            print("SUCCESS")

            print(decoded_token)
            email = decoded_token.get("email", "")
            found_user = User.objects.get(username=email)
            print("SUCCESS")
            if found_user:
                login(request, found_user)
                return redirect("/api/admin/")
            print("not success")
            raise Http404()

        except jwt.ExpiredSignatureError as e:
            print(e)
            raise Http404()

        except jwt.InvalidTokenError as e:
            print(e)
            raise Http404()

        except Exception as e:
            print("This is a different error")
            print(e)
            raise Http404()
