"""
Main routes for The Wizard of AWS portfolio site.
"""
from flask import Blueprint, render_template, abort
from flask_flatpages import FlatPages

main_bp = Blueprint('main', __name__)
pages = None  # Will be initialized in register_pages


def register_pages(flatpages_instance):
    """Register FlatPages instance with the blueprint."""
    global pages
    pages = flatpages_instance


@main_bp.route('/')
def index():
    """Home page route - The central hub for 'The Wizard of AWS'."""
    return render_template('index.html')


@main_bp.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@main_bp.route('/blog')
def blog():
    """Blog listing page route."""
    return render_template('blog.html')


@main_bp.route('/writing')
def writing():
    """Blog page route - Integration of Substack and Medium feeds."""
    return render_template('writing.html')


@main_bp.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')


@main_bp.route('/projects')
def projects():
    """Portfolio page route - Deep dives into technical repositories and architectures."""
    return render_template('projects.html')


@main_bp.route('/podcast')
def podcast():
    """Podcast page route."""
    return render_template('podcast.html')


@main_bp.route('/resources')
def resources():
    """Resources page route."""
    return render_template('resources.html')


@main_bp.route('/expertise')
def expertise():
    """Expertise page route."""
    return render_template('expertise.html')


@main_bp.route('/socials')
def socials():
    """Contact Me page route - Professional landing spot for inquiries and social links."""
    return render_template('socials.html')


@main_bp.route('/writing/<path:path>')
def writing_page(path):
    """Dynamic route for rendering Markdown files from pages directory."""
    if pages is None:
        abort(500, "FlatPages not initialized")
    
    # Get the page from FlatPages
    page = pages.get_or_404(path)
    
    return render_template('writing_page.html', page=page)
