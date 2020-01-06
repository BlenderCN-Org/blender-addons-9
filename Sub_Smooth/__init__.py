bl_info = {
    "name": "Sub Smooth",
    "author": "Neeraj Lagwankar",
    "description": "A simple addon to subdivide and smooth the selected object",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": " View3D > Object",
    "warning": "",
    "category": "Generic"
}

import bpy
from bpy.types import (Operator)


# Since it's an Object operator, the naming convention for class is:
# OBJECT_OT_lower_case

class OBJECT_OT_subsmooth(Operator):
    bl_label = "SubSmooth"
    bl_idname = "object.subsmooth"
    bl_description = "A simple addon to subdivide and smooth the selected object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        # These were copied from the log after performing the necessary steps
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].render_levels = 4
        bpy.context.object.modifiers["Subdivision"].levels = 4
        bpy.ops.object.shade_smooth()


        return {"FINISHED"}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_subsmooth.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_subsmooth)

    # Appending to the Objects menu for execution
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_subsmooth)
    bpy.types.VIEW3D_MT_object.remove(menu_func)



if __name__ == "__main__":
    register()
