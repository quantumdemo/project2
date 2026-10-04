from flask import Blueprint, render_template, abort
from app.models import Service, Project, Industry

services_bp = Blueprint('services', __name__, url_prefix='/services')

@services_bp.route('/')
def index():
    services = Service.query.order_by(Service.number).all()
    return render_template('services/index.html', services=services)

@services_bp.route('/<slug>')
def detail(slug):
    service = Service.query.filter_by(slug=slug).first_or_404()
    related_projects = Project.query.filter_by(service_slug=slug).all()
    all_industries = Industry.query.all()
    related_industries = [ind for ind in all_industries if ind.relevant_service_slugs and slug in ind.relevant_service_slugs]
    return render_template(
        'services/detail.html',
        service=service,
        related_projects=related_projects,
        related_industries=related_industries
    )
