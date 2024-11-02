from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import salary_controller
from ..domain.salary import Salary

salary_bp = Blueprint('salary', __name__, url_prefix='/salary')


@salary_bp.route('', methods=['GET'])
def get_all_salarys() -> Response:
    return make_response(jsonify(salary_controller.find_all()), HTTPStatus.OK)


@salary_bp.route('', methods=['POST'])
def create_salary() -> Response:
    content = request.get_json()
    salary = Salary.create_from_dto(content)
    salary_controller.create(salary)
    return make_response(jsonify(salary.put_into_dto()), HTTPStatus.CREATED)


@salary_bp.route('/<int:salary_id>', methods=['GET'])
def get_salary(salary_id: int) -> Response:
    return make_response(jsonify(salary_controller.find_by_id(salary_id)), HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['PUT'])
def update_salary(salary_id: int) -> Response:
    content = request.get_json()
    salary = Salary.create_from_dto(content)
    salary_controller.update(salary_id, salary)
    return make_response("salary updated", HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['PATCH'])
def patch_salary(salary_id: int) -> Response:
    content = request.get_json()
    salary_controller.patch(salary_id, content)
    return make_response("salary updated", HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['DELETE'])
def delete_salary(salary_id: int) -> Response:
    salary_controller.delete(salary_id)
    return make_response("salary deleted", HTTPStatus.OK)