import os
import yaml


def get_config(root_key=None):
    path = os.getenv('CONFIG_PATH', 'dev_config.yml')

    try:
        with open(path) as f:
            d = yaml.load(f.read())
            return d if not root_key else d[root_key]
    except OSError as e:
        raise InvalidConfigError(
            """Config file {} not found.
            Use CONFIG_PATH environment variable.
            """.format(path)
        ) from e
    except KeyError as e:
        raise InvalidConfigError(
            "root_key {} not found in {}".format(
                root_key, path
            )
        ) from e


class InvalidConfigError(Exception):
    pass
