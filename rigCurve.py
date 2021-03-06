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
    scale_z = self.scale_z
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
    scale_z = self.scale_z
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


def add_type8(self, context, label):

    label = "Triangle"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0.353553, 0), (-0.707107, -0.353553, 0), (0, -0.353553, 0.707107), (0, 0.353553, 0), (0.707107, -0.353553, 0), (0, -0.353553, -0.707107), (0, 0.353553, 0), (-0.707107, -0.353553, 0), (0, -0.353553, -0.707107), (0.707107, -0.353553, 0), (0, -0.353553, 0.707107), (-0.707107, -0.353553, 0)
            ]

    make_curve(self, context, verts, label)


def add_type3(self, context, label):

    label = "TwoDir2"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [

            (-1, 4.629236, 2.450668), (-2, 4.629236, 2.450668), (0, 5.326421, 4.325217), (2, 4.629236, 2.450668), (1, 4.629236, 2.450668), (1, 3.665508, 1.405481), (1, 2.267852, 0.462659), (1, 1.110897, 0), (1, -0.889103, 0), (1, -2.114391, 0.504006), (1, -3.440023, 1.402289), (1.00446, -4.407442, 2.450668), (2, -4.407442, 2.450668), (0, -5.104627, 4.325217), (-2, -4.407442, 2.450668), (-1, -4.407442, 2.450668), (-1, -3.378215, 1.365864), (-1, -2.138703, 0.534677), (-1, -0.889103, 0), (-1, 1.110897, 0), (-1, 2.179023, 0.427137), (-1, 3.565873, 1.333103), (-1, 4.629236, 2.450668)
            ]

    make_curve(self, context, verts, label)


def add_type2(self, context, label):

    label= "FourDir2"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (1, -0.889103, 0), (1, -2.114391, 0.504006), (1, -3.440023, 1.402289), (1.00446, -4.407442, 2.450668), (2, -4.407442, 2.450668), (0, -5.104627, 4.325217), (-2, -4.407442, 2.450668), (-1, -4.407442, 2.450668), (-1, -3.492158, 1.442272), (-1, -2.00951, 0.448043), (-1, -0.889103, 0), (-2.274182, -0.889103, 0.425797), (-3.508666, -0.889103, 1.358465), (-4.559936, -0.889103, 2.618453), (-4.559936, -1.889103, 2.618453), (-4.861653, 0.110897, 3.717883), (-4.559936, 2.110897, 2.618453), (-4.559936, 1.110897, 2.618453), (-3.695534, 1.110897, 1.525866), (-2.401371, 1.110897, 0.514104), (-1, 1.110897, 0), (-1, 2.230979, 0.447914), (-1, 3.608218, 1.361183), (-1, 4.629236, 2.450668), (-2, 4.629236, 2.450668), (0, 5.326421, 4.325217), (2, 4.629236, 2.450668), (1, 4.629236, 2.450668), (1, 3.669424, 1.408123), (1, 2.267852, 0.462659), (1, 1.110897, 0), (2.169576, 1.110897, 0.373148), (3.526285, 1.110897, 1.374248), (4.559936, 1.110897, 2.618453), (4.559936, 2.110897, 2.618453), (4.861653, 0.110897, 3.717883), (4.559936, -1.889103, 2.618453), (4.559936, -0.889103, 2.618453), (3.501808, -0.889103, 1.352321), (2.00506, -0.889103, 0.320659), (1, -0.889103, 0)
            ]

    make_curve(self, context, verts, label)


def add_type10(self, context, label):

    label = "Cross"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (1, 0, -3), (-1, 0, -3), (-0.578361, 0, -0.578361), (-3, 0, -1), (-3, 0, 1), (-0.578361, 0, 0.578361), (-1, 0, 3), (1, 0, 3), (0.578361, 0, 0.578361), (3, 0, 1), (3, 0, -1), (0.578361, 0, -0.578361), (1, 0, -3)
            ]

    make_curve(self, context, verts, label)


