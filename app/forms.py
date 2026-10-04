from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class ContactForm(FlaskForm):
    full_name = StringField(
        'Full Name',
        validators=[DataRequired(message="Please enter your full name."), Length(max=150)]
    )
    company_name = StringField(
        'Company Name',
        validators=[Optional(), Length(max=150)]
    )
    email = StringField(
        'Email Address',
        validators=[DataRequired(message="Please enter a valid email address."), Email(message="Invalid email address."), Length(max=150)]
    )
    phone = StringField(
        'Phone Number',
        validators=[DataRequired(message="Please enter your contact phone number."), Length(max=50)]
    )
    service_required = SelectField(
        'Service Required',
        choices=[
            ('', 'Select Service Required'),
            ('engineering-services', 'Engineering Services'),
            ('industrial-maintenance', 'Industrial Maintenance'),
            ('technical-procurement', 'Technical Procurement'),
            ('installation-commissioning', 'Installation & Commissioning'),
            ('project-support', 'Project Support'),
            ('other', 'General / Other Consultancy')
        ],
        validators=[DataRequired(message="Please select a service.")]
    )
    project_type = SelectField(
        'Project Type',
        choices=[
            ('', 'Select Project Scope'),
            ('new-installation', 'New Facility / Installation'),
            ('upgrade-retrofit', 'Infrastructure Upgrade / Retrofit'),
            ('routine-maintenance', 'Scheduled Routine Maintenance'),
            ('turnaround-shutdown', 'Plant Turnaround & Shutdown Support'),
            ('equipment-procurement', 'Industrial Equipment Procurement'),
            ('consulting', 'Technical Consulting & Feasibility')
        ],
        validators=[DataRequired(message="Please select a project type.")]
    )
    estimated_timeline = SelectField(
        'Estimated Timeline',
        choices=[
            ('', 'Select Expected Timeline'),
            ('immediate', 'Immediate (< 1 Month)'),
            ('1-3-months', '1 to 3 Months'),
            ('3-6-months', '3 to 6 Months'),
            ('6-plus-months', '6+ Months / Long Term Planning')
        ],
        validators=[DataRequired(message="Please select an estimated timeline.")]
    )
    project_description = TextAreaField(
        'Project Description',
        validators=[
            DataRequired(message="Please provide a brief description of your project scope."),
            Length(min=10, max=3000, message="Description must be between 10 and 3000 characters.")
        ]
    )
    preferred_contact_method = SelectField(
        'Preferred Contact Method',
        choices=[
            ('Email', 'Email'),
            ('Phone', 'Phone Call'),
            ('WhatsApp', 'WhatsApp / Direct Message')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit Project Enquiry')
