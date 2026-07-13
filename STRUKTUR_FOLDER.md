# 📁 Struktur Folder AI-Auto-Framework

## Organisasi Repository

```
AI-Auto-Framework/
├── 📄 Root Documentation
│   ├── README.md                      # Main documentation
│   ├── ROADMAP.md                     # Feature roadmap
│   ├── STRUKTUR_FOLDER.md             # Folder structure guide
│   ├── LAPORAN_PROGRESS.md            # Comprehensive progress report
│   ├── LAPORAN_STATUS_SINGKAT.md      # Quick status report
│   ├── LICENSE                        # MIT License
│   └── .gitignore                     # Git ignore patterns
│
├── 📁 src/                            # Main source code
│   ├── main.py                        # Entry point
│   ├── requirements.txt               # Python dependencies
│   ├── .env.example                   # Environment variables template
│   ├── .env                           # Environment variables (git-ignored)
│   │
│   ├── 📁 ai_provider/                # Phase 1: AI Provider Integration
│   │   ├── __init__.py
│   │   ├── groq.py                    # Groq AI client ✅
│   │   └── 📁 providers/
│   │       ├── __init__.py
│   │       ├── openai_provider.py     # OpenAI client ✅
│   │       ├── gemini_provider.py     # [TODO] Gemini client
│   │       ├── claude_provider.py     # [TODO] Claude client
│   │       └── ollama_provider.py     # [TODO] Ollama client
│   │
│   ├── 📁 ai_runner/                  # Phase 1: AI Runner ✅
│   │   ├── __init__.py
│   │   ├── config.py                  # Configuration
│   │   ├── providers.py               # Provider router
│   │   ├── response.py                # Response model
│   │   └── runner.py                  # Runner orchestrator
│   │
│   ├── 📁 prompt_engine/              # Phase 1: Prompt Engine ✅
│   │   ├── __init__.py
│   │   ├── builder.py                 # Prompt builder
│   │   └── 📁 templates/
│   │       ├── job_search.md
│   │       ├── resume.md
│   │       └── cover_letter.md
│   │
│   ├── 📁 job_search/                 # Phase 2: Job Search Engine ✅
│   │   ├── __init__.py
│   │   ├── engine.py                  # Main search engine
│   │   ├── parser.py                  # Job parser
│   │   ├── normalizer.py              # Data normalizer
│   │   ├── cache.py                   # Caching system [TODO]
│   │   └── 📁 sources/
│   │       ├── __init__.py
│   │       ├── base.py                # Base source class
│   │       ├── remotive.py            # Remotive API ✅
│   │       ├── linkedin.py            # [TODO] LinkedIn
│   │       ├── jobstreet.py           # [TODO] JobStreet
│   │       ├── glints.py              # [TODO] Glints
│   │       ├── kalibrr.py             # [TODO] Kalibrr
│   │       ├── indeed.py              # [TODO] Indeed
│   │       ├── kitaLulus.py           # [TODO] KitaLulus
│   │       ├── lokerid.py             # [TODO] Loker.id
│   │       ├── karir.py               # [TODO] Karir.com
│   │       ├── remoteok.py            # [TODO] RemoteOK
│   │       └── weworkremotely.py      # [TODO] WeWorkRemotely
│   │
│   ├── 📁 company_intel/              # Phase 3: Company Intelligence [TODO]
│   │   ├── __init__.py
│   │   ├── profile.py                 # Company profile
│   │   ├── scraper.py                 # Website scraper
│   │   ├── contact.py                 # Contact finder
│   │   └── validator.py               # Contact validator
│   │
│   ├── 📁 hrd_finder/                 # Phase 4: HRD Finder [TODO]
│   │   ├── __init__.py
│   │   ├── recruiter.py               # Recruiter finder
│   │   ├── email_finder.py            # Email finder
│   │   └── linkedin_scraper.py        # LinkedIn scraper
│   │
│   ├── 📁 resume_engine/              # Phase 5: Resume Engine [TODO]
│   │   ├── __init__.py
│   │   ├── generator.py               # Resume generator
│   │   ├── optimizer.py               # ATS optimizer
│   │   ├── scorer.py                  # Resume scorer
│   │   └── versioning.py              # Version management
│   │
│   ├── 📁 document_generator/         # Phase 6: Cover Letter Engine ✅
│   │   ├── __init__.py
│   │   ├── cover_letter.py            # Cover letter generator
│   │   ├── motivation_letter.py       # [TODO] Motivation letter
│   │   ├── followup_letter.py         # [TODO] Follow-up letter
│   │   └── exporter.py                # [TODO] Multi-format export
│   │
│   ├── 📁 portfolio_engine/           # Phase 7: Portfolio Engine [TODO]
│   │   ├── __init__.py
│   │   ├── generator.py               # Portfolio generator
│   │   ├── github.py                  # GitHub integration
│   │   └── exporter.py                # PDF export
│   │
│   ├── 📁 storage/                    # Phase 8: Google Workspace [TODO]
│   │   ├── __init__.py
│   │   ├── sheets.py                  # Google Sheets ✅
│   │   ├── docs.py                    # [TODO] Google Docs
│   │   ├── drive.py                   # [TODO] Google Drive
│   │   ├── calendar.py                # [TODO] Google Calendar
│   │   └── gmail.py                   # [TODO] Gmail
│   │
│   ├── 📁 email_engine/               # Phase 9: Email Automation [TODO]
│   │   ├── __init__.py
│   │   ├── smtp.py                    # SMTP
│   │   ├── gmail.py                   # Gmail API
│   │   ├── outlook.py                 # Outlook
│   │   ├── sendgrid.py                # SendGrid
│   │   └── templates.py               # Email templates
│   │
│   ├── 📁 database/                   # Phase 10: Database [TODO]
│   │   ├── __init__.py
│   │   ├── models.py                  # Data models
│   │   ├── sqlite.py                  # SQLite
│   │   ├── postgresql.py              # PostgreSQL
│   │   └── migrations.py              # DB migrations
│   │
│   ├── 📁 workflow/                   # Phase 11: Workflow [TODO]
│   │   ├── __init__.py
│   │   ├── pipeline.py                # Job pipeline
│   │   ├── analyzer.py                # Job analyzer
│   │   ├── scorer.py                  # Job scorer
│   │   └── executor.py                # Workflow executor
│   │
│   ├── 📁 scheduler/                  # Phase 12: Scheduler [TODO]
│   │   ├── __init__.py
│   │   ├── scheduler.py               # Job scheduler
│   │   ├── cron.py                    # Cron tasks
│   │   ├── retry.py                   # Retry logic
│   │   └── notifications.py           # Notifications
│   │
│   ├── 📁 dashboard/                  # Phase 13: Dashboard [TODO]
│   │   ├── __init__.py
│   │   ├── streamlit_app.py           # Streamlit UI
│   │   ├── api.py                     # FastAPI backend
│   │   ├── analytics.py               # Analytics
│   │   └── 📁 components/             # UI components
│   │
│   ├── 📁 monitoring/                 # Phase 14: Monitoring [TODO]
│   │   ├── __init__.py
│   │   ├── logger.py                  # Logging system
│   │   ├── metrics.py                 # Metrics
│   │   ├── alerts.py                  # Alerts
│   │   └── health.py                  # Health checks
│   │
│   ├── 📁 utils/                      # Utilities
│   │   ├── __init__.py
│   │   ├── config.py                  # Configuration utilities
│   │   ├── decorators.py              # Decorators
│   │   ├── validators.py              # Validators
│   │   ├── formatters.py              # Formatters
│   │   └── helpers.py                 # Helper functions
│   │
│   └── 📁 bot/                        # [FUTURE] Bot Integrations
│       ├── __init__.py
│       ├── telegram.py                # Telegram
│       ├── whatsapp.py                # WhatsApp
│       └── discord.py                 # Discord
│
├── 📁 tests/                          # Phase 15: Testing [TODO]
│   ├── __init__.py
│   ├── 📁 unit/
│   │   ├── test_ai_providers.py       # Provider tests
│   │   ├── test_job_search.py         # Search tests
│   │   ├── test_document_generator.py # Document tests
│   │   └── test_utils.py              # Utility tests
│   ├── 📁 integration/
│   │   ├── test_workflow.py           # Workflow tests
│   │   ├── test_end_to_end.py         # E2E tests
│   │   └── test_pipeline.py           # Pipeline tests
│   ├── �� fixtures/
│   │   ├── conftest.py                # Pytest config
│   │   ├── mock_data.py               # Mock data
│   │   └── factories.py               # Test factories
│   └── README.md                      # Testing guide
│
├── 📁 docs/                           # Phase 17: Documentation [TODO]
│   ├── README.md                      # Main docs
│   ├── 📁 guides/
│   │   ├── installation.md            # Installation
│   │   ├── configuration.md           # Configuration
│   │   ├── usage.md                   # Usage guide
│   │   └── troubleshooting.md         # Troubleshooting
│   ├── 📁 api/
│   │   ├── overview.md                # API overview
│   │   ├── endpoints.md               # Endpoints
│   │   └── examples.md                # Examples
│   ├── 📁 architecture/
│   │   ├── overview.md                # Architecture
│   │   ├── diagrams.md                # Diagrams
│   │   └── design_decisions.md        # Design decisions
│   └── 📁 examples/
│       ├── basic_search.py            # Basic search
│       ├── advanced_workflow.py       # Advanced workflow
│       └── customization.py           # Customization
│
├── 📁 .github/                        # Phase 16: DevOps [TODO]
│   ├── 📁 workflows/
│   │   ├── ci.yml                     # CI pipeline
│   │   ├── test.yml                   # Test pipeline
│   │   └── deploy.yml                 # Deploy pipeline
│   └── ISSUE_TEMPLATE.md              # Issue template
│
├── 📁 docker/                         # Docker configuration [TODO]
│   ├── Dockerfile                     # Main Dockerfile
│   ├── docker-compose.yml             # Docker compose
│   └── .dockerignore                  # Docker ignore
│
├── 📁 config/                         # Configuration files [TODO]
│   ├── development.yaml               # Dev config
│   ├── production.yaml                # Prod config
│   └── logging.yaml                   # Logging config
│
├── 📁 outputs/                        # Generated files
│   └── [Auto-generated documents]
│
└── 📁 logs/                           # Log files
    └── [Auto-generated logs]
```

