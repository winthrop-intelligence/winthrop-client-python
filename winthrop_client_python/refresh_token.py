import requests
import time

class WinthropClient:
    class RefreshToken:
        _token = None
        _expires_at = None

        TOKEN_GRANT_TYPE = 'client_credentials'
        CONTENT_TYPE = 'application/x-www-form-urlencoded'

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
            headers = {
                'Content-Type': cls.CONTENT_TYPE
            }
            data = cls._token_params()
            response = requests.post(cls.host, headers=headers, data=data)
            return response

        @classmethod
        def _token_params(cls):
            return {
                'grant_type': cls.TOKEN_GRANT_TYPE,
                'client_id': cls.client_id,
                'client_secret': cls.client_secret
            }

        @classmethod
        def _handle_response(cls, response):
            if response.status_code == 200:
                parsed_response = response.json()
                cls._token = parsed_response['access_token']
                expires_in = int(parsed_response['expires_in'])
                cls._expires_at = time.time() + expires_in
            else:
                raise Exception('Failed to retrieve access token')