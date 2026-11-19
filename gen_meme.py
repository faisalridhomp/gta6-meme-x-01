#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme: AI Vice City background + real make.fun
ghost mark + GTA 'WASTED -> PAID' joke text. Deterministic, local only.
Run: python3 gen_meme.py  -> writes meme.png (1024x1024) next to this file.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG = "assets/media-generation-gta6-meme-bg-0-2957f58f-dbdd-4bf2-8173-4bc0a87fac14.png"
MARK = "assets/mark-1024.png"
OUT = "meme.png"
W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def text(draw, cx, y, s, font, fill, stroke_w=6, stroke_fill="black"):
    w = draw.textlength(s, font=font)
    draw.text((cx - w / 2, y), s, font=font, fill=fill,
              stroke_width=stroke_w, stroke_fill=stroke_fill)


def main():
    img = Image.open(BG).convert("RGB").resize((W, H))
    # Top + bottom scrims for legibility
    scrim = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(scrim)
    d.rectangle([0, 0, W, 170], fill=110)
    d.rectangle([0, 620, W, H], fill=110)
    scrim = scrim.filter(ImageFilter.GaussianBlur(60))
    black = Image.new("RGB", (W, H), (0, 0, 0))
    img = Image.composite(black, img, scrim)
    draw = ImageDraw.Draw(img)

    # 1. Top line
    f_top = ImageFont.truetype(BOLD, 52)
    text(draw, W // 2, 44, "WAITED 13 YEARS FOR GTA 6", f_top, "white", 7)

    # 2. make.fun ghost mark, centred, with soft shadow
    mark = Image.open(MARK).convert("RGBA").resize((400, 400), Image.LANCZOS)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse([W // 2 - 195, 235, W // 2 + 195, 635], fill=(0, 0, 0, 140))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img.convert("RGBA"), shadow)
    img.paste(mark, (W // 2 - 200, 225), mark)
    draw = ImageDraw.Draw(img)

    # 3. WASTED, struck through in red
    f_wasted = ImageFont.truetype(BOLD, 68)
    wasted = "WASTED"
    ww = draw.textlength(wasted, font=f_wasted)
    wx, wy = W // 2 - ww / 2, 648
    draw.text((wx, wy), wasted, font=f_wasted, fill=(200, 200, 200),
              stroke_width=6, stroke_fill="black")
    # red strike line, slight tilt for meme energy
    draw.line([(wx - 6, wy + 36), (wx + ww + 6, wy + 36)], fill=(255, 30, 30), width=12)

    # 4. PAID. big green
    f_paid = ImageFont.truetype(BOLD, 118)
    text(draw, W // 2, 722, "PAID.", f_paid, (57, 255, 106), 9)

    # 5. Bottom pitch lines
    f_bot = ImageFont.truetype(BOLD, 40)
    text(draw, W // 2, 872, "MY AGENT MADE THIS MEME.", f_bot, "white", 6)
    text(draw, W // 2, 922, "make.fun PAID FOR IT.", f_bot, (255, 214, 64), 6)

    img.convert("RGB").save(OUT, "PNG")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
