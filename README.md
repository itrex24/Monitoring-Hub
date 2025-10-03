# Monitoring Hub

## Overview
A lightweight monitoring stack with **Prometheus**, **Grafana**, and a custom **Python exporter** that generates mock metrics (CPU, Disk, Uptime, Service Health).  

This project demonstrates how to build a full monitoring pipeline from scratch, provision dashboards automatically, and version-control the entire setup.

---

## Architecture
![Architecture Diagram](docs/architecture-diagram.png)

---

## Components
- **Prometheus** → scrapes metrics from exporters.  
- **Python Exporter** → mock `/metrics` endpoint using Flask + prometheus_client.  
- **Grafana** → dashboards for visualization (auto-provisioned).  

---

## Quickstart
1. Clone repo:
   ```bash
   git clone git@github.com:itrex24/Monitoring-Hub.git
   cd Monitoring-Hub

---

## Dashboard
Example Grafana dashboard auto-loads on startup:

![Dashboard Screenshot](docs/screenshots/dashboard.png)

Panels included:
- CPU Usage (time series)  
- Disk Usage (bar gauge)  
- Uptime (stat)  
- Service Health (table with UP/DOWN mapping)  

---

## Future Work
- **Dockerize the Python Exporter**  
  Package the mock metrics service into a container for easier deployment.  

- **Add Node Exporter**  
  Collect real system metrics (CPU, memory, disk) from the host machine.  

- **Integrate Real APIs**  
  Example: GitHub stars, weather API, or internal services → expose via Prometheus format.  

- **Kubernetes Deployment**  
  Run Prometheus, Grafana, and exporters in a local K8s cluster (kind or Minikube) to simulate a production-style environment.  

- **Terraform IaC**  
  Provision cloud infrastructure (VMs, managed Prometheus, Grafana) with Terraform.  

- **CI/CD Pipeline**  
  Automate build & deploy with GitHub Actions or Azure DevOps pipelines.  