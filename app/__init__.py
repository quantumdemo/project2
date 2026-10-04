from flask import Flask
from config import Config
from app.extensions import db, csrf
from app.seed_data import seed_database

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.services import services_bp
    from app.routes.projects import projects_bp
    from app.routes.contact import contact_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)

    # Context processors and global variables
    @app.context_processor
    def inject_global_data():
        from app.models import Service
        services = Service.query.order_by(Service.number).all()
        return {
            'nav_services': services,
            'demo_phone': '+234 (0) 1 234 5678',
            'demo_email': 'contact@primecore-demo.com',
            'demo_address': 'Industrial Zone, Ikeja, Lagos, Nigeria'
        }

    # Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        from flask import render_template
        return render_template('pages/404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        from flask import render_template
        return render_template('pages/500.html'), 500

    # Auto-create tables and seed data in dev/sqlite environment
    with app.app_context():
        db.create_all()
        try:
            seed_database(db)
        except Exception as e:
            app.logger.error(f"Error seeding database: {e}")

    return app
