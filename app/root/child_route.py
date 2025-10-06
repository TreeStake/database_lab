from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import child_controller
from ..domain.child import Child
from flasgger import swag_from

child_bp = Blueprint('child', __name__, url_prefix='/child')


@child_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Get all children',
    'description': 'Returns a list of all children in the system.',
    'responses': {
        200: {
            'description': 'List of children retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {"id": 1, "name": "Lev", "age": 5, "group_id": 1, "kindergarten_id": 1}
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
    'description': 'Creates a new child entry in the database.',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Lev'},
                    'age': {'type': 'integer', 'example': 5},
                    'group_id': {'type': 'integer', 'example': 1},
                    'kindergarten_id': {'type': 'integer', 'example': 1}
                },
                'required': ['name', 'age', 'group_id', 'kindergarten_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Child created successfully',
            'examples': {
                'application/json': {
                    "id": 1,
                    "name": "Lev",
                    "age": 5,
                    "group_id": 1,
                    "kindergarten_id": 1
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
    'description': 'Retrieves a specific child by their unique ID.',
    'parameters': [
        {
            'name': 'child_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the child to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Child retrieved successfully',
            'content': {
                'application/json': {
                    'example': {"id": 1, "name": "Lev", "age": 5, "group_id": 1, "kindergarten_id": 1}
                }
            }
        },
        404: {'description': 'Child not found'}
    }
})
def get_child(child_id: int) -> Response:
    return make_response(jsonify(child_controller.find_by_id(child_id)), HTTPStatus.OK)


@child_bp.route('/<int:child_id>', methods=['PUT'])
@swag_from({
    'tags': ['Child'],
    'summary': 'Update child by ID',
    'description': 'Replaces all fields of a child with new data.',
    'parameters': [
        {
            'name': 'child_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the child to update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Lev Updated'},
                    'age': {'type': 'integer', 'example': 6},
                    'group_id': {'type': 'integer', 'example': 2},
                    'kindergarten_id': {'type': 'integer', 'example': 1}
                },
                'required': ['name', 'age', 'group_id', 'kindergarten_id']
            }
        }
    ],
    'responses': {
        200: {'description': 'Child updated successfully'}
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
    'summary': 'Partially update child by ID',
    'description': 'Updates one or more fields of the child.',
    'parameters': [
        {
            'name': 'child_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the child to update partially'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Partial Update Name'},
                    'age': {'type': 'integer', 'example': 6},
                    'group_id': {'type': 'integer', 'example': 2}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Child partially updated successfully'},
        400: {'description': 'Invalid input data'}
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
    'description': 'Deletes a specific child record by their ID.',
    'parameters': [
        {
            'name': 'child_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the child to delete'
        }
    ],
    'responses': {
        200: {'description': 'Child deleted successfully'},
        404: {'description': 'Child not found'}
    }
})
def delete_child(child_id: int) -> Response:
    child_controller.delete(child_id)
    return make_response("child deleted", HTTPStatus.OK)