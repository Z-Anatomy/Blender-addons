# Z-Label Add-on for Blender

## Description

Z-Label is a Blender add-on designed for anatomical labeling workflows. It enables automatic creation, positioning, and management of text labels attached to mesh vertices with associated line objects. The add-on provides precise hierarchy control and selection behavior tailored for anatomy-focused 3D annotation.

## Features

- Create labels from selected meshes with connected line objects (`.j` suffix).
- Position labels automatically above selected vertices with hook modifiers created on the line.
- Only direct `.j` lines follow label movement; other children remain fixed.
- Toggle selectability of all line objects via a checkbox in the UI.
- Convert label location transforms into delta transforms for animation workflows.
- Intuitive panel access in the "Z-Anatomy" sidebar tab.

## Installation

1. Download the add-on zip or `.py` file.
2. In Blender, go to `Edit > Preferences > Add-ons`.
3. Use the `Install...` button to select the downloaded file.
4. Enable the add-on from the list.

## Usage

- **Convert Meshes to Labels**:
  Select meshes and click **Convert Selected to Labels**.
- **Position Label + Hook**:
  In Edit Mode select a vertex, select the label, and click **Position label + hook automatically**.
- **Convert Location to Delta**:
  Select one or more labels and press **Convert location to delta**.
- **Toggle Line Selectability**:
  Use the checkbox at the bottom of the panel to toggle `.j` lines selectability.

## Author

- Marcin Zieliński  
- Gauthier KERVYN

## Compatibility

- Blender 2.80 and newer.

## License

Distributed under the [CC-BY-SA 4.0](LICENSE) license.

---

# Z-Anatomy Add-ons for Blender

A curated collection of Blender add-ons to streamline Z-Anatomy workflows: annotations, cross-sections, colors, translations, and more.

**Author**: Marcin Zieliński, Gauthier KERVYN  
**License**: [CC-BY-SA 4.0](LICENSE)  
**Compatibility**: Blender 2.80+

## 📦 Add-ons List

### 1. Z-Cross
**Description**: Manage cross-sections and cutting planes.  
**Features**:
- Integrates a node-group for cut materials.
- Named cutting planes support.
- Works with collections or objects.

---

### 2. Z-Def
**Description**: Syncs Blender text editor to `.txt` file matching the active object's data name.

---

### 3. Z-Hide
**Description**: Keeps lights on in local view and when hiding objects (under development).

---

### 4. Z-KeyColors
**Description**: Manage key colors for objects and collections.

---

### 5. Z-Label
**Description**: Creates labels from scratches: text + connecting lines.

---

### 6. Z-Label2
**Description**: Converts existing objects into labels for annotation purposes.

---

### 7. Z-List
**Description**: Copies selected object names for documentation or scripting.

---

### 8. Z-Mirror
**Description**: Toggle Mirror modifiers for mesh collections.

---

### 9. Z-Sync
**Description**: Synchronize render and viewport visibility of objects.

---

### 10. Z-Translate
**Description**: Switch languages and import translations for object names and data.

---

### 11. Z-Wiki
**Description**: Download Wikipedia articles into Blender's text editor.

---
