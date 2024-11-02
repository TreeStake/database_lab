from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import dismissal_controller
from ..domain.dismissal import Dismissal

dismissal_bp = Blueprint('dismissal', __name__, url_prefix='/dismissal')


@dismissal_bp.route('', methods=['GET'])
def get_all_dismissals() -> Response:
    return make_response(jsonify(dismissal_controller.find_all()), HTTPStatus.OK)


@dismissal_bp.route('', methods=['POST'])
def create_dismissal() -> Response:
    content = request.get_json()
    dismissal = Dismissal.create_from_dto(content)
    dismissal_controller.create(dismissal)
    return make_response(jsonify(dismissal.put_into_dto()), HTTPStatus.CREATED)


@dismissal_bp.route('/<int:dismissal_id>', methods=['GET'])
def get_dismissal(dismissal_id: int) -> Response:
    return make_response(jsonify(dismissal_controller.find_by_id(dismissal_id)), HTTPStatus.OK)


@dismissal_bp.route('/<int:dismissal_id>', methods=['PUT'])
def update_dismissal(dismissal_id: int) -> Response:
    content = request.get_json()
    goal = Dismissal.create_from_dto(content)
    dismissal_controller.update(dismissal_id, goal)
    return make_response("dismissal updated", HTTPStatus.OK)


@dismissal_bp.route('/<int:goal_id>', methods=['PATCH'])
def patch_dismissal(dismissal_id: int) -> Response:
    content = request.get_json()
    dismissal_controller.patch(dismissal_id, content)
    return make_response("dismissal updated", HTTPStatus.OK)


@dismissal_bp.route('/<int:goal_id>', methods=['DELETE'])
def delete_dismissal(dismissal_id: int) -> Response:
    dismissal_controller.delete(dismissal_id)
    return make_response("dismissal deleted", HTTPStatus.OK)