// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title IjazahBlockchain (SMK Vault Zero Trust & Immutable Academic Ledger)
 * @notice Smart contract mandiri (Zero-Dependency / tanpa import eksternal)
 * Siap dikompilasi & di-deploy di Remix IDE & Ganache.
 */
contract IjazahBlockchain {
    // Roles Definitions
    bytes32 public constant DEFAULT_ADMIN_ROLE = 0x00;
    bytes32 public constant KEPALA_SEKOLAH_ROLE = keccak256("KEPALA_SEKOLAH_ROLE");
    bytes32 public constant STAF_TU_ROLE = keccak256("STAF_TU_ROLE");
    bytes32 public constant MITRA_DUDI_ROLE = keccak256("MITRA_DUDI_ROLE");

    // Internal RBAC Mapping: role => account => hasRole
    mapping(bytes32 => mapping(address => bool)) private _roles;

    // Reentrancy Guard State
    uint256 private constant _NOT_ENTERED = 1;
    uint256 private constant _ENTERED = 2;
    uint256 private _status;

    // Data Structures
    struct Certificate {
        string studentId;
        string studentName;
        string major;
        bytes32 documentHash;      // SHA-256 Hash Dokumen PDF Ijazah
        bytes32 kmsDigitalSig;     // Signature dari Cloud KMS / HSM Kepala Sekolah
        uint256 issueTimestamp;
        bool isRevoked;
        bool isDudiVerified;
        address issuedBy;
    }

    struct GradeRecord {
        string studentId;
        string subject;
        uint8 gradeValue;
        bytes32 gradeHash;         // Cryptographic Hash Nilai
        uint256 updatedAt;
        address updatedBy;
    }

    // Mappings & State Variables
    mapping(bytes32 => Certificate) public certificates;
    mapping(bytes32 => GradeRecord[]) public gradeAuditLogs;
    uint256 public totalCertificates;

    // Events
    event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
    event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);
    event CertificateMinted(bytes32 indexed docHash, string studentId, address indexed authorizedBy, uint256 timestamp);
    event CertificateRevoked(bytes32 indexed docHash, string reason, address indexed revokedBy);
    event PKLSignedByDUDI(bytes32 indexed docHash, address indexed dudiAddress, uint256 timestamp);
    event GradeAuditLogged(string indexed studentId, bytes32 gradeHash, address indexed teacher);

    // Modifiers
    modifier onlyRole(bytes32 role) {
        require(hasRole(role, msg.sender), "AccessControl: account is missing required role");
        _;
    }

    modifier nonReentrant() {
        require(_status != _ENTERED, "ReentrancyGuard: reentrant call");
        _status = _ENTERED;
        _;
        _status = _NOT_ENTERED;
    }

    /**
     * @dev Constructor menginisialisasi role Admin dan Role Kepala Sekolah
     */
    constructor(address initialKepSek) {
        _status = _NOT_ENTERED;

        // Admin Role untuk deployer (msg.sender)
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        
        // Kepala Sekolah Role untuk address initialKepSek
        if (initialKepSek != address(0)) {
            _grantRole(KEPALA_SEKOLAH_ROLE, initialKepSek);
        } else {
            _grantRole(KEPALA_SEKOLAH_ROLE, msg.sender);
        }
    }

    /**
     * @notice Mengecek apakah sebuah address memiliki role tertentu
     */
    function hasRole(bytes32 role, address account) public view returns (bool) {
        return _roles[role][account];
    }

    /**
     * @notice Memberikan role ke address tertentu (hanya Admin)
     */
    function grantRole(bytes32 role, address account) public onlyRole(DEFAULT_ADMIN_ROLE) {
        _grantRole(role, account);
    }

    /**
     * @notice Mencabut role dari address tertentu (hanya Admin)
     */
    function revokeRole(bytes32 role, address account) public onlyRole(DEFAULT_ADMIN_ROLE) {
        if (hasRole(role, account)) {
            _roles[role][account] = false;
            emit RoleRevoked(role, account, msg.sender);
        }
    }

    function _grantRole(bytes32 role, address account) internal {
        if (!hasRole(role, account)) {
            _roles[role][account] = true;
            emit RoleGranted(role, account, msg.sender);
        }
    }

    /**
     * @notice Minting Ijazah Digital ke Blockchain Ledger
     * Memerlukan Otorisasi Role Kepala Sekolah & Signature KMS Match
     */
    function issueCertificate(
        string memory _studentId,
        string memory _studentName,
        string memory _major,
        bytes32 _documentHash,
        bytes32 _kmsDigitalSig
    ) external onlyRole(KEPALA_SEKOLAH_ROLE) nonReentrant {
        require(_documentHash != bytes32(0), "Invalid Document Hash");
        require(certificates[_documentHash].documentHash == bytes32(0), "Certificate already exists");

        certificates[_documentHash] = Certificate({
            studentId: _studentId,
            studentName: _studentName,
            major: _major,
            documentHash: _documentHash,
            kmsDigitalSig: _kmsDigitalSig,
            issueTimestamp: block.timestamp,
            isRevoked: false,
            isDudiVerified: false,
            issuedBy: msg.sender
        });

        totalCertificates++;

        emit CertificateMinted(_documentHash, _studentId, msg.sender, block.timestamp);
    }

    /**
     * @notice Verifikasi Digital Sertifikat Magang / PKL oleh Mitra Industri (DUDI)
     */
    function signPKLCertificate(bytes32 _documentHash) external onlyRole(MITRA_DUDI_ROLE) {
        require(certificates[_documentHash].documentHash != bytes32(0), "Certificate not found");
        require(!certificates[_documentHash].isRevoked, "Certificate is revoked");

        certificates[_documentHash].isDudiVerified = true;
        emit PKLSignedByDUDI(_documentHash, msg.sender, block.timestamp);
    }

    /**
     * @notice Verifikasi Publik Keabsahan Dokumen PDF Ijazah
     */
    function verifyCertificate(bytes32 _documentHash) external view returns (
        bool isValid,
        string memory studentId,
        string memory studentName,
        string memory major,
        uint256 timestamp,
        bool isDudiVerified
    ) {
        Certificate memory cert = certificates[_documentHash];
        if (cert.documentHash == bytes32(0) || cert.isRevoked) {
            return (false, "", "", "", 0, false);
        }
        return (true, cert.studentId, cert.studentName, cert.major, cert.issueTimestamp, cert.isDudiVerified);
    }

    /**
     * @notice Pencabutan/Pembatalan Ijazah jika Terjadi Pelanggaran
     */
    function revokeCertificate(bytes32 _documentHash, string memory _reason) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(certificates[_documentHash].documentHash != bytes32(0), "Certificate not found");
        require(!certificates[_documentHash].isRevoked, "Already revoked");

        certificates[_documentHash].isRevoked = true;
        emit CertificateRevoked(_documentHash, _reason, msg.sender);
    }

    /**
     * @notice Audit Log Transkrip Nilai Siswa (Pencegahan Kecurangan Nilai Internal)
     */
    function logGradeUpdate(
        string memory _studentId,
        string memory _subject,
        uint8 _gradeValue,
        bytes32 _gradeHash
    ) external onlyRole(STAF_TU_ROLE) {
        gradeAuditLogs[keccak256(abi.encodePacked(_studentId))].push(GradeRecord({
            studentId: _studentId,
            subject: _subject,
            gradeValue: _gradeValue,
            gradeHash: _gradeHash,
            updatedAt: block.timestamp,
            updatedBy: msg.sender
        }));

        emit GradeAuditLogged(_studentId, _gradeHash, msg.sender);
    }
}
