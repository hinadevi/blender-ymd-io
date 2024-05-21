from .file_io_ez import *
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
import bpy

class ImportEZ(bpy.types.Operator, ImportHelper):
    bl_idname = "import_scene.ez"
    bl_label = "Import a .ez"
    bl_options = {'PRESET', 'UNDO'}
    filename_ext = ".ez"
    filter_glob: StringProperty(default="*.ez", options={'HIDDEN'})
    
    def execute(self, context):
            return file_io_open_ez(context, self.filepath)
    
