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
# This ensures ALL routes are generated as directories containing index.html files
# Example: /writing becomes build/writing/index.html (not build/writing)
# This prevents FileExistsError when /writing and /writing/<path> both exist
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*']
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_INDICES'] = False
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

# Initialize Frozen-Flask
freezer = Freezer(app)


@freezer.register_generator
def page_generator():
    """
    Generator function for all pages that should be frozen.
    Routes are yielded to ensure directory structure with index.html files.
    """
    # Root route - no trailing slash (becomes build/index.html)
    yield '/'
    
    # Static routes with trailing slashes to ensure directory structure
    # This ensures: /projects -> build/projects/index.html, etc.
    yield '/projects/'
    yield '/writing/'  # Directory structure prevents conflict with /writing/<path> sub-pages
    yield '/socials/'
    
    # Dynamic routes for Markdown pages
    # These will become build/writing/<path>/index.html
    # Note: Flask-FlatPages paths don't include the .md extension
    for page in app.pages:
        # Yield with trailing slash to ensure directory structure
        yield f'/writing/{page.path}/'


if __name__ == '__main__':
    freezer.freeze()
