-- Database initialization script for RAG Chatbot
-- This script runs automatically when the PostgreSQL container starts

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Verify pgvector is installed
SELECT extname, extversion FROM pg_extension WHERE extname = 'vector';

-- Grant permissions (if needed)
-- GRANT ALL PRIVILEGES ON DATABASE ragchat TO postgres;

-- Note: Tables are created by SQLAlchemy's create_all()
-- This script only sets up extensions and initial configuration
