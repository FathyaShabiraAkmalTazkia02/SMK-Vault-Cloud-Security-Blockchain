import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Panduan Pengujian Remix IDE & Ganache - Smart Contract IjazahBlockchain</title>
    <style>
        @page {
            size: A4;
            margin: 15mm;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.5;
            margin: 0;
            padding: 10px;
            color: #0f172a;
            background: #ffffff;
        }
        .header {
            text-align: center;
            background: linear-gradient(135deg, #0284c7, #0f172a);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .header h1 {
            margin: 0;
            font-size: 18pt;
            letter-spacing: 0.5px;
        }
        .header p {
            margin: 5px 0 0 0;
            font-size: 11pt;
            color: #e0f2fe;
        }
        .step-card {
            border: 1px solid #cbd5e1;
            border-left: 6px solid #0284c7;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 18px;
            background: #f8fafc;
            page-break-inside: avoid;
        }
        .step-card.warning {
            border-left-color: #f59e0b;
            background: #fffbeb;
        }
        .step-card.success {
            border-left-color: #10b981;
            background: #f0fdf4;
        }
        .step-title {
            font-size: 12pt;
            font-weight: bold;
            color: #0f172a;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
        }
        .step-num {
            background: #0284c7;
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: inline-block;
            text-align: center;
            line-height: 24px;
            font-size: 10pt;
            margin-right: 10px;
        }
        .field-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 9.5pt;
        }
        .field-table th, .field-table td {
            border: 1px solid #cbd5e1;
            padding: 7px 10px;
        }
        .field-table th {
            background: #e2e8f0;
            color: #334155;
        }
        .code-val {
            font-family: 'Consolas', 'Courier New', monospace;
            background: #0f172a;
            color: #38bdf8;
            padding: 3px 6px;
            border-radius: 4px;
            font-size: 9pt;
            word-break: break-all;
        }
        .note-box {
            background: #eff6ff;
            border: 1px dashed #3b82f6;
            padding: 10px;
            font-size: 9pt;
            border-radius: 4px;
            margin-top: 8px;
            color: #1e40af;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>PANDUAN PRAKTIS PENGUJIAN REMIX IDE & GANACHE</h1>
        <p>Smart Contract: IjazahBlockchain.sol • Panduan Langkah Demi Langkah</p>
    </div>

    <!-- PENGUJIAN 0 -->
    <div class="step-card">
        <div class="step-title"><span class="step-num">0</span> TAHAP DEPLOYMENT SMART CONTRACT</div>
        <p style="margin: 5px 0; font-size: 9.5pt;">Persiapan awal sebelum menjalankan pengujian:</p>
        <ol style="margin: 5px 0; font-size: 9.5pt; padding-left: 20px;">
            <li>Buka Remix IDE (<code>remix.ethereum.org</code>) & buka file <code>IjazahBlockchain.sol</code>.</li>
            <li>Di tab <strong>Solidity Compiler</strong>, klik <strong>Compile IjazahBlockchain.sol</strong>.</li>
            <li>Di tab <strong>Deploy & Run Transactions</strong>, pilih Environment <code>Dev - Ganache Provider</code> (atau <code>Remix VM</code>).</li>
            <li>Pada kolom <code>initialKepSek</code> di sebelah tombol Deploy (oranye), masukkan:</li>
        </ol>
        <div style="margin-top: 5px;">
            <span class="code-val">0x0000000000000000000000000000000000000000</span>
        </div>
        <p style="margin: 5px 0; font-size: 9.5pt;">Klik tombol <strong>Deploy</strong> (Tunggu centang hijau ✔). Buka <strong>Deployed Contracts</strong> & klik <strong>Functions [+]</strong>.</p>
    </div>

    <!-- PENGUJIAN 1 -->
    <div class="step-card success">
        <div class="step-title"><span class="step-num">1</span> PENGUJIAN 1: Penerbitan Ijazah Digital (issueCertificate)</div>
        <p style="margin: 5px 0; font-size: 9.5pt;">Buka fungsi <strong>issueCertificate</strong> di Remix, lalu isikan parameter berikut:</p>
        
        <table class="field-table">
            <tr><th width="30%">Kolom Parameter</th><th>Nilai Isian (Copy-Paste)</th></tr>
            <tr><td><code>_studentId</code></td><td><span class="code-val">105841111923</span></td></tr>
            <tr><td><code>_studentName</code></td><td><span class="code-val">FATHYA SHABIRA A.T</span></td></tr>
            <tr><td><code>_major</code></td><td><span class="code-val">Rekayasa Perangkat Lunak</span></td></tr>
            <tr><td><code>_documentHash</code></td><td><span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span></td></tr>
            <tr><td><code>_kmsDigitalSig</code></td><td><span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span></td></tr>
        </table>
        
        <p style="margin: 8px 0 0 0; font-size: 9.5pt;">Klik tombol <strong>transact</strong>. <br>✅ <strong>Hasil Expected:</strong> Transaksi sukses (centang hijau ✔) & Event <code>CertificateMinted</code> terbit.</p>
    </div>

    <!-- PENGUJIAN 2 -->
    <div class="step-card">
        <div class="step-title"><span class="step-num">2</span> PENGUJIAN 2: Verifikasi Keabsahan Publik (verifyCertificate)</div>
        <p style="margin: 5px 0; font-size: 9.5pt;">Buka fungsi tombol biru <strong>verifyCertificate</strong>, masukkan parameter:</p>
        <div style="margin: 5px 0;">
            <strong>_documentHash:</strong><br>
            <span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span>
        </div>
        <p style="margin: 8px 0 0 0; font-size: 9.5pt;">Klik tombol <strong>call</strong>.<br>✅ <strong>Hasil Expected:</strong> Output <code>isValid: true</code>, <code>studentName: FATHYA SHABIRA A.T</code>, & <code>isDudiVerified: false</code>.</p>
    </div>

    <!-- PENGUJIAN 3 -->
    <div class="step-card warning">
        <div class="step-title"><span class="step-num">3</span> PENGUJIAN 3: Proteksi Hak Akses Zero-Trust / RBAC (Akses Ditolak)</div>
        <ol style="margin: 5px 0; font-size: 9.5pt; padding-left: 20px;">
            <li>Pada dropdown <strong>ACCOUNT</strong> paling atas Remix, ganti ke <strong>Akun Ke-2</strong> (Akun publik biasa).</li>
            <li>Coba jalankan kembali fungsi <code>issueCertificate</code>.</li>
            <li>Klik tombol <strong>transact</strong>.</li>
        </ol>
        <p style="margin: 5px 0 0 0; font-size: 9.5pt;">❌ <strong>Hasil Expected:</strong> Transaksi <strong>REVERTED (Gagal)</strong> dengan pesan error <code>AccessControl: account is missing required role</code>.</p>
    </div>

    <!-- PENGUJIAN 4 -->
    <div class="step-card success">
        <div class="step-title"><span class="step-num">4</span> PENGUJIAN 4: Verifikasi Sertifikat PKL DUDI (grantRole & signPKLCertificate)</div>
        <ol style="margin: 5px 0; font-size: 9.5pt; padding-left: 20px;">
            <li>Ganti dropdown <strong>ACCOUNT</strong> kembali ke <strong>Akun Ke-1 (Admin)</strong>.</li>
            <li>Buka fungsi <strong>grantRole</strong>, isikan:
                <br>• <code>role</code>: <span class="code-val">0x7a4a9f3b5f9037e5d8b8fb62ffec01c708ec7bc9eeef8c983a54b38d37452d3a</span>
                <br>• <code>account</code>: Salin Alamat Akun Ke-1 Anda dari dropdown ACCOUNT.
                <br>Klik <strong>transact</strong> (Centang Hijau ✔).
            </li>
            <li>Buka fungsi <strong>signPKLCertificate</strong>, isikan:
                <br>• <code>_documentHash</code>: <span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span>
                <br>Klik <strong>transact</strong> (Centang Hijau ✔).
            </li>
            <li>Panggil kembali <code>verifyCertificate</code>.</li>
        </ol>
        <p style="margin: 5px 0 0 0; font-size: 9.5pt;">✅ <strong>Hasil Expected:</strong> Atribut <code>isDudiVerified</code> kini berubah dari <code>false</code> menjadi <strong><code>true</code></strong>!</p>
    </div>

    <!-- PENGUJIAN 5 -->
    <div class="step-card">
        <div class="step-title"><span class="step-num">5</span> PENGUJIAN 5: Pencabutan / Pembatalan Ijazah (revokeCertificate)</div>
        <p style="margin: 5px 0; font-size: 9.5pt;">Buka fungsi <strong>revokeCertificate</strong>, isikan parameter:</p>
        <table class="field-table">
            <tr><th width="30%">Kolom Parameter</th><th>Nilai Isian</th></tr>
            <tr><td><code>_documentHash</code></td><td><span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span></td></tr>
            <tr><td><code>_reason</code></td><td><span class="code-val">Pelanggaran Integritas Akademik</span></td></tr>
        </table>
        <p style="margin: 8px 0 0 0; font-size: 9.5pt;">Klik <strong>transact</strong>, lalu panggil kembali <code>verifyCertificate</code>.<br>✅ <strong>Hasil Expected:</strong> Status <code>isValid</code> otomatis gugur menjadi <strong><code>false</code></strong> (Ijazah dibatalkan).</p>
    </div>

    <div class="note-box">
        💡 <strong>TIPS MEMBACA LOG REMIX:</strong><br>
        • <strong>Centang Hijau (✔)</strong> = Transaksi Berhasil Dieksekusi Ke Blockchain.<br>
        • <strong>Silang Merah (❌) / Revert</strong> = Akses Ditolak Oleh Aturan Zero-Trust Smart Contract (Berhasil Menghalau Serangan).
    </div>

</body>
</html>
"""

dir_path = os.path.dirname(__file__)
html_path = os.path.join(dir_path, 'Panduan_Pengujian_Remix_Ganache.html')
pdf_path = os.path.join(dir_path, 'Panduan_Pengujian_Remix_Ganache.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"File HTML Panduan Pengujian berhasil dibuat di: {html_path}")

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
args = [edge_exe, "--headless", f"--print-to-pdf={pdf_path}", html_path]

subprocess.run(args, check=True)

print(f"File PDF Panduan Pengujian berhasil dibuat di: {pdf_path}")