---

## 📊 Folder Organization by Phase

### ✅ Phase 1 - Core (COMPLETE)
- `src/ai_provider/`
- `src/ai_runner/`
- `src/prompt_engine/`

### 🔄 Phase 2 - Job Search (IN PROGRESS)
- `src/job_search/`

### ⏳ Phase 3-4 - Intelligence (PENDING)
- `src/company_intel/`
- `src/hrd_finder/`

### 🔄 Phase 5-7 - Documents (IN PROGRESS)
- `src/resume_engine/`
- `src/document_generator/`
- `src/portfolio_engine/`

### ⏳ Phase 8-9 - Integrations (PENDING)
- `src/storage/`
- `src/email_engine/`

### ⏳ Phase 10-14 - Infrastructure (PENDING)
- `src/database/`
- `src/workflow/`
- `src/scheduler/`
- `src/dashboard/`
- `src/monitoring/`

### ⏳ Phase 15-17 - DevOps & Docs (PENDING)
- `tests/`
- `.github/workflows/`
- `docs/`

---

## 📝 File Naming Convention

```
Module Files:      snake_case.py
Test Files:        test_*.py or *_test.py
Config Files:      lowercase.yaml / lowercase.yml
Documentation:     TitleCase.md or UPPERCASE.md
Folders:           lowercase_with_underscore/
```

---

## 🔐 Git Ignore Priority

```
.env                 # NEVER commit
.env.local          # NEVER commit
__pycache__/        # Python cache
*.pyc              # Python compiled
venv/              # Virtual env
.vscode/           # Editor config
.idea/             # IDE config
*.log              # Log files
.DS_Store          # macOS
outputs/[temp]     # Temp outputs
logs/              # Log directory
```

---

## 📋 Notes

- `✅` = Implemented & working
- `[TODO]` = Next to implement
- `[FUTURE]` = Future enhancement
- `[PHASE X]` = Belongs to specific phase

---

**Last Updated:** 13 July 2026  
**Status:** Ready for implementation
