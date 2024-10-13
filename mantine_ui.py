# component_cli.py

import json
import os
import shutil
from pathlib import Path
import typer
from rich.live import Live
from rich.table import Table
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()

BASE_DIR = Path("C:/Users/reedj/AppData/ui.mantine.dev/lib")

# Helper function to load attributes.json
def load_attributes(component_path: Path):
    attributes_file = component_path / "attributes.json"
    with open(attributes_file) as f:
        return json.load(f)

# 1. List all categories
@app.command("list-categories")
def list_categories():
    categories = set()
    for component_dir in BASE_DIR.iterdir():
        if component_dir.is_dir():
            attributes = load_attributes(component_dir)
            categories.add(attributes.get("category", "Unknown"))

    table = Table(title="Component Categories")
    table.add_column("Category", justify="left", style="cyan")
    for category in sorted(categories):
        table.add_row(category)

    console.print(table)

# 2. List all components
@app.command("list-components")
def list_components():
    table = Table(title="Components")
    table.add_column("Component Name", style="green")
    table.add_column("Category", style="cyan")

    for component_dir in BASE_DIR.iterdir():
        if component_dir.is_dir():
            attributes = load_attributes(component_dir)
            table.add_row(component_dir.name, attributes.get("category", "Unknown"))

    console.print(table)

# 3. List components filtered by category
@app.command("list-by-category")
def list_by_category(category: str):
    table = Table(title=f"Components in Category: {category}")
    table.add_column("Component Name", style="green")

    for component_dir in BASE_DIR.iterdir():
        if component_dir.is_dir():
            attributes = load_attributes(component_dir)
            if attributes.get("category") == category:
                table.add_row(component_dir.name)

    console.print(table)

# 4. Copy component to current or target directory
@app.command("copy-component")
def copy_component(component_name: str, target_dir: Path = Path(".")):
    source_dir = BASE_DIR / component_name
    if not source_dir.exists():
        print(f"[red]Component {component_name} does not exist![/red]")
        raise typer.Exit()

    shutil.copytree(source_dir, target_dir / component_name)
    print(f"[green]Component {component_name} copied to {target_dir}![/green]")

# 5. Add tag to component (by modifying attributes.json)
@app.command("add-tag")
def add_tag(component_name: str, tag: str):
    component_dir = BASE_DIR / component_name
    if not component_dir.exists():
        print(f"[red]Component {component_name} does not exist![/red]")
        raise typer.Exit()

    attributes = load_attributes(component_dir)
    tags = attributes.get("tags", [])
    tags.append(tag)
    attributes["tags"] = list(set(tags))  # Ensure no duplicate tags

    with open(component_dir / "attributes.json", "w") as f:
        json.dump(attributes, f, indent=2)

    print(f"[green]Tag {tag} added to {component_name}![/green]")

# 6. List components filtered by tag(s)
@app.command("list-by-tags")
def list_by_tags(tags: str):
    tag_list = tags.split(",")
    table = Table(title=f"Components with Tags: {', '.join(tag_list)}")
    table.add_column("Component Name", style="green")

    for component_dir in BASE_DIR.iterdir():
        if component_dir.is_dir():
            attributes = load_attributes(component_dir)
            component_tags = attributes.get("tags", [])
            if all(tag in component_tags for tag in tag_list):
                table.add_row(component_dir.name)

    console.print(table)

if __name__ == "__main__":
    app()
