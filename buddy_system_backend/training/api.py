"""Training api."""
from buddy_system_backend import Training, Module
from buddy_system_backend.training.schema import CustomTrainingSchema


def create_training_w_modules(request_data):
    """Create training with modules."""
    schema = CustomTrainingSchema()
    training = schema.load(request_data)
    modules = training["modules"]

    del training["modules"]
    training_created = Training.create(**training)
    for module in modules:
        module["training_id"] = training_created.id
        Module.create(**module)

    return training_created


def update_training_w_modules(training_id, request_data):
    """Update training with modules."""
    training = Training.get_by_id(training_id)

    schema = CustomTrainingSchema()
    training_dict = schema.load(request_data)

    old_modules = []
    new_modules = []

    for module_dict in training_dict["modules"]:
        if module_dict.get("id"):
            module = Module.get_by_id(module_dict.get("id"))
            module_updated = module.update(**module_dict)
            old_modules.append(module_updated)
        else:
            new_modules.append(module_dict)

    training_dict["modules"] = old_modules
    print(training_dict)
    training_updated = training.update(**training_dict)

    for module in new_modules:
        module["training_id"] = training_updated.id
        Module.create(**module)

    return training_updated