def add_type9(self, context, label):

    label = "LBox"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, 0.885618), (0.885618, 4.181748, 0.885618), (0.885618, 4.181748, -0.885618), (0.885618, -0.885618, -0.885618), (-0.885618, -0.885618, -0.885618), (-0.885618, 4.181748, -0.885618), (-0.885618, 4.181748, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, -0.885618), (-0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, 3.40897), (-0.885618, -0.885618, 3.40897), (-0.885618, -0.885618, -0.885618), (0.885618, -0.885618, -0.885618), (0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, -0.885618), (-0.885618, 0.885618, 0.885618), (0.885618, 0.885618, 0.885618), (0.885618, 0.885618, -0.885618), (0.885618, -0.885618, -0.885618), (0.885618, -0.885618, 0.885618), (0.885618, 0.885618, 0.885618), (0.885618, 0.885618, 3.40897), (0.885618, -0.885618, 3.40897), (0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 3.40897), (-0.885618, 0.885618, 3.40897), (-0.885618, 0.885618, 0.885618), (-0.885618, -0.885618, 0.885618), (0.885618, -0.885618, 0.885618), (0.885618, 4.181748, 0.885618), (-0.885618, 4.181748, 0.885618), (-0.885618, -0.885618, 0.885618), (-0.885618, -0.885618, 3.40897), (0.885618, -0.885618, 3.40897), (0.885618, 0.885618, 3.40897), (-0.885618, 0.885618, 3.40897)
            ]

    make_curve(self, context, verts, label)


def add_type7(self, context, label):

    label = "LShape"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0.00808211, 1.970597, -0.885618), (0.00808211, 0.885618, -0.885618), (0.00808211, -0.667646, -0.885618), (0.00808211, -0.885618, -0.605311), (0.00808211, -0.885618, 0.885618), (0.00808211, -0.885618, 3.150896), (0.00808211, -0.726974, 3.40897), (0.00808211, 0.0555548, 3.40897), (0.00808211, 0.69994, 3.40897), (0.00808211, 0.885618, 3.164617), (0.00808211, 0.885618, 2.031101), (0.00808211, 0.885618, 1.059437), (0.00808211, 1.053073, 0.885618), (0.00808211, 2.222163, 0.885618), (0.00808211, 4.018034, 0.885618), (0.00808211, 4.181748, 0.745968), (0.00808211, 4.181748, 0.0301532), (0.00808211, 4.181748, -0.627114), (0.00808211, 4.017326, -0.885618), (0.00808211, 2.844681, -0.885618), (0.00808211, 1.980747, -0.885618)
            ]

    make_curve(self, context, verts, label)


def add_type4(self, context, label):

    label = "Star"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, -2.993802), (-0.886951, 0, -0.993802), (-3, 0, -0.993802), (-1.271527, 0, 0.388976), (-2, 0, 3.006198), (-0.0221259, 0, 1.423899), (2, 0, 3.006198), (1.250591, 0, 0.383265), (3, 0, -0.993802), (0.894704, 0, -0.993802), (0, 0, -2.993802)
            ]

    make_curve(self, context, verts, label)


def add_type1(self, context, label):

    label = "Cross2"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-1, 0, 3), (1, 0, 3), (1, 0, 1), (3, 0, 1), (3, 0, -1), (1, 0, -1), (1, 0, -3), (-1, 0, -3), (-1, 0, -1), (-3, 0, -1), (-3, 0, 1), (-1, 0, 1), (-1, 0, 3)
            ]

    make_curve(self, context, verts, label)

def add_type11(self, context, label):

    label = "Prism"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-0.288675, 1, 0.5), (-0.288675, 1, -0.5), (0.57735, 1, 0), (-0.28123, 1, 0.495701), (-0.288675, -1, 0.5), (0.57735, -1, 0), (0.57735, 1, 0), (-0.288675, 1, -0.5), (-0.288675, -1, -0.5), (-0.288675, -1, 0.5), (0.57735, -1, 0), (-0.288675,-1, -0.5)
            ]

    make_curve(self, context, verts, label)

