import yaml


def is_valid_yml(block: str) -> bool:
    try:
        yaml.safe_load(block)
        return True
    except yaml.YAMLError:
        return False
