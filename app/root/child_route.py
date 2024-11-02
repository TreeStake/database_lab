from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import child_controller
from ..domain.child import Child

child_bp = Blueprint('child', __name__, url_prefix='/child')


@child_bp.route('', methods=['GET'])
def get_all_children() -> Response:
    return make_response(jsonify(child_controller.find_all()), HTTPStatus.OK)


@child_bp.route('', methods=['POST'])
def create_child() -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.create(child)
    return make_response(jsonify(child.put_into_dto()), HTTPStatus.CREATED)


@child_bp.route('/<int:child_id>', methods=['GET'])
def get_child(child_id: int) -> Response:
    return make_response(jsonify(child_controller.find_by_id(child_id)), HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['PUT'])
def update_child(child_id: int) -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.update(child_id, child)
    return make_response("child updated", HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['PATCH'])
def patch_child(child_id: int) -> Response:
    content = request.get_json()
    child_controller.patch(child_id, content)
    return make_response("child updated", HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['DELETE'])
def delete_child(child_id: int) -> Response:
    child_controller.delete(child_id)
    return make_response("child deleted", HTTPStatus.OK)