def add_type12(self, context, label):

    label = "IKFK"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (2, 0, 3), (2, 0, 4), (1, 0, 4), (1, 0, 3), (-1, 0, 3), (-1, 0, 4), (-2, 0, 4), (-2, 0, 1), (-1, 0, 1), (-1, 0, 2), (1, 0, 2), (1, 0, 1), (2, 0, 1), (2, 0, 3), (2, 0, 0), (-2, 0, 0), (-2, 0, -1), (-0.359129, 0, -1.016991), (-2, 0, -2), (-2, 0, -3), (0, 0, -2), (2, 0, -3), (2, 0, -2), (0.5, 0, -1), (2, 0, -1), (2, 0, 0), (2, 0, -4), (-2, 0, -4), (-2, 0, -7), (-1, 0, -7), (-1, 0, -5), (0, 0, -5), (0, 0, -6), (1, 0, -6), (1, 0, -5), (2, 0, -5), (2, 0, -4), (2, 0, -8), (-2, 0, -8), (-2, 0, -9), (-0.307096, 0, -8.989267), (-2, 0, -10), (-2, 0, -11), (0, 0, -10), (2, 0, -11), (2, 0, -10), (0.561828, 0, -9.002569), (2, 0, -9), (2, 0, -8)
            ]

    make_curve(self, context, verts, label)

def add_type13(self, context, label):

    label = "Diamond"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (3, 0, 3), (3, 0, -3), (-3, 0, -3), (-3, 0, 3), (3, 0, 3), (0, 3, 0), (3, 0, -3), (0, 3, 0), (-3, 0, -3), (0, 3, 0), (-3, 0, 3), (0, -3, 0), (-3, 0, -3), (0, -3, 0), (3, 0, -3), (0, -3, 0), (3, 0, 3)
            ]

    make_curve(self, context, verts, label)

def add_type14(self, context, label):

    label = "ThreeDArrow"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-2, 0, -3), (2, 0, -3), (2, 0, 3), (4, 0, 3), (0, 0, 7), (-4, 0, 3), (-2, 0, 3), (-2, 0, -3), (0, 0, -3), (0, 2, -3), (0, 2, 3), (0, 4, 3), (0, 0, 7), (0, -4, 3), (0, -2, 3), (0, -2, -3), (0, 0, -3)
            ]

    make_curve(self, context, verts, label)

def add_type15(self, context, label):

    label = "Single_Arrow_Circle_Ctrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, -7.050786), (0, 0, -7.050786), (0, 0, -7.050786), (2.350262, 0, -4.700524), (2.317171, 0, -4.733615), (2.317171, 0, -4.733615), (2.324232, 0, -4.726554), (1.175131, 0, -4.700524), (1.237241, 0, -4.700524), (1.210241, 0, -4.700524), (1.218626, 0, -4.700578), (1.175131, 0, -3.795461), (1.21844, 0, -3.782682), (1.21844, 0, -3.782682), (1.660143, 0, -3.618456), (2.212549, 0, -3.316805), (2.860755, 0, -2.781828), (3.300802, 0, -2.237835), (3.824186, 0, -1.154983), (3.947681, 0, -0.535972), (3.912447, 0, 0.595613), (3.763365, 0, 1.321012), (3.530664, 0, 1.880078), (3.193444, 0, 2.436584), (2.488276, 0, 3.122568), (1.954558, 0, 3.460073), (1.076035, 0, 3.878779), (-0.149442, 0, 3.982333), (-1.344506, 0, 3.760919), (-2.304674, 0, 3.307244), (-3.044527, 0, 2.564013), (-3.629874, 0, 1.621527), (-3.869502, 0, 0.896631), (-3.96371, 0, 0.19457), (-3.921556, 0, -0.582895), (-3.715943, 0, -1.246221), (-3.352063, 0, -2.013303), (-2.822503, 0, -2.763968), (-2.202315, 0, -3.312571), (-1.641639, 0, -3.629064), (-1.175131, 0, -3.804196), (-1.175131, 0, -3.810511), (-1.175131, 0, -3.810511), (-1.175131, 0, -4.700524), (-1.175131, 0, -4.700524), (-1.175131, 0, -4.700524), (-2.350262, 0, -4.700524), (-2.333839, 0, -4.700524), (-2.333839, 0, -4.700524), (0, 0, -7.050786), (0.00664033, 0, -7.044146), (0, 0, -7.050786)
            ]

    make_curve(self, context, verts, label)

