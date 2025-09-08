#!/usr/bin/env python3
"""
Simple launcher for the Access Shield landing page.
Opens the HTML file in the user's default browser.
"""

import webbrowser
import os
import sys
from pathlib import Path

def launch_landing_page():
    """Launch the landing page in the default browser."""
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    landing_page_path = script_dir / "landing_page.html"
    
    # Check if the landing page file exists
    if not landing_page_path.exists():
        print(f"Error: Landing page file not found at {landing_page_path}")
        print("Please ensure landing_page.html is in the same directory as this script.")
        return False
    
    # Convert to file:// URL
    landing_page_url = landing_page_path.as_uri()
    
    print("🚀 Launching Access Shield Landing Page...")
    print(f"📄 Opening: {landing_page_url}")
    
    try:
        # Open in default browser
        webbrowser.open(landing_page_url)
        print("✅ Landing page opened successfully!")
        print("\n📋 What's next:")
        print("   1. Browse the features and download options")
        print("   2. Download the appropriate package for your platform")
        print("   3. Follow the setup wizard to get started")
        print("\n💡 Tip: You can bookmark this page for future reference")
        return True
        
    except Exception as e:
        print(f"❌ Error opening landing page: {e}")
        print(f"\n🔧 Manual workaround:")
        print(f"   Open your browser and navigate to: {landing_page_url}")
        return False

def main():
    """Main entry point."""
    print("=" * 60)
    print("🛡️  Access Shield - Landing Page Launcher")
    print("=" * 60)
    
    success = launch_landing_page()
    
    if success:
        print("\n🎉 Enjoy exploring Access Shield!")
    else:
        print("\n😞 Something went wrong. Please try the manual workaround above.")
        sys.exit(1)

if __name__ == "__main__":
    main()






