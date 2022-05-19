# gpl: author d4mer

bl_info = {
    "name": "Rig Controllers",
    "author": "D4mer",
    "version": (1, 0, 0),
    "blender": (3, 1, 2),
    "location": "View3D > Add > Curve > Rig Controller",
    "description": "Adds a Rig Controller Curve",
    "warning": "",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/add_curve/extra_objects.html",
    "category": "Add Curve",
}


import bpy
from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        FloatProperty,
        EnumProperty,
        IntProperty,
        )
from bpy_extras.object_utils import (
        AddObjectHelper,
        object_data_add,
        )


def add_4DirArrow(self, context, label):

    label = "4DirArrow"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
           (-1.009675, -0.977991, 0),
            (-1.009675, -3.017713, 0),
            (-1.009675, -3.017713, 0),
            (-2, -3, 0),
            (0, -5, 0),
            (2, -3, 0),
            (1, -3, 0),
            (1, -1, 0),
            (3, -1, 0),
            (3, -2, 0),
            (5, 0, 0),
            (3, 2, 0),
            (3, 1, 0),
            (1, 1, 0),
            (1, 3, 0),
            (2, 3, 0),
            (0, 5, 0),
            (-2, 3, 0),
            (-1, 3, 0),
            (-1, 1, 0),
            (-3, 1, 0),
            (-3, 2, 0),
            (-5, 0, 0),
            (-3, -2, 0),
            (-3, -1, 0),
            (-1, -1, 0),
            ]


    make_curve(self, context, verts, label)

#
def add_Arrow(self, context, label):

    label = "Arrow"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
           (-1, 0, 0),
           (-2, 0, 0),
           (0, 0, -3),
           (2, 0, 0),
           (1, 0, 0),
           (1, 0, 3),
           (-1, 0, 3),
           (-1, 0, 0)
            ]


    make_curve(self, context, verts, label)


def add_type8(self, context label):

    label = "Triangle"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (0, 0.353553, 0), (-0.707107, -0.353553, 0), (0, -0.353553, 0.707107), (0, 0.353553, 0), (0.707107, -0.353553, 0), (0, -0.353553, -0.707107), (0, 0.353553, 0), (-0.707107, -0.353553, 0), (0, -0.353553, -0.707107), (0.707107, -0.353553, 0), (0, -0.353553, 0.707107), (-0.707107, -0.353553, 0)
            ]

    make_curve(self, context, verts, label)


def add_type3(self, context, label):

    label = "TwoDir2"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [

            (-1, 4.629236, 2.450668), (-2, 4.629236, 2.450668), (0, 5.326421, 4.325217), (2, 4.629236, 2.450668), (1, 4.629236, 2.450668), (1, 3.665508, 1.405481), (1, 2.267852, 0.462659), (1, 1.110897, 0), (1, -0.889103, 0), (1, -2.114391, 0.504006), (1, -3.440023, 1.402289), (1.00446, -4.407442, 2.450668), (2, -4.407442, 2.450668), (0, -5.104627, 4.325217), (-2, -4.407442, 2.450668), (-1, -4.407442, 2.450668), (-1, -3.378215, 1.365864), (-1, -2.138703, 0.534677), (-1, -0.889103, 0), (-1, 1.110897, 0), (-1, 2.179023, 0.427137), (-1, 3.565873, 1.333103), (-1, 4.629236, 2.450668)
            ]

    make_curve(self, context, verts, label)


