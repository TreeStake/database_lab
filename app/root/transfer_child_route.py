from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import transfer_child_controller
from ..domain.transfer_child import TransferChild

transfer_child_bp = Blueprint('transfer', __name__, url_prefix='/transfer')


@transfer_child_bp.route('', methods=['GET'])
def get_all_transfers() -> Response:
    return make_response(jsonify(transfer_child_controller.find_all()), HTTPStatus.OK)


@transfer_child_bp.route('', methods=['POST'])
def create_transfer() -> Response:
    content = request.get_json()
    transfer = TransferChild.create_from_dto(content)
    transfer_child_controller.create(transfer)
    return make_response(jsonify(transfer.put_into_dto()), HTTPStatus.CREATED)


@transfer_child_bp.route('/<int:transfer_id>', methods=['GET'])
def get_transfer(transfer_id: int) -> Response:
    return make_response(jsonify(transfer_child_controller.find_by_id(transfer_id)), HTTPStatus.OK)


@transfer_child_bp.route('/<int:transfer_id>', methods=['PUT'])
def update_transfer(transfer_id: int) -> Response:
    content = request.get_json()
    team = TransferChild.create_from_dto(content)
    transfer_child_controller.update(transfer_id, team)
    return make_response("Transfer updated", HTTPStatus.OK)


@transfer_child_bp.route('/<int:transfer_id>', methods=['PATCH'])
def patch_transfer(transfer_id: int) -> Response:
    content = request.get_json()
    transfer_child_controller.patch(transfer_id, content)
    return make_response("Transfer updated", HTTPStatus.OK)


@transfer_child_bp.route('/<int:transfer_id>', methods=['DELETE'])
def delete_transfer(team_id: int) -> Response:
    transfer_child_controller.delete(team_id)
    return make_response("Transfer deleted", HTTPStatus.OK)