# Maisel Kutaisi - online menu

Mobile-first bilingual (ქართული / English) menu page, styled to the
Maisel's Weisse label, plus the QR code and print-ready table cards.

## Files

| File | What it is |
|---|---|
| `index.html` | The menu page. Layout, styling and the `SITE` contact config. |
| `menu-data.js` | Every item and price. **This is the only file you edit day to day.** |
| `make-qr.py` | Generates `qr.svg` + `qr.png` from the live URL. |
| `card.html` | A4 sheet of four A6 table cards with the QR, ready to print and cut. |
| `logo.png` | Optional. Drop the real logo here and the page uses it automatically. |

## Changing a price or an item

Open `menu-data.js` and edit the line. Nothing else needs touching.

```js
{ka:"ხაჭაპური მეგრული", en:"Megrelian Khachapuri", p:[["","21.50"]]},
```

- `p:[["","21.50"]]` - one price, no size label.
- `p:[["1L","16.90"],["0.5L","8.90"]]` - several sizes.
- Optional `nka` / `nen` add the small grey note under the name.

Save, commit, push. The live page updates in about a minute.

## Contact details

Near the bottom of `index.html`:

```js
var SITE = {
  addressKa: "ქუთაისი, ...",
  addressEn: "..., Kutaisi",
  phone:     "+995 ...",
  hoursKa:   "ყოველდღე 12:00 - 02:00",
  hoursEn:   "Daily 12:00 - 02:00",
  facebook:  "https://...",
  instagram: "https://..."
};
```

Any field left as `""` is simply not shown.

## Regenerating the QR

```bash
python -m pip install segno
python make-qr.py https://YOUR-LIVE-URL
```

Then open `card.html` and print it (A4, no margins, background graphics on).
Four cards per sheet.

The QR uses error correction level H, so it still scans with a logo covering
the middle or after normal wear on a table.

## Local preview

```bash
python -m http.server 8787
```

Then open http://127.0.0.1:8787/
