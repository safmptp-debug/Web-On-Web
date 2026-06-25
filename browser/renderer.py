"""
Page Renderer
Handles HTML/CSS rendering and page processing
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class PageRenderer:
    """Renders web pages from HTML content"""
    
    def __init__(self):
        self.user_agent = 'Web-On-Web/1.0 (Python Browser)'
        self.timeout = 10
        
    def fetch_page(self, url):
        """
        Fetch a web page from the given URL
        
        Args:
            url: The URL to fetch
            
        Returns:
            dict: Contains 'status', 'content', 'html', and 'error' keys
        """
        try:
            headers = {'User-Agent': self.user_agent}
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            return {
                'status': 'success',
                'status_code': response.status_code,
                'content': response.content,
                'html': response.text,
                'url': response.url,
                'error': None
            }
        except requests.exceptions.Timeout:
            return {
                'status': 'error',
                'error': 'Request timeout',
                'html': self.get_error_page('Timeout', 'The page took too long to load')
            }
        except requests.exceptions.ConnectionError:
            return {
                'status': 'error',
                'error': 'Connection error',
                'html': self.get_error_page('Connection Error', 'Unable to connect to the server')
            }
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'html': self.get_error_page('Error', str(e))
            }
            
    def parse_html(self, html_content):
        """
        Parse HTML content using BeautifulSoup
        
        Args:
            html_content: The HTML content to parse
            
        Returns:
            BeautifulSoup: Parsed HTML object
        """
        return BeautifulSoup(html_content, 'html.parser')
        
    def extract_links(self, html_content, base_url):
        """
        Extract all links from HTML content
        
        Args:
            html_content: The HTML content
            base_url: The base URL for resolving relative links
            
        Returns:
            list: List of absolute URLs
        """
        soup = self.parse_html(html_content)
        links = []
        
        for link in soup.find_all('a', href=True):
            url = link['href']
            # Skip anchors and javascript links
            if url.startswith('#') or url.startswith('javascript:'):
                continue
            # Resolve relative URLs
            absolute_url = urljoin(base_url, url)
            links.append(absolute_url)
            
        return links
        
    def extract_images(self, html_content, base_url):
        """
        Extract all images from HTML content
        
        Args:
            html_content: The HTML content
            base_url: The base URL for resolving relative URLs
            
        Returns:
            list: List of image URLs
        """
        soup = self.parse_html(html_content)
        images = []
        
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                absolute_url = urljoin(base_url, src)
                images.append({
                    'url': absolute_url,
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })
                
        return images
        
    def extract_metadata(self, html_content):
        """
        Extract metadata from HTML content
        
        Args:
            html_content: The HTML content
            
        Returns:
            dict: Metadata including title, description, etc.
        """
        soup = self.parse_html(html_content)
        
        metadata = {
            'title': soup.title.string if soup.title else 'No title',
            'description': None,
            'keywords': None,
            'author': None
        }
        
        for meta in soup.find_all('meta'):
            name = meta.get('name', '').lower()
            content = meta.get('content', '')
            
            if name == 'description':
                metadata['description'] = content
            elif name == 'keywords':
                metadata['keywords'] = content
            elif name == 'author':
                metadata['author'] = content
                
        return metadata
        
    def get_error_page(self, title, message):
        """
        Generate an error page
        
        Args:
            title: Error title
            message: Error message
            
        Returns:
            str: HTML error page
        """
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error - {title}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .error-container {{
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                    text-align: center;
                }}
                h1 {{
                    color: #e74c3c;
                    margin-top: 0;
                }}
                p {{
                    color: #666;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <h1>⚠ {title}</h1>
                <p>{message}</p>
            </div>
        </body>
        </html>
        """
