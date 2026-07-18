class BuilderError(Exception):
    """Base Builder exception."""


class ModuleExistsError(BuilderError):
    """Raised when a module already exists."""


class InvalidModuleNameError(BuilderError):
    """Raised when a module name is invalid."""


class TemplateNotFoundError(BuilderError):
    """Raised when a template cannot be found."""
