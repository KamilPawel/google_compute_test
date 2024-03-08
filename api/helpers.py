from datetime import datetime, timedelta
from uuid import uuid4
from django.conf import settings
import jwt


def send_email(email):
    unique_token = str(uuid4())
    exp_time = datetime.utcnow() + timedelta(minutes=10)
    jwt_token = jwt.encode(
        {"uuid": unique_token, "exp": exp_time, "email": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    print(f"Sending {jwt_token} to {email}")
