from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import adress_controller
from ..domain.adress import Address

adress_bp = Blueprint('adress', __name__, url_prefix='/adress')


@adress_bp.route('', methods=['GET'])
def get_all_adresses() -> Response:
    return make_response(jsonify(adress_controller.find_all()), HTTPStatus.OK)


@adress_bp.route('', methods=['POST'])
def create_adress() -> Response:
    content = request.get_json()
    adress = Address.create_from_dto(content)
    adress_controller.create(adress)
    return make_response(jsonify(adress.put_into_dto()), HTTPStatus.CREATED)


@adress_bp.route('/<int:adress_id>', methods=['GET'])
def get_adress(adress_id: int) -> Response:
    return make_response(jsonify(adress_controller.find_by_id(adress_id)), HTTPStatus.OK)


@adress_bp.route('/<int:adress_id>', methods=['PUT'])
def update_adress(adress_id: int) -> Response:
    content = request.get_json()
    adress = Address.create_from_dto(content)
    adress_controller.update(adress_id, adress)
    return make_response("adress updated", HTTPStatus.OK)


@adress_bp.route('/<int:adress_id>', methods=['PATCH'])
def patch_adress(adress_id: int) -> Response:
    content = request.get_json()
    adress_controller.patch(adress_id, content)
    return make_response("adress updated", HTTPStatus.OK)


@adress_bp.route('/<int:adress_id>', methods=['DELETE'])
def delete_adress(adress_id: int) -> Response:
    adress_controller.delete(adress_id)
    return make_response("adress deleted", HTTPStatus.OK)