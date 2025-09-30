# 📊 Monitoring Hub (Mock Version)

## Goal
A one-stop **monitoring hub** that aggregates metrics (PRTG, Tenable, IIS, etc.) into **Prometheus + Grafana**.

- **Phase 1 (now)**: Mock data with a tiny Python service.
- **Phase 2**: Real collectors for work tools.
- **Phase 3**: Optional Azure VM deployment.

## Architecture (Phase 1 – Mock)

![Architecture Diagram](docs/architecture-diagram.png)

## Tech Stack
- Python (collectors)
- Prometheus (TSDB)
- Grafana (visuals)
- Docker Compose (local)

## Roadmap
- [ ] Mock metrics service (`/metrics` in Prometheus format)
- [ ] Prometheus + Grafana via Docker Compose
- [ ] Dashboards (CPU, uptime, disk)
- [ ] Real collectors: PRTG, Tenable, IIS
- [ ] Optional: Deploy to Azure VM

## Quick Start (coming next)
- `docker-compose up -d`
- `python python-scripts/mock_metrics.py`
