# Evidence Notes M03

## Lingkungan
- Azure VM, Ubuntu Server 24.04.4 LTS
- 2 vCPU, sekitar 892 MiB RAM, 61 GB disk, swap 1 GB (dibuat manual)
- Berbeda dari spesifikasi modul (1 vCPU / 1 GB / 20 GB).

## Hasil verifikasi
- SSH: root login off, password off, key-only, AllowUsers gistiegusniar
  (lihat ssh-hardening.txt).
- UFW aktif, port 22 dan 80 (lihat ufw.txt); Azure NSG juga 22 dan 80.
- Backend Gunicorn hanya 127.0.0.1:8000 (lihat ports.txt).
- Service cc-m03 dikelola systemd dan aktif setelah reboot (lihat service.txt).
- /health mengembalikan HTTP 200, internal dan publik.
- Test eksternal dari laptop: HTTP 200 OK, header `Via: 1.1 Caddy`.

## Insiden dan troubleshooting
1. SSH password masih aktif setelah hardening: `sshd -T` menunjukkan
   `passwordauthentication yes`. Penyebab: file bawaan cloud-init
   (50-cloud-init.conf) dibaca lebih dulu daripada 99-pti2802.conf.
   Perbaikan: rename menjadi 00-pti2802.conf, lalu `sshd -T` menunjukkan `no`.
2. Service cc-m03 crash loop (`Address already in use`, port 8000).
   Penyebab: Gunicorn tes manual masih berjalan sebagai job [2] karena
   `kill %1` menunjuk job Flask yang sudah mati. Perbaikan: `kill %2`,
   verifikasi `ss` kosong, lalu start service. Bukti: incident-port-in-use.txt.
3. Warning `Control server error: Permission denied` pada Gunicorn 26.x
   (ProtectHome=true). Perbaikan: tambah `--no-control-socket`.

## Catatan
IP publik disamarkan sebagai <PUBLIC_IP>.
