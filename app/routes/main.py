from flask import Blueprint, render_template, send_from_directory, current_app, Response
from app.models import Service, Project, Industry
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    services = Service.query.order_by(Service.number).all()
    featured_projects = Project.query.filter_by(featured=True).all()
    industries = Industry.query.all()
    return render_template(
        'pages/index.html',
        services=services,
        featured_projects=featured_projects,
        industries=industries
    )

@main_bp.route('/about')
def about():
    return render_template('pages/about.html')

@main_bp.route('/industries')
def industries():
    all_industries = Industry.query.all()
    return render_template('pages/industries.html', industries=all_industries)

@main_bp.route('/company-profile')
def company_profile():
    return render_template('pages/company_profile.html')

@main_bp.route('/company-profile/download')
def download_company_profile():
    doc_dir = os.path.join(current_app.root_path, 'static', 'documents')
    filename = 'primecore-company-profile.pdf'
    return send_from_directory(doc_dir, filename, as_attachment=True)

@main_bp.route('/robots.txt')
def robots():
    content = "User-agent: *\nAllow: /\nSitemap: " + current_app.config.get('SITE_URL', 'https://primecore.afixtech.demo') + "/sitemap.xml\n"
    return Response(content, mimetype='text/plain')

@main_bp.route('/sitemap.xml')
def sitemap():
    services = Service.query.all()
    projects = Project.query.all()

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Static pages
    static_endpoints = [
        ('main.index', 1.0),
        ('main.about', 0.8),
        ('services.index', 0.9),
        ('main.industries', 0.8),
        ('projects.index', 0.9),
        ('main.company_profile', 0.8),
        ('contact.index', 0.9)
    ]

    from flask import url_for
    for endpoint, priority in static_endpoints:
        xml.append('  <url>')
        xml.append(f'    <loc>{url_for(endpoint, _external=True)}</loc>')
        xml.append(f'    <priority>{priority}</priority>')
        xml.append('  </url>')

    for s in services:
        xml.append('  <url>')
        xml.append(f'    <loc>{url_for("services.detail", slug=s.slug, _external=True)}</loc>')
        xml.append('    <priority>0.85</priority>')
        xml.append('  </url>')

    for p in projects:
        xml.append('  <url>')
        xml.append(f'    <loc>{url_for("projects.detail", slug=p.slug, _external=True)}</loc>')
        xml.append('    <priority>0.85</priority>')
        xml.append('  </url>')

    xml.append('</urlset>')
    return Response('\n'.join(xml), mimetype='application/xml')
