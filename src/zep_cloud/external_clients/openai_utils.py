"""
Utility functions for Zep OpenAI integration.
"""

import logging
from typing import Any, Dict, List, Optional

from zep_cloud.types import Message

logger = logging.getLogger(__name__)


class ZepOpenAIError(Exception):
    """Base exception for Zep OpenAI wrapper errors."""

    pass


# Zep-specific parameters that should be filtered out before OpenAI calls
ZEP_PARAMS = {"session_id", "context_placeholder", "skip_zep_on_error"}


def extract_zep_params(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract Zep-specific parameters from kwargs.

    Args:
        kwargs: Dictionary of parameters

    Returns:
        Dictionary containing only Zep-specific parameters
    """
    return {k: kwargs.pop(k) for k in ZEP_PARAMS if k in kwargs}


def remove_zep_params(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove Zep-specific parameters from kwargs, returning a clean dict for OpenAI.

    Args:
        kwargs: Dictionary of parameters

    Returns:
        Dictionary with Zep parameters removed
    """
    return {k: v for k, v in kwargs.items() if k not in ZEP_PARAMS}


def has_context_placeholder(
    messages: List[Dict[str, Any]], placeholder: str = "{context}"
) -> bool:
    """
    Check if any message contains the context placeholder.

    Args:
        messages: List of message dictionaries
        placeholder: Context placeholder string to search for

    Returns:
        True if placeholder is found in any message content
    """
    if not placeholder:  # Empty placeholder doesn't make sense
        return False
    
    # Optimization: Context placeholders are typically in system messages or early messages
    # Search system messages first, then limit search to first few messages for performance
    system_messages = []
    other_messages = []
    
    for message in messages:
        if message.get("role") == "system":
            system_messages.append(message)
        else:
            other_messages.append(message)
    
    # Check system messages first (most likely to contain placeholders)
    for message in system_messages:
        content = message.get("content", "")
        if isinstance(content, str) and placeholder in content:
            return True
    
    # Check first 3 non-system messages (context placeholders are usually early in conversation)
    for message in other_messages[:3]:
        content = message.get("content", "")
        if isinstance(content, str) and placeholder in content:
            return True
    
    # If we have more than 3 non-system messages, check the rest (for completeness)
    if len(other_messages) > 3:
        for message in other_messages[3:]:
            content = message.get("content", "")
            if isinstance(content, str) and placeholder in content:
                return True
    
    return False


def inject_context(
    messages: List[Dict[str, Any]],
    context: Optional[str],
    placeholder: str = "{context}",
) -> List[Dict[str, Any]]:
    """
    Inject context into messages by replacing placeholder.

    Args:
        messages: List of message dictionaries
        context: Context string to inject (can be None)
        placeholder: Placeholder string to replace

    Returns:
        List of messages with context injected
    """
    if not context:
        context = ""

    processed_messages = []
    for message in messages:
        new_message = message.copy()
        content = message.get("content", "")

        if isinstance(content, str) and placeholder in content:
            new_message["content"] = content.replace(placeholder, context)

        processed_messages.append(new_message)

    return processed_messages


def extract_conversation_messages(messages: List[Dict[str, Any]], user_only: bool = False) -> List[Message]:
    """
    Extract conversation messages from OpenAI format and convert to Zep format.

    Args:
        messages: List of OpenAI format messages
        user_only: If True, only extract user messages (to avoid duplicating assistant messages)

    Returns:
        List of Zep Message objects for conversation messages only
    """
    conversation_messages = []

    for message in messages:
        role = message.get("role", "")
        content = message.get("content", "")

        # Filter based on user_only flag
        if user_only:
            # Only process user messages to avoid duplicating assistant messages
            if role == "user" and content:
                zep_message = Message(
                    role=role, role_type="user", content=content
                )
                conversation_messages.append(zep_message)
        else:
            # Process both user and assistant messages for conversation history
            if role in ["user", "assistant"] and content:
                # Map OpenAI roles to Zep roles
                zep_role = role
                zep_role_type = "user" if role == "user" else "assistant"

                zep_message = Message(
                    role=zep_role, role_type=zep_role_type, content=content
                )
                conversation_messages.append(zep_message)

    return conversation_messages


def safe_zep_operation(
    operation_func, skip_on_error: bool = True, operation_name: str = "Zep operation"
) -> Any:
    """
    Safely execute a Zep operation with error handling.

    Args:
        operation_func: Function to execute
        skip_on_error: Whether to skip/log errors or raise them
        operation_name: Name of the operation for logging

    Returns:
        Result of operation_func or None if error occurred

    Raises:
        Exception: If operation fails and skip_on_error is False
    """
    try:
        return operation_func()
    except Exception as e:
        if skip_on_error:
            logger.warning(f"{operation_name} failed: {e}")
            return None
        else:
            raise ZepOpenAIError(f"{operation_name} failed: {e}") from e


def normalize_messages_for_zep(
    messages: List[Dict[str, Any]], api_type: str = "chat"
) -> List[Message]:
    """
    Normalize different API message formats to Zep format.

    Args:
        messages: List of messages in OpenAI format
        api_type: Type of API ("chat" or "responses")

    Returns:
        List of normalized Zep Message objects
    """
    if api_type == "responses":
        return _convert_responses_messages_to_zep(messages)
    else:
        return _convert_chat_messages_to_zep(messages)


def _convert_chat_messages_to_zep(messages: List[Dict[str, Any]]) -> List[Message]:
    """Convert Chat Completions API messages to Zep format."""
    return extract_conversation_messages(messages)


def _convert_responses_messages_to_zep(messages: List[Dict[str, Any]]) -> List[Message]:
    """Convert Responses API messages to Zep format."""
    # For now, assume same format as chat. This can be extended based on actual API differences
    return extract_conversation_messages(messages)
