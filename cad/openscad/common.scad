// OpenHorizon-FC: shared OpenSCAD helper “library”
//
// These modules are small building blocks used by multiple parts (rounded plates,
// slots, standoffs, etc.). The goal is to keep the actual part files readable.
//
// Units: millimeters.

$fn = 64;

module rounded_rect_2d(w, h, r) {
  // A 2D rounded rectangle centered at the origin.
  // `r` is clamped so it never exceeds half the smaller dimension.
  r2 = min(r, min(w, h) / 2);
  hull() {
    translate([ w/2 - r2,  h/2 - r2]) circle(r=r2);
    translate([-w/2 + r2,  h/2 - r2]) circle(r=r2);
    translate([ w/2 - r2, -h/2 + r2]) circle(r=r2);
    translate([-w/2 + r2, -h/2 + r2]) circle(r=r2);
  }
}

module rounded_plate(w, h, t, r) {
  // A 3D plate made by extruding `rounded_rect_2d()`.
  linear_extrude(height=t) rounded_rect_2d(w, h, r);
}

module hole_cyl(d, h, center=true) {
  // Convenience wrapper to make “hole cylinders” read nicely at call-sites.
  cylinder(d=d, h=h, center=center);
}

module slot_2d(len, w) {
  // A 2D “capsule” slot centered at the origin.
  // `len` is the overall length end-to-end, `w` is the slot width.
  hull() {
    translate([ len/2, 0]) circle(d=w);
    translate([-len/2, 0]) circle(d=w);
  }
}

module slot(len, w, h) {
  // 3D version of `slot_2d()`.
  linear_extrude(height=h) slot_2d(len, w);
}

module standoff(d_outer, d_hole, h) {
  // Simple cylindrical standoff with a through-hole.
  // Useful for PCB mounting (prints as a solid with the hole cut out).
  difference() {
    cylinder(d=d_outer, h=h);
    translate([0,0,-0.1]) cylinder(d=d_hole, h=h+0.2);
  }
}

