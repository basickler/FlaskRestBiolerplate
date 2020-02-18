from flask import request
from flask_restplus import Resource, reqparse, Namespace, fields
from ..dto.test_dto import TestDto
#from ..service.user_service import save_new_user, get_all_users, get_a_user

api = TestDto.api


@api.route('/')
class Hello(Resource):
    @api.doc('Just a super easy get test')
    def get(self):
        """Hello World Test"""
        return ["Hello World"]

    @api.expect(TestDto.test_post_model, validate=True)
    def post(self):
        all_params = request.json
        name = all_params['name']
        return f"Hello {name}"
