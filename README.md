# GorgiasGrowth — E-commerce Auto-Responder
### Built on Gorgias patterns (implementation package)

**Category:** E-commerce Support Automation | **Deployment:** Your Stack (Gorgias-webhook compatible) | **Sector:** D2C brands, Shopify/WooCommerce sellers

---

## Overview

GorgiasGrowth answers WISMO ("where is my order") tickets automatically: it parses
the order ID from the customer's message, looks up status (shipped / delivered /
processing / delayed), and replies in the customer's name with proactive
compensation messaging for delays.

Webhook contract matches Gorgias HTTP integrations — plug into your helpdesk of
choice.

## Key Features

- Order-ID extraction from free-form messages ("OD9001")
- Status-aware personalized replies; auto credit promise on delays
- Mock order store included — swap for Shopify/Gorgias API
- Health endpoint + FastAPI docs UI built-in

## Business Value

| Metric | Impact |
|--------|--------|
| WISMO tickets | ~60% of e-comm tickets fully automated |
| CSAT on delays | Proactive credit messaging defuses anger |
| Integration time | One webhook endpoint |

## How It Works

```
Customer msg ──► /gorgias-webhook ──► extract OD#### ──► lookup ──► personalized reply
```

## Technical Requirements

- Python 3.10+ host
- Gorgias/Shopify credentials for live order data

## Installation & Setup — Step by Step

```powershell
cd 36-gorgiasgrowth-ecommerce-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn gorgias_responder:app --port 8077
# try the interactive docs:
start http://localhost:8077/docs
```

## Customization for Your Business

- Point lookups at your Shopify Admin API or OMS
- Add intents: cancellation, size exchange, invoice copy
- Localize replies per customer region/language

## What's Included

- Responder service (`gorgias_responder.py`)
- Sample order data (`orders_mock.json`)
- Documentation and 1 customization session

---

*Turn your biggest ticket category into a zero-touch experience.*
