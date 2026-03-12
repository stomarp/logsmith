CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

CREATE TABLE IF NOT EXISTS logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ NOT NULL,
    service TEXT NOT NULL,
    level TEXT NOT NULL,
    trace_id TEXT,
    span_id TEXT,
    user_id TEXT,
    endpoint TEXT,
    status_code INT,
    latency_ms INT,
    message TEXT NOT NULL,
    metadata JSONB
);

CREATE INDEX IF NOT EXISTS idx_logs_timestamp ON logs (timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_logs_trace_id ON logs (trace_id);
CREATE INDEX IF NOT EXISTS idx_logs_user_id ON logs (user_id);
CREATE INDEX IF NOT EXISTS idx_logs_endpoint ON logs (endpoint);
CREATE INDEX IF NOT EXISTS idx_logs_status_code ON logs (status_code);
CREATE INDEX IF NOT EXISTS idx_logs_message_trgm ON logs USING GIN (message gin_trgm_ops);