from flask import Blueprint, render_template, abort
from app.models import Project, Service

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/')
def index():
    projects = Project.query.order_by(Project.number).all()
    categories = sorted(list(set(p.category for p in projects)))
    return render_template('projects/index.html', projects=projects, categories=categories)

@projects_bp.route('/<slug>')
def detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    related_projects = Project.query.filter(Project.id != project.id, Project.category == project.category).limit(3).all()
    if not related_projects:
        related_projects = Project.query.filter(Project.id != project.id).limit(3).all()

    service = Service.query.filter_by(slug=project.service_slug).first() if project.service_slug else None

    return render_template(
        'projects/detail.html',
        project=project,
        related_projects=related_projects,
        service=service
    )
