# 📸 Bukti Pengujian Web & Smart Contract Remix IDE (SMK Vault)

Folder ini berisi dokumentasi bukti pengujian lengkap aplikasi web **SMK Vault** dan **Smart Contract `IjazahBlockchain.sol`** pada **Remix IDE & Ganache Provider**.

---

## 📑 Daftar Bukti Pengujian

### 1. 🌐 Web Application - Dashboard Overview
![01_web_dashboard_overview](01_web_dashboard_overview.png)
* **Deskripsi**: Tampilan utama web dashboard SMK Vault dengan statistik real-time WAF & Edge Defense, KMS Encryption Vault, Blockchain Ledger, dan Matriks Multi-Cloud Architecture (AWS vs GCP).

---

### 2. 💎 Web Application - Block Payload & Immutability Chain (Block #3)
![02_web_block_minted_modal](02_web_block_minted_modal.png)
* **Deskripsi**: Modal detail block payload hasil minting ijazah digital siswa **FATHYA SHABIRA A.T** (NISN `105841111923`) dengan SHA-256 hash `4531659a28aca57685953d9d88dd6ccd822716793f22a6c5ffe82d3f34f6219c` dan otorisasi Cloud KMS HSM Key Kepala Sekolah.

---

### 3. 📜 Remix IDE - Minting Ijazah Digital (`issueCertificate`)
![03_remix_issue_certificate](03_remix_issue_certificate.png)
* **Deskripsi**: Eksekusi fungsi `issueCertificate` oleh Kepala Sekolah (`Account 66`). Transaksi **berhasil (Centang Hijau ✔)** dan dicatat pada Block #2 Ganache Provider.

---

### 4. 🔍 Remix IDE - Verifikasi Publik Keabsahan (`verifyCertificate`)
![04_remix_verify_certificate](04_remix_verify_certificate.png)
* **Deskripsi**: Kueri verifikasi publik mengembalikan status **`isValid: true`** untuk siswa FATHYA SHABIRA A.T, membuktikan dokumen terdaftar secara sah di ledger.

---

### 5. 🛡️ Remix IDE - Proteksi Keamanan Zero-Trust RBAC (Akses Ditolak)
![05_remix_zero_trust_protection](05_remix_zero_trust_protection.png)
* **Deskripsi**: Pengujian akses publik tanpa wewenang (`Account 67`). Transaksi **ditolak/GAGAL (Reverted)** oleh Smart Contract, membuktikan sistem pertahanan Zero-Trust RBAC bekerja 100%.

---

### 6. 🏢 Remix IDE - Otorisasi Role Mitra DUDI (`grantRole`)
![06_remix_grant_role_dudi](06_remix_grant_role_dudi.png)
* **Deskripsi**: Admin (`Account 66`) memberikan otorisasi `MITRA_DUDI_ROLE` kepada `Account 67`. Transaksi berhasil dan event `RoleGranted` terbit pada Block #4.

---

### 7. 📖 Remix IDE - Pembacaan Verifikasi dari Account 67 (`verifyCertificate`)
![07_remix_verify_after_dudi](07_remix_verify_after_dudi.png)
* **Deskripsi**: Pembacaan kueri verifikasi ijazah oleh Account 67 yang telah disahkan.
