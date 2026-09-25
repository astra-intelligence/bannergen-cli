# BannerGen — AI Social Media Banner Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Buy on Gumroad](https://img.shields.io/badge/Buy%20on%20Gumroad-%241+-green?logo=gumroad)](https://grantshatz.gumroad.com/l/oushyg)
[![Try Free Web App](https://img.shields.io/badge/Try%20Free-Web%20App-blue)](https://astra-intelligence.github.io/bannergen-cli/app.html)

**Turn any idea into a professional social media banner in seconds — for free.**

👉 **[Try the FREE Web App](https://astra-intelligence.github.io/bannergen-cli/app.html)** — No install needed, just paste your free FAL key.

BannerGen is an AI-powered social media banner generator for Twitter/X, LinkedIn, Instagram, YouTube, Facebook, and GitHub OG images. Available as a free web app or a $1+ CLI tool.

![Sample Banner - Modern Tech Office](https://astra-intelligence.github.io/bannergen-cli/sample_banner_tech.png)
*Generated with BannerGen — try it free at the [web app](https://astra-intelligence.github.io/bannergen-cli/app.html)*

## 🔗 Buy CLI — $1+ (Pay What You Want)

**[Purchase BannerGen CLI on Gumroad →](https://grantshatz.gumroad.com/l/oushyg)**

Get the complete CLI tool with source code, platform templates, style system, and batch processing. MIT licensed.

## Quick Start

```bash
# Install from source
pip install git+https://github.com/astra-intelligence/bannergen-cli.git

# Set your FAL.ai API key
export FAL_KEY="your-key-here"

# Generate a banner
bannergen generate "Modern tech startup office with city view" --platform linkedin --brand "Acme Corp"
```

> 💡 **Prefer a ready-made banner?** Get a custom AI-generated banner for your brand for just **$1** on [Gumroad →](https://grantshatz.gumroad.com/l/oushyg)

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