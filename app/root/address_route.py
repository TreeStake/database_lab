from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import address_controller
from ..domain.address import Address

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.route('', methods=['GET'])
def get_all_addresses() -> Response:
    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)


@address_bp.route('', methods=['POST'])
def create_address() -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.route('/<int:address_id>', methods=['GET'])
def get_address(address_id: int) -> Response:
    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['PUT'])
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("adress updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['PATCH'])
def patch_address(address_id: int) -> Response:
    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("adress updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['DELETE'])
def delete_address(address_id: int) -> Response:
    address_controller.delete(address_id)
    return make_response("adress deleted", HTTPStatus.OK)