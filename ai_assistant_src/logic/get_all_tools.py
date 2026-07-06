from tools.tools import AgentTool


def get_all_tools_list():
    tools_child = [x() for x in AgentTool.__subclasses__()]

    tools = [
        {
            "type": "function",
            "function": {
                "name": t.get_name(),
                "description": t.get_description(),
                "parameters": t.get_parameters(),
            }
        }
        for t in tools_child
    ]

    return tools
