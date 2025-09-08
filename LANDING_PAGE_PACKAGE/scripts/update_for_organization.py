#!/usr/bin/env python3
"""
Organization Update Script
=========================

This script helps you customize the landing page for your GitHub organization.
"""

import os
import re
from pathlib import Path

class OrganizationUpdater:
    """Updates landing page content for organization deployment."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.landing_page_file = self.project_root / "landing_page.html"
        
    def get_organization_info(self):
        """Get organization information from user."""
        print("🏢 Access Shield Landing Page - Organization Setup")
        print("=" * 60)
        print()
        
        org_name = input("Enter your GitHub organization name: ").strip()
        if not org_name:
            print("❌ Organization name is required!")
            return None
            
        org_description = input("Enter organization description (optional): ").strip()
        org_email = input("Enter organization email (optional): ").strip()
        org_website = input("Enter organization website (optional): ").strip()
        
        return {
            'org_name': org_name,
            'org_description': org_description or f"{org_name} - Professional Software Solutions",
            'org_email': org_email or f"contact@{org_name.lower()}.com",
            'org_website': org_website or f"https://{org_name.lower()}.com"
        }
    
    def update_landing_page(self, org_info):
        """Update landing page with organization information."""
        print(f"\n📝 Updating landing page for {org_info['org_name']}...")
        
        if not self.landing_page_file.exists():
            print(f"❌ Landing page file not found: {self.landing_page_file}")
            return False
        
        # Read current content
        with open(self.landing_page_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update organization name in title
        content = re.sub(
            r'<title>Access Shield - Secure Access\. Simplified\.</title>',
            f'<title>{org_info["org_name"]} - Access Shield Landing Page</title>',
            content
        )
        
        # Update hero section
        content = re.sub(
            r'<h1 class="display-4 fw-bold mb-4">\s*<i class="fas fa-shield-alt me-3"></i>Access Shield\s*</h1>',
            f'<h1 class="display-4 fw-bold mb-4">\n                <i class="fas fa-shield-alt me-3"></i>{org_info["org_name"]}\n            </h1>',
            content
        )
        
        # Update description
        content = re.sub(
            r'<p class="mb-5">Access Shield continuously monitors accounts, teams, and repos for excessive privileges, risky workflows, and misconfigurations\.<br>Built on Zero Trust principles with AI explainability — so you see not just alerts, but the "why" behind them\.</p>',
            f'<p class="mb-5">{org_info["org_description"]}<br>Access Shield continuously monitors accounts, teams, and repos for excessive privileges, risky workflows, and misconfigurations.</p>',
            content
        )
        
        # Update footer
        content = re.sub(
            r'<h5><i class="fas fa-shield-alt me-2"></i>Access Shield</h5>\s*<p class="text-muted">AI-Powered GitHub Access Governance</p>',
            f'<h5><i class="fas fa-shield-alt me-2"></i>{org_info["org_name"]}</h5>\n                    <p class="text-muted">{org_info["org_description"]}</p>',
            content
        )
        
        # Add contact information
        contact_html = f'''
                    <p class="text-muted">Email: {org_info["org_email"]}</p>
                    <p class="text-muted">Website: {org_info["org_website"]}</p>'''
        
        content = re.sub(
            r'<p class="text-muted">&copy; 2024 Access Shield\. All rights reserved\.</p>',
            f'{contact_html}\n                    <p class="text-muted">&copy; 2024 {org_info["org_name"]}. All rights reserved.</p>',
            content
        )
        
        # Write updated content
        with open(self.landing_page_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Landing page updated successfully!")
        return True
    
    def update_readme(self, org_info):
        """Update README with organization information."""
        print(f"\n📝 Updating README for {org_info['org_name']}...")
        
        readme_file = self.project_root / "README.md"
        if not readme_file.exists():
            print("⚠️  README.md not found, skipping...")
            return True
        
        # Read current content
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update organization information
        content = re.sub(
            r'# 🎨 Access Shield Landing Page Package',
            f'# 🎨 {org_info["org_name"]} - Access Shield Landing Page',
            content
        )
        
        # Add organization info section
        org_section = f'''
## 🏢 Organization Information

- **Organization**: {org_info['org_name']}
- **Description**: {org_info['org_description']}
- **Email**: {org_info['org_email']}
- **Website**: {org_info['org_website']}
- **GitHub Pages URL**: https://{org_info['org_name'].lower()}.github.io/access-shield-landing

'''
        
        # Insert organization section after the main description
        content = re.sub(
            r'(A professional, responsive landing page system for Access Shield AI - the AI-powered GitHub access governance platform\.)',
            r'\1' + org_section,
            content
        )
        
        # Write updated content
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ README updated successfully!")
        return True
    
    def create_deployment_instructions(self, org_info):
        """Create organization-specific deployment instructions."""
        print(f"\n📝 Creating deployment instructions for {org_info['org_name']}...")
        
        instructions = f"""# 🚀 Deployment Instructions for {org_info['org_name']}

## Quick Deployment Steps

### 1. Create Repository in Organization
1. Go to https://github.com/{org_info['org_name']}
2. Click "New repository"
3. Name: `access-shield-landing`
4. Description: "Access Shield Landing Page - {org_info['org_description']}"
5. Make it **Public**
6. Don't initialize with README
7. Click "Create repository"

### 2. Upload Files
1. Upload all files from this package
2. Commit message: "Initial commit: Access Shield Landing Page"
3. Click "Commit changes"

### 3. Enable GitHub Pages
1. Go to Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: "main" and "/ (root)"
4. Click "Save"

### 4. Access Your Site
Your landing page will be live at:
**https://{org_info['org_name'].lower()}.github.io/access-shield-landing**

## Organization Information
- **Name**: {org_info['org_name']}
- **Description**: {org_info['org_description']}
- **Email**: {org_info['org_email']}
- **Website**: {org_info['org_website']}

## Next Steps
1. Test your live site
2. Share with your team
3. Customize further as needed
4. Set up monitoring and analytics

---
**Created**: {os.popen('date').read().strip()}
**Organization**: {org_info['org_name']}
"""
        
        instructions_file = self.project_root / "DEPLOYMENT_INSTRUCTIONS.md"
        with open(instructions_file, 'w', encoding='utf-8') as f:
            f.write(instructions)
        
        print("✅ Deployment instructions created!")
        return True
    
    def run(self):
        """Run the organization update process."""
        # Get organization information
        org_info = self.get_organization_info()
        if not org_info:
            return False
        
        print(f"\n🎯 Updating package for {org_info['org_name']}...")
        
        # Update files
        success = True
        success &= self.update_landing_page(org_info)
        success &= self.update_readme(org_info)
        success &= self.create_deployment_instructions(org_info)
        
        if success:
            print(f"\n🎉 Package updated successfully for {org_info['org_name']}!")
            print(f"\n📋 Next steps:")
            print(f"1. Review the updated files")
            print(f"2. Follow DEPLOYMENT_INSTRUCTIONS.md")
            print(f"3. Deploy to https://github.com/{org_info['org_name']}")
            print(f"4. Your site will be live at: https://{org_info['org_name'].lower()}.github.io/access-shield-landing")
        else:
            print(f"\n❌ Some updates failed. Please check the output above.")
        
        return success

def main():
    """Main function."""
    updater = OrganizationUpdater()
    updater.run()

if __name__ == "__main__":
    main()
