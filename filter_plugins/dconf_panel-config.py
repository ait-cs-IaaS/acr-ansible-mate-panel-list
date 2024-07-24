from collections import defaultdict


class FilterModule(object):
    def filters(self):
        return {
            "launcher_object": self.launcher_object,
        }

    def launcher_object(self, properties, **kwargs):

        name = kwargs.get("name", None)

        new_launcher_object = {
            "object-type": "launcher",
            "toplevel-id": "top",
            "position": 20,
            "menu-path": "applications:/",
            "launcher-location": f"/usr/share/applications/{ name }.desktop",
        }

        new_launcher_object.update(properties)
        config_string = []

        section = f"{name}"
        config_string.append(f"\n[{section}]")

        for key, value in new_launcher_object.items():
            config_string.append(format_dconf_value(key, value))

        formated_config = "\n".join(config_string)

        return formated_config


def format_dconf_value(key, value):

    if isinstance(value, bool):
        # Convert Bollean to string
        return f"{key}={str(value).lower()}"

    if isinstance(value, int) or isinstance(value, list):
        # Values that cannot have quotes
        return f"{key}={value}"
    else:
        # Ensure values are wrapped with single quotes (')
        return f"{key}='{value}'"
