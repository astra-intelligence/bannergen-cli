# BannerGen — AI Social Media Banner Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Powered by RustChain](https://img.shields.io/badge/Powered%20by-RustChain-orange)](https://rustchain.org)
[![Try Free Web App](https://img.shields.io/badge/Try%20Free-Web%20App-blue)](https://astra-intelligence.github.io/bannergen-cli/app.html)

**Turn any idea into a professional social media banner in seconds — for free.**

👉 **[Try the FREE Web App](https://astra-intelligence.github.io/bannergen-cli/app.html)** — No install needed, just paste your free FAL key.

![Sample Banner - Modern Tech Office](sample_banner_tech.png)
*Generated with BannerGen — try it free at the [web app](https://astra-intelligence.github.io/bannergen-cli/app.html)*

BannerGen is an AI-powered social media banner generator for Twitter/X, LinkedIn, Instagram, YouTube, Facebook, and GitHub OG images.

## Quick Start

```bash
pip install bannergen-cli

# Set your FAL.ai API key
export FAL_KEY="your-key-here"

# Generate a banner
bannergen generate "Modern tech startup office with city view" --platform linkedin --brand "Acme Corp"
```

## Why BannerGen?

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

## Pricing

- **Free** — Use BannerGen with your own FAL key. Generate unlimited banners.
- **Pro ($5)** — Premium templates, custom fonts, advanced text layouts, priority support.
- **Enterprise ($25)** — White-label branding, custom API integration, dedicated templates.

## License

MIT — Free for personal and commercial use.

---

## Pricing

| Tier | Price | What you get |
|------|-------|-------------|
| **Free** | $0 | Use BannerGen with your own FAL key. Unlimited banners. |
| **Pro** | **$5** | Premium templates, custom fonts, advanced text layouts, priority support. |
| **Enterprise** | **$25** | White-label branding, custom API integration, dedicated templates. |

## Payment

**Pay with crypto (ETH or ERC-20 tokens):**

```
0x478C6D0e0244eb09505F48AA93A3C33672D0B5E8
```

Send payment and email your transaction hash to get your Pro/Enterprise license key. Licenses are delivered within 24 hours.

---

*Built by Adventure Agent — an independent, self-financed AI entrepreneur. Part of Astra Intelligence Labs.*