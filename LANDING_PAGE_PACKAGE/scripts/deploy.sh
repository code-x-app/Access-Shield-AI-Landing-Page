#!/bin/bash

# 🚀 Access Shield Landing Page Deployment Script
# This script automates the deployment of your landing page

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="access-shield-landing"
GITHUB_USERNAME=""
REPOSITORY_NAME="access-shield-landing"
DEPLOYMENT_TYPE="static"  # static, flask, docker

# Functions
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}🚀 Access Shield Landing Page Deployer${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check prerequisites
check_prerequisites() {
    print_info "Checking prerequisites..."
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install git first."
        exit 1
    fi
    
    # Check if python is installed
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3 first."
        exit 1
    fi
    
    # Check if pip is installed
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 is not installed. Please install pip3 first."
        exit 1
    fi
    
    print_success "All prerequisites are installed"
}

# Install dependencies
install_dependencies() {
    print_info "Installing dependencies..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
        print_success "Dependencies installed from requirements.txt"
    else
        pip3 install flask flask-socketio
        print_success "Basic dependencies installed"
    fi
}

# Create GitHub repository
create_github_repo() {
    if [ -z "$GITHUB_USERNAME" ]; then
        print_warning "GitHub username not set. Skipping repository creation."
        print_info "To create a repository manually:"
        print_info "1. Go to https://github.com/new"
        print_info "2. Create a new repository named '$REPOSITORY_NAME'"
        print_info "3. Don't initialize with README (we'll push our code)"
        return
    fi
    
    print_info "Creating GitHub repository..."
    
    # Check if gh CLI is installed
    if command -v gh &> /dev/null; then
        gh repo create $REPOSITORY_NAME --public --description "Access Shield Landing Page - Professional landing page for Access Shield AI"
        print_success "GitHub repository created"
    else
        print_warning "GitHub CLI not installed. Please create repository manually:"
        print_info "1. Go to https://github.com/new"
        print_info "2. Create a new repository named '$REPOSITORY_NAME'"
        print_info "3. Don't initialize with README"
    fi
}

# Initialize git repository
init_git() {
    print_info "Initializing git repository..."
    
    if [ ! -d ".git" ]; then
        git init
        print_success "Git repository initialized"
    else
        print_info "Git repository already exists"
    fi
    
    # Add all files
    git add .
    
    # Create initial commit
    git commit -m "Initial commit: Access Shield Landing Page"
    print_success "Files committed to git"
}

# Deploy to GitHub
deploy_to_github() {
    print_info "Deploying to GitHub..."
    
    # Add remote origin
    if [ -n "$GITHUB_USERNAME" ]; then
        git remote add origin https://github.com/$GITHUB_USERNAME/$REPOSITORY_NAME.git
    else
        print_warning "GitHub username not set. Please add remote manually:"
        print_info "git remote add origin https://github.com/YOUR_USERNAME/$REPOSITORY_NAME.git"
        return
    fi
    
    # Push to GitHub
    git branch -M main
    git push -u origin main
    print_success "Code pushed to GitHub"
}

# Deploy to Netlify
deploy_to_netlify() {
    print_info "Deploying to Netlify..."
    
    # Check if Netlify CLI is installed
    if command -v netlify &> /dev/null; then
        netlify deploy --prod --dir .
        print_success "Deployed to Netlify"
    else
        print_warning "Netlify CLI not installed. Please deploy manually:"
        print_info "1. Go to https://app.netlify.com"
        print_info "2. Drag and drop the landing_page.html file"
        print_info "3. Or connect your GitHub repository"
    fi
}

# Deploy to Vercel
deploy_to_vercel() {
    print_info "Deploying to Vercel..."
    
    # Check if Vercel CLI is installed
    if command -v vercel &> /dev/null; then
        vercel --prod
        print_success "Deployed to Vercel"
    else
        print_warning "Vercel CLI not installed. Please deploy manually:"
        print_info "1. Go to https://vercel.com"
        print_info "2. Import your GitHub repository"
        print_info "3. Deploy automatically"
    fi
}

# Test deployment
test_deployment() {
    print_info "Testing deployment..."
    
    if [ "$DEPLOYMENT_TYPE" = "flask" ]; then
        # Test Flask server
        python3 landing_page.py &
        SERVER_PID=$!
        sleep 5
        
        # Test if server is running
        if curl -f http://localhost:8080 > /dev/null 2>&1; then
            print_success "Flask server is running on http://localhost:8080"
        else
            print_error "Flask server failed to start"
        fi
        
        # Kill server
        kill $SERVER_PID
    else
        # Test static files
        python3 -m http.server 8000 &
        SERVER_PID=$!
        sleep 2
        
        # Test if server is running
        if curl -f http://localhost:8000/landing_page.html > /dev/null 2>&1; then
            print_success "Static files are accessible on http://localhost:8000"
        else
            print_error "Static files are not accessible"
        fi
        
        # Kill server
        kill $SERVER_PID
    fi
}

# Main deployment function
main() {
    print_header
    
    # Get user input
    read -p "Enter your GitHub username (or press Enter to skip): " GITHUB_USERNAME
    read -p "Enter repository name (default: access-shield-landing): " REPO_NAME
    if [ -n "$REPO_NAME" ]; then
        REPOSITORY_NAME="$REPO_NAME"
    fi
    
    echo
    echo "Select deployment type:"
    echo "1) Static hosting (GitHub Pages, Netlify, Vercel)"
    echo "2) Flask server"
    echo "3) Docker container"
    read -p "Enter choice (1-3): " DEPLOYMENT_CHOICE
    
    case $DEPLOYMENT_CHOICE in
        1) DEPLOYMENT_TYPE="static" ;;
        2) DEPLOYMENT_TYPE="flask" ;;
        3) DEPLOYMENT_TYPE="docker" ;;
        *) print_error "Invalid choice"; exit 1 ;;
    esac
    
    # Run deployment steps
    check_prerequisites
    install_dependencies
    init_git
    create_github_repo
    deploy_to_github
    
    if [ "$DEPLOYMENT_TYPE" = "static" ]; then
        deploy_to_netlify
        deploy_to_vercel
    fi
    
    test_deployment
    
    print_success "Deployment completed successfully!"
    echo
    print_info "Next steps:"
    print_info "1. Check your GitHub repository: https://github.com/$GITHUB_USERNAME/$REPOSITORY_NAME"
    print_info "2. Enable GitHub Pages in repository settings"
    print_info "3. Test your live site"
    print_info "4. Share with your team!"
    echo
    print_success "🎉 Your landing page is now live!"
}

# Run main function
main "$@"
