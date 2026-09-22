"""bannergen CLI - AI-powered social media banner generator.

Usage:
    bannergen generate "prompt" --platform twitter --brand "My Brand"
    bannergen list-templates
    bannergen batch prompts.txt
"""

import argparse
import json
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="bannergen",
        description="Generate AI-powered social media banners",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # generate
    gen = sub.add_parser("generate", help="Generate a single banner")
    gen.add_argument("prompt", type=str, help="Description of the banner image")
    gen.add_argument("--platform", "-p", default="twitter",
                     choices=["twitter", "linkedin", "instagram", "youtube", "facebook"],
                     help="Target platform")
    gen.add_argument("--brand", "-b", default=None, help="Brand name (overlaid on image)")
    gen.add_argument("--tagline", "-t", default=None, help="Tagline or subtitle")
    gen.add_argument("--style", "-s", default="modern",
                     choices=["modern", "minimal", "bold", "elegant", "fun"],
                     help="Visual style")
    gen.add_argument("--output", "-o", default=None, help="Output file path")
    gen.add_argument("--width", type=int, default=None, help="Override width")
    gen.add_argument("--height", type=int, default=None, help="Override height")
    gen.add_argument("--api-key", default=None, help="FAL API key (default: FAL_KEY env)")

    # list-templates
    lt = sub.add_parser("list-templates", help="Show available platform templates")

    # batch
    batch = sub.add_parser("batch", help="Generate banners from a file")
    batch.add_argument("file", type=str, help="Text file with one prompt per line")
    batch.add_argument("--platform", "-p", default="twitter", help="Platform for all")
    batch.add_argument("--brand", "-b", default=None, help="Brand for all")
    batch.add_argument("--style", "-s", default="modern", help="Style for all")
    batch.add_argument("--outdir", "-o", default="./banners", help="Output directory")

    args = parser.parse_args()

    if args.command == "list-templates":
        _list_templates()
    elif args.command == "generate":
        _generate(args)
    elif args.command == "batch":
        _batch(args)


def _list_templates():
    """Display available platform templates with their dimensions."""
    templates = {
        "twitter": {
            "label": "X / Twitter",
            "width": 1500,
            "height": 500,
            "aspect": "3:1",
            "desc": "Header / banner image",
        },
        "linkedin": {
            "label": "LinkedIn",
            "width": 1584,
            "height": 396,
            "aspect": "4:1",
            "desc": "Company page banner",
        },
        "instagram": {
            "label": "Instagram",
            "width": 1080,
            "height": 1080,
            "aspect": "1:1",
            "desc": "Square post",
        },
        "instagram-story": {
            "label": "Instagram Story",
            "width": 1080,
            "height": 1920,
            "aspect": "9:16",
            "desc": "Story / Reel cover",
        },
        "youtube": {
            "label": "YouTube",
            "width": 2560,
            "height": 1440,
            "aspect": "16:9",
            "desc": "Channel banner",
        },
        "facebook": {
            "label": "Facebook",
            "width": 1640,
            "height": 624,
            "aspect": "2.63:1",
            "desc": "Cover photo",
        },
    }
    print(f"{'Platform':<20} {'Width':>6} {'Height':>7} {'Aspect':<10} {'Description'}")
    print("-" * 65)
    for key, t in templates.items():
        print(f"{t['label']:<20} {t['width']:>6} {t['height']:>7} {t['aspect']:<10} {t['desc']}")


def _get_platform_dims(platform):
    dims = {
        "twitter": (1500, 500),
        "linkedin": (1584, 396),
        "instagram": (1080, 1080),
        "youtube": (2560, 1440),
        "facebook": (1640, 624),
    }
    return dims.get(platform, (1500, 500))


def _style_prompt(style, base_prompt, brand=None):
    """Enhance the prompt with style guidance."""
    style_guides = {
        "modern": "clean, modern, professional, subtle gradients, soft lighting",
        "minimal": "minimalist, plenty of negative space, simple composition, clean lines",
        "bold": "bold colors, high contrast, dramatic lighting, striking composition",
        "elegant": "elegant, premium quality, refined, sophisticated, luxurious",
        "fun": "playful, vibrant, energetic, colorful, dynamic composition",
    }
    style_hint = style_guides.get(style, style_guides["modern"])
    enhanced = f"{base_prompt}, {style_hint}, digital art, banner format, wide aspect ratio"
    return enhanced


