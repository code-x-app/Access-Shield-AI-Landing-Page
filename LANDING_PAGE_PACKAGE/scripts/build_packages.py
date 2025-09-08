#!/usr/bin/env python3
"""
Package Builder for Access Shield Landing Page
==============================================

This script creates optimized packages for different deployment scenarios.
"""

import os
import sys
import shutil
import zipfile
import json
from datetime import datetime
from pathlib import Path

class PackageBuilder:
    """Builds optimized packages for the landing page."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.build_dir = self.project_root / "build"
        self.packages_dir = self.project_root / "packages"
        
    def create_directories(self):
        """Create necessary directories."""
        self.build_dir.mkdir(exist_ok=True)
        self.packages_dir.mkdir(exist_ok=True)
        
    def build_static_package(self):
        """Build static HTML package."""
        print("📦 Building static HTML package...")
        
        static_dir = self.build_dir / "static"
        static_dir.mkdir(exist_ok=True)
        
        # Copy main files
        files_to_copy = [
            "landing_page.html",
            "launch_landing_page.py",
            "README.md"
        ]
        
        for file in files_to_copy:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, static_dir)
                print(f"  ✅ Copied {file}")
        
        # Copy documentation
        docs_dir = static_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        docs_src = self.project_root / "docs"
        if docs_src.exists():
            shutil.copytree(docs_src, docs_dir, dirs_exist_ok=True)
            print("  ✅ Copied documentation")
        
        # Create package info
        package_info = {
            "name": "Access Shield Landing Page - Static",
            "version": "1.0.0",
            "type": "static",
            "description": "Static HTML landing page for Access Shield AI",
            "files": [
                "landing_page.html",
                "launch_landing_page.py",
                "README.md",
                "docs/"
            ],
            "requirements": [],
            "deployment": "Static hosting (GitHub Pages, Netlify, Vercel)",
            "created": datetime.now().isoformat()
        }
        
        with open(static_dir / "package_info.json", "w") as f:
            json.dump(package_info, f, indent=2)
        
        # Create zip package
        zip_path = self.packages_dir / "access-shield-landing-static.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(static_dir):
                for file in files:
                    file_path = Path(root) / file
                    arc_path = file_path.relative_to(static_dir)
                    zipf.write(file_path, arc_path)
        
        print(f"  ✅ Created {zip_path}")
        return zip_path
    
    def build_flask_package(self):
        """Build Flask server package."""
        print("📦 Building Flask server package...")
        
        flask_dir = self.build_dir / "flask"
        flask_dir.mkdir(exist_ok=True)
        
        # Copy Flask files
        files_to_copy = [
            "landing_page.py",
            "launch_landing_page.py",
            "README.md"
        ]
        
        for file in files_to_copy:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, flask_dir)
                print(f"  ✅ Copied {file}")
        
        # Copy templates
        templates_dir = flask_dir / "templates"
        templates_src = self.project_root / "templates"
        if templates_src.exists():
            shutil.copytree(templates_src, templates_dir, dirs_exist_ok=True)
            print("  ✅ Copied templates")
        
        # Copy static assets
        static_dir = flask_dir / "static"
        static_src = self.project_root / "static"
        if static_src.exists():
            shutil.copytree(static_src, static_dir, dirs_exist_ok=True)
            print("  ✅ Copied static assets")
        
        # Create requirements.txt
        requirements = [
            "flask>=2.0.0",
            "flask-socketio>=5.0.0",
            "python-dotenv>=0.19.0"
        ]
        
        with open(flask_dir / "requirements.txt", "w") as f:
            f.write("\n".join(requirements))
        print("  ✅ Created requirements.txt")
        
        # Create package info
        package_info = {
            "name": "Access Shield Landing Page - Flask",
            "version": "1.0.0",
            "type": "flask",
            "description": "Flask-based landing page server for Access Shield AI",
            "files": [
                "landing_page.py",
                "launch_landing_page.py",
                "requirements.txt",
                "templates/",
                "static/",
                "README.md"
            ],
            "requirements": requirements,
            "deployment": "Flask server, Docker, Cloud platforms",
            "created": datetime.now().isoformat()
        }
        
        with open(flask_dir / "package_info.json", "w") as f:
            json.dump(package_info, f, indent=2)
        
        # Create zip package
        zip_path = self.packages_dir / "access-shield-landing-flask.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(flask_dir):
                for file in files:
                    file_path = Path(root) / file
                    arc_path = file_path.relative_to(flask_dir)
                    zipf.write(file_path, arc_path)
        
        print(f"  ✅ Created {zip_path}")
        return zip_path
    
    def build_docker_package(self):
        """Build Docker package."""
        print("📦 Building Docker package...")
        
        docker_dir = self.build_dir / "docker"
        docker_dir.mkdir(exist_ok=True)
        
        # Copy Flask files
        files_to_copy = [
            "landing_page.py",
            "README.md"
        ]
        
        for file in files_to_copy:
            src = self.project_root / file
            if src.exists():
                shutil.copy2(src, docker_dir)
                print(f"  ✅ Copied {file}")
        
        # Copy templates and static
        templates_dir = docker_dir / "templates"
        templates_src = self.project_root / "templates"
        if templates_src.exists():
            shutil.copytree(templates_src, templates_dir, dirs_exist_ok=True)
            print("  ✅ Copied templates")
        
        static_dir = docker_dir / "static"
        static_src = self.project_root / "static"
        if static_src.exists():
            shutil.copytree(static_src, static_dir, dirs_exist_ok=True)
            print("  ✅ Copied static assets")
        
        # Create Dockerfile
        dockerfile_content = """FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8080/ || exit 1

