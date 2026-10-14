# Requirements

## Problem Statement
Administrator laboratorium mengalami kesulitan memantau peminjaman perangkat
karena pencatatan tidak terpusat. Sistem menyediakan daftar perangkat, status
ketersediaan, dan catatan peminjaman sehingga penggunaan perangkat dapat
ditelusuri dan keterlambatan pengembalian dapat ditindaklanjuti.

## Target Users
- Administrator laboratorium: mengelola perangkat dan peminjaman.
- Mahasiswa peminjam: melihat perangkat yang tersedia.

## User Needs
- Sebagai administrator, saya ingin melihat perangkat yang belum dikembalikan,
  sehingga saya dapat menindaklanjuti keterlambatan.
- Sebagai mahasiswa, saya ingin melihat perangkat yang tersedia,
  sehingga saya tahu apa yang bisa dipinjam.

## Functional Requirements
- FR-01 Sistem menampilkan halaman utama.
- FR-02 Sistem menyediakan health endpoint (`/health`).
- FR-03 Sistem menampilkan metadata aplikasi (`/api/info`).
- FR-04 Sistem menampilkan daftar perangkat beserta status (`/api/devices`).

## Non-Functional Requirements
- NFR-01 Backend hanya listen pada loopback.
- NFR-02 Aplikasi dikelola systemd.
- NFR-03 Request publik masuk melalui reverse proxy.
- NFR-04 Secret tidak disimpan pada Git repository.
- NFR-05 Health endpoint mengembalikan HTTP 200 saat sehat.
- NFR-06 Deployment dapat direproduksi dari repository.
- NFR-07 Arsitektur sesuai resource VPS kecil.

## Scope M03
In scope: repository, requirements, architecture, ADR, baseline Flask app,
SSH hardening, Gunicorn, systemd, Caddy, HTTP public deployment.
Out of scope: database, login, Docker, IaC, CI/CD, TLS/domain.

## Constraints (kondisi aktual VPS)
- Microsoft Azure VM, Ubuntu Server 24.04.4 LTS
- 2 vCPU (nproc = 2), RAM sekitar 892 MiB, disk 61 GB
- Swap 1 GB (dibuat manual)
- Public IPv4
- Catatan: spesifikasi modul adalah 1 vCPU / 1 GB / 20 GB; konfigurasi
  Gunicorn tetap 1 worker + 2 thread mengikuti modul.

## Acceptance Criteria M03
- [x] first deployment accessible
- [x] health endpoint works