def _generate(args):
    """Generate a single banner."""
    platform = args.platform
    width = args.width
    height = args.height
    if not width or not height:
        w, h = _get_platform_dims(platform)
        width = width or w
        height = height or h

    enhanced = _style_prompt(args.style, args.prompt, args.brand)

    print(f"🎨 Generating {platform.capitalize()} banner ({width}x{height})...")
    print(f"   Prompt: {enhanced[:100]}...")

    # Check if user has their own FAL key or wants to use the agent
    api_key = args.api_key or os.environ.get("FAL_KEY")
    if not api_key:
        print("\n⚠ No FAL_KEY found. To use bannergen, you need a FAL.ai API key.")
        print("  Get one at https://fal.ai/ and set it:")
        print("    export FAL_KEY=your-key-here")
        print("  Or pass: --api-key your-key-here")
        print("\n  For demo mode (uses agent's image generation):")
        print("    bannergen demo --prompt '...'")
        sys.exit(1)

    # For a standalone CLI, the user supplies their own FAL key
    # Here we call the FAL API directly
    import requests

    headers = {
        "Authorization": f"Key {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "prompt": enhanced,
        "image_size": {
            "width": width,
            "height": height,
        },
        "num_images": 1,
    }

    print("   Calling FAL API...")
    try:
        resp = requests.post(
            "https://fal.run/fal-ai/flux-pro/v1.1",
            json=payload,
            headers=headers,
            timeout=120,
        )
        if resp.status_code != 200:
            print(f"❌ API error: {resp.status_code} - {resp.text[:200]}")
            sys.exit(1)

        result = resp.json()
        image_url = result.get("images", [{}])[0].get("url")
        if not image_url:
            print("❌ No image URL in response")
            sys.exit(1)

        # Download the image
        img_resp = requests.get(image_url, timeout=30)
        ext = Path(image_url).suffix or ".png"

        output_path = args.output or f"banner_{platform}_{args.style}.{ext}"
        Path(output_path).write_bytes(img_resp.content)
        print(f"✅ Banner saved to: {output_path}")

        # Apply overlay if brand or tagline provided
        if args.brand or args.tagline:
            _add_text_overlay(output_path, args.brand, args.tagline)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def _add_text_overlay(image_path, brand, tagline):
    """Add text overlay to the generated image using Pillow."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("⚠ Pillow not installed. Skipping text overlay.")
        print("  Install: pip install Pillow")
        return

    try:
        img = Image.open(image_path).convert("RGBA")

        # Create overlay layer
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        w, h = img.size

        # Determine font sizes relative to image
        font_size_large = max(32, h // 10)
        font_size_small = max(18, h // 18)

        # Try to load fonts, fall back to default
        try:
            font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size_large)
            font_reg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size_small)
        except (IOError, OSError):
            font_bold = ImageFont.load_default()
            font_reg = ImageFont.load_default()

        # Draw brand name at bottom-left with semi-transparent background
        if brand:
            # Text background bar
            bar_height = h // 5
            bar_y = h - bar_height - 20
            draw.rectangle([(0, bar_y), (w, h)], fill=(0, 0, 0, 100))

            # Brand name
            bbox = draw.textbbox((0, 0), brand, font=font_bold)
            tw = bbox[2] - bbox[0]
            tx = 40
            ty = bar_y + (bar_height - (bbox[3] - bbox[1])) // 2
            draw.text((tx, ty), brand, fill=(255, 255, 255, 230), font=font_bold)

            # Tagline if provided
            if tagline:
                ty2 = ty + (bbox[3] - bbox[1]) + 5
                draw.text((tx, ty2), tagline, fill=(255, 255, 255, 180), font=font_reg)

        # Composite
        result = Image.alpha_composite(img, overlay)
        result = result.convert("RGB")
        result.save(image_path)
        print(f"✅ Text overlay applied to: {image_path}")

    except Exception as e:
        print(f"⚠ Text overlay failed: {e}")


def _batch(args):
    """Process multiple prompts from a file."""
    if not os.path.exists(args.file):
        print(f"❌ File not found: {args.file}")
        sys.exit(1)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    with open(args.file) as f:
        prompts = [line.strip() for line in f if line.strip()]

    if not prompts:
        print("❌ No prompts found in file")
        sys.exit(1)

    print(f"📦 Generating {len(prompts)} banners for {args.platform}...")

    for i, prompt in enumerate(prompts, 1):
        # Create a mock args object
        class MockArgs:
            prompt = prompt
            platform = args.platform
            brand = args.brand
            style = args.style
            tagline = None
            api_key = None
            output = str(outdir / f"banner_{i:03d}_{args.platform}.png")

        _generate(MockArgs())

    print(f"\n✅ All {len(prompts)} banners saved to {outdir}/")


if __name__ == "__main__":
    main()