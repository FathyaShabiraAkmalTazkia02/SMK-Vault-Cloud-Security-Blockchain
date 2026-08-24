import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Naskah Video & Panduan Pengujian Remix IDE & Ganache</title>
    <style>
        @page {
            size: A4;
            margin: 15mm;
        }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
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
            padding: 22px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .header h1 {
            margin: 0;
            font-size: 18pt;
            letter-spacing: 0.5px;
        }
        .header p {
            margin: 6px 0 0 0;
            font-size: 11pt;
            color: #e0f2fe;
        }
        .section-header {
            background: #f1f5f9;
            border-left: 5px solid #0284c7;
            padding: 8px 12px;
            font-size: 12pt;
            font-weight: bold;
            color: #0f172a;
            margin-top: 25px;
            margin-bottom: 15px;
            border-radius: 0 4px 4px 0;
        }
        .step-box {
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            margin-bottom: 20px;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            page-break-inside: avoid;
            overflow: hidden;
        }
        .step-header {
            background: #0f172a;
            color: #ffffff;
            padding: 10px 15px;
            font-weight: bold;
            font-size: 11pt;
            display: flex;
            align-items: center;
        }
        .step-number {
            background: #0284c7;
            color: white;
            border-radius: 50%;
            width: 22px;
            height: 22px;
            display: inline-block;
            text-align: center;
            line-height: 22px;
            font-size: 10pt;
            margin-right: 10px;
        }
        .step-body {
            padding: 15px;
        }
        .action-box {
            background: #f8fafc;
            border-left: 4px solid #3b82f6;
            padding: 10px 12px;
            margin-bottom: 12px;
            border-radius: 0 4px 4px 0;
            font-size: 9.5pt;
        }
        .narration-box {
            background: #f0fdf4;
            border-left: 4px solid #10b981;
            padding: 12px;
            margin-bottom: 12px;
            border-radius: 0 4px 4px 0;
            font-size: 9.5pt;
            color: #065f46;
            font-style: italic;
        }
        .narration-title {
            font-weight: bold;
            font-style: normal;
            color: #047857;
            margin-bottom: 4px;
            display: block;
        }
        .field-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 9pt;
        }
        .field-table th, .field-table td {
            border: 1px solid #cbd5e1;
            padding: 6px 10px;
            text-align: left;
        }
        .field-table th {
            background: #e2e8f0;
            color: #334155;
        }
        .code-val {
            font-family: 'Consolas', 'Courier New', monospace;
            background: #0f172a;
            color: #38bdf8;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 8.5pt;
            word-break: break-all;
        }
        .master-card {
            background: #f0f9ff;
            border: 1px solid #bae6fd;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 20px;
            font-size: 9.5pt;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>NASKAH VIDEO & PANDUAN PENGUJIAN REMIX IDE & GANACHE</h1>
        <p>Pengujian Smart Contract IjazahBlockchain.sol • Skrip Narasi Video & Copy-Paste Parameter</p>
    </div>

    <div class="master-card">
        <strong>🔑 DATA MASTER LENGKAP PENGUJIAN (COPY-PASTE):</strong><br>
        • <strong>Document Hash SHA-256:</strong> <span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span><br>
        • <strong>Nama Siswa:</strong> <span class="code-val">FATHYA SHABIRA A.T</span> &nbsp;|&nbsp; <strong>NISN:</strong> <span class="code-val">105841111923</span> &nbsp;|&nbsp; <strong>Jurusan:</strong> <span class="code-val">Rekayasa Perangkat Lunak</span><br>
        • <strong>Hash MITRA_DUDI_ROLE:</strong> <span class="code-val">0x7a4a9f3b5f9037e5d8b8fb62ffec01c708ec7bc9eeef8c983a54b38d37452d3a</span>
    </div>

    <!-- STAGE 0: INTRO & DEPLOYMENT -->
    <div class="section-header">TAHAP 1: PEMBUKAAN VIDEO & DEPLOYMENT KONTRAK</div>

    <div class="step-box">
        <div class="step-header"><span class="step-number">0</span> PENDAHULUAN & DEPLOYMENT SMART CONTRACT</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> Tampilkan halaman utama Remix IDE (<code>remix.ethereum.org</code>) & Ganache GUI. Pada Remix tab <em>Deploy & Run Transactions</em>, pilih Environment <code>Dev - Ganache Provider</code> (atau <code>Remix VM</code>). Isi kolom <code>initialKepSek</code> dengan <span class="code-val">0x0000000000000000000000000000000000000000</span> lalu klik <strong>Deploy</strong>. Buka <strong>Deployed Contracts</strong> -> klik <strong>Functions [+]</strong>.
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Halo semuanya! Pada video kali ini, saya akan mendemonstrasikan pengujian Smart Contract IjazahBlockchain.sol menggunakan Remix IDE dan Ganache. Pertama, kita hubungkan Remix dengan Ganache, lalu kita lakukan deployment smart contract. Setelah berhasil di-deploy dengan centang hijau, akun deployer secara otomatis memiliki otorisasi sebagai Admin dan Kepala Sekolah."
            </div>
        </div>
    </div>

    <!-- STAGE 1: ISSUE CERTIFICATE -->
    <div class="section-header">TAHAP 2: SKENARIO PENGUJIAN UTAMA</div>

    <div class="step-box">
        <div class="step-header"><span class="step-number">1</span> PENGUJIAN 1: Penerbitan Ijazah Digital (issueCertificate)</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> Buka fungsi <strong>issueCertificate</strong> di Remix. Masukkan parameter berikut lalu klik <strong>transact</strong> (Tunjukkan centang hijau ✔ di terminal).
                <table class="field-table">
                    <tr><th width="30%">Kolom Parameter</th><th>Nilai Isian (Copy-Paste)</th></tr>
                    <tr><td><code>_studentId</code></td><td><span class="code-val">105841111923</span></td></tr>
                    <tr><td><code>_studentName</code></td><td><span class="code-val">FATHYA SHABIRA A.T</span></td></tr>
                    <tr><td><code>_major</code></td><td><span class="code-val">Rekayasa Perangkat Lunak</span></td></tr>
                    <tr><td><code>_documentHash</code></td><td><span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span></td></tr>
                    <tr><td><code>_kmsDigitalSig</code></td><td><span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span></td></tr>
                </table>
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Pengujian pertama adalah penerbitan Ijazah Digital oleh Kepala Sekolah. Kita memanggil fungsi issueCertificate dengan memasukkan SHA-256 Document Hash dan KMS Digital Signature. Transaksi berhasil dieksekusi dan data ijazah kini resmi terkunci secara permanen di blockchain Ganache."
            </div>
        </div>
    </div>

    <!-- STAGE 2: VERIFY CERTIFICATE -->
    <div class="step-box">
        <div class="step-header"><span class="step-number">2</span> PENGUJIAN 2: Verifikasi Keabsahan Publik (verifyCertificate)</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> Buka fungsi tombol biru <strong>verifyCertificate</strong>. Masukkan <code>_documentHash</code>: <span class="code-val">0xe04bb039ad76b96cc9c9170a4f4c47edc713dba55cbf2b6226c3d63f995cb77b</span> lalu klik <strong>call</strong>. Tunjukkan output <code>isValid: true</code>.
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Pengujian kedua adalah verifikasi publik. Siapapun dapat mengecek keaslian ijazah hanya dengan memasukkan Document Hash ke fungsi verifyCertificate. Hasil mengembalikan status isValid: true beserta identitas siswa, membuktikan dokumen asli dan terdaftar di ledger."
            </div>
        </div>
    </div>

    <!-- STAGE 3: RBAC PROTECT -->
    <div class="step-box">
        <div class="step-header"><span class="step-number">3</span> PENGUJIAN 3: Proteksi Hak Akses Zero-Trust RBAC (Akses Ditolak)</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> Pada dropdown <strong>ACCOUNT</strong> paling atas Remix, pilih Akun Ke-2 (Akun publik). Coba panggil lagi <code>issueCertificate</code> lalu klik <strong>transact</strong>. Tunjukkan error merah <code>AccessControl: account is missing required role</code>.
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Pengujian ketiga adalah pembuktian keamanan Zero-Trust. Di sini saya mencoba menerbitkan ijazah menggunakan akun publik biasa. Transaksi langsung ditolak dan di-revert dengan error missing role. Ini membuktikan pihak luar tidak bisa memalsukan atau menerbitkan ijazah."
            </div>
        </div>
    </div>

    <!-- STAGE 4: DUDI SIGN -->
    <div class="step-box">
        <div class="step-header"><span class="step-number">4</span> PENGUJIAN 4: Verifikasi Sertifikat PKL Mitra DUDI (grantRole & signPKLCertificate)</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> 
                1. Ubah ACCOUNT ke Akun 1 (Admin). Buka <strong>grantRole</strong>:
                <br>• <code>role</code>: <span class="code-val">0x7a4a9f3b5f9037e5d8b8fb62ffec01c708ec7bc9eeef8c983a54b38d37452d3a</span>
                <br>• <code>account</code>: Salin Alamat Akun 1 Anda dari dropdown ACCOUNT -> Klik <strong>transact</strong>.
                <br>2. Buka <strong>signPKLCertificate</strong>, masukkan <code>_documentHash</code> -> Klik <strong>transact</strong>.
                <br>3. Panggil lagi <code>verifyCertificate</code> -> Tunjukkan <code>isDudiVerified</code> berubah menjadi <code>true</code>.
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Pengujian keempat adalah penandatanganan digital sertifikat magang oleh Mitra Industri DUDI. Setelah akun industri diberikan role, mereka memanggil signPKLCertificate. Saat dipanggil di verifikasi publik, atribut isDudiVerified kini berubah menjadi true, membuktikan ijazah telah diverifikasi industri."
            </div>
        </div>
    </div>

    <!-- STAGE 5: REVOCATION & OUTRO -->
    <div class="step-box">
        <div class="step-header"><span class="step-number">5</span> PENGUJIAN 5: Pencabutan Ijazah (revokeCertificate) & PENUTUP</div>
        <div class="step-body">
            <div class="action-box">
                <strong>🖥️ AKSI DI LAYAR:</strong> Buka <strong>revokeCertificate</strong>, masukkan <code>_documentHash</code> & <code>_reason: "Pelanggaran Integritas Akademik"</code> -> Klik <strong>transact</strong>. Panggil lagi <code>verifyCertificate</code> -> Tunjukkan <code>isValid</code> berubah menjadi <code>false</code>.
            </div>
            <div class="narration-box">
                <span class="narration-title">🔊 NARASI SUARA (APA YANG DIUCAPKAN):</span>
                "Pengujian terakhir adalah pencabutan ijazah jika terjadi pelanggaran. Admin memanggil revokeCertificate. Saat diverifikasi ulang, status isValid otomatis gugur menjadi false. Kesimpulannya, seluruh fungsi smart contract IjazahBlockchain telah berhasil diuji 100% dan berjalan sempurna. Terima kasih!"
            </div>
        </div>
    </div>

</body>
</html>
"""

dir_path = os.path.dirname(__file__)
html_path = os.path.join(dir_path, 'Naskah_Video_dan_Panduan_Pengujian_Remix.html')
pdf_path = os.path.join(dir_path, 'Naskah_Video_dan_Panduan_Pengujian_Remix.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"File HTML Naskah & Panduan berhasil dibuat di: {html_path}")

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
args = [edge_exe, "--headless", f"--print-to-pdf={pdf_path}", html_path]

subprocess.run(args, check=True)

print(f"File PDF Naskah & Panduan berhasil dibuat di: {pdf_path}")
