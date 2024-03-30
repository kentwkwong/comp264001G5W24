# from flask import request, jsonify
# import requests
import boto3
import requests

# define credentials
client_id = '7bu7si89rrf21h6e117arjake0'
client_secret = 'ifcqd0lurp2aumgvkbcqsnfp7fap2eo2vncu9v1amrj3vn8qoe9'
user_domain = "301242732"
region = "ca-central-1"
redirect_uri = 'http://localhost:8000/loggedin'

def get_user_email(authorization_code):

    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorization_code,
        'redirect_uri': redirect_uri
    }
    token_url = f'https://{user_domain}.auth.{region}.amazoncognito.com/oauth2/token'

    try:
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get('access_token')
            id_token = token_data.get('id_token')
            refresh_token = token_data.get('refresh_token')

            # Use the tokens as needed
            print(">"*50)
            print("Access Token:", access_token)
            print("ID Token:", id_token)
            print("Refresh Token:", refresh_token)
            print(">"*50)
            client = boto3.client('cognito-idp', region_name=region)
            user_info_response = client.get_user(
                AccessToken=access_token
            )
            email = [attr['Value'] for attr in user_info_response['UserAttributes'] if attr['Name'] == 'email'][0]
            return email

        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Error: {e}"
