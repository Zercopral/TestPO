import allure
from jsonschema import validate


@allure.step('Validating schema')
def validate_schema(instance: dict, schema: dict) -> None:
    try:
        validate(instance=instance, schema=schema)
        return True
    except Exception as e:
        return False