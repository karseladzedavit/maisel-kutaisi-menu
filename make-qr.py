"""Generate the Maisel Kutaisi menu QR code.

Usage:  python make-qr.py https://your-menu-url.example

Writes qr.svg (vector, for print) and qr.png (2000px, for screens/social).
Error correction is set to H so the code still scans if the card gets
scuffed or a logo is dropped in the middle.
"""
import sys
import segno

NAVY = "#16386B"

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python make-qr.py <url>")
    url = sys.argv[1]

    qr = segno.make(url, error="h")

    qr.save("qr.svg", scale=10, border=2, dark=NAVY, light="#FFFFFF")
    qr.save("qr.png", scale=24, border=2, dark=NAVY, light="#FFFFFF")

    print("url     :", url)
    print("version :", qr.version, "| error correction: H (30%)")
    print("wrote   : qr.svg, qr.png")

if __name__ == "__main__":
    main()
