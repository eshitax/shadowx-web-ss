from flask import Flask, request, send_file, render_template, jsonify
from flask_cors import CORS
from io import BytesIO
import requests
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

THUM_IO_BASE = "https://image.thum.io"

# Store screenshot history
screenshot_history = []

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html', history=screenshot_history)

@app.route('/ss', methods=['GET'])
def take_screenshot():
    """
    API endpoint to take website screenshots
    
    Query Parameters:
    - url: Website URL (required)
    - size: default, resized, full, custom (optional, default: default)
    - width: Custom width in pixels (for size=custom)
    - height: Custom height in pixels (for size=custom)
    """
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400
    
    size = request.args.get('size', 'default')
    width = request.args.get('width', type=int)
    height = request.args.get('height', type=int)
    
    try:
        # Clean URL
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Build Thum.io URL path
        path_parts = ['get']
        
        if size == 'resized':
            path_parts.extend(['width', '400', 'height', '300'])
        elif size == 'full':
            path_parts.append('fullpage')
            path_parts.extend(['width', '1200'])
        elif size == 'custom':
            if width:
                path_parts.extend(['width', str(width)])
            if height:
                path_parts.extend(['height', str(height)])
            if not width and not height:
                path_parts.extend(['width', '600'])
        
        path_parts.append(url)
        
        # Build full URL
        image_url = f"{THUM_IO_BASE}/{'/'.join(path_parts)}"
        
        # Fetch screenshot
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Store in history
        screenshot_history.append({
            'url': url,
            'size': size,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'image_url': image_url
        })
        if len(screenshot_history) > 50:
            screenshot_history.pop(0)
        
        # Return image
        return send_file(
            BytesIO(response.content),
            mimetype='image/png',
            as_attachment=False,
            download_name=f'screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        )
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch screenshot: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get screenshot history"""
    return jsonify(screenshot_history)

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """Clear screenshot history"""
    screenshot_history.clear()
    return jsonify({'message': 'History cleared'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)