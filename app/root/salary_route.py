from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import salary_controller
from ..domain.salary import Salary
from flasgger import swag_from

salary_bp = Blueprint('salary', __name__, url_prefix='/salary')


@salary_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Get all salaries',
    'description': 'Returns a list of all salaries in the system.',
    'responses': {
        200: {
            'description': 'List of salaries retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {
                            "amount": 30000,
                            "experience": "2 years",
                            "id": 1
                        }
                    ]
                }
            }
        }
    }
})
def get_all_salarys() -> Response:
    return make_response(jsonify(salary_controller.find_all()), HTTPStatus.OK)


@salary_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Create a new salary record',
    'description': 'Creates a new salary entry in the database.',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "amount": {"type": "integer", "example": 30000},
                        "experience": {"type": "string", "example": "2 years"}
                    },
                    'required': ['amount', 'experience']
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Salary created successfully',
            'content': {
                'application/json': {
                    'example': {
                        "amount": 30000,
                        "experience": "2 years",
                        "id": 1
                    }
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_salary() -> Response:
    content = request.get_json()
    salary = Salary.create_from_dto(content)
    salary_controller.create(salary)
    return make_response(jsonify(salary.put_into_dto()), HTTPStatus.CREATED)


@salary_bp.route('/<int:salary_id>', methods=['GET'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Get salary by ID',
    'description': 'Returns a salary record by its ID.',
    'parameters': [
        {'name': 'salary_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Salary retrieved successfully',
            'content': {
                'application/json': {
                    'example': {
                        "amount": 30000,
                        "experience": "2 years",
                        "id": 1
                    }
                }
            }
        },
        404: {'description': 'Salary not found'}
    }
})
def get_salary(salary_id: int) -> Response:
    return make_response(jsonify(salary_controller.find_by_id(salary_id)), HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['PUT'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Update salary by ID',
    'description': 'Updates all fields of a salary record by its ID.',
    'parameters': [
        {'name': 'salary_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "amount": {"type": "integer", "example": 35000},
                        "experience": {"type": "string", "example": "3 years"}
                    },
                    'required': ['amount', 'experience']
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Salary updated successfully'},
        400: {'description': 'Invalid input data'}
    }
})
def update_salary(salary_id: int) -> Response:
    content = request.get_json()
    salary = Salary.create_from_dto(content)
    salary_controller.update(salary_id, salary)
    return make_response("salary updated", HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Partially update salary by ID',
    'description': 'Updates one or more fields of a salary record by its ID.',
    'parameters': [
        {'name': 'salary_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "amount": {"type": "integer", "example": 35000},
                        "experience": {"type": "string", "example": "3 years"}
                    }
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Salary partially updated successfully'},
        400: {'description': 'Invalid input data'}
    }
})
def patch_salary(salary_id: int) -> Response:
    content = request.get_json()
    salary_controller.patch(salary_id, content)
    return make_response("salary updated", HTTPStatus.OK)


@salary_bp.route('/<int:salary_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Salary'],
    'summary': 'Delete salary by ID',
    'description': 'Deletes a salary record by its ID.',
    'parameters': [
        {'name': 'salary_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {'description': 'Salary deleted successfully'},
        404: {'description': 'Salary not found'}
    }
})
def delete_salary(salary_id: int) -> Response:
    salary_controller.delete(salary_id)
    return make_response("salary deleted", HTTPStatus.OK)