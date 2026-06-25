"""
Web On Web - Flask Web Browser
Main entry point for the web application
"""

from flask import Flask, render_template, request, jsonify
from browser.renderer import PageRenderer
from browser.history import BrowsingHistory
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'web-on-web-secret-key'

# Global instances
renderer = PageRenderer()
history = BrowsingHistory()

@app.route('/')
def index():
    """Render the main browser page"""
    return render_template('index.html')

@app.route('/api/navigate', methods=['POST'])
def navigate():
    """Navigate to a URL"""
    data = request.json
    url = data.get('url', '')
    
    if not url:
        return jsonify({'error': 'URL required'}), 400
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Fetch the page
    result = renderer.fetch_page(url)
    
    # Add to history
    if result['status'] == 'success':
        history.add_entry(url)
    
    return jsonify(result)

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get browsing history"""
    limit = request.args.get('limit', 50, type=int)
    hist = history.get_history(limit)
    return jsonify(hist)

@app.route('/api/history/search', methods=['GET'])
def search_history():
    """Search history"""
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    results = history.search_history(query)
    return jsonify(results)

@app.route('/api/history/most-visited', methods=['GET'])
def most_visited():
    """Get most visited pages"""
    limit = request.args.get('limit', 10, type=int)
    pages = history.get_most_visited(limit)
    return jsonify(pages)

@app.route('/api/history/clear', methods=['POST'])
def clear_history():
    """Clear all history"""
    history.clear_history()
    return jsonify({'status': 'success'})

@app.route('/api/extract/links', methods=['POST'])
def extract_links():
    """Extract links from HTML"""
    data = request.json
    html = data.get('html', '')
    base_url = data.get('base_url', '')
    
    links = renderer.extract_links(html, base_url)
    return jsonify({'links': links})

@app.route('/api/extract/images', methods=['POST'])
def extract_images():
    """Extract images from HTML"""
    data = request.json
    html = data.get('html', '')
    base_url = data.get('base_url', '')
    
    images = renderer.extract_images(html, base_url)
    return jsonify({'images': images})

@app.route('/api/extract/metadata', methods=['POST'])
def extract_metadata():
    """Extract metadata from HTML"""
    data = request.json
    html = data.get('html', '')
    
    metadata = renderer.extract_metadata(html)
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
