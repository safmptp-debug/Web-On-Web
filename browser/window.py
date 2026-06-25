"""
Main Browser Window
Handles the UI and browser controls
"""

from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
    QPushButton, QLineEdit, QLabel, QMessageBox, QTabWidget
)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

from browser.renderer import PageRenderer
from browser.history import BrowsingHistory

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web On Web - Python Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize components
        self.history = BrowsingHistory()
        self.renderer = PageRenderer()
        self.current_url = ""
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Top navigation bar
        nav_layout = QHBoxLayout()
        
        # Back button
        self.back_btn = QPushButton("◀ Back")
        self.back_btn.clicked.connect(self.go_back)
        nav_layout.addWidget(self.back_btn)
        
        # Forward button
        self.forward_btn = QPushButton("Forward ▶")
        self.forward_btn.clicked.connect(self.go_forward)
        nav_layout.addWidget(self.forward_btn)
        
        # Refresh button
        self.refresh_btn = QPushButton("⟳ Refresh")
        self.refresh_btn.clicked.connect(self.refresh_page)
        nav_layout.addWidget(self.refresh_btn)
        
        # Home button
        self.home_btn = QPushButton("⌂ Home")
        self.home_btn.clicked.connect(self.go_home)
        nav_layout.addWidget(self.home_btn)
        
        main_layout.addLayout(nav_layout)
        
        # URL bar
        url_layout = QHBoxLayout()
        url_label = QLabel("URL:")
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL or search...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_bar)
        
        main_layout.addLayout(url_layout)
        
        # Tabs
        self.tab_widget = QTabWidget()
        self.add_new_tab()
        
        main_layout.addWidget(self.tab_widget)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        central_widget.setLayout(main_layout)
        
    def add_new_tab(self):
        """Add a new browser tab"""
        tab = QWebEngineView()
        tab.setUrl(QUrl("about:blank"))
        
        tab_index = self.tab_widget.addTab(tab, "New Tab")
        self.tab_widget.setCurrentIndex(tab_index)
        
        # Load home page
        self.load_home_page(tab)
        
    def load_home_page(self, tab):
        """Load the home page"""
        home_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Web On Web - Home</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 50px;
                    border-radius: 10px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                }
                h1 {
                    color: #333;
                    margin: 0;
                }
                p {
                    color: #666;
                    font-size: 18px;
                }
                .features {
                    margin-top: 30px;
                    text-align: left;
                }
                .feature {
                    margin: 10px 0;
                    padding: 10px;
                    background: #f0f0f0;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌐 Welcome to Web On Web</h1>
                <p>A Python-based Web Browser</p>
                <div class="features">
                    <h3>Features:</h3>
                    <div class="feature">✓ HTML/CSS Rendering</div>
                    <div class="feature">✓ Web Navigation</div>
                    <div class="feature">✓ Tab Support</div>
                    <div class="feature">✓ History Management</div>
                    <div class="feature">✓ Multiple Downloads</div>
                </div>
            </div>
        </body>
        </html>
        """
        tab.setHtml(home_html)
        
    def navigate_to_url(self):
        """Navigate to the URL entered in the address bar"""
        url = self.url_bar.text()
        if not url:
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        self.current_url = url
        
        try:
            current_tab = self.tab_widget.currentWidget()
            if current_tab:
                current_tab.setUrl(QUrl(url))
                self.url_bar.setText(url)
                self.history.add_entry(url)
                self.statusBar().showMessage(f"Loading {url}...")
        except Exception as e:
            self.statusBar().showMessage(f"Error: {str(e)}")
            
    def go_back(self):
        """Go back in history"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab and current_tab.history().canGoBack():
            current_tab.history().back()
            
    def go_forward(self):
        """Go forward in history"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab and current_tab.history().canGoForward():
            current_tab.history().forward()
            
    def refresh_page(self):
        """Refresh the current page"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            current_tab.reload()
            self.statusBar().showMessage("Refreshing page...")
            
    def go_home(self):
        """Go to home page"""
        current_tab = self.tab_widget.currentWidget()
        if current_tab:
            self.load_home_page(current_tab)
            self.url_bar.setText("about:home")