# Run the application
CMD ["python", "landing_page.py"]
"""
        
        with open(docker_dir / "Dockerfile", "w") as f:
            f.write(dockerfile_content)
        print("  ✅ Created Dockerfile")
        
        # Create requirements.txt
        requirements = [
            "flask>=2.0.0",
            "flask-socketio>=5.0.0",
            "python-dotenv>=0.19.0",
            "gunicorn>=20.0.0"
        ]
        
        with open(docker_dir / "requirements.txt", "w") as f:
            f.write("\n".join(requirements))
        print("  ✅ Created requirements.txt")
        
        # Create docker-compose.yml
        compose_content = """version: '3.8'

services:
  landing-page:
    build: .
    ports:
      - "8080:8080"
    environment:
      - FLASK_ENV=production
      - FLASK_DEBUG=False
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/"]
      interval: 30s
      timeout: 10s
      retries: 3
"""
        
        with open(docker_dir / "docker-compose.yml", "w") as f:
            f.write(compose_content)
        print("  ✅ Created docker-compose.yml")
        
        # Create package info
        package_info = {
            "name": "Access Shield Landing Page - Docker",
            "version": "1.0.0",
            "type": "docker",
            "description": "Docker containerized landing page for Access Shield AI",
            "files": [
                "Dockerfile",
                "docker-compose.yml",
                "requirements.txt",
                "landing_page.py",
                "templates/",
                "static/",
                "README.md"
            ],
            "requirements": requirements,
            "deployment": "Docker, Kubernetes, Cloud platforms",
            "created": datetime.now().isoformat()
        }
        
        with open(docker_dir / "package_info.json", "w") as f:
            json.dump(package_info, f, indent=2)
        
        # Create zip package
        zip_path = self.packages_dir / "access-shield-landing-docker.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(docker_dir):
                for file in files:
                    file_path = Path(root) / file
                    arc_path = file_path.relative_to(docker_dir)
                    zipf.write(file_path, arc_path)
        
        print(f"  ✅ Created {zip_path}")
        return zip_path
    
    def build_all_packages(self):
        """Build all package types."""
        print("🚀 Building all packages...")
        print("=" * 50)
        
        self.create_directories()
        
        packages = []
        
        # Build static package
        static_package = self.build_static_package()
        packages.append(static_package)
        
        # Build Flask package
        flask_package = self.build_flask_package()
        packages.append(flask_package)
        
        # Build Docker package
        docker_package = self.build_docker_package()
        packages.append(docker_package)
        
        # Create summary
        print("\n" + "=" * 50)
        print("📦 Package Build Summary")
        print("=" * 50)
        
        for package in packages:
            size = package.stat().st_size / (1024 * 1024)  # MB
            print(f"✅ {package.name}: {size:.1f} MB")
        
        print(f"\n🎉 All packages built successfully!")
        print(f"📁 Packages location: {self.packages_dir}")
        
        return packages

def main():
    """Main function."""
    print("🛡️  Access Shield Landing Page - Package Builder")
    print("=" * 60)
    
    builder = PackageBuilder()
    packages = builder.build_all_packages()
    
    print("\n📋 Next steps:")
    print("1. Test the packages locally")
    print("2. Upload to your preferred hosting platform")
    print("3. Deploy and share with your team!")
    
    print("\n🎯 Package types available:")
    print("• Static HTML - For GitHub Pages, Netlify, Vercel")
    print("• Flask Server - For VPS, cloud platforms")
    print("• Docker - For containerized deployments")

if __name__ == "__main__":
    main()
