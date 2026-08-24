# 🛡️ SMK Vault - Cloud Security Architecture & Immutable Academic Ledger

[![Solidity](https://img.shields.io/badge/Solidity-v0.8.20-blue.svg)](https://soliditylang.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Trust%20Multi--Cloud-cyan.svg)](#)
[![Compliance](https://img.shields.io/badge/Security-FIPS%20140--2%20Level%203-emerald.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-violet.svg)](LICENSE)

**SMK Vault** adalah platform arsitektur keamanan siber berbasis **Zero-Trust Multi-Cloud (AWS & GCP)** dan **Immutable Blockchain Ledger** yang dirancang khusus untuk verifikasi keabsahan Ijazah Digital dan Sertifikat Praktik Kerja Lapangan (PKL) industri SMK secara real-time dan bebas dari pemalsuan dokumen.

---

## 🌟 Fitur Utama System Arsitektur

### 1. 🏢 Zero-Trust Multi-Cloud Security Matrix (AWS vs GCP)
* **Perimeter Defense**: Google Cloud Armor & AWS WAF + Shield dengan aturan Rate Limiting (100 req/min) serta mitigasi OWASP Top 10 (Anti-DDoS, SQLi, Stored XSS).
* **Identity & Access Management (IAM/RBAC)**: Otorisasi bertingkat berbasis perang (Role-Based Access Control) diperkuat dengan otentikasi wajib **TOTP MFA (Google Authenticator)**.
* **Isolated Private Compute Subnets**: Microservices beroperasi di dalam subnet privat terisolasi (10.0.2.0/24) tanpa IP publik langsung.
* **Hardware KMS & HSM**: Pengelolaan kunci enkripsi privat Kepala Sekolah menggunakan HSM standar **FIPS 140-2 Level 3** (AES-256 & RSA-4096).
* **Immutable WORM Storage**: Berkas PDF Ijazah disimpan pada S3 Object Lock / GCP Storage Lock dengan kebijakan *Write-Once-Read-Many* (retensi 50 tahun).

### 2. ⛓️ Smart Contract Solidity (`IjazahBlockchain.sol`)
* Smart contract mandiri (*Zero-Dependency / Tanpa Import Eksternal*) berbasis **Solidity v0.8.20** yang siap dikompilasi & di-deploy di **Remix IDE** dan **Ganache**.
* Fitur mencakup:
  * Control Access Zero-Trust (`DEFAULT_ADMIN_ROLE`, `KEPALA_SEKOLAH_ROLE`, `STAF_TU_ROLE`, `MITRA_DUDI_ROLE`).
  * ReentrancyGuard internal untuk perlindungan transaksi.
  * Audit logging transkrip nilai siswa oleh Guru/TU.
  * Verifikasi sertifikat magang industri via Wallet DUDI.
  * *Certificate Revocation* untuk pembatalan ijazah jika terjadi pelanggaran akademik.

### 3. 🔍 Public Verifier Portal & PDF Verification
* Verifikasi keabsahan dokumen PDF Ijazah secara instan menggunakan seret & drop (*Drag & Drop*).
* Ekstraksi otomatis `SHA-256 Ledger Hash` dari stream data PDF untuk mencocokkan keabsahan dokumen secara kriptografis terhadap rantai block ledger.
* Fitur *Quick Test Sandbox Demo* untuk mengunduh sampel dokumen **Valid (Asli)** dan **Palsu (Modifikasi 1 Karakter)** secara langsung.

### 4. 🧪 Cyber Security Pentest & Audit Lab
Simulasi pengujian keamanan interaktif untuk OWASP & Smart Contract SCSVS:
1. **Broken Access Control (IDOR)**: Pengujian penetrasi bypass role siswa.
2. **Parameter Manipulation (SQLi / XSS)**: Pengujian pemfilteran payload WAF.
3. **Cloud Infra Audit (Prowler)**: Verifikasi kepatuhan isolasi subnet & KMS.
4. **API Rate Limit (K6 Load Audit)**: Simulasi 200 Virtual Users hitting endpoint API.
5. **Unauthorized Minting (Hardhat)**: Percobaan panggil `issueCertificate` dari wallet publik.
6. **Document Hash Tampering (Slither)**: Pengujian presisi deteksi perubahan 1 karakter pada PDF.

---

## 📁 Struktur Direktori Project

```text
FINAL CSA/
├── index.html          # Antarmuka Web Dashboard & Command Center
├── style.css           # Desain UI Cyberpunk Glassmorphism & Responsif
├── app.js              # Logika Aplikasi, State RBAC, & Parsing SHA-256 PDF
├── smart_contracts.js  # Wrapper Export Kode Solidity ke UI
├── IjazahBlockchain.sol # Smart Contract Solidity v0.8.20 (Zero-Dependency)
├── bukti_pengujian/    # Folder Bukti Screenshot Pengujian Web & Remix IDE
├── .gitignore          # Konfigurasi Git Ignore
└── README.md           # Dokumentasi Utama Repository
```

---

## 📸 Bukti Pengujian Web & Remix IDE (Screenshots)

Dokumentasi lengkap foto & naskah hasil pengujian web portal serta smart contract dapat dilihat pada folder [**`bukti_pengujian/`**](bukti_pengujian/):

1. 🌐 **Web Dashboard Overview**: Matriks Multi-Cloud (AWS vs GCP) & Cloud Metrics.
2. 💎 **Web Block Payload**: Rincian Payload Block #3 (`FATHYA SHABIRA A.T`).
3. 📜 **Remix Minting**: Transaksi `issueCertificate` berhasil (Block #2 Ganache).
4. 🔍 **Remix Verification**: Hasil kueri `verifyCertificate` mengembalikan `isValid: true`.
5. 🛡️ **Remix Zero-Trust Protection**: Akses ditolak (`REVERTED`) saat dipanggil dari Account 67.
6. 🏢 **Remix Grant Role DUDI**: Pemberian hak akses `MITRA_DUDI_ROLE` ke Account 67.


---

## 🚀 Panduan Pengujian Smart Contract (Remix IDE & Ganache)

### Langkah 1: Kompilasi Smart Contract
1. Buka [Remix Ethereum IDE](https://remix.ethereum.org/).
2. Buat berkas baru bernama `IjazahBlockchain.sol` dan salin seluruh isi dari [`IjazahBlockchain.sol`](file:///c:/Chapter%20Of%20Me/CSA/FINAL%20CSA/IjazahBlockchain.sol).
3. Di tab **Solidity Compiler**, pilih versi compiler `0.8.20` lalu klik **Compile IjazahBlockchain.sol**.

### Langkah 2: Deployment
1. Di tab **Deploy & Run Transactions**, pilih Environment `Dev - Ganache Provider` (atau `Remix VM (Cancun)`).
2. Pada kolom parameter constructor `initialKepSek`, isi dengan alamat address `0x0000000000000000000000000000000000000000` (otomatis menjadikan deployer sebagai Kepala Sekolah).
3. Klik tombol **Deploy** hingga muncul status centang hijau (✔).

### Langkah 3: Eksekusi Fungsi
1. **Minting Ijazah (`issueCertificate`)**: Panggil dengan parameter `_studentId`, `_studentName`, `_major`, `_documentHash`, dan `_kmsDigitalSig`.
2. **Verifikasi Publik (`verifyCertificate`)**: Panggil menggunakan `_documentHash` untuk memastikan `isValid: true`.
3. **Pengujian Proteksi Zero-Trust**: Pindah akun wallet ke **Akun Ke-2 (Publik)** di dropdown Remix, lalu panggil kembali `issueCertificate`. Transaksi dipastikan **REVERTED (Gagal)** dengan error `AccessControl: account is missing required role`.

---

## 👤 Penulis / Author

* **Fathya Shabira Akmal Tazkia**
* Project: *Cloud Security Architecture & Immutable Academic Ledger (SMK Vault)*

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
