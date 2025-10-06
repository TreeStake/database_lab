from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import toy_controller
from ..domain.toy import Toy
from flasgger import swag_from

toy_bp = Blueprint('toy', __name__, url_prefix='/toy')


@toy_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Get all toys',
    'description': 'Returns a list of all toys in the system.',
    'responses': {
        200: {
            'description': 'List of toys retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {
                            "group_educators_id": 1,
                            "group_id": 1,
                            "group_kindergarten_id": 1,
                            "id": 1,
                            "name": "Ball",
                            "number": "15"
                        }
                    ]
                }
            }
        }
    }
})
def get_all_toys() -> Response:
    return make_response(jsonify(toy_controller.find_all()), HTTPStatus.OK)


@toy_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Create a new toy',
    'description': 'Creates a new toy entry in the database.',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "group_educators_id": {"type": "integer", "example": 1},
                    "group_id": {"type": "integer", "example": 1},
                    "group_kindergarten_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Ball"},
                    "number": {"type": "string", "example": "15"}
                },
                'required': ["group_educators_id", "group_id", "group_kindergarten_id", "name", "number"]
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Toy created successfully',
            'examples': {
                'application/json': {
                    "id": 1,
                    "group_educators_id": 1,
                    "group_id": 1,
                    "group_kindergarten_id": 1,
                    "name": "Ball",
                    "number": "15"
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_toy() -> Response:
    content = request.get_json()
    toy = Toy.create_from_dto(content)
    toy_controller.create(toy)
    return make_response(jsonify(toy.put_into_dto()), HTTPStatus.CREATED)


@toy_bp.route('/<int:toy_id>', methods=['GET'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Get toy by ID',
    'description': 'Returns a toy record by its ID.',
    'parameters': [
        {'name': 'toy_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Toy retrieved successfully',
            'content': {
                'application/json': {
                    'example': {
                        "group_educators_id": 1,
                        "group_id": 1,
                        "group_kindergarten_id": 1,
                        "id": 1,
                        "name": "Ball",
                        "number": "15"
                    }
                }
            }
        },
        404: {'description': 'Toy not found'}
    }
})
def get_toy(toy_id: int) -> Response:
    return make_response(jsonify(toy_controller.find_by_id(toy_id)), HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['PUT'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Update toy by ID',
    'description': 'Updates all fields of a toy record by its ID.',
    'parameters': [
        {
            'name': 'toy_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the toy to update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "group_educators_id": {"type": "integer", "example": 2},
                    "group_id": {"type": "integer", "example": 2},
                    "group_kindergarten_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Cube"},
                    "number": {"type": "string", "example": "10"}
                },
                'required': ["group_educators_id", "group_id", "group_kindergarten_id", "name", "number"]
            }
        }
    ],
    'responses': {
        200: {'description': 'Toy updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Toy not found'}
    }
})
def update_toy(toy_id: int) -> Response:
    content = request.get_json()
    toy = Toy.create_from_dto(content)
    toy_controller.update(toy_id, toy)
    return make_response("toy updated", HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Partially update toy by ID',
    'description': 'Updates one or more fields of a toy record by its ID.',
    'parameters': [
        {
            'name': 'toy_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the toy to partially update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "group_educators_id": {"type": "integer", "example": 2},
                    "group_id": {"type": "integer", "example": 2},
                    "group_kindergarten_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Cube"},
                    "number": {"type": "string", "example": "10"}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Toy partially updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Toy not found'}
    }
})
def patch_toy(toy_id: int) -> Response:
    content = request.get_json()
    toy_controller.patch(toy_id, content)
    return make_response("toy updated", HTTPStatus.OK)


@toy_bp.route('/<int:toy_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Toy'],
    'summary': 'Delete toy by ID',
    'description': 'Deletes a toy record by its ID.',
    'parameters': [
        {'name': 'toy_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {'description': 'Toy deleted successfully'},
        404: {'description': 'Toy not found'}
    }
})
def delete_toy(toy_id: int) -> Response:
    toy_controller.delete(toy_id)
    return make_response("toy deleted", HTTPStatus.OK)