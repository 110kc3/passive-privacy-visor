# Research and design rationale

## Why the project rejects active light

Historic camera-privacy wearables used near-infrared illumination. The National Institute of Informatics' [PrivacyVisor paper](https://dl.ifip.org/IFIP-TC11/hal-01492817v1) demonstrated that direction, but it is not a reliable basis for a modern universal device.

[FacePET's camera experiments](https://www.mdpi.com/2079-9292/7/12/379) found that infrared emitters did not affect the tested iPhones because of their infrared filtering, so its researchers moved to visible LEDs. Camera makers also document that ordinary color cameras commonly place an [IR-cut filter](https://softwareservices.flir.com/FG-PGE-50S5-IP/latest/40-Installation/InfraredFilters-FG-IP.htm) in the optical path.

Visible emitters solve neither comfort nor discretion, while do-it-yourself optical emitters create avoidable exposure and assessment problems. [IEC 62471](https://webstore.iec.ch/en/publication/7076) exists specifically to evaluate photobiological safety of lamps and lamp systems, including LEDs across ultraviolet, visible, and infrared wavelengths. A finished source/system must be assessed; buying a nominally low-power LED is not the same thing.

The safest practical conclusion for this build is simple: use no emitter at all.

## Why overlapping grids

The steel guard and angled tulle form two regular spatial grids. Camera sampling can turn fine grids into larger false bands that shift with viewing angle, focus, and movement. Stage-scrim supplier ShowTex likewise warns that [overlapping scrim layers can create a moire effect](https://www.showtex.com/en/products/soft-goods/backdrops-ceilings/scrim-netting-gauze/gobelintulle).

That source describes theatrical scrim rather than the exact purchased craft tulle, so it establishes the mechanism, not guaranteed performance. The practical angle must be found with the target camera.

## Why physical occlusion remains primary

Moiré is fragile: resolution changes, autofocus, stabilization, and compression can weaken it. Matte foam facets provide camera-independent obstruction of brows, cheek contours, and jaw geometry. They are deliberately soft, lightweight, and outside the viewing corridor.

## Why retroreflective accents are secondary

Retroreflective material returns a portion of incident light toward its source; 3M describes the glass-bead construction and wide-angle response of [Scotchlite 8910](https://www.3m.co.uk/3M/en_GB/p/d/b00012425/). This can create local flare when illumination is close to a camera lens.

The project uses a generic craft tape, not the 3M product, so only direct testing can establish its response. It is a decorative camera experiment, not a safety marking and not the primary privacy mechanism.

## Evidence hierarchy used here

1. Passive physical occlusion: dependable in principle, though coverage varies by view.
2. Mesh/tulle moire: plausible and tunable, but camera-dependent.
3. Retroreflective flare: lighting-dependent bonus.
4. Active IR/visible illumination: rejected for compatibility, comfort, and safety reasons.
