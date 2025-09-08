from pydantic import BaseModel, Field
from typing import Optional

class Course(BaseModel):
    id: str = Field(..., description="Unique identifier for the course")
    name: str = Field(..., max_length=100, description="Name of the course")
    description: Optional[str] = Field(None, max_length=500, description="Course description")
    is_active: bool = Field(default=True, description="Course active status")

class CourseContent(BaseModel):
    id: int = Field(..., description="Unique identifier for the course content")
    course_id: str = Field(..., description="ID of the associated course")
    title: str = Field(..., max_length=100, description="Title of the content")
    content: str = Field(..., description="Content details")
    is_published: bool = Field(default=False, description="Content published status")

class CourseContentSummary(BaseModel):
    id: int = Field(..., description="Unique identifier for the course content")
    title: str = Field(..., max_length=100, description="Title of the content")
    is_published: bool = Field(default=False, description="Content published status")

class CourseSummary(BaseModel):
    course_id: str = Field(..., description="ID of the associated course")
    content_summary: list[CourseContentSummary] = Field(..., description="List of course content summaries")

class UserInfo(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    name: str = Field(..., max_length=100, description="Name of the user")
    role: str = Field(..., max_length=50, description="Role of the user (e.g., student, instructor)")