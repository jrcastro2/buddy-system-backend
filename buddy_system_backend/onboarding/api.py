"""Onboarding api."""
from buddy_system_backend import Training, Onboarding, User, Role, Template
from buddy_system_backend.onboarding.model import OnboardingUser, \
    OnboardingTaskUser
from buddy_system_backend.onboarding.schema import OnboardingSchema, \
    ModelOnboardingSchema


def update_onboarding(onboarding, request_data):
    """Updates onboarding."""
    schema = OnboardingSchema()
    model_schema = ModelOnboardingSchema()

    onboarding_dict = schema.load(request_data)
    trainings = Training.get_by_ids(onboarding_dict["trainings"])

    onboarding_model_dict = model_schema.load(request_data, partial=True)
    for item in onboarding_dict["users"]:
        user = User.get_by_id(item["user"])
        role = Role.get_by_id(item["role"])
        OnboardingUser.create(
            user=user, onboarding=onboarding, role=role
        )

    onboarding.trainings = trainings
    onboarding.update(**onboarding_model_dict)
    return onboarding


def create_onboarding(request_data):
    """Creates onboarding."""
    schema = OnboardingSchema()
    model_schema = ModelOnboardingSchema()

    onboarding_dict = schema.load(request_data)
    trainings = Training.get_by_ids(onboarding_dict.get("trainings", []))
    template = Template.get_by_id(onboarding_dict.get("template_id", ""))

    onboarding_model_dict = model_schema.load(request_data, partial=True)

    onboarding_created = Onboarding.create(**onboarding_model_dict)

    user_role_dict = {}

    for item in onboarding_dict["users"]:
        user = User.get_by_id(item["user"])
        role = Role.get_by_id(item["role"])
        user_role_dict[role.id] = user
        OnboardingUser.create(
            user=user, onboarding=onboarding_created, role=role
        )

    for section in template.sections:
        for task in section.tasks:
            OnboardingTaskUser.create(
                user=user_role_dict.get(task.role_id), onboarding=onboarding_created, task=task,
            )

    onboarding_created.trainings = trainings

    # TODO what happens if we send a non-existing training
    onboarding_created.save()
    return onboarding_created
