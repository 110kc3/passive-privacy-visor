# Camera and wearer test plan

The goal is evidence about a specific camera setup, not a universal anonymity claim. Preserve a baseline clip from the same position and lighting for every visor clip.

## Setup

- Test only a consenting adult in a private, uncluttered space.
- Place the camera on a stable support at approximately eye height.
- Use the normal camera app with beauty filters and portrait effects disabled.
- Keep resolution, frame rate, zoom, exposure mode, background, and lighting unchanged within each baseline/visor pair.
- Use a plain background and remove distinctive clothing if the purpose is evaluating the face effect alone.

## Minimum matrix

Run a baseline and visor clip for each row:

| ID | Camera | Distance | Lighting | Camera light |
|---|---|---:|---|---|
| D1 | rear phone camera | 1 m | diffuse daylight | off |
| D2 | rear phone camera | 3 m | diffuse daylight | off |
| I1 | rear phone camera | 1 m | indoor room light | off |
| I2 | rear phone camera | 3 m | indoor room light | off |
| F1 | rear phone camera | 1 m | indoor room light | flash/torch on |
| F2 | rear phone camera | 3 m | indoor room light | flash/torch on |
| W1 | laptop webcam | normal seated distance | indoor room light | off |
| M1 | front phone camera | arm's length | indoor room light | screen/flash off |

For each ten-second clip, look forward for four seconds, turn about 30 degrees left, return, then turn about 30 degrees right. Do not walk while wearing the visor.

## Log fields

Copy [`templates/test-results.csv`](../templates/test-results.csv) for each build revision. Record:

- device and camera direction;
- resolution and frame rate;
- measured or paced distance;
- lighting and camera-light state;
- tulle angle and overlay revision;
- whether a face box appears, if the stock camera shows one;
- human landmark-disruption score;
- wearer visibility/comfort result;
- notes and safe next change.

## Manual scoring

Reviewers should not be told which tulle angle is expected to work best.

| Score | Meaning |
|---:|---|
| 0 | Visor is decorative; major landmarks remain stable and easy to read |
| 1 | Some aliasing/occlusion, but eyes-brow-nose-mouth geometry remains mostly stable |
| 2 | Multiple major landmarks are fragmented or hidden through most of the clip |
| 3 | The visible face is consistently difficult for a human reviewer to parse |

A face-detector box is only an extra observation. Its absence does not establish anonymity, and a detector is not an identity-recognition system.

## Prototype acceptance gate

A revision is worth keeping when:

- every wearer safety check passes before and after the recording session;
- no part loosens, catches, or moves into the eye corridor;
- the target real-world camera/lighting rows average at least score 2;
- the effect survives both forward and 30-degree views;
- the same reviewer sees a clear improvement over baseline footage.

If it fails visually but passes safely, adjust one exterior variable and retest. If it fails any safety check, stop using the revision regardless of camera performance.

## Data hygiene

Store only the footage needed for comparison. Get explicit permission before sharing a participant's face. Crop or blur bystanders and remove location metadata before publishing results.
