from flask_restplus import Resource
from ..dto.file_dto import FileDto
# from flask import request

api = FileDto.api
file_post_parser = FileDto.file_post_parser


# Note maximum file size accepted is set by
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@api.route('/', methods=['POST'])
class FileTest(Resource):
    @api.doc('File testing operations. Upload and download.')
    @api.expect(file_post_parser)
    def post(self):
        args = file_post_parser.parse_args()
        fobj = args['picture']
        output_path = FileDto.get_fobj_path(fobj)
        fobj.save(output_path)
        return {"file": f"{args['picture']}", "new_path": output_path}

