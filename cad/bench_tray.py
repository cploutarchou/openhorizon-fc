import build123d as bd
import common
from ocp_vscode import show

# -----------------------------------------------------------------------------
# USER PARAMS
# -----------------------------------------------------------------------------
tray_w = 140
tray_h = 90
tray_t = 3.0
corner_r = 10

# Pico 2 mounting
pico_mount_dx = 48.0
pico_mount_dy = 21.0
pico_hole_d = 2.6
pico_standoff_h = 6.0
pico_standoff_d = 6.5

# ESP32 DevKit mounting
esp_mount_dx = 44.0
esp_mount_dy = 20.0
esp_hole_d = 2.6
esp_standoff_h = 8.0
esp_standoff_d = 6.5

# ESC mounting pattern
esc_30_5 = True
esc_20 = True
esc_hole_d_m3 = 3.2
esc_hole_d_m2 = 2.4

# Zip-tie / strap slots
zip_slot_len = 10
zip_slot_w = 3.2

# -----------------------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------------------


def mount_pattern(dx, dy, hole_d):
    locs = []
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            locs.append((sx * dx / 2, sy * dy / 2, 0))

    with bd.BuildPart() as p:
        with bd.Locations(locs):
            common.hole_cyl(hole_d, tray_t + 2)
    return p.part


def add_zip_slots():
    with bd.BuildPart() as p:
        # Two slots on each side
        with bd.Locations((0, tray_h / 2 - 10, 0)):
            common.slot(zip_slot_len, zip_slot_w, tray_t + 1)
        with bd.Locations((0, -tray_h / 2 + 10, 0)):
            common.slot(zip_slot_len, zip_slot_w, tray_t + 1)
        with bd.Locations((tray_w / 2 - 12, 0, 0)):
            with bd.Rotation(0, 0, 90):
                common.slot(zip_slot_len, zip_slot_w, tray_t + 1)
        with bd.Locations((-tray_w / 2 + 12, 0, 0)):
            with bd.Rotation(0, 0, 90):
                common.slot(zip_slot_len, zip_slot_w, tray_t + 1)
    return p.part


def standoff_group(dx, dy, h, d_outer, d_hole):
    locs = []
    for sx in [-1, 1]:
        for sy in [-1, 1]:
            locs.append((sx * dx / 2, sy * dy / 2, tray_t))

    with bd.BuildPart() as p:
        with bd.Locations(locs):
            bd.add(common.standoff(d_outer, d_hole, h))
    return p.part


with bd.BuildPart() as bench_tray:
    # Base
    bd.add(common.rounded_plate(tray_w, tray_h, tray_t, corner_r))

    # Subtract slots
    with bd.Locations((0, 0, 0)):  
        bd.add(add_zip_slots(), mode=bd.Mode.SUBTRACT)

    # Board mounting holes
    with bd.Locations((-35, 10, 0)):
        bd.add(
            mount_pattern(pico_mount_dx, pico_mount_dy, pico_hole_d),
            mode=bd.Mode.SUBTRACT,
        )

    with bd.Locations((35, 10, 0)):
        bd.add(
            mount_pattern(esp_mount_dx, esp_mount_dy, esp_hole_d), mode=bd.Mode.SUBTRACT
        )

    # ESC mounting pattern
    with bd.Locations((0, -18, 0)):
        if esc_30_5:
            bd.add(mount_pattern(30.5, 30.5, esc_hole_d_m3), mode=bd.Mode.SUBTRACT)
        if esc_20:
            bd.add(mount_pattern(20, 20, esc_hole_d_m2), mode=bd.Mode.SUBTRACT)

    # Add standoffs
    with bd.Locations((-35, 10, 0)):
        bd.add(
            standoff_group(
                pico_mount_dx,
                pico_mount_dy,
                pico_standoff_h,
                pico_standoff_d,
                pico_hole_d,
            )
        )

    with bd.Locations((35, 10, 0)):
        bd.add(
            standoff_group(
                esp_mount_dx, esp_mount_dy, esp_standoff_h, esp_standoff_d, esp_hole_d
            )
        )

if __name__ == "__main__":
    show(bench_tray)
