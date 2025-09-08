"""
Access Shield Client Landing Page
Professional landing page for client downloads and onboarding.
"""

import os
import json
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_file, redirect, url_for
from flask_socketio import SocketIO, emit
import logging

logger = logging.getLogger(__name__)

# Create Flask app for landing page
landing_app = Flask(__name__, 
                    template_folder='../ui/templates',
                    static_folder='../ui/static')
landing_app.config['SECRET_KEY'] = 'access_shield_landing_secret_key'
socketio = SocketIO(landing_app, cors_allowed_origins="*")

@landing_app.route('/')
def home():
    """Main landing page"""
    return render_template('landing_page.html')

@landing_app.route('/download')
def download_page():
    """Download page with package information"""
    return render_template('download_page.html')

@landing_app.route('/download/access-shield-client')
def download_client():
    """Download the Access Shield client package"""
    try:
        # In production, this would serve the actual client package
        # For demo, we'll create a placeholder package
        package_path = create_client_package()
        return send_file(
            package_path,
            as_attachment=True,
            download_name='AccessShield-Client-v1.0.0.exe',
            mimetype='application/octet-stream'
        )
    except Exception as e:
        logger.error(f"Error serving client package: {e}")
        return jsonify({'error': 'Package not available'}), 404

@landing_app.route('/download/access-shield-server')
def download_server():
    """Download the Access Shield server package"""
    try:
        # In production, this would serve the actual server package
        package_path = create_server_package()
        return send_file(
            package_path,
            as_attachment=True,
            download_name='AccessShield-Server-v1.0.0.zip',
            mimetype='application/zip'
        )
    except Exception as e:
        logger.error(f"Error serving server package: {e}")
        return jsonify({'error': 'Package not available'}), 404

@landing_app.route('/api/client-info')
def get_client_info():
    """Get client package information"""
    return jsonify({
        'success': True,
        'client_package': {
            'name': 'Access Shield Client',
            'version': '1.0.0',
            'size': '45.2 MB',
            'platform': 'Windows 10/11, macOS, Linux',
            'requirements': {
                'os': 'Windows 10+, macOS 10.15+, Ubuntu 18.04+',
                'ram': '4 GB minimum, 8 GB recommended',
                'storage': '500 MB free space',
                'network': 'Internet connection required'
            },
            'features': [
                'GitHub organization access governance',
                'Real-time security monitoring',
                'Policy compliance checking',
                'AI-powered threat detection',
                'Multi-channel notifications',
                'Audit logging and reporting',
                'Client feedback system',
                'Framework update management'
            ],
            'last_updated': datetime.now().isoformat()
        }
    })

@landing_app.route('/api/server-info')
def get_server_info():
    """Get server package information"""
    return jsonify({
        'success': True,
        'server_package': {
            'name': 'Access Shield Server',
            'version': '1.0.0',
            'size': '125.8 MB',
            'platform': 'Docker, Kubernetes, Cloud',
            'requirements': {
                'os': 'Linux (Ubuntu 20.04+ recommended)',
                'ram': '8 GB minimum, 16 GB recommended',
                'storage': '10 GB free space',
                'network': 'Internet connection required',
                'database': 'PostgreSQL 12+'
            },
            'features': [
                'Centralized access governance',
                'Multi-tenant support',
                'REST API and webhooks',
                'Advanced analytics and reporting',
                'Enterprise-grade security',
                'Scalable architecture',
                'Cloud deployment ready',
                'High availability support'
            ],
            'last_updated': datetime.now().isoformat()
        }
    })

@landing_app.route('/api/download-stats')
def get_download_stats():
    """Get download statistics"""
    return jsonify({
        'success': True,
        'stats': {
            'total_downloads': 1247,
            'client_downloads': 892,
            'server_downloads': 355,
            'active_installations': 156,
            'last_24h_downloads': 23
        }
    })

@landing_app.route('/onboarding')
def onboarding():
    """Client onboarding page"""
    return render_template('client_onboarding.html')

@landing_app.route('/support')
def support():
    """Support and documentation page"""
    return render_template('client_support.html')

@landing_app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # In production, this would save to database and send notifications
        logger.info(f"Contact form submission: {data}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message. We will get back to you within 24 hours.'
        })
        
    except Exception as e:
        logger.error(f"Error processing contact form: {e}")
        return jsonify({
            'success': False,
            'error': 'Failed to process your message'
        }), 500

def create_client_package():
    """Create client package (placeholder for demo)"""
    # In production, this would create the actual executable package
    package_path = 'client_delivery/packages/AccessShield-Client-v1.0.0.exe'
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(package_path), exist_ok=True)
    
    # Create a placeholder file (in production, this would be the actual executable)
    if not os.path.exists(package_path):
        with open(package_path, 'wb') as f:
            f.write(b'Access Shield Client Package - Demo Version')
    
    return package_path

def create_server_package():
    """Create server package (placeholder for demo)"""
    # In production, this would create the actual server package
    package_path = 'client_delivery/packages/AccessShield-Server-v1.0.0.zip'
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(package_path), exist_ok=True)
    
    # Create a placeholder file (in production, this would be the actual server package)
    if not os.path.exists(package_path):
        with open(package_path, 'wb') as f:
            f.write(b'Access Shield Server Package - Demo Version')
    
    return package_path

@socketio.on('connect')
def handle_connect():
    """Handle WebSocket connection"""
    logger.info('Landing page client connected')
    emit('status', {'message': 'Connected to Access Shield landing page'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection"""
    logger.info('Landing page client disconnected')

def run_landing_page(host='localhost', port=8080, debug=False):
    """Run the landing page"""
    logger.info(f"Starting Access Shield landing page on {host}:{port}")
    socketio.run(landing_app, host=host, port=port, debug=debug)

if __name__ == "__main__":
    run_landing_page(debug=True)