def add_type16(self, context, label):

    label = "Double_Arrow_Circle_Ctrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, -8.685505), (0.0369838, 0, -8.648522), (0.0369838, 0, -8.648522), (2.895168, 0, -5.790337), (2.895168, 0, -5.790337), (2.895168, 0, -5.790337), (1.447584, 0, -5.790337), (1.447584, 0, -5.736439), (1.447584, 0, -5.736439), (1.447584, 0, -4.675435), (1.474008, 0, -4.667727), (1.474008, 0, -4.667727), (1.986189, 0, -4.483069), (2.665186, 0, -4.12478), (3.144082, 0, -3.777133), (3.559701, 0, -3.389635), (4.051877, 0, -2.777725), (4.435, 0, -2.106873), (4.742842, 0, -1.308889), (4.871536, 0, -0.571347), (4.871488, 0, 0.259015), (4.787352, 0, 0.953852), (4.631107, 0, 1.637656), (4.248535, 0, 2.462393), (3.771285, 0, 3.151174), (3.302706, 0, 3.640207), (2.532674, 0, 4.20796), (1.786261, 0, 4.573383), (1.4481, 0, 4.692066), (1.448016, 0, 4.753564), (1.448016, 0, 4.753564), (1.447584, 0, 5.790337), (1.463232, 0, 5.790337), (1.463232, 0, 5.790337), (2.895168, 0, 5.790337), (2.857754, 0, 5.827751), (2.857754, 0, 5.827751), (0, 0, 8.685505), (0, 0, 8.685505), (0, 0, 8.685505), (-2.895168, 0, 5.790337), (-2.842269, 0, 5.843236), (-2.842269, 0, 5.843236), (-2.85396, 0, 5.831545), (-1.447584, 0, 5.790337), (-1.447584, 0, 5.790337), (-1.447584, 0, 5.790337), (-1.447584, 0, 5.790337), (-1.447584, 0, 4.678282), (-1.447584, 0, 4.727004), (-1.447584, 0, 4.871745), (-1.710151, 0, 4.592539), (-2.225723, 0, 4.372681), (-2.8513, 0, 4.000271), (-3.402561, 0, 3.547376), (-3.894689, 0, 2.996109), (-4.270002, 0, 2.425704), (-4.600314, 0, 1.715896), (-4.808515, 0, 0.853778), (-4.88781, 0, 0.165257), (-4.841316, 0, -0.664557), (-4.574941, 0, -1.541681), (-4.241586, 0, -2.274387), (-3.758882, 0, -3.054594), (-2.826487, 0, -3.999382), (-2.370096, 0, -4.294559), (-1.447584, 0, -4.686195), (-1.466031, 0, -4.680558), (-1.447584, 0, -4.686195), (-1.447584, 0, -5.790337), (-1.447584, 0, -5.788416), (-1.447584, 0, -5.788416), (-2.895168, 0, -5.790337), (-2.895161, 0, -5.790337), (-2.895161, 0, -5.790337), (0, 0, -8.685505), (0.0308198, 0, -8.654686), (0.0308198, 0, -8.654686)
            ]

    make_curve(self, context, verts, label)

