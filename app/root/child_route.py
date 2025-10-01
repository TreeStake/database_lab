from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from, Schema, fields
from ..controller import child_controller
from ..domain.child import Child

child_bp = Blueprint('child', __name__, url_prefix='/child')

class ChildSchema(Schema):
    age = fields.Int(required=True, description="Age of the child")
    group_id = fields.Int(required=True, description="ID of the group")
    kindergarten_id = fields.Int(required=True, description="ID of the kindergarten")
    name = fields.Str(required=True, description="Name of the child")


@child_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Get all children',
    'responses': {
        200: {
            'description': 'List of all children',
            'content': {
                'application/json': {
                    'example': [
                        {"id": 1, "age": 5, "group_id": 1, "kindergarten_id": 1, "name": "Lev"}
                    ]
                }
            }
        }
    }
})
def get_all_children() -> Response:
    return make_response(jsonify(child_controller.find_all()), HTTPStatus.OK)


@child_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Create a new child',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': ChildSchema,
                'example': {"age": 5, "group_id": 1, "kindergarten_id": 1, "name": "Lev"}
            }
        }
    },
    'responses': {
        201: {
            'description': 'Child created',
            'content': {
                'application/json': {
                    'example': {"id": 1, "age": 5, "group_id": 1, "kindergarten_id": 1, "name": "Lev"}
                }
            }
        }
    }
})
def create_child() -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.create(child)
    return make_response(jsonify(child.put_into_dto()), HTTPStatus.CREATED)


@child_bp.route('/<int:child_id>', methods=['GET'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Get child by ID',
    'parameters': [
        {'name': 'child_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the child'}
    ],
    'responses': {
        200: {
            'description': 'Child details',
            'content': {
                'application/json': {
                    'example': {"id": 1, "age": 5, "group_id": 1, "kindergarten_id": 1, "name": "Lev"}
                }
            }
        }
    }
})
def get_child(child_id: int) -> Response:
    return make_response(jsonify(child_controller.find_by_id(child_id)), HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['PUT'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Update child by ID',
    'parameters': [
        {'name': 'child_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the child'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': ChildSchema,
                'example': {"age": 6, "group_id": 1, "kindergarten_id": 1, "name": "Lev Updated"}
            }
        }
    },
    'responses': {
        200: {
            'description': 'Child updated',
            'content': {
                'application/json': {
                    'example': {"id": 1, "age": 6, "group_id": 1, "kindergarten_id": 1, "name": "Lev Updated"}
                }
            }
        }
    }
})
def update_child(child_id: int) -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.update(child_id, child)
    return make_response("child updated", HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Patch child by ID (partial update)',
    'parameters': [
        {'name': 'child_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the child'}
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': ChildSchema,
                'example': {"age": 7}
            }
        }
    },
    'responses': {
        200: {
            'description': 'Child patched',
            'content': {
                'application/json': {
                    'example': {"id": 1, "age": 7, "group_id": 1, "kindergarten_id": 1, "name": "Lev"}
                }
            }
        }
    }
})
def patch_child(child_id: int) -> Response:
    content = request.get_json()
    child_controller.patch(child_id, content)
    return make_response("child updated", HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Delete child by ID',
    'parameters': [
        {'name': 'child_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the child'}
    ],
    'responses': {
        200: {
            'description': 'Child deleted',
            'content': {
                'application/json': {
                    'example': {"message": "child deleted"}
                }
            }
        }
    }
})
def delete_child(child_id: int) -> Response:
    child_controller.delete(child_id)
    return make_response("child deleted", HTTPStatus.OK)