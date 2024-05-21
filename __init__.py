import bpy
from .operators import *

bl_info = {
    "name": "ez importer for blender",
    "author": "hina",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "File > Import-Export > ez",
    "description": "Import Puni-puni(wib wob)'s model",
}

def draw_menu_import(self, context):
    bl_label = "Puni"
    bl_idname = "TOPBAR_MT_file_Puni_import"
    self.layout.operator(ImportEZ.bl_idname, text="Zip (EZ)")    

def register():
    bpy.utils.register_class(ImportEZ)
    bpy.types.TOPBAR_MT_file_import.append(draw_menu_import)

def unregister():
    bpy.utils.unregister_class(ImportEZ)
    bpy.types.TOPBAR_MT_file_import.remove(draw_menu_import)

if __name__ == "__main__":
    register()