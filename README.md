# WriteEngin — AI Content Generation Platform

Production-ready Flask app with multi-provider AI, payments, WordPress, and deployment configs.

## Quick Start

```bash
# Local dev
pip install -r requirements.txt
python app.py

# Production (Gunicorn)
gunicorn app:app --bind 0.0.0.0:5000 --workers 4

# Docker
docker build -t writeengin .
docker run -p 5000:5000 --env-file .env writeengin

# Railway
railway up

# Render (auto-detects render.yaml)
# Connect repo → Render → Deploy
```

## Environment Variables

Copy `.env.example` to `.env` and fill in:

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Flask session key (generate: `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `OPENAI_API_KEY` | OpenAI GPT-4o-mini (optional) |
| `ANTHROPIC_API_KEY` | Claude 3.5 Sonnet (optional) |
| `GEMINI_API_KEY` | Google Gemini Flash (optional) |
| `STRIPE_SECRET_KEY` | Stripe payments (optional) |
| `RAZORPAY_KEY_ID` | Razorpay payments (optional) |
| `MAIL_SERVER` | SMTP for emails (optional) |
| `DATABASE_URL` | PostgreSQL for production |

## Pages

| Page | Route | Auth |
|------|-------|------|
| Homepage | `/` | No |
| Login | `/login` | No |
| Register | `/register` | No |
| Pricing | `/pricing` | No |
| Dashboard | `/dashboard` | Yes |
| Blog Writer | `/tools/blog-writer` | Yes |
| Social Media | `/tools/social-media` | Yes |
| SEO Tools | `/tools/seo` | Yes |
| Image Generator | `/tools/image-generator` | Yes |
| Landing Pages | `/tools/landing-pages` | Yes |
| Content Calendar | `/content-calendar` | Yes |
| Analytics | `/analytics` | Yes |
| Settings | `/settings` | Yes |

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/generate-blog` | POST | Generate blog post |
| `/api/generate-social` | POST | Generate social posts |
| `/api/generate-landing` | POST | Generate landing page HTML |
| `/api/seo-analyze` | POST | Analyze keyword |
| `/api/save-content` | POST | Save to DB |
| `/api/schedule-post` | POST | Schedule social post |
| `/api/publish-wordpress` | POST | Publish to WordPress |
| `/api/test-wordpress` | POST | Test WP connection |
| `/api/create-payment` | POST | Create Stripe/Razorpay session |
| `/api/send-email` | POST | Send email |
| `/health` | GET | Health check |

## AI Engine

Multi-provider fallback chain:
1. **OpenRouter** (free, no credit card) — 20+ models: Llama 3.3, Gemini, Mistral, etc.
2. **Groq** (free, no credit card) — Llama 3.3 70B, Mixtral 8x7B on LPU hardware
3. OpenAI (GPT-4o-mini, paid)
4. Anthropic (Claude 3.5 Sonnet, paid)
5. Template fallback (offline mode, no API key needed)

### Free API Setup

1. **OpenRouter**: Go to https://openrouter.ai/sign-up → API Keys → Copy key
   - Set `OPENROUTER_API_KEY=sk-or-v1-...` in `.env`
2. **Groq**: Go to https://console.groq.com/keys → Create API Key → Copy key
   - Set `GROQ_API_KEY=gsk_...` in `.env`
3. Restart the app: `python app.py`

## Tech Stack

- **Backend:** Flask 3 + SQLAlchemy + Flask-Login
- **AI:** OpenAI / Anthropic / Gemini / Nous APIs
- **Payments:** Stripe + Razorpay
- **CMS:** WordPress REST API
- **Deployment:** Render / Railway / Docker
- **Database:** SQLite (dev) / PostgreSQL (prod)
