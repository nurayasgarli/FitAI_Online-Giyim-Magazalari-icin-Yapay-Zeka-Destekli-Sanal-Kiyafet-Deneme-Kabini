CREATE TABLE IF NOT EXISTS tryon_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    garment_type VARCHAR(32) NOT NULL,
    height_cm REAL NOT NULL,
    weight_kg REAL NOT NULL,
    body_size VARCHAR(16),
    person_image_path VARCHAR(255) NOT NULL,
    garment_image_path VARCHAR(255) NOT NULL,
    result_image_path VARCHAR(255),
    status VARCHAR(32) NOT NULL DEFAULT 'pending',
    processing_time_ms INTEGER,
    error_message TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_tryon_requests_status ON tryon_requests(status);
CREATE INDEX IF NOT EXISTS idx_tryon_requests_created_at ON tryon_requests(created_at);