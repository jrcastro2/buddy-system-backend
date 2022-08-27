"""Section api."""
from buddy_system_backend import Section, Task


def create_section_and_tasks(sections, template_id):
    """Create sections with tasks."""

    for section in sections:
        tasks = section["tasks"]
        del section["tasks"]
        section["template_id"] = template_id
        section = Section.create(**section)
        for task in tasks:
            task["section_id"] = section.id
            Task.create(**task)
