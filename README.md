# 🛡️ SMK Vault - Cloud Security Architecture & Immutable Academic Ledger

[![Solidity](https://img.shields.io/badge/Solidity-v0.8.20-blue.svg)](https://soliditylang.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Trust%20Multi--Cloud-cyan.svg)](#)
[![Compliance](https://img.shields.io/badge/Security-FIPS%20140--2%20Level%203-emerald.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-violet.svg)](LICENSE)

**SMK Vault** adalah platform arsitektur keamanan siber berbasis **Zero-Trust Multi-Cloud (AWS & GCP)** dan **Immutable Blockchain Ledger** yang dirancang khusus untuk verifikasi keabsahan Ijazah Digital dan Sertifikat Praktik Kerja Lapangan (PKL) industri SMK secara real-time dan bebas dari pemalsuan dokumen.

---

## 🌟 Fitur Utama System Arsitektur

### 1. 🏢 Zero-Trust Multi-Cloud Security (AWS & GCP)
- Mengimplementasikan arsitektur **Zero-Trust** dengan pemisahan layanan pada lingkungan Multi-Cloud (AWS & Google Cloud Platform).
- Perlindungan perimeter menggunakan **AWS WAF**, **AWS Shield**, dan **Google Cloud Armor** untuk mitigasi serangan DDoS serta OWASP Top 10.
- Penerapan **Role-Based Access Control (RBAC)** dan autentikasi **Multi-Factor Authentication (MFA)** untuk memastikan hanya pengguna yang berwenang dapat mengakses layanan.

### 2. 🔐 Cloud Key Management Service (KMS)
- Penandatanganan digital dilakukan menggunakan **Cloud Key Management Service (KMS)**.
- Private key tersimpan secara aman pada **Hardware Security Module (HSM)** sesuai standar **FIPS 140-2 Level 3**.
- Seluruh proses penandatanganan dilakukan tanpa mengekspos private key ke aplikasi.

### 3. ⛓️ Blockchain Academic Ledger
- Smart Contract dikembangkan menggunakan **Solidity v0.8.20**.
- Data ijazah dan sertifikat dicatat secara permanen pada Blockchain sehingga tidak dapat dimanipulasi.
- Mendukung proses penerbitan, verifikasi, pencabutan sertifikat, dan pengelolaan hak akses berbasis role.

### 4. 📄 Digital Certificate Verification
- Verifikasi keaslian ijazah digital menggunakan **SHA-256 Document Hash**.
- Dokumen dapat diverifikasi melalui portal publik tanpa memerlukan login.
- Sistem mampu mendeteksi perubahan sekecil satu karakter sehingga dokumen palsu dapat langsung dikenali.

### 5. 🛡️ Cyber Security Testing
- Menyediakan simulasi pengujian keamanan berdasarkan praktik terbaik keamanan aplikasi web dan smart contract.
- Meliputi pengujian RBAC, SQL Injection, Cross Site Scripting (XSS), API Security, Cloud Security Audit, hingga Smart Contract Access Control.

---

## 📁 Struktur Direktori Project

```text
SMK-Vault-Cloud-Security-Blockchain/
├── index.html
├── style.css
├── app.js
├── smart_contracts.js
├── IjazahBlockchain.sol
├── bukti_pengujian/
│   ├── README.md
│   ├── 01_dashboard_overview.png
│   ├── 02_web_input_data_kelulusan.png
│   ├── ...
│   └── 17_ganache_provider.png
├── .gitignore
└── README.md
```

---

## 📸 Dokumentasi Pengujian

Seluruh dokumentasi implementasi aplikasi web, Cloud Security, Blockchain, serta Smart Contract tersedia pada folder berikut:

➡️ **[`bukti_pengujian/`](bukti_pengujian/)**

Folder tersebut berisi **17 screenshot** yang mendokumentasikan seluruh proses implementasi, meliputi:

- Dashboard Overview
- Input Data Kelulusan
- Draft Kelulusan
- Multi-Factor Authentication (MFA)
- Cloud KMS Workspace
- KMS Signing Success
- Student Portal
- Download PDF
- Verifikasi Dokumen Valid
- Verifikasi Dokumen Invalid
- Cyber Pentest Lab
- Deploy & Minting Smart Contract
- Verifikasi Smart Contract
- RBAC Protection
- Grant Role
- Verify After Grant Role
- Ganache Provider

---

## 🚀 Panduan Menjalankan Project

### 1. Menjalankan Aplikasi Web

Clone repository:

```bash
git clone https://github.com/FathyaShabiraAkmalTazkia02/SMK-Vault-Cloud-Security-Blockchain.git
```

Masuk ke folder project:

```bash
cd SMK-Vault-Cloud-Security-Blockchain
```

Selanjutnya buka file:

```text
index.html
```

menggunakan browser modern seperti Google Chrome atau Microsoft Edge.

---

## ⛓️ Pengujian Smart Contract (Remix IDE & Ganache)

### Langkah 1 — Kompilasi Smart Contract

1. Buka **Remix Ethereum IDE**.
2. Buat file baru bernama `IjazahBlockchain.sol`.
3. Salin seluruh isi file dari repository.
4. Pilih compiler **Solidity v0.8.20**.
5. Klik **Compile IjazahBlockchain.sol**.

---

### Langkah 2 — Deploy Smart Contract

1. Buka menu **Deploy & Run Transactions**.
2. Pilih Environment:
   - **Dev - Ganache Provider**, atau
   - **Remix VM (Cancun)**.
3. Isi parameter constructor `initialKepSek` menggunakan alamat wallet yang akan menjadi Kepala Sekolah.
4. Klik **Deploy**.

---

### Langkah 3 — Pengujian Fitur Smart Contract

Lakukan pengujian terhadap fungsi berikut:

- `issueCertificate()`
- `verifyCertificate()`
- `grantRole()`
- `revokeCertificate()`

Selanjutnya lakukan pengujian **RBAC Protection** dengan menggunakan akun yang tidak memiliki hak akses. Sistem akan menolak transaksi (**Reverted**) sebagai bukti bahwa mekanisme Role-Based Access Control berjalan dengan baik.

---

## 🛠️ Teknologi yang Digunakan

### Front-End
- HTML5
- CSS3
- JavaScript (ES6)

### Blockchain
- Solidity v0.8.20
- Remix IDE
- Ganache

### Cloud Security
- Zero-Trust Architecture
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA)
- Cloud Key Management Service (KMS)
- Hardware Security Module (HSM)
- SHA-256 Cryptographic Hash

---

## 👤 Author

**Fathya Shabira Akmal Tazkia**

Project:

**SMK Vault – Cloud Security Architecture & Immutable Academic Ledger**

---

## 📄 License

Project ini menggunakan lisensi **MIT License**.
