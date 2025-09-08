from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from schame import CourseSummary, CourseContent, UserInfo, CourseContentSummary
from COURSES import course as course_obj, course_content as course_content_list
# Initialize FastMCP server with enhanced metadata for 2025-06-18 spec
mcp : FastMCP = FastMCP(
    name="cotutor-server",
    stateless_http=True # When true we don't need handshake or initialize things.
)

@mcp.tool()
def user_info(user_id: str) -> UserInfo:
    """Return user information for a given user ID."""
    # Dummy implementation, replace with actual user retrieval logic
    users = [
        UserInfo(user_id="1", name="Zeeshan", role="student"),
        UserInfo(user_id="2", name="Zain", role="student")
    ]
    for user in users:
        if user.user_id == user_id:
            return user
    return {"error": "User not found"}

@mcp.tool()
def course_summary(course_id: str) -> CourseSummary:
    """Return a summary of course content titles for a given course ID."""
    if course_id not in [course.id for course in course_obj]:
        raise ValueError("Course not found")
    summary = CourseSummary(
        course_id=course_id,
        content_summary= [
            CourseContentSummary(
                id=content.id,
                title=content.title,
                is_published=content.is_published
            ) for content in course_content_list if content.course_id == course_id
        ]
    )
    return summary

@mcp.tool()
def course_content(course_id: str, content_id: str) -> CourseContent:
    "Return detailed content for a specific course and content ID."
    for content in course_content_list:
        if content.course_id == course_id and content.id == int(content_id):
            return content
    raise ValueError("Course content not found")

mcp_app : Starlette = mcp.streamable_http_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:mcp_app", host="127.0.0.1", port=8001, reload=True)
