from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ProjectRequest:
    prompt: str


@dataclass
class DesignProfile:
    industry: str = "general"
    style: str = "modern"
    theme: str = "dark"
    framework: str = "nextjs"
    css: str = "tailwind"
    animations: List[str] = field(default_factory=list)


@dataclass
class PagePlan:
    name: str
    sections: List[str] = field(default_factory=list)


@dataclass
class ProjectPlan:
    title: str
    profile: DesignProfile
    pages: List[PagePlan] = field(default_factory=list)
    components: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)
    
