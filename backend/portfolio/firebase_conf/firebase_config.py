from django.conf import settings
import firebase_admin


def firebase_init():
    # Firebase configuration
    firebase_credentials = firebase_admin.credentials.Certificate(
        {
            "type": settings.FIREBASE_ACCOUNT_TYPE,
            "project_id": settings.FIREBASE_PROJECT_ID,
            "private_key_id": settings.FIREBASE_PRIVATE_KEY_ID,
            "private_key": settings.FIREBASE_PRIVATE_KEY.replace("\\n", "\n"),
            "client_email": settings.FIREBASE_CLIENT_EMAIL,
            "client_id": settings.FIREBASE_CLIENT_ID,
            "auth_uri": settings.FIREBASE_AUTH_URI,
            "token_uri": settings.FIREBASE_TOKEN_URI,
            "auth_provider_x509_cert_url": settings.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
            "client_x509_cert_url": settings.FIREBASE_CLIENT_X509_CERT_URL,
        }
    )

    cred = firebase_admin.credentials.Certificate(firebase_credentials)
    app = firebase_admin.initialize_app(cred)
    return app
