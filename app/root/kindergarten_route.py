from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import kindergarten_controller
from ..domain.kindergarten import Kindergarten
kindergarten_bp = Blueprint('kindergarten', __name__, url_prefix='/kindergarten')


@kindergarten_bp.route('', methods=['GET'])
def get_all_kindergartens() -> Response:
    return make_response(jsonify(kindergarten_controller.find_all()), HTTPStatus.OK)


@kindergarten_bp.route('', methods=['POST'])
def create_kindergarten() -> Response:
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.create(kindergarten)
    return make_response(jsonify(kindergarten.put_into_dto()), HTTPStatus.CREATED)


@kindergarten_bp.route('/<int:kindergarten_id>', methods=['GET'])
def get_kindergarten(kindergarten_id: int) -> Response:
    return make_response(jsonify(kindergarten_controller.find_by_id(kindergarten_id)), HTTPStatus.OK)


@kindergarten_bp.route('/<int:kindergarten_id>', methods=['PUT'])
def update_kindergarten(kindergarten_id: int) -> Response:
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.update(kindergarten_id, kindergarten)
    return make_response("kindergarten updated", HTTPStatus.OK)


@kindergarten_bp.route('/<int:kindergarten_id>', methods=['PATCH'])
def patch_kindergarten(kindergarten_id: int) -> Response:
    content = request.get_json()
    kindergarten_controller.patch(kindergarten_id, content)
    return make_response("kindergarten updated", HTTPStatus.OK)


@kindergarten_bp.route('/<int:kindergarten_id>', methods=['DELETE'])
def delete_kindergarten(kindergarten_id: int) -> Response:
    kindergarten_controller.delete(kindergarten_id)
    return make_response("kindergarten deleted", HTTPStatus.OK)