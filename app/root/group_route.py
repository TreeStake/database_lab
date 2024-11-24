from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import group_controller
from ..domain.group import Group, create_dynamic_tables_from_groups

group_bp = Blueprint('group', __name__, url_prefix='/group')


@group_bp.route('', methods=['GET'])
def get_all_groups() -> Response:
    return make_response(jsonify(group_controller.find_all()), HTTPStatus.OK)


@group_bp.route('', methods=['POST'])
def create_group() -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.create(group)
    return make_response(jsonify(group.put_into_dto()), HTTPStatus.CREATED)

@group_bp.route('/create_dynamic_tables', methods=['POST'])
def create_tables_endpoint():
    table_names = create_dynamic_tables_from_groups()
    if isinstance(table_names, str):
        return jsonify({"error": table_names}), 404
    return jsonify({"message": f"Tables {', '.join(table_names)} created successfully!"}), 201


@group_bp.route('/<int:group_id>', methods=['GET'])
def get_group(group_id: int) -> Response:
    return make_response(jsonify(group_controller.find_by_id(group_id)), HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['PUT'])
def update_group(group_id: int) -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.update(group_id, group)
    return make_response("group updated", HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['PATCH'])
def patch_group(group_id: int) -> Response:
    content = request.get_json()
    group_controller.patch(group_id, content)
    return make_response("group updated", HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['DELETE'])
def delete_group(group_id: int) -> Response:
    group_controller.delete(group_id)
    return make_response("group deleted", HTTPStatus.OK)