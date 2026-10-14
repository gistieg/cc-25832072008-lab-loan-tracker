# Lab Loan Tracker

Cloud Computing — PTI 2802  
Pertemuan 3 — Project Inception

## Author
Nama: Gistie / NIM: 25832072008 / Kelas: 2B

## Problem
Administrator laboratorium kesulitan memantau peminjaman perangkat karena
pencatatan tidak terpusat.

## Target Users
Administrator laboratorium dan mahasiswa peminjam.

## Features M03
- baseline application (Flask)
- endpoint `/health`, `/api/info`, `/api/devices`
- VPS deployment

## Architecture

```mermaid
flowchart LR
    U[User] --> C[Caddy]
    C --> G[Gunicorn]
    G --> F[Flask]
```

## Infrastructure
- Azure VM, Ubuntu Server 24.04
- 2 vCPU, sekitar 892 MiB RAM, 61 GB disk
- Caddy, Gunicorn, systemd, UFW

## Health Check
`GET /health`

## Deployment
See `docs/deployment.md`.

## Security
- key-only SSH
- root SSH disabled
- UFW enabled
- backend loopback-only

## Current Limitations
- HTTP only
- no persistent database
- no container
- manual deployment

## Roadmap
M04 DNS/HTTPS, M05 Data, M06 Container, M07 IaC, M09 CI/CD
