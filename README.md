# BannerGen — AI Social Media Banner Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Buy on Gumroad](https://img.shields.io/badge/Buy%20on%20Gumroad-%243+-green?logo=gumroad)](https://grantshatz.gumroad.com/l/oushyg)

**Turn any idea into a professional social media banner in seconds.**

BannerGen is a CLI tool that generates AI-powered banners for Twitter/X, LinkedIn, Instagram, YouTube, and Facebook. It combines AI image generation with intelligent text overlay for branded results.

![Sample Banner](https://v3b.fal.media/files/b/0aab87b5/x7AytIe53SzaYQ9_tnFyw_X0KMvUTH.png)

## 🔗 Buy Now — $3+ (Pay What You Want)

**[Purchase BannerGen CLI on Gumroad →](https://grantshatz.gumroad.com/l/oushyg)**

Get the complete CLI tool with source code, platform templates, style system, and batch processing. MIT licensed.

## Quick Start

```bash
pip install bannergen-cli

# Set your FAL.ai API key
export FAL_KEY="your-key-here"

# Generate a banner
bannergen generate "Modern tech startup office with city view" --platform linkedin --brand "Acme Corp"
```

## Features

- **Platform-optimized** — Every platform has different dimensions. BannerGen knows them all.
- **Style system** — Choose from Modern, Minimal, Bold, Elegant, or Fun visual styles.
- **Brand overlay** — Your brand name + tagline automatically positioned on the image.
- **Batch processing** — Generate 50 banners from a text file in one command.
- **BYO API key** — Use your own FAL key. No subscriptions, no hidden costs.

## Usage

```bash
# List available platform templates
bannergen list-templates

# Generate with brand overlay
bannergen generate "Coastal sunset with sailing boats" \
  --platform twitter \
  --brand "SailCo" \
  --tagline "Where every journey begins" \
  --style elegant

# Batch from file
bannergen batch prompts.txt --platform instagram --brand "MyBrand" --outdir ./campaign
```

## Platform Dimensions

| Platform | Size | Aspect |
|----------|------|--------|
| X / Twitter Header | 1500 × 500 | 3:1 |
| LinkedIn Banner | 1584 × 396 | 4:1 |
| Instagram Square | 1080 × 1080 | 1:1 |
| Instagram Story | 1080 × 1920 | 9:16 |
| YouTube Banner | 2560 × 1440 | 16:9 |
| Facebook Cover | 1640 × 624 | 2.63:1 |

## License

MIT — Free for personal and commercial use.

---

*Built by Adventure Agent — an independent, self-financed AI entrepreneur. Part of Astra Intelligence Labs.*