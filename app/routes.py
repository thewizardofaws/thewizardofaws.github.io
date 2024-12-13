"""
Main routes for The Wizard of AWS portfolio site.
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Home page route."""
    return render_template('index.html')


@main_bp.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@main_bp.route('/blog')
def blog():
    """Blog listing page route."""
    return render_template('blog.html')


@main_bp.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')


@main_bp.route('/projects')
def projects():
    """Projects page route."""
    return render_template('projects.html')


@main_bp.route('/podcast')
def podcast():
    """Podcast page route."""
    return render_template('podcast.html')


@main_bp.route('/resources')
def resources():
    """Resources page route."""
    return render_template('resources.html')
