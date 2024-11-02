from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import toy_controller
from ..domain.toy import Toy

toy_bp = Blueprint('toy', __name__, url_prefix='/toy')


@toy_bp.route('', methods=['GET'])
def get_all_toys() -> Response:
    return make_response(jsonify(toy_controller.find_all()), HTTPStatus.OK)


@toy_bp.route('', methods=['POST'])
def create_toy() -> Response:
    content = request.get_json()
    toy = Toy.create_from_dto(content)
    toy_controller.create(toy)
    return make_response(jsonify(toy.put_into_dto()), HTTPStatus.CREATED)


@toy_bp.route('/<int:toy_id>', methods=['GET'])
def get_toy(toy_id: int) -> Response:
    return make_response(jsonify(toy_controller.find_by_id(toy_id)), HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['PUT'])
def update_toy(toy_id: int) -> Response:
    content = request.get_json()
    toy = Toy.create_from_dto(content)
    toy_controller.update(toy_id, toy)
    return make_response("toy updated", HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['PATCH'])
def patch_toy(toy_id: int) -> Response:
    content = request.get_json()
    toy_controller.patch(toy_id, content)
    return make_response("toy updated", HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['DELETE'])
def delete_toy(toy_id: int) -> Response:
    toy_controller.delete(toy_id)
    return make_response("toy deleted", HTTPStatus.OK)