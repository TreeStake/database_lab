from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import educator_controller
from ..domain.educator import Educator
from flasgger import swag_from

educator_bp = Blueprint('educator', __name__, url_prefix='/educator')


@educator_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Get all educators',
    'description': 'Returns a list of all educators in the system.',
    'responses': {
        200: {
            'description': 'List of educators retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {
                            "dismissal_id": None,
                            "educator_awards": [
                                {"id": 1, "money": 1000, "name": "Best Teacher"}
                            ],
                            "events": [
                                {"date": "2023-12-25", "educators_id": 1, "id": 1, "name": "Christmas Party"}
                            ],
                            "hire": "2018-04-10",
                            "id": 1,
                            "kindergarten_id": 1,
                            "name": "Anna",
                            "salary_id": 1,
                            "surname": "Koval"
                        }
                    ]
                }
            }
        }
    }
})
def get_all_educators() -> Response:
    return make_response(jsonify(educator_controller.find_all()), HTTPStatus.OK)


@educator_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Create a new educator',
    'description': 'Creates a new educator entry in the database.',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "dismissal_id": {"type": "integer", "nullable": True, "example": None},
                        "hire": {"type": "string", "format": "date", "example": "2018-04-10"},
                        "id": {"type": "integer", "example": 1},
                        "kindergarten_id": {"type": "integer", "example": 1},
                        "name": {"type": "string", "example": "Anna"},
                        "salary_id": {"type": "integer", "example": 1},
                        "surname": {"type": "string", "example": "Koval"}
                    },
                    'required': ['name', 'surname', 'hire', 'kindergarten_id', 'salary_id']
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Educator created successfully',
            'content': {
                'application/json': {
                    'example': {
                        "dismissal_id": None,
                        "hire": "2018-04-10",
                        "id": 1,
                        "kindergarten_id": 1,
                        "name": "Anna",
                        "salary_id": 1,
                        "surname": "Koval"
                    }
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_educator() -> Response:
    content = request.get_json()
    educator = Educator.create_from_dto(content)
    educator_controller.create(educator)
    return make_response(jsonify(educator.put_into_dto()), HTTPStatus.CREATED)


@educator_bp.route('/<int:educator_id>', methods=['GET'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Get educator by ID',
    'description': 'Returns an educator record by its ID.',
    'parameters': [
        {'name': 'educator_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Educator retrieved successfully',
            'content': {
                'application/json': {
                    'example': {
                        "dismissal_id": None,
                        "educator_awards": [{"id": 1, "money": 1000, "name": "Best Teacher"}],
                        "events": [{"date": "2023-12-25", "educators_id": 1, "id": 1, "name": "Christmas Party"}],
                        "hire": "2018-04-10",
                        "id": 1,
                        "kindergarten_id": 1,
                        "name": "Anna",
                        "salary_id": 1,
                        "surname": "Koval"
                    }
                }
            }
        }
    }
})
def get_educator(educator_id: int) -> Response:
    return make_response(jsonify(educator_controller.find_by_id(educator_id)), HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['PUT'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Update educator by ID',
    'description': 'Updates all fields of an educator record by its ID.',
    'parameters': [
        {'name': 'educator_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "dismissal_id": {"type": "integer", "nullable": True, "example": None},
                        "hire": {"type": "string", "format": "date", "example": "2018-04-10"},
                        "kindergarten_id": {"type": "integer", "example": 1},
                        "name": {"type": "string", "example": "Anna"},
                        "salary_id": {"type": "integer", "example": 1},
                        "surname": {"type": "string", "example": "Koval"}
                    },
                    'required': ['name', 'surname', 'hire', 'kindergarten_id', 'salary_id']
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Educator updated successfully'},
        400: {'description': 'Invalid input data'}
    }
})
def update_educator(educator_id: int) -> Response:
    content = request.get_json()
    educator = Educator.create_from_dto(content)
    educator.update(educator_id, educator)
    return make_response("educator updated", HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Partially update educator by ID',
    'description': 'Updates one or more fields of an educator record by its ID.',
    'parameters': [
        {'name': 'educator_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        "dismissal_id": {"type": "integer", "nullable": True, "example": None},
                        "hire": {"type": "string", "format": "date", "example": "2018-04-10"},
                        "kindergarten_id": {"type": "integer", "example": 1},
                        "name": {"type": "string", "example": "Anna"},
                        "salary_id": {"type": "integer", "example": 1},
                        "surname": {"type": "string", "example": "Koval"}
                    }
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Educator partially updated successfully'},
        400: {'description': 'Invalid input data'}
    }
})
def patch_educator(educator_id: int) -> Response:
    content = request.get_json()
    educator_controller.patch(educator_id, content)
    return make_response("educator updated", HTTPStatus.OK)


@educator_bp.route('/<int:educator_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Educator'],
    'summary': 'Delete educator by ID',
    'description': 'Deletes an educator record by its ID.',
    'parameters': [
        {'name': 'educator_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {'description': 'Educator deleted successfully'},
        404: {'description': 'Educator not found'}
    }
})
def delete_educator(educator_id: int) -> Response:
    educator_controller.delete(educator_id)
    return make_response("educator deleted", HTTPStatus.OK)