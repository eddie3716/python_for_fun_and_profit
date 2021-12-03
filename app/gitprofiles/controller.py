from flask import Blueprint
from flask import Response

bp = Blueprint("gitprofiles", __name__)


@bp.route("/v1/")
def get():
    return Response(200)