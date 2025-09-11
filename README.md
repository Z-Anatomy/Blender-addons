# Z-Anatomy Add-ons for Blender

A collection of Blender add-ons designed to streamline workflows for Z-Anatomy: cross-sections, labels, colors, translations, documentation, and more.

**Author**: Marcin Zieliński
**License**: [CC-BY-SA 4.0](LICENSE)
**Compatibility**: Blender 2.80 and later

---

## 📦 Add-ons List

### 1. Z-Cross
**Description**: Manage cross-sections and cutting planes.
**Features**:
- Integrates a specific node-group into all materials.
- Manages named cutting planes (X, Y, Z).
- Supports collections and individual objects.
**Included Files**:
- `Cross-sections.blend` (example node-group and cutting planes).

---

### 2. Z-Def
**Description**: Syncs the text editor with a `.txt` file matching the active object's data name.
**Features**:
- Automatic text editor synchronization.
- Toggle sync via a dedicated panel.

---

### 3. Z-Hide
**Description**: Maintains lights on in local view and when hiding other objects.
**Note**: It still needs to be fixed. Please help.

---

### 4. Z-KeyColors
**Description**: Manage key colors for objects and collections.
**Features**:
- Assign and toggle "Key Color" property.
- Automatic UI updates.
**Included Files**:
- Example `.blend` file showing material structure.

---

### 5. Z-Label
**Description**: Create and manage text labels at vertices.
**Features**:
- Create custom labels at selected vertices.
- Use existing text names as labels.
- Convert label transforms to delta.
- Easy label editing via UI panel.

---

### 6. Z-Sync
**Description**: Sync object render visibility with viewport visibility.
**Features**:
- One-click sync for all objects.
- Dedicated UI panel for quick access.

---

### 7. Z-Translate
**Description**: Translate object names and text data using a translation list.
**Features**:
- Switch between languages for object names.
- Import custom translation dictionaries.
- Automatic updates based on selected language.

---

### 8. Z-Wiki
**Description**: Download Wikipedia articles directly into Blender.
**Features**:
- Fetch articles based on a list of phrases.
- Automatic text formatting and cleaning.
- Integration into Blender's text editor.
- Report of matched/unmatched phrases.

---

## 📥 Installation (for all add-ons)
1. Download the `.zip` file of the desired add-on.
2. In Blender, go to `Edit > Preferences > Add-ons`.
3. Click `Install from Disk` and select the `.zip` file.
4. Enable the add-on by checking the box.

---

## 📜 Usage
Each add-on adds a panel in Blender's UI, usually under the **"Z-Anatomy"** tab (in the **N-panel** or sidebar).
For detailed instructions, refer to the specific README inside each `.zip` file.

---

## 📂 Repository Contents
- Each add-on is provided as a `.zip` file containing:
  - The add-on code.
  - A specific README.md (visible after unzipping).
  - Sometimes an example `.blend` file.

---

## 💡 Notes
- All add-ons are compatible with Blender 2.80+.
- To report a bug or request a feature, open an [issue](https://github.com/your-username/your-repo/issues).
- Contributions are welcome via pull requests!

---
