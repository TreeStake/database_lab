from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import dismissal_controller
from ..domain.dismissal import Dismissal
from flasgger import swag_from

dismissal_bp = Blueprint('dismissal', __name__, url_prefix='/dismissal')


@dismissal_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Get all dismissals',
    'description': 'Returns a list of all dismissals in the system.',
    'responses': {
        200: {
            'description': 'List of dismissals retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {"id": 1, "date": "2023-05-12", "reason": "Dismissal"}
                    ]
                }
            }
        }
    }
})
def get_all_dismissals() -> Response:
    return make_response(jsonify(dismissal_controller.find_all()), HTTPStatus.OK)


@dismissal_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Create a new dismissal',
    'description': 'Creates a new dismissal entry in the database.',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'date': {'type': 'string', 'format': 'date', 'example': '2023-05-12'},
                        'reason': {'type': 'string', 'example': 'Dismissal'}
                    },
                    'required': ['date', 'reason']
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Dismissal created successfully',
            'content': {
                'application/json': {
                    'example': {"id": 1, "date": "2023-05-12", "reason": "Dismissal"}
                }
            }
        }
    }
})
def create_dismissal() -> Response:
    content = request.get_json()
    dismissal = Dismissal.create_from_dto(content)
    dismissal_controller.create(dismissal)
    return make_response(jsonify(dismissal.put_into_dto()), HTTPStatus.CREATED)


@dismissal_bp.route('/<int:dismissal_id>', methods=['GET'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Get dismissal by ID',
    'description': 'Returns a dismissal record by its ID.',
    'parameters': [
        {'name': 'dismissal_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Dismissal retrieved successfully',
            'content': {
                'application/json': {
                    'example': {"id": 1, "date": "2023-05-12", "reason": "Dismissal"}
                }
            }
        }
    }
})
def get_dismissal(dismissal_id: int) -> Response:
    return make_response(jsonify(dismissal_controller.find_by_id(dismissal_id)), HTTPStatus.OK)


@dismissal_bp.route('/<int:dismissal_id>', methods=['PUT'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Update dismissal by ID',
    'description': 'Updates all fields of a dismissal record by its ID.',
    'parameters': [
        {'name': 'dismissal_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'date': {'type': 'string', 'format': 'date', 'example': '2023-05-12'},
                        'reason': {'type': 'string', 'example': 'Dismissal'}
                    },
                    'required': ['date', 'reason']
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Dismissal updated successfully'}
    }
})
def update_dismissal(dismissal_id: int) -> Response:
    content = request.get_json()
    dismissal = Dismissal.create_from_dto(content)
    dismissal_controller.update(dismissal_id, dismissal)
    return make_response("dismissal updated", HTTPStatus.OK)


@dismissal_bp.route('/<int:dismissal_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Partially update dismissal by ID',
    'description': 'Updates one or more fields of the dismissal record.',
    'parameters': [
        {
            'name': 'dismissal_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the dismissal to update partially'
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'date': {'type': 'string', 'format': 'date', 'example': '2023-05-20'},
                        'reason': {'type': 'string', 'example': 'New Reason'}
                    }
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Dismissal partially updated successfully'},
        400: {'description': 'Invalid input data'}
    }
})
def patch_dismissal(dismissal_id: int) -> Response:
    content = request.get_json()
    dismissal_controller.patch(dismissal_id, content)
    return make_response("dismissal updated", HTTPStatus.OK)


@dismissal_bp.route('/<int:dismissal_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Dismissal'],
    'summary': 'Delete dismissal by ID',
    'description': 'Deletes a dismissal record by its ID.',
    'parameters': [
        {'name': 'dismissal_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'Dismissal deleted successfully'}
    }
})
def delete_dismissal(dismissal_id: int) -> Response:
    dismissal_controller.delete(dismissal_id)
    return make_response("dismissal deleted", HTTPStatus.OK)