def add_type17(self, context, label):

    label = "Arc_Arrow_Ctrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-4.94713, 3.881462, 0), (-4.94713, 3.881462, 0), (-6.899999, 5.931974, 0), (-6.899999, 5.931974, 0), (-6.899999, 0.805694, 0), (-6.899999, 0.805694, 0), (-2.017827, 0.854515, 0), (-2.017827, 0.854515, 0), (-3.970696, 2.905027, 0), (-3.970696, 2.905027, 0), (-2.896618, 3.930283, 0), (-0.162602, 4.955539, 0), (2.717879, 3.930283, 0), (4.084887, 2.807384, 0), (4.036065, 2.758562, 0), (2.034375, 0.952159, 0), (2.034375, 0.952159, 0), (7.01419, 0.952159, 0), (7.01419, 0.952159, 0), (6.965368, 5.980795, 0), (6.965368, 5.980795, 0), (5.158964, 3.930283, 0), (5.158964, 3.930283, 0), (3.401383, 5.5414, 0), (0.0326846, 6.908408, 0), (-3.433657, 5.590222, 0), (-4.800665, 3.83264,0)
            ]

    make_curve(self, context, verts, label)

def add_type18(self, context, label):

    label = "Three_Arrow_Ctrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-2, 0, -7), (-2, 0, 7), (-5, 0, 7), (0, 0, 11), (5, 0, 7), (2, 0, 7), (2, 0, 2), (7, 0, 2), (7, 0, 5), (12, 0, 0), (7, 0, -5), (7, 0, -2), (2, 0, -2), (2, 0, -7), (5, 0, -7), (0, 0, -11), (-5, 0, -7), (-2, 0, -7)
            ]

    make_curve(self, context, verts, label)

def add_type19(self, context, label):

    label = "ThreeArrowCircleCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (5.954375, 0, 0), (5.93551, 0, 0.018865), (5.93551, 0, 0.018865), (3.969583, 0, -1.984792), (3.969583, 0, -1.977665), (3.969583, 0, -1.977665), (3.969583, 0, -0.992396), (3.969583, 0, -0.992396), (3.969583, 0, -0.992396), (3.212475, 0, -1.006085), (3.210758, 0, -1.011503), (3.210758, 0, -1.011503), (3.063541, 0, -1.394509), (2.792032, 0, -1.88311), (2.4753, 0, -2.286401), (2.023526, 0, -2.692718), (1.572117, 0, -2.974168), (1.25718, 0, -3.115953), (0.992396, 0, -3.205259), (0.992396, 0, -3.205259), (1.036527, 0, -3.190375), (0.992396, 0, -3.969583), (0.992396, 0, -3.969583), (0.992396, 0, -3.969583), (1.984792, 0, -3.969583), (1.978514, 0, -3.969583), (1.978514, 0, -3.969583), (1.953143, 0, -3.969583), (0, 0, -5.954375), (-0.00208572, 0, -5.952289), (-0.00208572, 0, -5.952289), (-0.00208572, 0, -5.952289), (-1.984792, 0, -3.969583), (-1.932191, 0, -4.022184), (-1.95919, 0, -3.995185), (-0.992396, 0, -3.969583), (-1.012602, 0, -3.969583), (-1.012602, 0, -3.969583), (-0.992396, 0, -3.212636), (-1.034209, 0, -3.199649), (-1.034209, 0, -3.199649), (-1.447264, 0, -3.037648), (-2.022083, 0, -2.693945), (-2.44715, 0, -2.316608), (-2.853578, 0, -1.787552), (-3.145386, 0, -1.198483), (-3.269586, 0, -0.462303), (-3.288761, 0, 0.200968), (-3.191936, 0, 0.871049), (-2.965965, 0, 1.584102), (-2.66566, 0, 2.175173), (-2.183924, 0, 2.631242), (-1.655148, 0, 2.940961), (-0.992396, 0, 3.20721), (-1.032066, 0, 3.195247), (-0.992396, 0, 3.231347), (-0.992396, 0, 3.969583), (-1.009272, 0, 3.969583), (-1.009272, 0, 3.969583), (-1.984792, 0, 3.969583), (-1.984792, 0, 3.969583), (-1.984792, 0, 3.969583), (0, 0, 5.954375), (-0.020494, 0, 5.933881), (-0.020494, 0, 5.933881), (1.984792, 0, 3.969583), (1.984792, 0, 3.969583), (1.984792, 0, 3.969583), (0.992396, 0, 3.969583), (0.992396, 0, 3.967242), (0.992396, 0, 3.967242), (0.992749, 0, 3.21666), (0.992735, 0, 3.226798), (0.992735, 0, 3.226798), (1.188167, 0, 3.149308), (1.474, 0, 3.026236), (1.731359, 0, 2.887712), (2.032469, 0, 2.686289), (2.272291, 0, 2.488206), (2.498609, 0, 2.260783), (2.7344, 0, 1.966351), (2.930671, 0, 1.656262), (3.066702, 0, 1.387543), (3.219665, 0, 0.992396), (3.219425, 0, 0.993136), (3.219425, 0, 0.993136), (3.969583, 0, 0.992396), (3.965942, 0, 0.992396), (3.965942, 0, 0.992396), (3.969583, 0, 1.984792), (3.969583, 0, 1.983607), (3.969583, 0, 1.983607), (5.954375, 0, 0), (5.938654, 0, 0.0157208), (5.938654, 0, 0.0157208)
            ]

    make_curve(self, context, verts, label)

