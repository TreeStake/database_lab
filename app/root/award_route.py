from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from, Schema, fields
from ..controller import award_controller
from ..domain.award import Award

award_bp = Blueprint('award', __name__, url_prefix='/award')

class AwardSchema(Schema):
    money = fields.Int(required=True, description="Amount of money for the award")
    name = fields.Str(required=True, description="Name of the award")

@award_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Get all awards',
    'responses': {
        200: {
            'description': 'List of all awards',
            'content': {
                'application/json': {
                    'example': [
                        {"id": 1, "money": 1000, "name": "Best Teacher"}
                    ]
                }
            }
        }
    }
})
def get_all_awards() -> Response:
    return make_response(jsonify(award_controller.find_all()), HTTPStatus.OK)


@award_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Create a new award',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': AwardSchema,
                'example': {"money": 10000, "name": "Best Teacher"}
            }
        }
    },
    'responses': {
        201: {
            'description': 'Award created',
            'content': {
                'application/json': {
                    'example': {"id": 1, "money": 10000, "name": "Best Teacher"}
                }
            }
        }
    }
})
def create_award() -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.create(award)
    return make_response(jsonify(award.put_into_dto()), HTTPStatus.CREATED)


@award_bp.route('/<int:award_id>', methods=['GET'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Get award by ID',
    'parameters': [
        {'name': 'award_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the award'}
    ],
    'responses': {
        200: {
            'description': 'Award details',
            'content': {
                'application/json': {
                    'example': {"id": 1, "money": 1000, "name": "Best Teacher"}
                }
            }
        }
    }
})
def get_award(award_id: int) -> Response:
    return make_response(jsonify(award_controller.find_by_id(award_id)), HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['PUT'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Update award by ID',
    'parameters': [
        {'name': 'award_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the award'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': AwardSchema,
                'example': {"money": 1500, "name": "Top Teacher"}
            }
        }
    },
    'responses': {
        200: {
            'description': 'Award updated',
            'content': {
                'application/json': {
                    'example': {"id": 1, "money": 1500, "name": "Top Teacher"}
                }
            }
        }
    }
})
def update_award(award_id: int) -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.update(award_id, award)
    return make_response("award updated", HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Patch award by ID',
    'parameters': [
        {'name': 'award_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the award'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': AwardSchema,
                'example': {"money": 2000}
            }
        }
    },
    'responses': {
        200: {
            'description': 'Award patched',
            'content': {
                'application/json': {
                    'example': {"id": 1, "money": 2000, "name": "Best Teacher"}
                }
            }
        }
    }
})
def patch_award(award_id: int) -> Response:
    content = request.get_json()
    award_controller.patch(award_id, content)
    return make_response("award updated", HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Delete award by ID',
    'parameters': [
        {'name': 'award_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the award'}
    ],
    'responses': {
        200: {
            'description': 'Award deleted',
            'content': {
                'application/json': {
                    'example': {"message": "award deleted"}
                }
            }
        }
    }
})
def delete_award(award_id: int) -> Response:
    award_controller.delete(award_id)
    return make_response("award deleted", HTTPStatus.OK)