import urllib3
import json
import time


class WinthropClient:
    class RefreshToken:
        _token = None
        _expires_at = None

        TOKEN_GRANT_TYPE = "client_credentials"
        CONTENT_TYPE = "application/x-www-form-urlencoded"

        client_id = None
        client_secret = None
        host = None

        @classmethod
        def access_token(cls):
            if cls._token is None or time.time() >= cls._expires_at:
                cls._generate_access_token()
            return cls._token

        @classmethod
        def _generate_access_token(cls):
            response = cls._make_request()
            cls._handle_response(response)

        @classmethod
        def _make_request(cls):
            http = urllib3.PoolManager()
            headers = {"Content-Type": cls.CONTENT_TYPE}
            data = cls._token_params()
            encoded_data = urllib3.request.encode_url(data)

            response = http.request(
                "POST", cls.host, headers=headers, body=encoded_data
            )
            return response

        @classmethod
        def _token_params(cls):
            return {
                "grant_type": cls.TOKEN_GRANT_TYPE,
                "client_id": cls.client_id,
                "client_secret": cls.client_secret,
            }

        @classmethod
        def _handle_response(cls, response):
            if response.status == 200:
                parsed_response = json.loads(response.data.decode("utf-8"))
                cls._token = parsed_response["access_token"]
                expires_in = int(parsed_response["expires_in"])
                cls._expires_at = time.time() + expires_in
            else:
                raise Exception(
                    f"Failed to retrieve access token: {response.status} - {response.data.decode('utf-8')}"
                )
