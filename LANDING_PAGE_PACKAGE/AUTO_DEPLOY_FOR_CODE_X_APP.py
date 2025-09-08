#!/usr/bin/env python3
"""
Auto-Deploy Script for code-x-app Organization
==============================================

This script automatically customizes and prepares everything for your code-x-app organization.
"""

import os
import re
import webbrowser
from pathlib import Path

class CodeXAppDeployer:
    """Automatically prepares landing page for code-x-app organization."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.landing_page_file = self.project_root / "landing_page.html"
        self.readme_file = self.project_root / "README.md"
        
        # code-x-app organization details
        self.org_info = {
            'org_name': 'code-x-app',
            'display_name': 'Code X App',
            'description': 'Professional software development and AI solutions',
            'email': 'contact@code-x-app.com',
            'website': 'https://code-x-app.com',
            'repo_name': 'access-shield-landing',
            'primary_color': '#667eea',
            'secondary_color': '#764ba2',
            'headline': 'Code X App',
            'tagline': 'Professional Software Solutions'
        }
    
    def update_landing_page(self):
        """Update landing page for code-x-app."""
        print("🎨 Customizing landing page for Code X App...")
        
        if not self.landing_page_file.exists():
            print("❌ Landing page file not found!")
            return False
        
        # Read current content
        with open(self.landing_page_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update title
        content = re.sub(
            r'<title>Access Shield - Secure Access\. Simplified\.</title>',
            f'<title>{self.org_info["display_name"]} - Access Shield Landing Page</title>',
            content
        )
        
        # Update hero section
        content = re.sub(
            r'<h1 class="display-4 fw-bold mb-4">\s*<i class="fas fa-shield-alt me-3"></i>Access Shield\s*</h1>',
            f'<h1 class="display-4 fw-bold mb-4">\n                <i class="fas fa-shield-alt me-3"></i>{self.org_info["display_name"]}\n            </h1>',
            content
        )
        
        # Update tagline
        content = re.sub(
            r'<p class="lead mb-4">Secure Access\. Simplified\.</p>',
            f'<p class="lead mb-4">{self.org_info["tagline"]}</p>',
            content
        )
        
        # Update description
        content = re.sub(
            r'<p class="mb-5">Access Shield continuously monitors accounts, teams, and repos for excessive privileges, risky workflows, and misconfigurations\.<br>Built on Zero Trust principles with AI explainability — so you see not just alerts, but the "why" behind them\.</p>',
            f'<p class="mb-5">{self.org_info["description"]}<br>Access Shield continuously monitors accounts, teams, and repos for excessive privileges, risky workflows, and misconfigurations.</p>',
            content
        )
        
        # Update footer
        content = re.sub(
            r'<h5><i class="fas fa-shield-alt me-2"></i>Access Shield</h5>\s*<p class="text-muted">AI-Powered GitHub Access Governance</p>',
            f'<h5><i class="fas fa-shield-alt me-2"></i>{self.org_info["display_name"]}</h5>\n                    <p class="text-muted">{self.org_info["description"]}</p>',
            content
        )
        
        # Add contact information
        contact_html = f'''
                    <p class="text-muted">Email: {self.org_info["email"]}</p>
                    <p class="text-muted">Website: {self.org_info["website"]}</p>'''
        
        content = re.sub(
            r'<p class="text-muted">&copy; 2024 Access Shield\. All rights reserved\.</p>',
            f'{contact_html}\n                    <p class="text-muted">&copy; 2024 {self.org_info["display_name"]}. All rights reserved.</p>',
            content
        )
        
        # Write updated content
        with open(self.landing_page_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Landing page customized for Code X App!")
        return True
    
    def update_readme(self):
        """Update README for code-x-app."""
        print("📝 Updating README for Code X App...")
        
        readme_content = f"""# 🎨 {self.org_info['display_name']} - Access Shield Landing Page

