"""
Browsing History Management
Tracks user navigation history
"""

from datetime import datetime
from typing import List

class BrowsingHistory:
    """Manages browsing history"""
    
    def __init__(self, max_entries=1000):
        self.entries: List[dict] = []
        self.max_entries = max_entries
        self.current_index = -1
        
    def add_entry(self, url, title=None):
        """
        Add a URL to history
        
        Args:
            url: The URL to add
            title: Optional page title
        """
        # Remove any forward history if we're not at the end
        if self.current_index < len(self.entries) - 1:
            self.entries = self.entries[:self.current_index + 1]
            
        # Check for duplicate consecutive entries
        if self.entries and self.entries[-1]['url'] == url:
            return
            
        entry = {
            'url': url,
            'title': title or url,
            'timestamp': datetime.now(),
            'visit_count': 1
        }
        
        # Check if URL already exists
        for existing_entry in self.entries:
            if existing_entry['url'] == url:
                existing_entry['visit_count'] += 1
                existing_entry['timestamp'] = datetime.now()
                self.current_index = self.entries.index(existing_entry)
                return
                
        self.entries.append(entry)
        
        # Limit history size
        if len(self.entries) > self.max_entries:
            self.entries.pop(0)
        else:
            self.current_index += 1
            
    def go_back(self):
        """
        Move to previous entry in history
        
        Returns:
            dict: The previous history entry or None
        """
        if self.current_index > 0:
            self.current_index -= 1
            return self.entries[self.current_index]
        return None
        
    def go_forward(self):
        """
        Move to next entry in history
        
        Returns:
            dict: The next history entry or None
        """
        if self.current_index < len(self.entries) - 1:
            self.current_index += 1
            return self.entries[self.current_index]
        return None
        
    def can_go_back(self) -> bool:
        """Check if we can go back"""
        return self.current_index > 0
        
    def can_go_forward(self) -> bool:
        """Check if we can go forward"""
        return self.current_index < len(self.entries) - 1
        
    def get_history(self, limit=50):
        """
        Get recent history entries
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            list: Recent history entries
        """
        return list(reversed(self.entries[-limit:]))
        
    def clear_history(self):
        """Clear all history"""
        self.entries.clear()
        self.current_index = -1
        
    def search_history(self, query) -> List[dict]:
        """
        Search history for entries matching the query
        
        Args:
            query: Search query (searches in URLs and titles)
            
        Returns:
            list: Matching history entries
        """
        query_lower = query.lower()
        results = []
        
        for entry in self.entries:
            if (query_lower in entry['url'].lower() or 
                query_lower in entry['title'].lower()):
                results.append(entry)
                
        return results
        
    def get_most_visited(self, limit=10):
        """
        Get the most frequently visited pages
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            list: Most visited entries sorted by visit count
        """
        sorted_entries = sorted(
            self.entries,
            key=lambda x: x['visit_count'],
            reverse=True
        )
        return sorted_entries[:limit]
