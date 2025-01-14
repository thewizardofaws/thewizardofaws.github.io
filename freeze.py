"""
Frozen-Flask script to build static site into /build directory.
"""
import sys
import os
# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Workaround for Werkzeug 3.x compatibility
try:
    from werkzeug.routing import Map
    if not hasattr(Map, 'charset'):
        Map.charset = 'utf-8'
except (ImportError, AttributeError):
    pass

# Monkeypatch for Frozen-Flask 0.18 compatibility with Flask 3.x
import flask_frozen
original_static_rules_endpoints = flask_frozen.Freezer._static_rules_endpoints
def patched_static_rules_endpoints(self):
    """Patched version that works with Flask 3.x"""
    endpoints = set()
    for rule in self.app.url_map.iter_rules():
        if rule.endpoint == 'static':
            endpoints.add(rule.endpoint)
    return endpoints
flask_frozen.Freezer._static_rules_endpoints = patched_static_rules_endpoints

# Import app.py as a module
import importlib.util
app_py_path = os.path.join(os.path.dirname(__file__), 'app.py')
spec = importlib.util.spec_from_file_location("app_py", app_py_path)
app_py = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_py)

from flask_frozen import Freezer

# Get create_app from the imported module
create_app = app_py.create_app

# Create the Flask app instance
app = create_app()

# Configure Frozen-Flask for directory-based routing
# This ensures routes like /writing become build/writing/index.html
# instead of build/writing (which conflicts with /writing/<path> sub-pages)
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*']
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_INDICES'] = False
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

# Initialize Frozen-Flask with custom URL builder to handle directory conflicts
freezer = Freezer(app)

# Override the URL builder to ensure directory structure for routes with sub-paths
def url_for_writing_index():
    """Generate /writing/ URL to ensure directory structure"""
    return '/writing/'

# Register a custom generator that handles the /writing conflict
@freezer.register_generator
def writing_index_generator():
    """Generate /writing/ as a directory to avoid conflict with /writing/<path>"""
    yield '/writing/'


@freezer.register_generator
def page_generator():
    """
    Generator function for all pages that should be frozen.
    This can be extended to include dynamic routes.
    """
    # Static routes - only yield routes that actually exist
    yield '/'
    yield '/projects'
    # Note: /writing/ is handled by writing_index_generator to avoid conflicts
    yield '/socials'
    
    # Dynamic routes for Markdown pages
    # These will become build/writing/<path>/index.html
    for page in app.pages:
        yield f'/writing/{page.path}'


if __name__ == '__main__':
    freezer.freeze()
