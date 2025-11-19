from langchain_core.tools import tool

@tool(parse_docstring=True)
def create_environment(name: str) -> str:
    """Create a new environment.

    Args:
        name: The name of the environment to create.

    Returns:
        A message indicating the result of the operation.
    """
    return f"Environment '{name}' created."

@tool(parse_docstring=True)
def check_permission(username: str) -> bool:
    """Check if the user has permission.

    Args:
        username: The name of the user to check.

    Returns:
        True if the user has permission, False otherwise.
    """
    if(username == "weiqiang"):
        return True
    else:
        return False