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


def register():
    bpy.utils.register_class(OBJECT_OT_subsmooth)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_subsmooth)


if __name__ == "__main__":
    register()