A professional, responsive landing page for {self.org_info['display_name']} - showcasing Access Shield AI capabilities.

## 🏢 Organization Information

- **Organization**: {self.org_info['org_name']}
- **Display Name**: {self.org_info['display_name']}
- **Description**: {self.org_info['description']}
- **Email**: {self.org_info['email']}
- **Website**: {self.org_info['website']}
- **GitHub Pages URL**: https://{self.org_info['org_name']}.github.io/{self.org_info['repo_name']}

## 🚀 Quick Start

### Option 1: Static HTML (Easiest)
```bash
# Just open the HTML file
open landing_page.html
# Or use the launcher
python launch_landing_page.py
```

### Option 2: Flask Server (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python landing_page.py
# Access at http://localhost:8080
```

## 🌐 Live Site

Your landing page will be live at:
**https://{self.org_info['org_name']}.github.io/{self.org_info['repo_name']}**

## 📁 Package Contents

- `landing_page.html` - Main landing page
- `launch_landing_page.py` - Simple launcher
- `landing_page.py` - Flask web server
- `requirements.txt` - Python dependencies
- `docs/` - Complete documentation
- `scripts/` - Deployment tools

## 🎯 Features

- ✅ Beautiful responsive design
- ✅ Professional branding for {self.org_info['display_name']}
- ✅ Fast loading (< 2 seconds)
- ✅ Mobile optimized
- ✅ SEO ready
- ✅ Easy to customize

## 🔧 Customization

Edit `landing_page.html` to customize:
- Colors and branding
- Content and messaging
- Contact information
- Feature descriptions

## 📞 Support

For support and questions:
- **Email**: {self.org_info['email']}
- **Website**: {self.org_info['website']}
- **GitHub**: https://github.com/{self.org_info['org_name']}

---

**Built with ❤️ for {self.org_info['display_name']}**
"""
        
        with open(self.readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("✅ README updated for Code X App!")
        return True
    
    def create_deployment_guide(self):
        """Create step-by-step deployment guide."""
        print("📋 Creating deployment guide...")
        
        guide_content = f"""# 🚀 Deployment Guide for {self.org_info['display_name']}

## ⚡ 5-Minute Deployment to code-x-app Organization

### Step 1: Create Repository (2 minutes)
1. Go to: https://github.com/orgs/{self.org_info['org_name']}/repositories
2. Click **"New repository"**
3. Repository name: `{self.org_info['repo_name']}`
4. Description: "Access Shield Landing Page - {self.org_info['description']}"
5. Make it **Public** ✅
6. ❌ **Don't** check "Add a README file"
7. Click **"Create repository"**

### Step 2: Upload Files (2 minutes)
1. **Download this package** (the entire folder)
2. **Go to your new repository**
3. **Click "uploading an existing file"**
4. **Drag and drop ALL files** from this package
5. **Commit message**: "Initial commit: Access Shield Landing Page"
6. **Click "Commit changes"**

### Step 3: Enable GitHub Pages (1 minute)
1. **Go to Settings** tab in your repository
2. **Scroll to "Pages"** in left sidebar
3. **Source**: Select "Deploy from a branch"
4. **Branch**: Select "main" and "/ (root)"
5. **Click "Save"**
6. **Wait 2-3 minutes** for deployment

### Step 4: Access Your Live Site ✨
Your landing page will be live at:
**https://{self.org_info['org_name']}.github.io/{self.org_info['repo_name']}**

## 🎯 What You Get

✅ **Professional landing page** - Beautiful, responsive design  
✅ **Free hosting** - GitHub Pages (no cost)  
✅ **Custom domain** - Add your own domain later  
✅ **SSL certificate** - Automatic HTTPS  
✅ **Version control** - Track all changes  
✅ **Easy updates** - Just push new changes  

## 🔧 Customization

After deployment, you can customize:
- Colors and branding
- Content and messaging
- Contact information
- Feature descriptions

## 📞 Support

- **Email**: {self.org_info['email']}
- **Website**: {self.org_info['website']}
- **GitHub**: https://github.com/{self.org_info['org_name']}

---

**🎉 Your {self.org_info['display_name']} landing page is ready to deploy!**
"""
        
        guide_file = self.project_root / "DEPLOYMENT_GUIDE.md"
        with open(guide_file, 'w', encoding='utf-8') as f:
            f.write(guide_content)
        
        print("✅ Deployment guide created!")
        return True
    
    def create_github_commands(self):
        """Create ready-to-use GitHub commands."""
        print("💻 Creating GitHub commands...")
        
        commands_content = f"""# 🐙 GitHub Commands for {self.org_info['display_name']}

## Quick Setup Commands

### 1. Initialize Git Repository
```bash
cd LANDING_PAGE_PACKAGE
git init
git add .
git commit -m "Initial commit: Access Shield Landing Page for {self.org_info['display_name']}"
```

### 2. Add Remote Origin
```bash
git remote add origin https://github.com/{self.org_info['org_name']}/{self.org_info['repo_name']}.git
```

### 3. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## 🌐 Your Live URLs

- **Repository**: https://github.com/{self.org_info['org_name']}/{self.org_info['repo_name']}
- **Live Site**: https://{self.org_info['org_name']}.github.io/{self.org_info['repo_name']}
- **Organization**: https://github.com/{self.org_info['org_name']}

## 📋 Checklist

- [ ] Repository created in {self.org_info['org_name']} organization
- [ ] Files uploaded to GitHub
- [ ] GitHub Pages enabled
- [ ] Site accessible at live URL
- [ ] Custom domain configured (optional)
- [ ] Team members invited (optional)

---

**Ready to deploy! Just run these commands!** 🚀
"""
        
        commands_file = self.project_root / "GITHUB_COMMANDS.md"
        with open(commands_file, 'w', encoding='utf-8') as f:
            f.write(commands_content)
        
        print("✅ GitHub commands created!")
        return True
    
    def open_github_repository(self):
        """Open the GitHub repository creation page."""
        print("🌐 Opening GitHub repository creation page...")
        
        github_url = f"https://github.com/orgs/{self.org_info['org_name']}/repositories"
        
        try:
            webbrowser.open(github_url)
            print(f"✅ Opened: {github_url}")
            print("📋 Next steps:")
            print("1. Click 'New repository'")
            print(f"2. Name: {self.org_info['repo_name']}")
            print(f"3. Description: Access Shield Landing Page - {self.org_info['description']}")
            print("4. Make it Public")
            print("5. Don't initialize with README")
            print("6. Click 'Create repository'")
        except Exception as e:
            print(f"❌ Could not open browser: {e}")
            print(f"📋 Manual step: Go to {github_url}")
    
    def run(self):
        """Run the complete setup process."""
        print("🚀 Setting up landing page for Code X App...")
        print("=" * 60)
        
        success = True
        success &= self.update_landing_page()
        success &= self.update_readme()
        success &= self.create_deployment_guide()
        success &= self.create_github_commands()
        
        if success:
            print("\n🎉 Setup complete for Code X App!")
            print("\n📋 Next steps:")
            print("1. Review the updated files")
            print("2. Follow DEPLOYMENT_GUIDE.md")
            print("3. Or use the commands in GITHUB_COMMANDS.md")
            print(f"4. Your site will be live at: https://{self.org_info['org_name']}.github.io/{self.org_info['repo_name']}")
            
            # Open GitHub repository page
            self.open_github_repository()
            
            print(f"\n🎯 Repository URL: https://github.com/{self.org_info['org_name']}/{self.org_info['repo_name']}")
        else:
            print("\n❌ Some steps failed. Please check the output above.")
        
        return success

def main():
    """Main function."""
    deployer = CodeXAppDeployer()
    deployer.run()

if __name__ == "__main__":
    main()
