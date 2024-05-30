Hier ist die Beschreibung für GitHub:

---

## Automatic Pip Updater

This Python script automates the process of upgrading `pip` and updating all outdated packages installed via `pip`.

### Features

- **Upgrade Pip**: Checks the current version of `pip` and upgrades it if necessary.
- **List Outdated Packages**: Retrieves a list of all outdated packages.
- **Update Packages**: Automatically updates all outdated packages to their latest versions.

### Usage

Run the script using Python:

```bash
python script_name.py
```

### Requirements

- Python 3.x
- `pip`

### Code Explanation

The script performs the following steps:

1. **Upgrade Pip**:
    - Displays the current `pip` version.
    - Upgrades `pip` to the latest version.
    - Displays the new `pip` version.

2. **Get Outdated Packages**:
    - Retrieves a list of all outdated packages in JSON format.

3. **Update Packages**:
    - Updates each outdated package to the latest version.
