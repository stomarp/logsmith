# Logsmith

Logsmith is a small observability and debugging tool for backend services.

It ingests structured logs from services, stores them in Postgres, allows searching and grouping by trace ID, and uses an LLM to help explain incidents.

---

## Architecture

- **Demo service**: FastAPI app that simulates a backend service (e.g. orders-service), emits structured logs with trace IDs, and sends them to Logsmith.

- **Logsmith backend**: FastAPI service that exposes:
  - `POST /ingest` – ingest batches of logs
  - `GET /logs` – list and filter logs
  - `GET /traces/{trace_id}` – view logs grouped by trace
  - `GET /incidents` – simple incident listing (errors or slow requests)
  - `GET /incidents/{trace_id}/explain` – AI-generated root cause analysis

- **Storage**: Postgres with structured columns and a JSONB metadata field.

- **Frontend**: React + Vite dashboard for filters, log table, trace view, and AI explanation panel.

- **AI**: OpenAI API used to summarize incidents and suggest likely causes.

---

## Planned Tech Stack

Backend
- Python 3.11
- FastAPI
- SQLAlchemy
- Postgres

Frontend
- React
- Vite
- TypeScript

Infra
- Docker Compose
- GitHub Actions (later)

---

## MVP Features

For the MVP, the focus will be:

- Log ingestion
- Log storage in Postgres
- Log search and filtering
- Trace-based debugging
- Incident listing
- AI-generated incident explanation
- Demo service to generate logs