from schame import Course, CourseContent


course : list[Course] = [
    Course(
    id="AI-001",
    name="Introduction to Prompt Engineering",
    description="Learn the basics of prompt engineering.",
    is_active=True
    ),
    Course(
        id="Python-101",
        name="Advanced Prompt Engineering",
        description="Deep dive into advanced techniques of prompt engineering.",
        is_active=False
    )
]

course_content : list[CourseContent] = [
    CourseContent(
    id=1,
    course_id="AI-001",
    title="Getting Started with Prompt Engineering",
    # Read content from markdown file
    content=open("00_prompt_engineering/readme.md", encoding="utf-8").read(),
    is_published=True
),
    CourseContent(
        id=2,
        course_id="AI-001",
        title="Context Engineering",
        content=open("00_prompt_engineering/context_engineering_tutorial.md", encoding="utf-8").read(),
        is_published=True
    ),
    CourseContent(
        id=3,
        course_id="AI-001",
        title="Six Part Prompting Framework",
        content=open("00_prompt_engineering/six_part_prompting_framework.md", encoding="utf-8").read(),
        is_published=False
    )
]

