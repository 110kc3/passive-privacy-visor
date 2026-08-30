# Bill of materials: Gliwice, Poland

Checked **2026-08-30**. Destination assumption: a normal residential address in central Gliwice, postcode `44-100`.

The shops expose Polish delivery methods and prices, but neither public product page validates a particular street address. Enter the exact address at checkout before paying. Item prices, promotions, shipping, and stock can change.

## Recommended two-shop order

### Order A: faceguard from Allegro

| Qty | Item | Price | Shipping | Checked line total |
|---:|---|---:|---:|---:|
| 1 | [NEO Tools 97-392 adjustable steel-mesh faceguard](https://allegro.pl/produkt/przylbica-czolowa-neo-tools-z-regulacja-kata-i-obwodu-fc42e7fc-8807-4177-ba6c-fd812e5e5d3f) | 48.59 zl | 10.49 zl | **59.08 zl** |

The listing describes a `200 x 350 mm`, `313 g`, CE-marked faceguard with circumference, depth, face-distance, and angle adjustment. The listed delivery charge was 10.49 zl. Confirm it remains available for the precise Gliwice address at checkout.

Alternative: [Media Expert lists the same NEO 97-392](https://www.mediaexpert.pl/dom-i-ogrod/odziez-robocza/przylbiceprzylbice/oslona-twarzy-neo-97-392) at 48.59 zl and offers delivery or store collection. Its public page does not expose a stable standard shipping price, so it is not used in the delivered total. Free collection could reduce the budget if a nearby branch has stock.

### Order B: overlay materials from Stoklasa

| Profile | Qty | Item and selected variant | Price |
|---|---:|---|---:|
| Core | 1 m | [Stiff tulle](https://www.stoklasa.pl/tiul-sztywny-x160513), black; choose the stiffest available black variant | 13.29 zl |
| Core | 1 m | [Double-sided hook-and-loop tape, 20 mm](https://www.stoklasa.pl/tasma-rzep-szerokosc-20-mm-dwustronna-x128198), black | 6.81 zl |
| Core | 1 pack / 5 m | [Sew-on reflective tape, 25 mm](https://www.stoklasa.pl/tasma-odblaskowa-szerokosc-25-mm-do-naszycia-x150425) | 12.50 zl |
| Core | 1 pack / 2 sheets | [Non-adhesive Moosgummi foam, 20 x 30 cm](https://www.stoklasa.pl/pianka-gumowa-moosgummi-20x30cm-x130828?barva=144227), black | 5.60 zl |
| Complete only | 1 card | [Hand-sewing needle set](https://www.stoklasa.pl/zestaw-igiel-do-szycia-recznego-x151300) | 5.41 zl |
| Complete only | 1 spool | [Unipoly polyester thread, 1000 m](https://www.stoklasa.pl/nici-poliestrowe-unipoly-nawoj-1000-m-x150393), black `999` | 10.61 zl |

[Stoklasa's Polish delivery page](https://www.stoklasa.pl/zpusoby-doruceni-a-plateb-x3903) lists the normal GLS home-delivery price as **12.70 zl including VAT**. Its [FAQ](https://www.stoklasa.pl/najczesciej-zadawane-pytania-x31078) says orders are ordinarily prepared within two working days and can be sent to Poland. A temporary promotion visible on the check date was deliberately excluded.

## Totals

| Profile | Allegro items | Allegro shipping | Stoklasa items | Stoklasa shipping | Delivered total |
|---|---:|---:|---:|---:|---:|
| Core, needle/thread already owned | 48.59 zl | 10.49 zl | 38.20 zl | 12.70 zl | **109.98 zl** |
| Complete from scratch | 48.59 zl | 10.49 zl | 54.22 zl | 12.70 zl | **126.00 zl** |

The complete kit includes much more thread, reflective tape, and needle capacity than one visor consumes, so later overlays will be cheaper.

The machine-readable values live in [`data/bom.json`](../data/bom.json). Verify the arithmetic with:

```bash
python3 scripts/budget.py --profile all
```

## Tools expected on hand

- paper or thin card for the first pattern;
- ruler and washable marker or chalk;
- scissors suitable for fabric and thin foam;
- small sewing clips or ordinary paper clips;
- phone/camera and a stable support for testing.

Do not use staples, exposed wire, rigid sharp fasteners, or clipped cable-tie tails near the face.

## Base alternative

If the NEO guard becomes unavailable, [PolskiDrwal lists the Oregon 515064 mesh shield](https://polskidrwal.pl/2409-siatkowa-oslona-twarzy-515064.html) at 66.42 zl with shipping from 12 zl (at least 78.42 zl delivered). The page states CE and EN 1731 compliance. Verify that the chosen head carrier is included and adjustable before substituting it.

## Buying checklist

- [ ] Destination and final shipping verified for the exact Gliwice address
- [ ] Black, stiff tulle variant selected
- [ ] Non-adhesive black foam selected
- [ ] Double-sided hook-and-loop selected, not adhesive-backed tape
- [ ] Sew-on reflective tape selected; never treated as safety PPE
- [ ] No active infrared, laser, strobe, or visible-LED components added
