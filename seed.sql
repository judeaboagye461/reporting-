CREATE TABLE IF NOT EXISTS distributions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    distribution_date DATE NOT NULL,
    weight INTEGER NOT NULL CHECK (weight >= 0)
);

INSERT INTO distributions (distribution_date, weight)
VALUES
    ('2026-08-31', 900),
    ('2026-09-01', 100),
    ('2026-09-15', 250),
    ('2026-09-30', 150),
    ('2026-10-01', 800);