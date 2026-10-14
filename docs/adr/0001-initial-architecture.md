# ADR-0001: Initial VPS Deployment Architecture

## Status
Accepted

## Context
Proyek Lab Loan Tracker di-deploy pada VM Azure Ubuntu Server 24.04
(2 vCPU, sekitar 892 MiB RAM, 61 GB disk). Resource RAM terbatas.

## Decision
- Flask
- Gunicorn 1 worker, 2 thread
- systemd
- Caddy
- UFW
- GitHub

## Alternatives
1. Node.js + PM2
2. NGINX + Gunicorn
3. Docker
4. PHP-FPM

## Rationale
- Python 3.12 sudah tersedia default di Ubuntu 24.04.
- Gunicorn pada loopback mengecilkan attack surface; hanya Caddy yang publik.
- Caddy konfigurasinya singkat dan siap HTTPS otomatis di M04.
- systemd menjaga service hidup setelah logout dan reboot.
- Docker belum dipakai karena containerization dijadwalkan di M06.

## Consequences
### Positive
- Footprint kecil (service sekitar 30 MB RAM).
- Mudah dipahami dan di-troubleshoot.
- Siap dikembangkan ke HTTPS dan database.
### Negative
- Hanya HTTP pada M03.
- Deployment masih manual.
- Single point of failure (satu VPS).

## Review Trigger
Review pada M06/M07.