def add_type20(self, context, label):

    label = "FourArrowCtrlNarrow"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, 8), (-3, 0, 5), (-1, 0, 5), (-1, 0, 1), (-5, 0, 1), (-5, 0, 3), (-8, 0, 0), (-5, 0, -3), (-5, 0, -1), (-1, 0, -1), (-1, 0, -5), (-3, 0, -5), (0, 0, -8), (3, 0, -5), (1, 0, -5), (1, 0, -1), (5, 0, -1), (5, 0, -3), (8, 0, 0), (5, 0, 3), (5, 0, 1), (1, 0, 1), (1, 0, 5), (3, 0, 5), (0, 0, 8)
            ]

    make_curve(self, context, verts, label)

def add_type21(self, context, label):

    label = "FourArrowCtrlWide"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (7, 0, 0), (4, 0, -3), (4, 0, -2), (2, 0, -2), (2, 0, -4), (3, 0, -4), (0, 0, -7), (-3, 0, -4), (-2, 0, -4), (-2, 0, -2), (-4, 0, -2), (-4, 0, -3), (-7, 0, 0), (-4, 0, 3), (-4, 0, 2), (-2, 0, 2), (-2, 0, 4), (-3, 0, 4), (0, 0, 7), (3, 0, 4), (2, 0, 4), (2, 0, 2), (4, 0, 2), (4, 0, 3), (7, 0, 0)
            ]

    make_curve(self, context, verts, label)

