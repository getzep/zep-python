"""
Message cache for preventing duplicate messages in Zep integration.
"""

import threading
from datetime import datetime
from typing import Dict, Optional, Set, Tuple


class MessageCache:
    """
    Thread-safe cache for tracking messages to prevent duplicates.
    
    Uses a combination of thread_id, role, content hash, and timestamp window
    to identify duplicate messages.
    """
    
    def __init__(self):
        """Initialize the message cache with thread-safe storage."""
        self._cache: Dict[str, Set[Tuple[str, str, float]]] = {}
        self._lock = threading.RLock()
        
    def is_message_seen(self, thread_id: str, role: str, content: str, created_at: datetime) -> bool:
        """
        Check if a message has been seen before to prevent duplicates.
        
        Args:
            thread_id: The thread/session ID
            role: Message role ("user" or "assistant")
            content: The message content
            created_at: When the message was created
            
        Returns:
            True if message was already seen, False if it's new
        """
        if not content or not content.strip():
            return True  # Empty messages are considered duplicates
            
        # Create a simple hash of the content for comparison
        content_hash = str(hash(content.strip()))
        timestamp = created_at.timestamp()
        
        message_key = (role, content_hash, timestamp)
        
        with self._lock:
            # Initialize thread cache if it doesn't exist
            if thread_id not in self._cache:
                self._cache[thread_id] = set()
                
            thread_cache = self._cache[thread_id]
            
            # Check for exact match first
            if message_key in thread_cache:
                return True
                
            # Check for near-duplicate messages (same role, content, within 1 second)
            for cached_role, cached_hash, cached_timestamp in thread_cache:
                if (cached_role == role and 
                    cached_hash == content_hash and 
                    abs(cached_timestamp - timestamp) < 1.0):
                    return True
                    
            # Message is new, add to cache
            thread_cache.add(message_key)
            
            # Clean up old entries (keep only last 1000 messages per thread)
            if len(thread_cache) > 1000:
                # Remove oldest entries
                sorted_entries = sorted(thread_cache, key=lambda x: x[2])
                self._cache[thread_id] = set(sorted_entries[-1000:])
                
            return False
            
    def clear_thread(self, thread_id: str) -> None:
        """
        Clear cache for a specific thread.
        
        Args:
            thread_id: The thread ID to clear
        """
        with self._lock:
            self._cache.pop(thread_id, None)
            
    def clear_all(self) -> None:
        """Clear all cached messages."""
        with self._lock:
            self._cache.clear()


# Global cache instance
_message_cache: Optional[MessageCache] = None
_cache_lock = threading.RLock()


def get_message_cache() -> MessageCache:
    """
    Get the global message cache instance.
    
    Returns:
        MessageCache: Thread-safe message cache instance
    """
    global _message_cache
    
    if _message_cache is None:
        with _cache_lock:
            if _message_cache is None:
                _message_cache = MessageCache()
                
    return _message_cache