def add_type2(self, context, label):

    label= "FourDir2"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (1, -0.889103, 0), (1, -2.114391, 0.504006), (1, -3.440023, 1.402289), (1.00446, -4.407442, 2.450668), (2, -4.407442, 2.450668), (0, -5.104627, 4.325217), (-2, -4.407442, 2.450668), (-1, -4.407442, 2.450668), (-1, -3.492158, 1.442272), (-1, -2.00951, 0.448043), (-1, -0.889103, 0), (-2.274182, -0.889103, 0.425797), (-3.508666, -0.889103, 1.358465), (-4.559936, -0.889103, 2.618453), (-4.559936, -1.889103, 2.618453), (-4.861653, 0.110897, 3.717883), (-4.559936, 2.110897, 2.618453), (-4.559936, 1.110897, 2.618453), (-3.695534, 1.110897, 1.525866), (-2.401371, 1.110897, 0.514104), (-1, 1.110897, 0), (-1, 2.230979, 0.447914), (-1, 3.608218, 1.361183), (-1, 4.629236, 2.450668), (-2, 4.629236, 2.450668), (0, 5.326421, 4.325217), (2, 4.629236, 2.450668), (1, 4.629236, 2.450668), (1, 3.669424, 1.408123), (1, 2.267852, 0.462659), (1, 1.110897, 0), (2.169576, 1.110897, 0.373148), (3.526285, 1.110897, 1.374248), (4.559936, 1.110897, 2.618453), (4.559936, 2.110897, 2.618453), (4.861653, 0.110897, 3.717883), (4.559936, -1.889103, 2.618453), (4.559936, -0.889103, 2.618453), (3.501808, -0.889103, 1.352321), (2.00506, -0.889103, 0.320659), (1, -0.889103, 0)
            ]

    make_curve(self, context, verts, label)


def add_type10(self, context, label):

    label = "Cross"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (1, 0, -3), (-1, 0, -3), (-0.578361, 0, -0.578361), (-3, 0, -1), (-3, 0, 1), (-0.578361, 0, 0.578361), (-1, 0, 3), (1, 0, 3), (0.578361, 0, 0.578361), (3, 0, 1), (3, 0, -1), (0.578361, 0, -0.578361), (1, 0, -3)
            ]

    make_curve(self, context, verts, label)


def add_type9(self, context, label):

    label = "LBox"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, 0.885618), (0.885618, 4.181748, 0.885618), (0.885618, 4.181748, -0.885618), (0.885618, -0.885618, -0.885618), (-0.885618, -0.885618, -0.885618), (-0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, -0.885618), (-0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, 3.40897), (-0.885618, -0.885618, 3.40897), (-0.885618, -0.885618, -0.885618), (0.885618, -0.885618, -0.885618), (0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, 0.885618), (0.885618, 0.885618, 0.885618), (0.885618, 0.885618, -0.885618), (0.885618, -0.885618, -0.885618), (0.885618, -0.885618, 0.885618), (0.885618, 0.885618, 0.885618), (0.885618, 0.885618, 3.40897), (0.885618, -0.885618, 3.40897), (0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 3.40897), (-0.885618, 0.885618, 3.40897), (-0.885618, 0.885618, 0.885618), (-0.885618, -0.885618, 0.885618), (0.885618, -0.885618, 0.885618), (0.885618, 4.181748, 0.885618), (-0.885618, 4.181748, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 3.40897), (0.885618, -0.885618, 3.40897), (0.885618, 0.885618, 3.40897), (-0.885618, 0.885618, 3.40897)
            ]

    make_curve(self, context, verts, label)


def add_type7(self, context, label):

    label = "LShape"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (0.00808211, 1.970597, -0.885618), (0.00808211, 0.885618, -0.885618), (0.00808211, -0.667646, -0.885618), (0.00808211, -0.885618, -0.605311), (0.00808211, -0.885618, 0.885618), (0.00808211, -0.885618, 3.150896), (0.00808211, -0.726974, 3.40897), (0.00808211, 0.0555548, 3.40897), (0.00808211, 0.69994, 3.40897), (0.00808211, 0.885618, 3.164617), (0.00808211, 0.885618, 2.031101), (0.00808211, 0.885618, 1.059437), (0.00808211, 1.053073, 0.885618), (0.00808211, 2.222163, 0.885618), (0.00808211, 4.018034, 0.885618), (0.00808211, 4.181748, 0.745968), (0.00808211, 4.181748, 0.0301532), (0.00808211, 4.181748, -0.627114), (0.00808211, 4.017326, -0.885618), (0.00808211, 2.844681, -0.885618), (0.00808211, 1.980747, -0.885618)
            ]

    make_curve(self, context, verts, label)


