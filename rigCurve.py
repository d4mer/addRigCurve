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
#
#
# def add_type8(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.850431, -0.009091,
#             0.0, -0.818807, -0.130518,
#             0.0, -0.944931, 0.055065,
#             0.0, -0.393355, -0.035521,
#             0.0, 0.0, 0.348298,
#             0.0, 0.393355, -0.035521,
#             0.0, 0.978373, 0.185638,
#             0.0, 0.771617, 0.272819,
#             0.0, 0.864179, 0.188103, 0.0]
#             ]
#     lhandles = [
#             [(-0.90478, -0.025302, 0.0),
#             (-0.753279, -0.085571, 0.0),
#             (-1.06406, -0.047879, 0.0),
#             (-0.622217, -0.022501, 0.0),
#             (0.181, 0.34879, 0.0),
#             (-0.101464, -0.063669, 0.0),
#             (0.933064, 0.03001, 0.0),
#             (0.82418, 0.39899, 0.0),
#             (0.827377, 0.144945, 0.0)]
#             ]
#     rhandles = [
#             [(-0.796079, 0.007121, 0.0),
#             (-0.931521, -0.207832, 0.0),
#             (-0.822288, 0.161045, 0.0),
#             (0.101464, -0.063671, 0.0),
#             (-0.181193, 0.347805, 0.0),
#             (0.622217, -0.022502, 0.0),
#             (1.022383, 0.336808, 0.0),
#             (0.741059, 0.199468, 0.0),
#             (0.900979, 0.231258, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type3(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.78652, -0.070157,
#             0.0, -0.697972, -0.247246,
#             0.0, -0.953385, -0.002048,
#             0.0, 0.0, 0.0,
#             0.0, 0.917448, 0.065788,
#             0.0, 0.448535, 0.515947,
#             0.0, 0.6111, 0.190831, 0.0]
#             ]
#     lhandles = [
#             [(-0.86511, -0.112965, 0.0),
#             (-0.61153, -0.156423, 0.0),
#             (-1.103589, -0.199934, 0.0),
#             (-0.446315, 0.135163, 0.0),
#             (0.669383, -0.254463, 0.0),
#             (0.721512, 0.802759, 0.0),
#             (0.466815, 0.112232, 0.0)]
#             ]
#     rhandles = [
#             [(-0.707927, -0.027348, 0.0),
#             (-0.846662, -0.40347, 0.0),
#             (-0.79875, 0.201677, 0.0),
#             (0.446315, -0.135163, 0.0),
#             (1.196752, 0.42637, 0.0),
#             (0.289834, 0.349204, 0.0),
#             (0.755381, 0.269428, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type2(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.719632, -0.08781, 0.0,
#             -0.605138, -0.31612, 0.0,
#             -0.935392, 0.0, 0.0,
#             0.0, 0.0, 0.0,
#             0.935392, 0.0, 0.0,
#             0.605138, -0.316119, 0.0,
#             0.719632, -0.08781, 0.0]
#             ]
#     lhandles = [
#             [(-0.82125, -0.142999, 0.0),
#             (-0.493366, -0.199027, 0.0),
#             (-1.129601, -0.25513, 0.0),
#             (-0.467584, 0.00044, 0.0),
#             (0.735439, 0.262646, 0.0),
#             (0.797395, -0.517531, 0.0),
#             (0.618012, -0.032614, 0.0)]
#             ]
#     rhandles = [
#             [(-0.618009, -0.032618, 0.0),
#             (-0.797396, -0.517532, 0.0),
#             (-0.735445, 0.262669, 0.0),
#             (0.468041, -0.00044, 0.0),
#             (1.129616, -0.255119, 0.0),
#             (0.493365, -0.199025, 0.0),
#             (0.821249, -0.143004, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type10(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.999637, 0.000348,
#             0.0, 0.259532, -0.017841,
#             0.0, 0.482303, 0.780429,
#             0.0, 0.573183, 0.506898, 0.0],
#             [0.259532, -0.017841,
#             0.0, 0.554919, -0.140918,
#             0.0, 0.752264, -0.819275,
#             0.0, 0.824152, -0.514881, 0.0]
#             ]
#     lhandles = [
#             [(-1.258333, -0.258348, 0.0),
#             (-0.240006, -0.15259, 0.0),
#             (0.79037, 0.857575, 0.0),
#             (0.376782, 0.430157, 0.0)],
#             [(0.224917, -0.010936, 0.0),
#             (0.514858, -0.122809, 0.0),
#             (1.057957, -0.886925, 0.0),
#             (0.61945, -0.464285, 0.0)]
#             ]
#     rhandles = [
#             [(-0.74094, 0.259045, 0.0),
#             (0.768844, 0.119545, 0.0),
#             (0.279083, 0.729538, 0.0),
#             (0.643716, 0.534458, 0.0)],
#             [(0.294147, -0.024746, 0.0),
#             (1.03646, -0.358598, 0.0),
#             (0.547718, -0.774008, 0.0),
#             (0.897665, -0.533051, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type9(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [0.260968, -0.668118,
#             0.0, 0.108848, -0.381587,
#             0.0, 0.537002, -0.77303,
#             0.0, -0.600421, -0.583106,
#             0.0, -0.600412, 0.583103,
#             0.0, 0.537002, 0.773025,
#             0.0, 0.108854, 0.381603,
#             0.0, 0.260966, 0.668129, 0.0]
#             ]
#     lhandles = [
#             [(0.387973, -0.594856, 0.0),
#             (-0.027835, -0.532386, 0.0),
#             (0.775133, -0.442883, 0.0),
#             (-0.291333, -1.064385, 0.0),
#             (-0.833382, 0.220321, 0.0),
#             (0.291856, 1.112891, 0.0),
#             (0.346161, 0.119777, 0.0),
#             (0.133943, 0.741389, 0.0)]
#             ]
#     rhandles = [
#             [(0.133951, -0.741386, 0.0),
#             (0.346154, -0.119772, 0.0),
#             (0.291863, -1.112896, 0.0),
#             (-0.833407, -0.220324, 0.0),
#             (-0.29134, 1.064389, 0.0),
#             (0.775125, 0.442895, 0.0),
#             (-0.029107, 0.533819, 0.0),
#             (0.387981, 0.594873, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type7(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.850431, -0.009091,
#             0.0, -0.818807, -0.130518,
#             0.0, -0.944931, 0.055065, 0.0,
#             -0.393355, -0.035521,
#             0.0, 0.0, 0.348298,
#             0.0, 0.393355, -0.035521,
#             0.0, 0.944931, 0.055065,
#             0.0, 0.818807, -0.130518,
#             0.0, 0.850431, -0.009091, 0.0]
#             ]
#     lhandles = [
#             [(-0.90478, -0.025302, 0.0),
#             (-0.753279, -0.085571, 0.0),
#             (-1.06406, -0.047879, 0.0),
#             (-0.622217, -0.022502, 0.0),
#             (0.181, 0.348791, 0.0),
#             (-0.101464, -0.063671, 0.0),
#             (0.822288, 0.161045, 0.0),
#             (0.931521, -0.207832, 0.0),
#             (0.796079, 0.007121, 0.0)]
#             ]
#     rhandles = [
#             [(-0.796079, 0.007121, 0.0),
#             (-0.931521, -0.207832, 0.0),
#             (-0.822288, 0.161045, 0.0),
#             (0.101464, -0.063671, 0.0),
#             (-0.181193, 0.347805, 0.0),
#             (0.622217, -0.022502, 0.0),
#             (1.06406, -0.047879, 0.0),
#             (0.753279, -0.085571, 0.0),
#             (0.90478, -0.025302, 0.0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type4(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [0.072838, -0.071461,
#             0.0, -0.175451, -0.130711,
#             0.0, 0.207269, 0.118064,
#             0.0, 0, -1.0, 0.0]
#             ]
#     lhandles = [
#             [(0.042135, 0.039756, 0),
#             (-0.086769, -0.265864, 0),
#             (0.002865, 0.364657, 0),
#             (0.233116, -0.596115, 0)]
#             ]
#     rhandles = [
#             [(0.103542, -0.182683, 0),
#             (-0.327993, 0.101765, 0),
#             (0.417702, -0.135803, 0),
#             (-0.233116, -1.403885, 0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)
#
#
# def add_type1(self, context):
#
#     scale_x = self.scale_x
#     scale_y = self.scale_y
#     verts = [
#             [-0.71753, -0.08781,
#             0, -0.60337, -0.31612, 0,
#             -0.93266, 0, 0, 0, 0, 0, 0.93266,
#             0, 0, 0.60337, 0.31612,
#             0, 0.71753, 0.08781, 0]
#             ]
#     lhandles = [
#             [(-0.81885, -0.143002, 0),
#             (-0.491926, -0.199026, 0),
#             (-1.126316, -0.255119, 0),
#             (-0.446315, 0.135164, 0),
#             (0.733297, -0.26265, 0),
#             (0.795065, 0.517532, 0),
#             (0.616204, 0.03262, 0)]
#             ]
#     rhandles = [
#             [(-0.616204, -0.032618, 0),
#             (-0.795067, -0.517532, 0),
#             (-0.733297, 0.262651, 0),
#             (0.446315, -0.135163, 0),
#             (1.126316, 0.255119, 0),
#             (0.491924, 0.199026, 0),
#             (0.81885, 0.143004, 0)]
#             ]
#     make_curve(self, context, verts, lhandles, rhandles)


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

#        if self.types == 1:
#            add_type1(self, context)
#        if self.types == 2:
#            add_type2(self, context)
#        if self.types == 3:
#            add_type3(self, context)
#        if self.types == 4:
#            add_type4(self, context)
        if self.types == 5:
            add_Arrow(self, context, 'Arrow')
        if self.types == 6:
            add_4DirArrow(self, context, '4DirArrow')
#        if self.types == 7:
#            add_type7(self, context)
#        if self.types == 8:
#            add_type8(self, context)
#        if self.types == 9:
#            add_type9(self, context)
#        if self.types == 10:
#            add_type10(self, context)

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