def add_type22(self, context, label):

    label = "CircleFourArrowCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, 0.829101), (0, 0, 0.829101), (0, 0, 0.829101), (0.276367, 0, 0.552734), (0.275255, 0, 0.553846), (0.275255, 0, 0.553846), (0.275466, 0, 0.553635), (0.275466, 0, 0.553635), (0.138183, 0, 0.552734), (0.138183, 0, 0.552734), (0.138183, 0, 0.552734), (0.138233, 0, 0.447895), (0.138228, 0, 0.451043), (0.138228, 0, 0.451043), (0.171324, 0, 0.436248), (0.262067, 0, 0.388863), (0.311761, 0, 0.350623), (0.364664, 0, 0.295083), (0.40064, 0, 0.243416), (0.429134, 0, 0.188478), (0.452791, 0, 0.138183), (0.452791, 0, 0.138183), (0.552734, 0, 0.138183), (0.552734, 0, 0.139748), (0.552734, 0, 0.139943), (0.552734, 0, 0.276367), (0.553838, 0, 0.275263), (0.553838, 0, 0.275263), (0.829101, 0, 0), (0.826616, 0, 0.00248429), (0.826616, 0, 0.00248429), (0.552734, 0, -0.276367), (0.5537, 0, -0.275401), (0.5537, 0, -0.275401), (0.552734, 0, -0.138183), (0.552734, 0, -0.138183), (0.552734, 0, -0.138183), (0.447312, 0, -0.14009), (0.447312, 0, -0.14009), (0.447312, 0, -0.14009), (0.422761, 0, -0.202372), (0.384478, 0, -0.268521), (0.339054, 0, -0.324353), (0.295282, 0, -0.364501), (0.237637, 0, -0.403904), (0.178648, 0, -0.432462), (0.138183, 0, -0.446308), (0.143545, 0, -0.444724), (0.145821, 0, -0.443736), (0.138183, 0, -0.552734), (0.146556, 0, -0.552734), (0.146556, 0, -0.552734), (0.276367, 0, -0.552734), (0.274499, 0, -0.552734), (0.274499, 0, -0.552734), (0, 0, -0.829101), (-0.00325581, 0, -0.825845), (-0.00325581, 0, -0.825845), (-0.00271318, 0, -0.826387), (-0.276367, 0, -0.552734), (-0.275745, 0, -0.552734), (-0.275745, 0, -0.552734), (-0.138183, 0, -0.55222), (-0.138183, 0, -0.545565), (-0.138183, 0, -0.545565), (-0.138183, 0, -0.447335), (-0.138661, 0, -0.44719), (-0.138661, 0, -0.44719), (-0.175927, 0, -0.43409), (-0.225456, 0, -0.410871), (-0.29873, 0, -0.361713), (-0.352347, 0, -0.3098), (-0.397625, 0, -0.248441), (-0.429543, 0, -0.187502), (-0.448148, 0, -0.137417), (-0.448148, 0, -0.137417), (-0.448148, 0, -0.137417), (-0.552734, 0, -0.138183), (-0.548607, 0, -0.138183), (-0.548607, 0, -0.138183), (-0.549649, 0, -0.138182), (-0.552734, 0, -0.276367), (-0.552734, 0, -0.268315), (-0.552734, 0, -0.268315), (-0.829101, 0, 0), (-0.827812, 0, 0.00128908), (-0.827812, 0, 0.00128908), (-0.552734, 0, 0.276367), (-0.552734, 0, 0.276367), (-0.552734, 0, 0.276367), (-0.552734, 0, 0.138183), (-0.552734, 0, 0.140036), (-0.552734, 0, 0.140036), (-0.550617, 0, 0.138183), (-0.449357, 0, 0.133453), (-0.447565, 0, 0.139286), (-0.447565, 0, 0.139286), (-0.428898, 0, 0.188976), (-0.405892, 0, 0.234567), (-0.37082, 0, 0.287256), (-0.322486, 0, 0.340826), (-0.265379, 0, 0.386547), (-0.201814, 0, 0.422532), (-0.138183, 0, 0.446579), (-0.138183, 0, 0.451091), (-0.138183, 0, 0.451091), (-0.138183, 0, 0.552734), (-0.138183, 0, 0.552734), (-0.138183, 0, 0.552734), (-0.276367, 0, 0.552734), (-0.275739, 0, 0.553362), (-0.275739, 0, 0.553362), (0, 0, 0.829101), (0.000445676, 0, 0.828655), (0, 0, 0.829101)
            ]

    make_curve(self, context, verts, label)

def add_type23(self, context, label):

    label = "CurvedFourArrowCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (0, 0, 8), (-3, 0, 5), (-1, 0, 5), (-1, 0, 1), (-5, 0, 1), (-5, 0, 3), (-8, 0, 0), (-5, 0, -3), (-5, 0, -1), (-1, 0, -1), (-1, 0, -5), (-3, 0, -5), (0, 0, -8), (3, 0, -5), (1, 0, -5), (1, 0, -1), (5, 0, -1), (5, 0, -3), (8, 0, 0), (5, 0, 3), (5, 0, 1), (1, 0, 1), (1, 0, 5), (3, 0, 5), (0, 0, 8)
            ]

    make_curve(self, context, verts, label)

