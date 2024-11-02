from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import educator_has_award_controller
from ..domain.educator_has_awards import EducatorHasAwards

educator_has_award_bp = Blueprint('educator_award', __name__, url_prefix='/educator-award')


@educator_has_award_bp.route('', methods=['GET'])
def get_all_educator_awards() -> Response:
    return make_response(jsonify(educator_has_award_controller.find_all()), HTTPStatus.OK)


@educator_has_award_bp.route('', methods=['POST'])
def create_educator_award() -> Response:
    content = request.get_json()
    educator_has_award = EducatorHasAwards.create_from_dto(content)
    educator_has_award_controller.create(educator_has_award)
    return make_response(jsonify(educator_has_award.put_into_dto()), HTTPStatus.CREATED)


@educator_has_award_bp.route('/<int:educator_award_id>', methods=['GET'])
def get_educator_award(educator_award_id: int) -> Response:
    return make_response(jsonify(educator_has_award_controller.find_by_id(educator_award_id)), HTTPStatus.OK)


@educator_has_award_bp.route('/<int:educator_award_id>', methods=['PUT'])
def update_educator_award(educator_award_id: int) -> Response:
    content = request.get_json()
    educator_has_award = EducatorHasAwards.create_from_dto(content)
    educator_has_award_controller.update(educator_award_id, educator_has_award)
    return make_response("educator_has_award updated", HTTPStatus.OK)


@educator_has_award_bp.route('/<int:educator_award_id>', methods=['PATCH'])
def patch_educator_award(educator_award_id: int) -> Response:
    content = request.get_json()
    educator_has_award_controller.patch(educator_award_id, content)
    return make_response("educator_has_award updated", HTTPStatus.OK)


@educator_has_award_bp.route('/<int:educator_award_id>', methods=['DELETE'])
def delete_educator_award(educator_award_id: int) -> Response:
    educator_has_award_controller.delete(educator_award_id)
    return make_response("educator_has_award deleted", HTTPStatus.OK)