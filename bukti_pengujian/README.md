# 📸 Bukti Pengujian Web & Smart Contract (SMK Cloud Security & Blockchain Vault)

Folder ini berisi dokumentasi pengujian implementasi aplikasi web **SMK Cloud Security & Blockchain Vault** beserta pengujian **Smart Contract `IjazahBlockchain.sol`** menggunakan **Remix IDE** dan **Ganache Provider**.

---

# 🌐 Implementasi Web

## 1. 📊 Dashboard Overview
[**01_dashboard_overview.png**](01_dashboard_overview.png)

**Deskripsi:**
Menampilkan dashboard utama aplikasi SMK Cloud Security & Blockchain Vault yang memperlihatkan statistik keamanan secara real-time, meliputi WAF & Edge Defense, KMS Encryption Vault, Blockchain Ledger, Zero-Trust Status, serta Matriks Multi-Cloud Architecture (AWS vs GCP).

---

## 2. 📝 Input Data Kelulusan
[**02_web_input_data_kelulusan.png**](02_web_input_data_kelulusan.png)

**Deskripsi:**
Staf Tata Usaha menginput data kelulusan siswa berupa nama, NISN, jurusan, dan nilai rata-rata sebelum diajukan kepada Kepala Sekolah untuk proses penandatanganan digital.

---

## 3. ✅ Draft Kelulusan Berhasil Diajukan
[**03_web_draft_submitted.png**](03_web_draft_submitted.png)

**Deskripsi:**
Sistem menampilkan notifikasi bahwa data kelulusan berhasil dikirim ke antrian persetujuan Kepala Sekolah dan siap diproses menggunakan Cloud KMS.

---

## 4. 🔐 MFA Authentication
[**04_web_mfa_authentication.png**](04_web_mfa_authentication.png)

**Deskripsi:**
Kepala Sekolah wajib melakukan autentikasi Multi-Factor Authentication (MFA) menggunakan kode OTP sebelum memperoleh akses ke proses penandatanganan ijazah digital.

---

## 5. 🔑 Cloud KMS Signing Workspace
[**05_web_kms_workspace.png**](05_web_kms_workspace.png)

**Deskripsi:**
Halaman kerja Kepala Sekolah untuk melakukan otorisasi menggunakan Cloud KMS Hardware Security Module (HSM) sebelum ijazah dicatat ke Blockchain Ledger.

---

## 6. ✔️ KMS Signing Berhasil
[**06_web_kms_sign_success.png**](06_web_kms_sign_success.png)

**Deskripsi:**
Notifikasi bahwa proses penandatanganan digital menggunakan Cloud KMS berhasil dilakukan dan data ijazah telah berhasil dicatat pada Blockchain Ledger.

---

## 7. 👨‍🎓 Student Self-Service Portal
[**07_web_student_portal.png**](07_web_student_portal.png)

**Deskripsi:**
Portal mandiri siswa yang menampilkan daftar ijazah digital yang telah diterbitkan beserta hash SHA-256 dan tombol unduh dokumen resmi.

---

## 8. 📥 Download Ijazah Digital
[**08_web_download_pdf.png**](08_web_download_pdf.png)

**Deskripsi:**
Proses pengunduhan ijazah digital dalam format PDF yang telah diterbitkan dan tersimpan pada Blockchain Ledger.

---

## 9. ✅ Verifikasi Dokumen Valid
[**09_web_certificate_verified.png**](09_web_certificate_verified.png)

**Deskripsi:**
Halaman verifikasi publik yang menunjukkan bahwa hash dokumen sesuai dengan data yang tersimpan pada Blockchain sehingga status dokumen dinyatakan **VALID**.

---

## 10. ❌ Deteksi Dokumen Palsu
[**10_web_certificate_invalid.png**](10_web_certificate_invalid.png)

**Deskripsi:**
Sistem mendeteksi adanya perubahan isi dokumen (1 karakter dimodifikasi) sehingga hash tidak cocok dengan Blockchain Ledger dan dokumen dinyatakan **INVALID/FALSIFIED**.

---

## 11. 🛡️ Cyber Pentest & Audit Lab
[**11_web_cyber_pentest_lab.png**](11_web_cyber_pentest_lab.png)

**Deskripsi:**
Halaman simulasi pengujian keamanan yang mencakup OWASP Web Security Testing Guide, Smart Contract SCSVS, RBAC Bypass, SQL Injection, Cloud Security Audit, dan API Rate Limiting.

---

# ⛓️ Pengujian Smart Contract (Remix IDE & Ganache)

## 12. 📜 Deploy & Minting Ijazah (`issueCertificate`)
[**12_remix_issue_certificate.png**](12_remix_issue_certificate.png)

**Deskripsi:**
Admin/Kepala Sekolah berhasil menjalankan fungsi `issueCertificate`. Transaksi berhasil dan data ijazah dicatat pada Blockchain.

---

## 13. 🔍 Verifikasi Sertifikat (`verifyCertificate`)
[**13_remix_verify_certificate.png**](13_remix_verify_certificate.png)

**Deskripsi:**
Pemanggilan fungsi `verifyCertificate` mengembalikan status **isValid = true**, membuktikan dokumen telah terdaftar secara sah pada Blockchain.

---

## 14. 🚫 Zero-Trust RBAC Protection
[**14_remix_rbac_protection.png**](14_remix_rbac_protection.png)

**Deskripsi:**
Pengguna tanpa hak akses mencoba melakukan proses minting sertifikat dan transaksi ditolak (Reverted), membuktikan mekanisme Role-Based Access Control (RBAC) berjalan dengan baik.

---

## 15. 👥 Grant Role Mitra DUDI
[**15_remix_grant_role.png**](15_remix_grant_role.png)

**Deskripsi:**
Administrator memberikan hak akses `MITRA_DUDI_ROLE` kepada akun lain menggunakan fungsi `grantRole`. Event `RoleGranted` berhasil diterbitkan.

---

## 16. 📖 Verifikasi Setelah Mendapat Role
[**16_remix_verify_after_grant_role.png**](16_remix_verify_after_grant_role.png)

**Deskripsi:**
Akun yang telah memperoleh role berhasil melakukan verifikasi sertifikat menggunakan fungsi `verifyCertificate`.

---

## 17. 🖥️ Ganache Blockchain Network
[**17_ganache_provider.png**](17_ganache_provider.png)

**Deskripsi:**
Tampilan jaringan Ganache Provider yang digunakan sebagai blockchain lokal selama proses deployment, transaksi, dan pengujian Smart Contract.
