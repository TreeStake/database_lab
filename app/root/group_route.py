from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import group_controller
from ..domain.group import Group
from flasgger import swag_from

group_bp = Blueprint('group', __name__, url_prefix='/group')


@group_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Get all groups',
    'description': 'Returns a list of all groups in the system.',
    'responses': {
        200: {
            'description': 'List of groups retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {
                            "amount": "20",
                            "children": [
                                {
                                    "age": 5,
                                    "group_id": 1,
                                    "id": 1,
                                    "kindergarten_id": 1,
                                    "name": "Lev"
                                }
                            ],
                            "educators_id": 1,
                            "id": 1,
                            "kindergarten_id": 1,
                            "name": "Stars",
                            "toys": [
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
                    ]
                }
            }
        }
    }
})
def get_all_groups() -> Response:
    return make_response(jsonify(group_controller.find_all()), HTTPStatus.OK)


@group_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Create a new group',
    'description': 'Creates a new group entry in the database.',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "amount": {"type": "string", "example": "20"},
                    "educators_id": {"type": "integer", "example": 1},
                    "kindergarten_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Stars"}
                },
                'required': ['amount', 'educators_id', 'kindergarten_id', 'name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Group created successfully',
            'examples': {
                'application/json': {
                    "amount": "20",
                    "children": None,
                    "educators_id": 1,
                    "kindergarten_id": 1,
                    "name": "Stars",
                    "toys": None
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_group() -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.create(group)
    return make_response(jsonify(group.put_into_dto()), HTTPStatus.CREATED)


@group_bp.route('/<int:group_id>', methods=['GET'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Get group by ID',
    'description': 'Returns a group record by its ID.',
    'parameters': [
        {'name': 'group_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Group retrieved successfully',
            'content': {
                'application/json': {
                    'example': {
                        "amount": "20",
                        "children": [
                            {"age": 5, "group_id": 1, "id": 1, "kindergarten_id": 1, "name": "Lev"}
                        ],
                        "educators_id": 1,
                        "id": 1,
                        "kindergarten_id": 1,
                        "name": "Stars",
                        "toys": [
                            {"group_educators_id": 1, "group_id": 1, "group_kindergarten_id": 1, "id": 1, "name": "Ball", "number": "15"}
                        ]
                    }
                }
            }
        },
        404: {'description': 'Group not found'}
    }
})
def get_group(group_id: int) -> Response:
    return make_response(jsonify(group_controller.find_by_id(group_id)), HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['PUT'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Update group by ID',
    'description': 'Replaces all fields of a group record with new data.',
    'parameters': [
        {
            'name': 'group_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the group to update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "amount": {"type": "string", "example": "20"},
                    "educators_id": {"type": "integer", "example": 1},
                    "kindergarten_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Stars"}
                },
                'required': ['amount', 'educators_id', 'kindergarten_id', 'name']
            }
        }
    ],
    'responses': {
        200: {'description': 'Group updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Group not found'}
    }
})
def update_group(group_id: int) -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.update(group_id, group)
    return make_response("group updated", HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Partially update group by ID',
    'description': 'Updates one or more fields of a group record by its ID.',
    'parameters': [
        {
            'name': 'group_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the group to partially update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "amount": {"type": "string", "example": "25"},
                    "name": {"type": "string", "example": "Stars Updated"},
                    "kindergarten_id": {"type": "integer", "example": 1},
                    "educators_id": {"type": "integer", "example": 2}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Group partially updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Group not found'}
    }
})
def patch_group(group_id: int) -> Response:
    content = request.get_json()
    group_controller.patch(group_id, content)
    return make_response("group updated", HTTPStatus.OK)


@group_bp.route('/<int:group_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Group'],
    'summary': 'Delete group by ID',
    'description': 'Deletes a group record by its ID.',
    'parameters': [
        {'name': 'group_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {'description': 'Group deleted successfully'},
        404: {'description': 'Group not found'}
    }
})
def delete_group(group_id: int) -> Response:
    group_controller.delete(group_id)
    return make_response("group deleted", HTTPStatus.OK)