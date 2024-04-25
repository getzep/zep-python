from zep.types.models_role_type import ModelsRoleType


def get_zep_message_role_type(role) -> ModelsRoleType:
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