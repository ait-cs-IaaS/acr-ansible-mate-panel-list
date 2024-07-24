# Ansible-Role: acr-ansible-mate-panel-list

AIT-CyberRange: Customizes ubuntu mate desktop environment.


## Requirements

- Debian or Ubuntu 

## Role Variables

**Example config:**

```yaml
client_launcher_objects:
  caja-filebrowser:
    position: 15
  firefox:
    position: 20
  thunderbird:
    position: 25
  mate-terminal:
    position: 30
```

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - acr-ansible-mate-panel-list
```

## License

GPL-3.0

## Author

- Lenhard Reuter