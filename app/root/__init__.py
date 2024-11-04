from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .address_route import address_bp
    from .award_route import award_bp
    from .child_route import child_bp
    from .dismissal_route import dismissal_bp
    from .educator_has_awards_route import educator_has_awards_bp
    from .educator_route import educator_bp
    from .event_route import event_bp
    from .group_route import group_bp
    from .kindergarten_route import kindergarten_bp
    from .salary_route import salary_bp
    from .toy_route import toy_bp

    app.register_blueprint(address_bp)
    app.register_blueprint(award_bp)
    app.register_blueprint(child_bp)
    app.register_blueprint(dismissal_bp)
    app.register_blueprint(educator_has_awards_bp)
    app.register_blueprint(educator_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(kindergarten_bp)
    app.register_blueprint(salary_bp)
    app.register_blueprint(toy_bp)