def add_type4(self, context, label):

    label = "Star"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (0, 0, -2.993802), (-0.886951, 0, -0.993802), (-3, 0, -0.993802), (-1.271527, 0, 0.388976), (-2, 0, 3.006198), (-0.0221259, 0, 1.423899), (2, 0, 3.006198), (1.250591, 0, 0.383265), (3, 0, -0.993802), (0.894704, 0, -0.993802), (0, 0, -2.993802)
            ]

    make_curve(self, context, verts, label)


def add_type1(self, context, label):

    label = "TwoDir"
    scale_x = self.scale_x
    scale_y = self.scale_y
    verts = [
            (-1, 0, -2), (-2, 0, -2), (0, 0, -4), (2, 0, -2), (1, 0, -2), (1, 0, 1), (2, 0, 1), (0, 0, 3), (-2, 0, 1), (-1, 0, 1), (-1, 0, -2)
            ]
    lhandles = [
            [(-0.81885, -0.143002, 0),
            (-0.491926, -0.199026, 0),
            (-1.126316, -0.255119, 0),
            (-0.446315, 0.135164, 0),
            (0.733297, -0.26265, 0),
            (0.795065, 0.517532, 0),
            (0.616204, 0.03262, 0)]
            ]
    rhandles = [
            [(-0.616204, -0.032618, 0),
            (-0.795067, -0.517532, 0),
            (-0.733297, 0.262651, 0),
            (0.446315, -0.135163, 0),
            (1.126316, 0.255119, 0),
            (0.491924, 0.199026, 0),
            (0.81885, 0.143004, 0)]
            ]
    make_curve(self, context, verts, label)


def make_curve(self, context, verts, label):

    types = self.types
    curveData = bpy.data.curves.new(name=label, type='CURVE')
#    curveData.dimensions = '3D'
#    curveData.resolution_u = 2


    newSpline = curveData.splines.new('POLY')
    newSpline.points.add(len(verts)-1)
    for i, coord in enumerate(verts):
     x,y,z = coord
     newSpline.points[i].co = (x, y, z, 1)

    # create Object
    Curve = object_data_add(context, curveData, operator=self)
    Curve.select_set(True) # place in active scene



#    # create object
#    if bpy.context.mode == 'EDIT_CURVE':
#        Curve = context.active_object

#        for spline in Curve.data.splines:
#                for point in spline.points:
#                    point.select = False

#        for p in range(len(verts)):
#            c = 0
#            newSpline = Curve.data.splines.new(type='POLY')          # newSpline
#

#    else:
#        # create curve
#        dataCurve = bpy.data.curves.new(name='RigCurve', type='CURVE')  # curvedatablock
#        for p in range(len(verts)):
#            c = 0
#            newSpline = dataCurve.splines.new(type='POLY')          # newSpline
#

#        # create object with newCurve
#        Curve = object_data_add(context, dataCurve, operator=self)  # place in active scene


    # set curveOptions
    Curve.data.dimensions = self.shape
    Curve.data.use_path = True
    if self.shape == '3D':
        Curve.data.fill_mode = 'FULL'
    else:
        Curve.data.fill_mode = 'BOTH'

    # move and rotate spline in edit mode
    if bpy.context.mode == 'EDIT_CURVE':
        if self.align == "WORLD":
            location = self.location - context.active_object.location
            bpy.ops.transform.translate(value = location, orient_type='GLOBAL')
            bpy.ops.transform.rotate(value = self.rotation[0], orient_axis = 'X', orient_type='GLOBAL')
            bpy.ops.transform.rotate(value = self.rotation[1], orient_axis = 'Y', orient_type='GLOBAL')
            bpy.ops.transform.rotate(value = self.rotation[2], orient_axis = 'Z', orient_type='GLOBAL')

        elif self.align == "VIEW":
            bpy.ops.transform.translate(value = self.location)
            bpy.ops.transform.rotate(value = self.rotation[0], orient_axis = 'X')
            bpy.ops.transform.rotate(value = self.rotation[1], orient_axis = 'Y')
            bpy.ops.transform.rotate(value = self.rotation[2], orient_axis = 'Z')

        elif self.align == "CURSOR":
            location = context.active_object.location
            self.location = bpy.context.scene.cursor.location - location
            self.rotation = bpy.context.scene.cursor.rotation_euler

            bpy.ops.transform.translate(value = self.location)
            bpy.ops.transform.rotate(value = self.rotation[0], orient_axis = 'X')
            bpy.ops.transform.rotate(value = self.rotation[1], orient_axis = 'Y')
            bpy.ops.transform.rotate(value = self.rotation[2], orient_axis = 'Z')

