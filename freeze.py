"""
Frozen-Flask script to build static site into /build directory.
"""
from flask_frozen import Freezer
from app import create_app

# Create the Flask app instance
app = create_app()

# Initialize Frozen-Flask
freezer = Freezer(app)


@freezer.register_generator
def page_generator():
    """
    Generator function for all pages that should be frozen.
    This can be extended to include dynamic routes.
    """
    # Static routes
    yield '/'
    yield '/about'
    yield '/blog'
    yield '/writing'
    yield '/expertise'
    yield '/contact'
    yield '/projects'
    yield '/podcast'
    yield '/resources'
    yield '/socials'
    
    # Dynamic routes for Markdown pages
    for page in app.pages:
        yield {'path': f'/writing/{page.path}'}


if __name__ == '__main__':
    freezer.freeze()
