"""
Flask application factory for The Wizard of AWS portfolio site.
"""
from flask import Flask
from flask_flatpages import FlatPages


def create_app(config=None):
    """
    Application factory pattern for creating Flask app instances.
    
    Args:
        config: Optional configuration dictionary
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Default configuration
    app.config.update({
        'FLATPAGES_ROOT': 'pages',
        'FLATPAGES_EXTENSION': '.md',
        'FLATPAGES_MARKDOWN_EXTENSIONS': ['codehilite', 'fenced_code', 'tables'],
        'FLATPAGES_AUTO_RELOAD': True,
    })
    
    # Override with provided config if any
    if config:
        app.config.update(config)
    
    # Initialize FlatPages for markdown content
    pages = FlatPages(app)
    app.pages = pages
    
    # Register blueprints/routes here
    from app.routes import main_bp, register_pages
    register_pages(pages)
    app.register_blueprint(main_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
