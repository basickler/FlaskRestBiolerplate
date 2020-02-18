from flask_restplus import Namespace, fields  #, reqparse


class TestDto:
    api = Namespace('test', description='Testing Operations')

    # Alternative way to define the inputs... subtle annoying difference from the api.model
    #test_post_reqparse = reqparse.RequestParser(bundle_errors=True)
    #test_post_reqparse.add_argument('name', type=str, location='json', help="Name to say hello too :P. Required")

    test_post_model = api.model(
        'test', {
            'name': fields.String(required=True, location='json', help="Name to say hello too :P. Required")
        })

