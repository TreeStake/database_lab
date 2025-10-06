from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import event_controller
from ..domain.event import Event
from flasgger import swag_from

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Get all events',
    'description': 'Returns a list of all events in the system.',
    'responses': {
        200: {
            'description': 'List of events retrieved successfully',
            'content': {
                'application/json': {
                    'example': [
                        {
                            "date": "2023-12-25",
                            "educators_id": 1,
                            "id": 1,
                            "name": "Christmas Party"
                        }
                    ]
                }
            }
        }
    }
})
def get_all_events() -> Response:
    return make_response(jsonify(event_controller.find_all()), HTTPStatus.OK)


@event_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Create a new event',
    'description': 'Creates a new event entry in the database.',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "date": {"type": "string", "format": "date", "example": "2023-12-25"},
                    "educators_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Christmas Party"}
                },
                'required': ['date', 'educators_id', 'name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Event created successfully',
            'examples': {
                'application/json': {
                    "date": "2023-12-25",
                    "educators_id": 1,
                    "id": 1,
                    "name": "Christmas Party"
                }
            }
        },
        400: {'description': 'Invalid input data'}
    }
})
def create_event() -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.CREATED)


@event_bp.route('/<int:event_id>', methods=['GET'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Get event by ID',
    'description': 'Returns an event record by its ID.',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Event retrieved successfully',
            'content': {
                'application/json': {
                    'example': {
                        "date": "2023-12-25",
                        "educators_id": 1,
                        "id": 1,
                        "name": "Christmas Party"
                    }
                }
            }
        },
        404: {'description': 'Event not found'}
    }
})
def get_event(event_id: int) -> Response:
    return make_response(jsonify(event_controller.find_by_id(event_id)), HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['PUT'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Update event by ID',
    'description': 'Replaces all fields of an event record with new data.',
    'parameters': [
        {
            'name': 'event_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the event to update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "date": {"type": "string", "format": "date", "example": "2023-12-25"},
                    "educators_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Christmas Party"}
                },
                'required': ['date', 'educators_id', 'name']
            }
        }
    ],
    'responses': {
        200: {'description': 'Event updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Event not found'}
    }
})
def update_event(event_id: int) -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.update(event_id, event)
    return make_response("event updated", HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Partially update event by ID',
    'description': 'Updates one or more fields of an event record by its ID.',
    'parameters': [
        {
            'name': 'event_id',
            'in': 'path',
            'schema': {'type': 'integer'},
            'required': True,
            'description': 'ID of the event to partially update'
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    "date": {"type": "string", "format": "date", "example": "2023-12-31"},
                    "educators_id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "New Year Party"}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Event partially updated successfully'},
        400: {'description': 'Invalid input data'},
        404: {'description': 'Event not found'}
    }
})
def patch_event(event_id: int) -> Response:
    content = request.get_json()
    event_controller.patch(event_id, content)
    return make_response("event updated", HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Event'],
    'summary': 'Delete event by ID',
    'description': 'Deletes an event record by its ID.',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'schema': {'type': 'integer'}, 'required': True}
    ],
    'responses': {
        200: {'description': 'Event deleted successfully'},
        404: {'description': 'Event not found'}
    }
})
def delete_event(event_id: int) -> Response:
    event_controller.delete(event_id)
    return make_response("event deleted", HTTPStatus.OK)