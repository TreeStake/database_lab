from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import educator_controller
from ..domain.educator import Educator

educator_bp = Blueprint('educator', __name__, url_prefix='/educator')


@educator_bp.route('', methods=['GET'])
def get_all_educators() -> Response:
    return make_response(jsonify(educator_controller.find_all()), HTTPStatus.OK)


@educator_bp.route('', methods=['POST'])
def create_educator() -> Response:
    content = request.get_json()
    educator = Educator.create_from_dto(content)
    educator_controller.create(educator)
    return make_response(jsonify(educator.put_into_dto()), HTTPStatus.CREATED)


@educator_bp.route('/<int:educator_id>', methods=['GET'])
def get_educator(educator_id: int) -> Response:
    return make_response(jsonify(educator_controller.find_by_id(educator_id)), HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['PUT'])
def update_educator(educator_id: int) -> Response:
    content = request.get_json()
    educator = Educator.create_from_dto(content)
    educator.update(educator_id, educator)
    return make_response("educator updated", HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['PATCH'])
def patch_educator(educator_id: int) -> Response:
    content = request.get_json()
    educator_controller.patch(educator_id, content)
    return make_response("educator updated", HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['DELETE'])
def delete_educator(educator_id: int) -> Response:
    educator_controller.delete(educator_id)
    return make_response("educator deleted", HTTPStatus.OK)