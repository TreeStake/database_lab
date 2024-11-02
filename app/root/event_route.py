from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import event_controller
from ..domain.event import Event

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('', methods=['GET'])
def get_all_events() -> Response:
    return make_response(jsonify(event_controller.find_all()), HTTPStatus.OK)


@event_bp.route('', methods=['POST'])
def create_event() -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.CREATED)


@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id: int) -> Response:
    return make_response(jsonify(event_controller.find_by_id(event_id)), HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id: int) -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.update(event_id, event)
    return make_response("event updated", HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['PATCH'])
def patch_event(event_id: int) -> Response:
    content = request.get_json()
    event_controller.patch(event_id, content)
    return make_response("event updated", HTTPStatus.OK)


@event_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id: int) -> Response:
    event_controller.delete(event_id)
    return make_response("event deleted", HTTPStatus.OK)