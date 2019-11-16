# tk-entities

Shotgun application that displays the list of shotgun entities and
corresponding fields.

![Screenshot-1.png](Screenshot-1.png)
***
### How to install
```
env/includes/app_locations.yml:
```
```yml
# entities
apps.tk-entities.location:
  type: git
  name: tk-entities
  path: https://github.com/ymesh/tk-entities.git
  version: v0.0.1
```

```
env/includes/settings/tk-desktop.yml:
```

```yml
includes:
- ../app_locations.yml
...
# project
settings.tk-desktop.project:
  apps:
    ...
    tk-entities:
        location: "@apps.tk-entities.location"
```
---

Copy the repository folder inside your pipeline config:
```
config
install
    apps
    app_store
    core
    engines
    git
        tk-entities.git
            v0.0.1
                <git repository content>

```
Then, inside your pipeline config folder, run command:
```
./tank cache_apps
```