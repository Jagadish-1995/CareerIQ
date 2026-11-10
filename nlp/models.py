from pydantic import BaseModel, Field
from typing import List, Dict


class Education(BaseModel):

    degree: str = ""

    institution: str = ""

    specialization: str = ""

    year: str = ""


class Project(BaseModel):

    name: str = ""

    description: str = ""

    technologies: List[str] = []


class ResumeProfile(BaseModel):

    name: str = ""

    email: str = ""

    phone: str = ""

    linkedin: str = ""

    github: str = ""

    summary: str = ""

    education: List[Education] = Field(
        default_factory=list
    )

    skills: Dict[str, List[str]] = Field(
        default_factory=dict
    )

    experience: List[dict] = Field(
        default_factory=list
    )

    projects: List[Project] = Field(
        default_factory=list
    )

    certifications: List[str] = Field(
        default_factory=list
    )