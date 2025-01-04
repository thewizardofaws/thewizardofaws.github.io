# The Wizard of AWS

A professional portfolio website for AWS expertise, DevOps insights, and cloud innovation. This site is built using **Flask** and **Frozen-Flask** to generate a static site that can be deployed to GitHub Pages.

## Technology Stack

This is a **Flask-based static site generator** that uses:

- **Flask** - Python web framework
- **Frozen-Flask** - Generates static HTML files from Flask routes
- **Flask-FlatPages** - Renders Markdown files as pages
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **Jinja2** - Template engine

## Architecture

The site follows the **Application Factory Pattern** for Flask:

- `app.py` - Main application factory
- `app/routes.py` - Route definitions and blueprints
- `freeze.py` - Static site generation script
- `templates/` - Jinja2 templates
- `pages/` - Markdown content files (rendered via Flask-FlatPages)
- `static/` - CSS, images, and other static assets

## Development

### Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

4. Visit `http://localhost:5000` in your browser

### Building Static Site

To generate the static site for deployment:

```bash
python freeze.py
```

This creates a `/build` directory with all static HTML files ready for deployment.

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions:

- **Workflow**: `.github/workflows/deploy.yml`
- **Trigger**: Pushes to `main` branch
- **Process**: 
  1. Installs Python and dependencies
  2. Runs `freeze.py` to build static site
  3. Deploys `/build` folder to `gh-pages` branch

The workflow runs on every push to the `main` branch, automatically building and deploying the site.

## Project Structure

```
thewizardofaws.github.io/
│
├── app.py                 # Flask application factory
├── freeze.py              # Static site generator
├── requirements.txt       # Python dependencies
│
├── app/
│   ├── __init__.py
│   └── routes.py         # Route definitions
│
├── templates/             # Jinja2 templates
│   ├── base.html         # Base template
│   ├── index.html         # Homepage
│   ├── writing.html      # Writing feed
│   ├── expertise.html    # Expertise page
│   ├── projects.html     # Projects showcase
│   ├── socials.html      # Social media hub
│   └── writing_page.html # Markdown page template
│
├── pages/                 # Markdown content files
│   └── *.md              # Content files (rendered via /writing/<path>)
│
├── static/                # Static assets
│   ├── css/
│   │   └── style.css     # Custom design system
│   ├── favicon.ico       # Site favicon
│   └── images/           # Image assets
│
├── .github/
│   └── workflows/
│       └── deploy.yml     # CI/CD deployment workflow
│
└── build/                 # Generated static site (gitignored)
```

## Features

- **Responsive Design** - Mobile-first, works on all devices
- **Dark Mode** - Deep tech dark theme with AWS orange accents
- **Markdown Support** - Write content in Markdown, rendered as HTML
- **SEO Optimized** - OpenGraph tags for social sharing
- **Static Generation** - Fast, secure, and scalable static site

## About

I'm KC Tyler, a Senior DevOps Engineer specializing in AWS cloud architecture, Python, Terraform, and cloud migrations. As the leader of the AWS Utah User Group, I'm passionate about AWS evangelism and focus on distributed systems, serverless solutions, and generative AI.

## Connect

- [LinkedIn](https://www.linkedin.com/in/thewizardofaws/)
- [YouTube](https://www.youtube.com/@thewizardofaws)
- [Substack](https://thewizardofaws.substack.com)
- [GitHub](https://github.com/thewizardofaws)

## License

All rights reserved. © 2025 The Wizard of AWS
