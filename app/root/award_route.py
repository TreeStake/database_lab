from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import award_controller
from ..domain.award import Award
from flasgger import swag_from

award_bp = Blueprint('award', __name__, url_prefix='/award')

@award_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Get all awards',
    'description': 'Returns a list of all available awards.',
    'responses': {
        200: {
            'description': 'List of awards',
            'examples': {
                'application/json': [
                    {"id": 1, "money": 1000, "name": "Best Teacher"},
                    {"id": 2, "money": 500, "name": "Best Student"}
                ]
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
    'description': 'Creates a new award and returns its data.',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'money': {
                        'type': 'integer',
                        'description': 'Amount of money for the award',
                        'example': 1000
                    },
                    'name': {
                        'type': 'string',
                        'description': 'Name of the award',
                        'example': 'Best Teacher'
                    }
                },
                'required': ['money', 'name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Award created successfully',
            'examples': {
                'application/json': {"id": 1, "money": 1000, "name": "Best Teacher"}
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
    'description': 'Returns award details for a given ID.',
    'parameters': [
        {
            'name': 'award_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the award'
        }
    ],
    'responses': {
        200: {
            'description': 'Award found',
            'examples': {
                'application/json': {"id": 1, "money": 1000, "name": "Best Teacher"}
            }
        },
        404: {'description': 'Award not found'}
    }
})
def get_award(award_id: int) -> Response:
    return make_response(jsonify(award_controller.find_by_id(award_id)), HTTPStatus.OK)


@award_bp.route('/<int:award_id>', methods=['PUT'])
@swag_from({
    'tags': ['Award'],
    'summary': 'Update an award by ID',
    'description': 'Replaces all fields of an existing award.',
    'parameters': [
        {
            'name': 'award_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the award to update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'money': {
                        'type': 'integer',
                        'description': 'Updated amount of money',
                        'example': 1500
                    },
                    'name': {
                        'type': 'string',
                        'description': 'Updated award name',
                        'example': 'Top Mentor'
                    }
                },
                'required': ['money', 'name']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Award updated successfully',
            'examples': {
                'application/json': {"id": 1, "money": 1500, "name": "Top Mentor"}
            }
        },
        404: {'description': 'Award not found'}
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
    'summary': 'Partially update award by ID',
    'description': 'Updates one or more fields of an award.',
    'parameters': [
        {
            'name': 'award_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the award to patch'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'money': {
                        'type': 'integer',
                        'description': 'New money value (optional)',
                        'example': 1200
                    },
                    'name': {
                        'type': 'string',
                        'description': 'New name (optional)',
                        'example': 'Honorary Mention'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Award partially updated',
            'examples': {
                'application/json': {"id": 1, "money": 1200, "name": "Honorary Mention"}
            }
        },
        404: {'description': 'Award not found'}
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
    'description': 'Deletes an award by its ID.',
    'parameters': [
        {
            'name': 'award_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the award to delete'
        }
    ],
    'responses': {
        200: {'description': 'Award deleted successfully'},
        404: {'description': 'Award not found'}
    }
})
def delete_award(award_id: int) -> Response:
    award_controller.delete(award_id)
    return make_response("award deleted", HTTPStatus.OK)