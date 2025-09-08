# 🚀 Landing Page Deployment Guide

This guide covers various deployment options for your Access Shield landing page.

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for version control)
- Web server (for production)

## 🌐 Deployment Options

### 1. Static Hosting (Recommended for Demos)

#### GitHub Pages
```bash
# 1. Create a new repository
git init
git add .
git commit -m "Initial commit"

# 2. Push to GitHub
git remote add origin https://github.com/yourusername/access-shield-landing.git
git push -u origin main

# 3. Enable GitHub Pages
# Go to Settings > Pages > Source: Deploy from a branch
# Select main branch and / (root) folder
```

#### Netlify
```bash
# 1. Build your site
# (landing_page.html is already built)

# 2. Deploy to Netlify
# Option A: Drag and drop landing_page.html to Netlify
# Option B: Connect GitHub repository
# Option C: Use Netlify CLI
npm install -g netlify-cli
netlify deploy --prod --dir .
```

#### Vercel
```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy
vercel --prod
```

### 2. Web Server Deployment

#### Apache
```apache
# .htaccess file
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ landing_page.html [QSA,L]

# Enable mod_rewrite
# sudo a2enmod rewrite
# sudo systemctl restart apache2
```

#### Nginx
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/landing/page;
    index landing_page.html;

    location / {
        try_files $uri $uri/ /landing_page.html;
    }
}
```

### 3. Flask Server Deployment

#### Production WSGI Server
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 landing_page:landing_app
```

#### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "landing_page.py"]
```

```bash
# Build and run
docker build -t access-shield-landing .
docker run -p 8080:8080 access-shield-landing
```

## 🔧 Configuration

### Environment Variables
```bash
# Flask configuration
export FLASK_ENV=production
export FLASK_DEBUG=False
export SECRET_KEY=your-secret-key

# Server configuration
export HOST=0.0.0.0
export PORT=8080
```

### SSL/HTTPS Setup
```bash
# Using Let's Encrypt
sudo apt install certbot python3-certbot-apache
sudo certbot --apache -d yourdomain.com

# Or with Nginx
sudo certbot --nginx -d yourdomain.com
```

## 📊 Monitoring & Analytics

### Google Analytics
```html
<!-- Add to <head> section -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Performance Monitoring
```html
<!-- Add to <head> section -->
<script>
  // Performance monitoring
  window.addEventListener('load', function() {
    const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
    console.log('Page load time:', loadTime + 'ms');
  });
</script>
```

## 🔒 Security Considerations

### HTTPS Only
```apache
# .htaccess
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Security Headers
```apache
# .htaccess
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

## 📈 Performance Optimization

### Minification
```bash
# Install minification tools
npm install -g html-minifier cssnano-cli uglify-js

# Minify HTML
html-minifier --collapse-whitespace --remove-comments --minify-js --minify-css landing_page.html -o landing_page.min.html

# Minify CSS
cssnano landing_page.css landing_page.min.css

# Minify JavaScript
uglifyjs landing_page.js -o landing_page.min.js
```

### CDN Integration
```html
<!-- Use CDN for external resources -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

## 🧪 Testing

### Local Testing
```bash
# Test static version
python -m http.server 8000
# Access at http://localhost:8000

# Test Flask version
python landing_page.py
# Access at http://localhost:8080
```

### Production Testing
```bash
# Test with curl
curl -I http://yourdomain.com
curl -I https://yourdomain.com

# Test performance
curl -w "@curl-format.txt" -o /dev/null -s http://yourdomain.com
```

## 📝 Maintenance

### Regular Updates
- Update dependencies monthly
- Check for security vulnerabilities
- Monitor performance metrics
- Update content as needed

### Backup Strategy
```bash
# Backup landing page
tar -czf landing_page_backup_$(date +%Y%m%d).tar.gz LANDING_PAGE_PACKAGE/

# Backup to cloud
aws s3 cp landing_page_backup_$(date +%Y%m%d).tar.gz s3://your-backup-bucket/
```

## 🆘 Troubleshooting

### Common Issues

#### 1. Page Not Loading
- Check file permissions
- Verify web server configuration
- Check firewall settings

#### 2. CSS/JS Not Loading
- Check file paths
- Verify MIME types
- Check browser console for errors

#### 3. Flask Server Issues
- Check Python version
- Verify dependencies
- Check port availability

### Debug Mode
```bash
# Enable debug mode
export FLASK_DEBUG=True
python landing_page.py
```

## 📞 Support

For deployment issues:
- Check the troubleshooting section
- Review server logs
- Contact system administrator
- Create GitHub issue

---

**Happy Deploying! 🚀**
