# Design specification

## Objective

Create a wearable that visibly fragments a consenting wearer's face in normal phone and webcam recordings without projecting light toward the wearer or camera.

The first version prioritizes:

1. eye safety;
2. an unobstructed central viewing corridor;
3. parts that can be bought now in Poland;
4. reversible assembly;
5. a strong cyberpunk appearance even when the camera-distortion effect is weak.

## Architecture

### 1. Base: adjustable steel-mesh faceguard

The NEO 97-392 provides a head carrier and a curved `350 x 200 mm` mesh surface. Use the original adjustments for circumference, depth, face distance, and visor angle. Do not drill, cut, bend, paint, or glue the base.

The base mesh is the only layer allowed across the eye corridor. Its regular grid may already alias on some cameras, but its main role is structural.

### 2. Removable angled screen

Cut one piece of stiff black tulle to follow the outer face of the guard, then remove a generous eye window. Rotate the tulle approximately `5-10 degrees` relative to the steel grid before securing it around the perimeter with short double-sided hook-and-loop straps.

The overlap of two grid pitches can create large moving moire bands in sampled video. The effect is camera-dependent, so the angle is deliberately tunable. Keep the tulle on the camera-facing side of the steel mesh.

### 3. Landmark-breaking panels

Attach five matte-black foam pieces to the tulle carrier:

- two brow fins above the eye corridor;
- two cheek plates outside the nose and mouth airflow area;
- one small chin plate.

Use rounded corners and soft material. The starter shapes in [`assets/panel-template-a4.svg`](../assets/panel-template-a4.svg) are intentionally conservative and must be adapted to the wearer. Their purpose is to break the familiar brow-cheek-jaw geometry, not to press against the face.

### 4. Retroreflective accents

Stitch small pieces of sew-on reflective tape to the outward face of the foam. Space them asymmetrically. They may flare when a phone flash or lamp is close to the camera axis, but they do not create light and are not relied on for the core obscuration.

The sourced craft tape is explicitly not a safety marking. Do not use it as visibility PPE.

## Fit zones

All dimensions are initial targets, not universal anatomy.

| Zone | Starting size | Rule |
|---|---:|---|
| Overall tulle carrier | about `325 x 180 mm` | Trim from a paper pattern made on the unworn guard |
| Clear eye corridor | at least `180 x 60 mm` | Enlarge until the wearer has comfortable central and peripheral vision |
| Brow fins | `70 x 24 mm` each | Entirely above the eye corridor |
| Cheek plates | about `65 x 52 mm` each | Outside nose and mouth airflow paths |
| Chin plate | about `90 x 34 mm` | No contact with lips, throat, or neck |
| Reflective tabs | `20 x 40 mm` or smaller | Outward-facing and below/above the sightline |

Never mark or cut material while the guard is being worn. Maintain at least `20 mm` clearance between every added hard edge or stitch tail and the eye corridor.

## Target requirements

| ID | Requirement | Verification |
|---|---|---|
| S1 | No powered or emitting components | Visual inspection |
| S2 | No added material in the eye corridor | Front and wearer-side inspection |
| S3 | Nothing sharp or loose on the wearer side | Finger sweep and shake test while unworn |
| S4 | Original adjustment and flip-up motion remain free | Cycle each control 20 times |
| S5 | Overlay can be removed without tools | Timed dry run while seated |
| U1 | Ten-minute seated wear causes no strain, pressure, or breathing issue | Wearer report; stop at first symptom |
| V1 | Facial landmarks look less stable than the no-visor baseline | Paired camera test |
| V2 | At least one useful configuration works in the target lighting/camera setup | Test matrix, not assumption |

## Known limits

- Moire can disappear when focus, distance, resolution, or camera processing changes.
- Retroreflection needs illumination near the camera axis and does little in diffuse daylight.
- Matte panels provide reliable physical occlusion but may make the wearer more distinctive.
- The lower face can remain partially readable to preserve airflow.
- Recognition can use signals other than a face.
- Adding anything to a certified faceguard means the completed wearable must not be treated as certified PPE.