class add_rigcurve(Operator, AddObjectHelper):
    bl_idname = "curve.rigcurve"
    bl_label = "Add Rig ContrCurve"
    bl_description = "Create a Rig Contr Curve"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    types : IntProperty(
            name="Type",
            description="Type of rig curve",
            default=6,
            min=1, max=10
            )
    scale_x : FloatProperty(
            name="Scale X",
            description="Scale on X axis",
            default=1.0
            )
    scale_y : FloatProperty(
            name="Scale Y",
            description="Scale on Y axis",
            default=1.0
            )
    # Curve Options
    shape : EnumProperty(
            name="2D / 3D",
            description="2D or 3D Curve",
            items=[
            ('2D', "2D", "2D"),
            ('3D', "3D", "3D")
            ]
            )

    edit_mode : BoolProperty(
            name="Show in edit mode",
            default=True,
            description="Show in edit mode"
            )

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.label(text = "Curve:")
        col.prop(self, "types")

        col = layout.column(align=True)
        col.label(text = "Resize:")
        col.prop(self, "scale_x")
        col.prop(self, "scale_y")

        row = layout.row()
        row.prop(self, "shape", expand=True)

        col = layout.column(align=True)
        col.row().prop(self, "edit_mode", expand=True)

        col = layout.column(align=True)
        # AddObjectHelper props
        col.prop(self, "align")
        col.prop(self, "location")
        col.prop(self, "rotation")

    def execute(self, context):
        # turn off 'Enter Edit Mode'
        use_enter_edit_mode = bpy.context.preferences.edit.use_enter_edit_mode
        bpy.context.preferences.edit.use_enter_edit_mode = False

        if self.types == 1:
            add_type1(self, context, "TwoDir")
        if self.types == 2:
            add_type2(self, context, "FourDir2")
        if self.types == 3:
            add_type3(self, context, "TwoDir2")
       if self.types == 4:
           add_type4(self, context, "Star")
        if self.types == 5:
            add_Arrow(self, context, 'Arrow')
        if self.types == 6:
            add_4DirArrow(self, context, '4DirArrow')
       if self.types == 7:
           add_type7(self, context, "LShape")
       if self.types == 8:
           add_type8(self, context, "Triangle")
       if self.types == 9:
           add_type9(self, context, "LBox")
       if self.types == 10:
           add_type10(self, context, "Cross")

        if use_enter_edit_mode:
            bpy.ops.object.mode_set(mode = 'EDIT')

        # restore pre operator state
        bpy.context.preferences.edit.use_enter_edit_mode = use_enter_edit_mode

        if self.edit_mode:
            bpy.ops.object.mode_set(mode = 'EDIT')
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')

        return {'FINISHED'}


# Registration

def add_rigcurve_button(self, context):
    self.layout.operator(
            add_rigcurve.bl_idname,
            text="Add Rig Contr Curve",
            icon='PLUGIN'
            )


def register():
    bpy.utils.register_class(add_rigcurve)
    bpy.types.VIEW3D_MT_curve_add.append(add_rigcurve_button)


def unregister():
    bpy.utils.unregister_class(add_rigcurve)
    bpy.types.VIEW3D_MT_curve_add.remove(add_rigcurve_button)


if __name__ == "__main__":
    register()
