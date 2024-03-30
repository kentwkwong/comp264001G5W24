from chalice import Chalice, Response
import chalicelib.cognito_service as cognito
import chalicelib.storage_service as s3
import chalicelib.webscrape_service as comprehend
import json

app = Chalice(app_name='Capabilities')


@app.route('/')
def index():
    s3.reset_tier('kentwkwong@gmail.com')
    with open('../Website/index.html','r') as f:
        html_content = f.read()
    return Response(
        body=html_content,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )

@app.route('/loggedin')
def loggedin():
    authorization_code = app.current_request.query_params['code']
    try:
        # reduce read/write to Cognito
        email = cognito.get_user_email(authorization_code)

        # email = "kentwkwong@gmail.com"
        user = s3.register_user(email)
        with open('../Website/logged_in.html','r') as f:
            html_content = f.read()
        html_content= html_content.replace('${email}', email)
        html_content= html_content.replace('${tier}', str(user['tier']))
        return Response(
            body=html_content,
            status_code=200,
            headers={'Content-Type': 'text/html'}
        )
    except Exception as e:
        print(e)


@app.route('/loggedout')
def loggedout():
    with open('../Website/logged_out.html','r') as f:
        html_content = f.read()
    return Response(
        body=html_content,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )

@app.route('/upgrade_user/{email}', methods=['PUT'])
def upgrade_user(email):
    return s3.upgrade_tier(email)


@app.route('/stockcode/{code}', methods=['PUT'])
def stockcode(code):
    return comprehend.get_content(code)
