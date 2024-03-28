from chalice import Chalice, Response
from chalice import CognitoUserPoolAuthorizer
app = Chalice(app_name='Capabilities')

authorizer = CognitoUserPoolAuthorizer(
    'MyPool', provider_arns=['arn:aws:cognito-idp:ca-central-1:905418377930:userpool/ca-central-1_p1MezIG2a'],
    scopes=["https://www.youtube.com/"])


@app.route('/')
def index():
    with open('../Website/index.html','r') as f:
        html_content = f.read()
    return Response(
        body=html_content,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )

@app.route('/loggedin')
def loggedin():
    with open('../Website/logged_in.html','r') as f:
        html_content = f.read()
    return Response(
        body=html_content,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )

@app.route('/loggedout')
def loggedout():
    with open('../Website/logged_out.html','r') as f:
        html_content = f.read()
    return Response(
        body=html_content,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )

@app.route('/user-pools', methods=['GET'], authorizer=authorizer)
def authenticated():
    return {"success": True}


@app.route('/stockcode')
def index():
    # obj = webscrape_service()
    # articles = obj.get_content()
    # cleaning = datacleaning_service(articles)
    # dict = cleaing.data_cleanup(cleaning)
    # comp = comprehend_serivce(dict)
    # dict = comp.get_score(dict)
    print()
    # return json{} # depends what information FE needs
    return {"key": "abc", "value":"def123"}

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
