from flask import Flask, Response
from prometheus_client import Gauge, Counter, generate_latest, CollectorRegistry
import random, time

app = Flask(__name__)
registry = CollectorRegistry()

# Define metrics
cpu_g = Gauge('mock_cpu_percent', 'CPU usage percent', registry=registry)
disk_g = Gauge('mock_disk_used_gb', 'Disk used (GB)', registry=registry)
uptime = Counter('mock_uptime_seconds_total', 'Uptime seconds', registry=registry)
svc_g = Gauge('mock_service_health', 'Service health (1=up,0=down)', ['service'], registry=registry)

last = time.time()

@app.route("/metrics")
def metrics():
    global last
    now = time.time()
    uptime.inc(now - last)
    last = now

    cpu_g.set(random.uniform(5, 80))
    disk_g.set(random.uniform(50, 350))

    for s in ["api", "worker", "scheduler"]:
        svc_g.labels(service=s).set(1 if random.random() > 0.1 else 0)

    return Response(generate_latest(registry),
                    mimetype="text/plain; version=0.0.4; charset=utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
