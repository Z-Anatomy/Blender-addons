# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# Informations sur l'add-on

bl_info = {
    "name": "Z-Mirror",
    "author": "Gauthier Kervyn, Z-Anatomy",
    "description": "Activate or not the mirror modifiers on the main collections",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Interface"
}

import bpy

class ZANATOMY_PT_sync_panel(bpy.types.Panel):
    bl_label = "Z-Mirror"
    bl_idname = "VIEW3D_PT_Symmetrize"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Z-Anatomy'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Limiter à 10 collections principales
        collections = [col for col in bpy.data.collections if not col.hide_viewport]
        for collection in collections[:9]:
            row = layout.row()
            row.prop(collection, "zanatomy_mirror_enabled", text=collection.name)

def update_mirror_modifiers(collection, context):
    for obj in collection.objects:
        if obj.type == 'MESH':
            for modifier in obj.modifiers:
                if modifier.type == 'MIRROR':
                    modifier.show_viewport = collection.zanatomy_mirror_enabled
                    modifier.show_render = collection.zanatomy_mirror_enabled

def register():
    # Ajouter une propriété personnalisée à chaque collection
    bpy.types.Collection.zanatomy_mirror_enabled = bpy.props.BoolProperty(
        name="Enable Mirror",
        description="Enable or disable all Mirror modifiers in this collection",
        default=True,
        update=update_mirror_modifiers
    )
    bpy.utils.register_class(ZANATOMY_PT_sync_panel)

def unregister():
    del bpy.types.Collection.zanatomy_mirror_enabled
    bpy.utils.unregister_class(ZANATOMY_PT_sync_panel)

if __name__ == "__main__":
    register()
