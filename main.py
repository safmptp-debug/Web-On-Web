#!/usr/bin/env python3
"""
Web On Web - A Python-based Web Browser
Main entry point for the application
"""

import sys
from PyQt5.QtWidgets import QApplication
from browser.window import BrowserWindow

def main():
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
