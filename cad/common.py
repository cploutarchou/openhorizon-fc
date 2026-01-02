import build123d as bd


def rounded_rect_2d(w, h, r):
    """A 2D rounded rectangle centered at the origin."""
    r2 = min(r, min(w, h) / 2)
    return bd.RectangleRounded(w, h, r2)


def rounded_plate(w, h, t, r):
    """A 3D plate made by extruding rounded_rect_2d()."""
    with bd.BuildPart() as p:
        with bd.BuildSketch():
            rounded_rect_2d(w, h, r)
        bd.extrude(amount=t)
    return p.part


def hole_cyl(d, h):
    """Convenience wrapper for a cylinder hole (centered)."""
    return bd.Cylinder(radius=d / 2, height=h)


def slot_2d(length, w):
    """
    A 2D “capsule” slot centered at the origin.
    Matches OpenSCAD logic: centers are at +/- length/2.
    Total length is length + w.
    """
    return bd.SlotCenterToCenter(length, w)


def slot(length, w, h):
    """3D version of slot_2d()."""
    with bd.BuildPart() as p:
        with bd.BuildSketch():
            slot_2d(length, w)
        bd.extrude(amount=h)
    return p.part


def standoff(d_outer, d_hole, h):
    """Simple cylindrical standoff with a through-hole. Base at Z=0."""
    with bd.BuildPart() as p:
        bd.Cylinder(
            radius=d_outer / 2,
            height=h,
            align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
        )
        bd.Cylinder(
            radius=d_hole / 2,
            height=h + 0.2,
            align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
            mode=bd.Mode.SUBTRACT,
        )
        # Note: The hole subtraction might need to be shifted down slightly to ensure clean cut,
        # but align MIN with h+0.2 should cover it if we shift Z down by 0.1.
        # Actually, let's just center the hole on the standoff's center Z but make it longer.
        # Or stick to the align MIN and move it down.

    # Re-doing standoff to be robust
    with bd.BuildPart() as p2:
        bd.Cylinder(
            radius=d_outer / 2,
            height=h,
            align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
        )
        with bd.Locations((0, 0, -0.1)):
            bd.Cylinder(
                radius=d_hole / 2,
                height=h + 0.2,
                align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN),
                mode=bd.Mode.SUBTRACT,
            )
    return p2.part