def add_type24(self, context, label):

    label = "TrapezoidalCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-2, 0, 2), (2, 0, 2), (2, 0, -2), (-2, 0, -2), (-2, 0, 2), (-1.5, 1, 1.5), (1.5, 1, 1.5), (2, 0, 2), (1.5, 1, 1.5), (1.5, 1, -1.5), (2, 0, -2), (1.5, 1, -1.5), (-1.5, 1, -1.5), (-2, 0, -2), (-1.5, 1, -1.5), (-1.5, 1, 1.5)
            ]

    make_curve(self, context, verts, label)

def add_type25(self, context, label):

    label = "flowerCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (2, 0, 2), (2, 0, 2), (2, 0, 2), (0, 0, 0), (2, 0, -2), (2, 0, -2), (2, 0, -2), (0, 0, 0), (-2, 0, -2), (-2, 0, -2), (-2, 0, -2), (0, 0, 0), (-2, 0, 2), (-2, 0, 2), (-2, 0, 2), (0, 0, 0), (2, 0, 2), (2, 0, 2), (2, 0, 2)
            ]

    make_curve(self, context, verts, label)

def add_type26(self, context, label):

    label = "SaddleCtrl"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-3, 3, 0), (-3.06664, 2.038278, -0.00022901), (-3.199921, 0.114835, -0.00068703), (-2.200317, -3.459341, 0.00274812), (0.00118997, -4.277469, -0.0103054), (2.195557, -3.430781, 0.0384737), (3.21658, 0.00059217, -0.143589), (2.938121, 3.428412, 0.535883), (3.030934, 4.28576, -1.999943), (2.938141, 3.428549, -4.536111), (3.216501, 4.55515e-05, -3.855613), (2.195853, -3.428731, -4.041437), (8.54678e-05, -4.285122, -3.978641), (-2.196195, -3.430781, -4.044001), (-3.215305, 0.00824482, -3.845357), (-2.942585, 3.397801, -4.574571), (-3.014354, 4.40055, -1.856357), (-3.004785, 3.46685, -0.618786), (-3, 3, 0)
            ]

    make_curve(self, context, verts, label)


def add_type27(self, context, label):

    label = "BentPlus"
    scale_x = self.scale_x
    scale_y = self.scale_y
    scale_z = self.scale_z
    verts = [
            (-1, 0, 3), (1, 0, 3), (1, .5, 1), (3, 0, 1), (3, 0, -1), (1, .5, -1), (1, 0, -3), (-1, 0, -3), (-1, .5, -1), (-3, 0, -1), (-3, 0, 1), (-1, .5, 1), (-1, 0, 3)
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
            default=1,
            min=1, max=27
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
    scale_z : FloatProperty(
            name="Scale Z",
            description="Scale on Z axis",
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
            default=False,
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
        if self.types == 11:
            add_type11(self, context, "Prism")
        if self.types == 12:
            add_type12(self, context, "IKFK")
        if self.types == 13:
            add_type13(self, context, "Diamond")
        if self.types == 14:
            add_type14(self, context, "ThreeDArrow")
        if self.types == 15:
            add_type15(self, context, "SingleArrowCircleCtrl")
        if self.types == 16:
            add_type16(self, context, "DoubleArrowCircleCtrl")
        if self.types == 17:
            add_type17(self, context, "ArcArrowCtrl")
        if self.types == 18:
            add_type18(self, context, "ThreeArrowCtrl")
        if self.types == 19:
            add_type19(self, context, "ThreeArrowCircleCtrl")
        if self.types == 20:
            add_type20(self, context, "FourArrowCtrlNarrow")
        if self.types == 21:
            add_type21(self, context, "FourArrowCtrlWide")
        if self.types == 22:
            add_type22(self, context, "CircleFourArrowCtrl")
        if self.types == 23:
            add_type23(self, context, "CurvedFourArrowCtrl")
        if self.types == 24:
            add_type24(self, context, "TrapezoidalCtrl")
        if self.types == 25:
            add_type25(self, context, "flowerCtrl")
        if self.types == 26:
            add_type26(self, context, "SaddleCtrl")
        if self.types == 27:
            add_type27(self, context, "BentPlus")

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
