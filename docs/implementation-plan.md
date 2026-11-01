# Implementation plan

## Current status

- [x] Select a no-emitter architecture
- [x] Define safety constraints and rejection criteria
- [x] Source a two-shop Polish BOM and normal shipping rates
- [x] Create geometry, starter templates, build instructions, and test records
- [x] Automate and test the purchase totals
- [x] Add continuous integration (CI) workflow running repository and budget test suites
- [x] Add automated test-results matrix and disruption score validator (`scripts/evaluate_results.py`)
- [ ] Buy parts for the exact Gliwice address
- [ ] Inspect and fit the unmodified faceguard
- [ ] Build and validate revision 1
- [ ] Publish consenting, metadata-cleaned test results

The repository is ready for procurement. Camera efficacy and wearer fit remain deliberately unclaimed until a physical unit is tested.

## Milestones

| Milestone | Work | Typical hands-on time | Exit gate |
|---|---|---:|---|
| M0 — procurement | Recheck links, choose core/complete profile, verify checkout totals | 20-30 min | Correct variants and delivery accepted |
| M1 — base acceptance | Assemble, inspect, fit, and test unmodified faceguard | 30-45 min | All baseline visibility/removal checks pass |
| M2 — paper prototype | Trace carrier, size eye corridor, place paper facets | 60-90 min | Helper and wearer approve seated fit |
| M3 — textile revision 1 | Sew tulle carrier, straps, foam, and accents | 2-3 h | Shake/tug/control-cycle checks pass |
| M4 — safety validation | Inspect inside, run one- and ten-minute seated gates | 20-30 min | Zero symptoms, snags, or sightline intrusions |
| M5 — camera characterization | Record paired clips across the minimum matrix | 60-90 min | Results logged for all target rows |
| M6 — tune one variable | Change tulle angle or one exterior panel detail | 30-60 min/round | Improvement repeats in a fresh paired test |

Allow one weekend after the materials arrive. Do not compress M1-M4 into a single fit session if the wearer develops fatigue or visual discomfort.

## Decision gates

### Gate A: checkout

Proceed only if the exact Gliwice address is accepted and the final total is still reasonable. If a price changes, update [`data/bom.json`](../data/bom.json), run the tests, and update the dated table in [`bom-pl.md`](bom-pl.md).

### Gate B: unmodified guard

If the original faceguard itself fails visibility, comfort, adjustment, or removal checks, return/replace it. Do not try to compensate by modifying the carrier.

### Gate C: paper fit

If a paper edge is visible to the wearer, enlarge the eye corridor or shrink the relevant panel. Camera appearance never overrides this gate.

### Gate D: finished mechanical inspection

Any loose part, interior knot, sharp edge, control snag, or contact with the face blocks wear testing. Repair it on the table and repeat the full inspection.

### Gate E: camera evidence

Keep a revision only if it passes every safety check and improves the target camera rows over their baselines. A visually weak but safe revision can be tuned; an unsafe revision is retired.

## Revision strategy

Use short labels on the CSV and carrier tag:

- `R0`: unmodified base;
- `R1-A5`: first overlay at 5-degree tulle rotation;
- `R1-A7`: same overlay at 7 degrees;
- `R2-*`: panel geometry changed.

Change one variable between labels. This separates actual camera response from lighting or expectation.

## Primary risks and controls

| Risk | Likelihood before testing | Control |
|---|---|---|
| Moire vanishes on the target camera | Medium/high | Tune angle/distance; retain foam occlusion as the primary effect |
| Peripheral vision is reduced | Medium | Oversized eye corridor, seated gate, stationary use only |
| Overlay catches the flip-up mechanism | Medium | Six removable straps, 20 control cycles before wear |
| Foam or stitching comes loose | Low/medium | Rounded soft panels, exterior knots, shake/tug test every session |
| Flash effect is weak | High in daylight | Treat reflective accents as optional styling, never core performance |
| Wearer becomes more visually distinctive | High | State the anonymity limit; use only where that tradeoff is acceptable |
| Shop price or stock changes | High over time | Dated data, two base suppliers, automated arithmetic |

## Definition of done for revision 1

- [ ] Exact checkout cost and arrival condition logged
- [ ] Baseline safety gate passed on the unmodified guard
- [ ] Printed calibration square measures `20 x 20 mm`
- [ ] Eye corridor contains no added material
- [ ] All seams, knots, and panels are on the exterior
- [ ] Adjustments and flip-up control complete 20 cycles without catching
- [ ] One-minute and ten-minute seated tests are symptom-free
- [ ] All minimum camera rows have paired baseline/visor clips
- [ ] Target rows average manual disruption score 2 or better
- [ ] Test CSV is committed without non-consenting faces or identifying metadata
