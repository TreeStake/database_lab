from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import address_controller
from ..domain.address import Address
from flasgger import swag_from

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Get all addresses',
    'responses': {
        200: {
            'description': 'List of all addresses',
            'content': {
                'application/json': {
                    'example': [{"id": 1, "street": "Khreshchatyk", "building_number": "12"}]
                }
            }
        }
    }
})
def get_all_addresses() -> Response:
    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)


@address_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Create new address',
    'description': 'Creates a new address entry. Fill in the parameters below to add an address.',
    'parameters': [
        {
            'name': 'street',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Street name (e.g. Chuprynky)'
        },
        {
            'name': 'building_number',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Building number (e.g. 12)'
        }
    ],
    'responses': {
        201: {
            'description': 'Address successfully created',
            'content': {
                'application/json': {
                    'example': {
                        "id": 1,
                        "street": "Chuprynky",
                        "building_number": "12"
                    }
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_address() -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.route('/<int:address_id>', methods=['GET'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Get address by ID',
    'parameters': [
        {
            'name': 'address_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the address'
        }
    ],
    'responses': {
        200: {
            'description': 'Address data',
            'content': {
                'application/json': {
                    'example': {"id": 1, "street": "Khreshchatyk", "building_number": "12"}
                }
            }
        }
    }
})
def get_address(address_id: int) -> Response:
    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['PUT'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Update entire address by ID',
    'description': 'Replaces all address fields with new values.',
    'parameters': [
        {
            'name': 'address_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the address to update'
        },
        {
            'name': 'street',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'New street name'
        },
        {
            'name': 'building_number',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'New building number'
        }
    ],
    'responses': {
        200: {
            'description': 'Address successfully updated',
            'content': {
                'application/json': {
                    'example': {"id": 1, "street": "New Street", "building_number": "15"}
                }
            }
        },
        400: {'description': 'Invalid or missing parameters'}
    }
})
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("adress updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Partially update address by ID',
    'description': 'Allows updating one or more address fields.',
    'parameters': [
        {
            'name': 'address_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the address to patch'
        },
        {
            'name': 'street',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Street name (optional)'
        },
        {
            'name': 'building_number',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Building number (optional)'
        }
    ],
    'responses': {
        200: {
            'description': 'Address partially updated',
            'content': {
                'application/json': {
                    'example': {"id": 1, "street": "Partial Update Street", "building_number": "12"}
                }
            }
        },
        400: {'description': 'No valid parameters provided'}
    }
})
def patch_address(address_id: int) -> Response:
    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("adress updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Address'],
    'summary': 'Delete address by ID',
    'parameters': [
        {'name': 'address_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Address deleted'}}
})
def delete_address(address_id: int) -> Response:
    address_controller.delete(address_id)
    return make_response("adress deleted", HTTPStatus.OK)
