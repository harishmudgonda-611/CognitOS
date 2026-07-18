ENGINE_TEMPLATES = {
    "__init__.py": '''"""
{name} Engine
"""''',

    "service.py": '''class {name}Service:

    def __init__(self):
        pass
''',

    "config.py": '''CONFIG = {{
    "name": "{lower}",
    "enabled": True
}}
''',

    "events.py": '''EVENTS = []
''',

    "models.py": '''from dataclasses import dataclass


@dataclass
class {name}Model:
    id: str = ""
''',

    "README.md": '''# {name}

Generated automatically by Cognit Builder.
'''
}
