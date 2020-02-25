import sys
import os
from flask_restx import Namespace, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'upload'))


class FileDto:
    api = Namespace('file', description='File Testing Operations')

    file_post_parser = reqparse.RequestParser()
    file_post_parser.add_argument('name', type=str, required=True, help="Name to say hello too :P. Required")
    file_post_parser.add_argument('picture', type=FileStorage, location='files', required=True,
                                  help="Test picture upload")

    @staticmethod
    def get_fobj_path(fobj):
        """
        Return secure filename to save file
        :param werkzeug.datastructures.FileStorage fobj: File object to get name for
        :return: str Filename
        """
        og_filename = secure_filename(fobj.filename)
        dest_fname = os.path.join(UPLOAD_FOLDER, og_filename)
        n = 1
        while os.path.isfile(dest_fname):
            dest_fname = os.path.join(UPLOAD_FOLDER, f"{n}_{og_filename}")
        return dest_fname