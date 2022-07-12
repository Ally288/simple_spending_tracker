PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE tags(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
);

CREATE TABLE merchants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    merchant_name VARCHAR,
    tag_id INTEGER NOT NULL,
        FOREIGN KEY (tag_id)
            REFERENCES tags (id)
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_date VARCHAR,
    transaction_amount FLOAT,
    tag_id INTEGER NOT NULL,
    merchant_id INTEGER NOT NULL,
        FOREIGN KEY (merchant_id)
            REFERENCES merchants (id)
        FOREIGN KEY (tag_id)
            REFERENCES tags (id)
);