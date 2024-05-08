from zep_cloud.types.role_type import RoleType


def get_zep_message_role_type(role) -> RoleType:
    if role == "human":
        return "user"
    elif role == "ai":
        return "assistant"
    elif role == "system":
        return "system"
    elif role == "function":
        return "function"
    elif role == "tool":
        return "tool"
    else:
        return "system"