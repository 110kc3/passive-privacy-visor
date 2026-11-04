# Safety rules

This prototype was selected specifically to avoid optical emitters. It contains no infrared LEDs, visible LEDs, lasers, strobes, batteries, or powered electronics. Do not add them.

## Non-negotiable constraints

- Keep the full central and peripheral eye corridor free of every added material. Only the faceguard's original mesh may cross it.
- Put all knots, cut edges, panels, and reflective surfaces on the camera-facing side.
- Do not drill, cut, bend, heat, glue, or paint the faceguard.
- Do not use exposed wire, staples, pins, hard spikes, magnets, or trimmed cable ties.
- Preserve the manufacturer's fit controls, flip-up range, and normal removal path.
- Never test alone the first time.
- Stop immediately for eye strain, headache, dizziness, nausea, panic, overheating, skin irritation, breathing difficulty, pressure, or reduced balance.

## Visibility gate

Perform these checks in a well-lit, uncluttered room while seated, first with the unmodified guard and again with the finished overlay:

1. Read ordinary phone interface text at arm's length with each eye and then both eyes.
2. Identify the helper's raised fingers at `1 m`, `3 m`, and at the left/right edge of comfortable vision without turning the head.
3. Identify high-contrast objects on the floor at `1 m` and `2 m`.
4. Look left, right, up, and down without any added edge entering the eye corridor.
5. Remove the visor using its normal mechanism without the overlay snagging.
6. Wear it seated for ten minutes. There must be no symptom or progressive visual discomfort.

Failure of any check means stop and enlarge/remove material. Passing this informal gate does not certify the device.

Mechanical and visibility safety checklists can be logged and verified using the automated safety gate tool:

```bash
python -m scripts.safety_gate data/reference-safety-log-r1.json
```

## Where not to wear it

The mesh reduces light and the design can restrict peripheral vision. Do not use it while:

- driving, cycling, skating, or operating machinery;
- crossing roads or moving through traffic;
- on stairs, platforms, roofs, construction sites, or near open water;
- doing sport, running, cooking, welding, or working near heat/flame;
- performing any task where full vision, hearing, identification, or PPE is required.

Use stationary, controlled photo/video sessions. Remove it before walking to or from the test position.

## Material and PPE limits

- Modified equipment is not certified PPE, even if the base product carries a conformity mark.
- Tulle and craft foam may ignite or melt. Keep them away from flame, heaters, sparks, and hot tools.
- The sourced reflective tape is decorative in this project and is not a safety visibility device.
- Air out new materials and stop if the wearer has a skin or respiratory reaction.
- Inspect stitching and straps before every use. Retire any cracked, corroded, permanently bent, or loose part.

## Recording ethics

Test on yourself or another fully informed, consenting adult. Keep bystanders and identifying background information out of test footage. Follow venue rules and applicable law. This project does not authorize interfering with cameras, damaging equipment, trespassing, impersonation, or evading a lawful obligation to identify yourself.
