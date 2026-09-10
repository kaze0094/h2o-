CREATE TABLE communities (
    id              VARCHAR(40) PRIMARY KEY,
    name            TEXT NOT NULL,
    region_code     TEXT NOT NULL,
    verified        BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE workers (
    id              VARCHAR(40) PRIMARY KEY,
    community_id    VARCHAR(40)
                    REFERENCES communities(id),
    status          TEXT NOT NULL,
    zone_code       TEXT,
    consent_valid   BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE worker_skills (
    worker_id       VARCHAR(40)
                    REFERENCES workers(id),
    skill_code      TEXT NOT NULL,
    score           NUMERIC(5,4) CHECK (
                        score >= 0 AND score <= 1
                    ),
    verification_status TEXT NOT NULL,
    verified_at     TIMESTAMPTZ,
    evidence_ref    TEXT,
    PRIMARY KEY (worker_id, skill_code)
);

-- Keep sensitive/accessibility data logically separated.
CREATE TABLE worker_restricted_profile (
    worker_id       VARCHAR(40) PRIMARY KEY
                    REFERENCES workers(id),
    encrypted_data  BYTEA NOT NULL,
    lawful_basis    TEXT,
    retention_until DATE
);

CREATE TABLE employers (
    id              VARCHAR(40) PRIMARY KEY,
    legal_name      TEXT NOT NULL,
    registration_id TEXT,
    verification_status TEXT NOT NULL,
    trust_score     NUMERIC(5,4),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE jobs (
    id              VARCHAR(40) PRIMARY KEY,
    employer_id     VARCHAR(40)
                    REFERENCES employers(id),
    task_type       TEXT NOT NULL,
    quantity        INTEGER NOT NULL CHECK (quantity > 0),
    deadline        TIMESTAMPTZ,
    quality_threshold NUMERIC(5,4),
    payment_status  TEXT NOT NULL,
    moderation_status TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE matches (
    id              BIGSERIAL PRIMARY KEY,
    job_id          VARCHAR(40) REFERENCES jobs(id),
    worker_id       VARCHAR(40) REFERENCES workers(id),
    score           NUMERIC(6,2),
    model_version   TEXT NOT NULL,
    explanation     JSONB,
    accepted        BOOLEAN,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE task_batches (
    id              VARCHAR(40) PRIMARY KEY,
    job_id          VARCHAR(40) REFERENCES jobs(id),
    community_id    VARCHAR(40)
                    REFERENCES communities(id),
    units_assigned  INTEGER NOT NULL,
    units_accepted  INTEGER DEFAULT 0,
    defect_count    INTEGER DEFAULT 0,
    status          TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE quality_checks (
    id              BIGSERIAL PRIMARY KEY,
    batch_id        VARCHAR(40)
                    REFERENCES task_batches(id),
    reviewer_role   TEXT NOT NULL,
    inspected_units INTEGER NOT NULL,
    defects         INTEGER NOT NULL,
    evidence_ref    TEXT,
    decision        TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE impact_events (
    id              BIGSERIAL PRIMARY KEY,
    event_type      TEXT NOT NULL,
    worker_id       VARCHAR(40),
    job_id          VARCHAR(40),
    metric_value    NUMERIC,
    source_type     TEXT NOT NULL,
    evidence_tier   INTEGER NOT NULL,
    evidence_ref    TEXT,
    occurred_at     TIMESTAMPTZ NOT NULL
);

CREATE TABLE consent_records (
    id              BIGSERIAL PRIMARY KEY,
    worker_id       VARCHAR(40) REFERENCES workers(id),
    purpose_code    TEXT NOT NULL,
    granted         BOOLEAN NOT NULL,
    policy_version  TEXT NOT NULL,
    recorded_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE audit_log (
    id              BIGSERIAL PRIMARY KEY,
    actor_id        TEXT NOT NULL,
    action          TEXT NOT NULL,
    object_type     TEXT NOT NULL,
    object_id       TEXT NOT NULL,
    metadata        JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
