# Mantine Component CLI

[![PyPI version](https://badge.fury.io/py/mantine-component-cli.svg)](https://badge.fury.io/py/mantine-component-cli)

A command-line interface (CLI) tool for managing mantine UI components in a directory structure, built with `Typer` and `Rich`. The tool supports listing components by category, filtering by tags, copying components, and modifying their attributes.

## Features

- **List Categories**: List all component categories based on `attributes.json`.
- **List Components**: Display all components along with their categories.
- **Filter by Category**: List components filtered by a specific category.
- **Copy Components**: Copy a selected component to the current or target directory.
- **Add Tags**: Add a tag to a component by modifying its `attributes.json`.
- **Filter by Tags**: List components that have specific tags.

## Installation

You can install this CLI tool via PyPI:

```bash
pip install mantine-component-cli
```

List all categories:
```bash
mantine-component-cli list-categories
```
List all components:
```bash

mantine-component-cli list-components```
List components filtered by category:
```bash

mantine-component-cli list-by-category --category app-cards```
Copy a component to the current or target directory:
```bash

mantine-component-cli copy-component --component-name ActionsGrid --target-dir ./my-target-dir```
Add a tag to a component:
```bash

mantine-component-cli add-tag --component-name ActionsGrid --tag new-feature```
List components filtered by tag(s):
```bash

mantine-component-cli list-by-tags --tags new-feature,urgent```
### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.