from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import award_controller
from ..domain.award import Award

award_bp = Blueprint('award', __name__, url_prefix='/award')


@award_bp.route('', methods=['GET'])
def get_all_awards() -> Response:
    return make_response(jsonify(award_controller.find_all()), HTTPStatus.OK)


@award_bp.route('', methods=['POST'])
def create_award() -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.create(award)
    return make_response(jsonify(award.put_into_dto()), HTTPStatus.CREATED)


@award_bp.route('/<int:award_id>', methods=['GET'])
def get_award(award_id: int) -> Response:
    return make_response(jsonify(award_controller.find_by_id(award_id)), HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['PUT'])
def update_award(award_id: int) -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.update(award_id, award)
    return make_response("award updated", HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['PATCH'])
def patch_award(award_id: int) -> Response:
    content = request.get_json()
    award_controller.patch(award_id, content)
    return make_response("award updated", HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['DELETE'])
def delete_award(award_id: int) -> Response:
    award_controller.delete(award_id)
    return make_response("award deleted", HTTPStatus.OK)