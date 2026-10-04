from datetime import datetime, timezone
from app.extensions import db

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    what_we_handle = db.Column(db.JSON, nullable=True) # list of strings
    key_capabilities = db.Column(db.JSON, nullable=True) # list of strings
    typical_applications = db.Column(db.JSON, nullable=True) # list of strings
    icon = db.Column(db.String(100), nullable=True)
    hero_image = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'number': self.number,
            'title': self.title,
            'short_description': self.short_description,
            'overview': self.overview,
            'what_we_handle': self.what_we_handle or [],
            'key_capabilities': self.key_capabilities or [],
            'typical_applications': self.typical_applications or [],
            'icon': self.icon,
            'hero_image': self.hero_image
        }

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    service_slug = db.Column(db.String(100), nullable=True)
    industry_slug = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(150), nullable=False, default="Lagos, Nigeria")
    status = db.Column(db.String(100), nullable=False, default="Completed Demo Project")
    short_description = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    challenge = db.Column(db.Text, nullable=False)
    approach = db.Column(db.Text, nullable=False)
    scope_of_work = db.Column(db.JSON, nullable=True) # list of items
    technical_highlights = db.Column(db.JSON, nullable=True) # list of items
    outcome = db.Column(db.Text, nullable=False)
    featured = db.Column(db.Boolean, default=False)
    main_image = db.Column(db.String(255), nullable=False)
    gallery_images = db.Column(db.JSON, nullable=True)

class Industry(db.Model):
    __tablename__ = 'industries'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    operational_challenges = db.Column(db.JSON, nullable=True)
    example_applications = db.Column(db.JSON, nullable=True)
    relevant_service_slugs = db.Column(db.JSON, nullable=True)
    image = db.Column(db.String(255), nullable=True)

class Enquiry(db.Model):
    __tablename__ = 'enquiries'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    company_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    service_required = db.Column(db.String(100), nullable=False)
    project_type = db.Column(db.String(100), nullable=False)
    estimated_timeline = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    preferred_contact_method = db.Column(db.String(50), nullable=False, default="Email")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
