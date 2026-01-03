import build123d as bd
from ocp_vscode import show

import common

# -----------------------------------------------------------------------------
#  PARAMS
# -----------------------------------------------------------------------------
plate_w = 80
plate_h = 80
plate_t = 4.0
corner_r = 8

arm_w = 12.0
arm_slot_clear = 0.6
arm_slot_len = 36.0

stack_30_5 = True
stack_20 = True
m3_hole_d = 3.2
m2_hole_d = 2.4

arm_clamp_hole_d = 3.2
arm_clamp_x1 = 12.0
arm_clamp_x2 = 28.0

def arm_slot(angle_deg):
    with bd.BuildPart() as p:
        with bd.Rotation(0, 0, angle_deg):
            with bd.Locations((plate_w / 2 - arm_slot_len / 2, 0, 0)):
                bd.add(common.slot(arm_slot_len, arm_w + arm_slot_clear, plate_t + 1))
    return p.part


def arm_clamp_holes(angle_deg):
    with bd.BuildPart() as p:
        with bd.Rotation(0, 0, angle_deg):
            with bd.Locations((arm_clamp_x1, 0, 0), (arm_clamp_x2, 0, 0)):
                bd.Cylinder(radius=arm_clamp_hole_d / 2, height=plate_t + 2)
    return p.part


with bd.BuildPart() as frame_center_bottom:
    # Base
    bd.add(common.rounded_plate(plate_w, plate_h, plate_t, corner_r))

    # Arm slots
    for angle in [45, 135, 225, 315]:
        bd.add(arm_slot(angle), mode=bd.Mode.SUBTRACT)
        bd.add(arm_clamp_holes(angle), mode=bd.Mode.SUBTRACT)

    # Electronics mounting 
    if stack_30_5:
        locs = []
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                locs.append((sx * 30.5 / 2, sy * 30.5 / 2))
        with bd.Locations(locs):
            bd.Cylinder(radius=m3_hole_d / 2, height=plate_t + 2, mode=bd.Mode.SUBTRACT)

    if stack_20:
        locs = []
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                locs.append((sx * 20 / 2, sy * 20 / 2))
        with bd.Locations(locs):
            bd.Cylinder(radius=m2_hole_d / 2, height=plate_t + 2, mode=bd.Mode.SUBTRACT)

if __name__ == "__main__":
    show(frame_center_bottom)
