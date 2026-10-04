from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import ContactForm
from app.models import Enquiry, Service
from app.extensions import db

contact_bp = Blueprint('contact', __name__, url_prefix='/contact')

@contact_bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        enquiry = Enquiry(
            full_name=form.full_name.data,
            company_name=form.company_name.data,
            email=form.email.data,
            phone=form.phone.data,
            service_required=form.service_required.data,
            project_type=form.project_type.data,
            estimated_timeline=form.estimated_timeline.data,
            project_description=form.project_description.data,
            preferred_contact_method=form.preferred_contact_method.data
        )
        db.session.add(enquiry)
        db.session.commit()

        flash('Thank you for your project enquiry. Our engineering technical team will review your specifications and contact you shortly.', 'success')
        return redirect(url_for('contact.index'))

    services = Service.query.order_by(Service.number).all()
    return render_template('pages/contact.html', form=form, services=services)
