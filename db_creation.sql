-- Create a new database
CREATE DATABASE mydatabase;

-- Connect to the newly created database (you would do this separately in your SQL client or application)
-- \c mydatabase;

-- Create the 'swaps' table
CREATE TABLE IF NOT EXISTS swaps (
    id_swap SERIAL PRIMARY KEY,
    id_item VARCHAR(255) NOT NULL,
    id_user_giver VARCHAR(255) NOT NULL,
    id_user_taker VARCHAR(255) NOT NULL,
    date_swap TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    item_metadata JSONB DEFAULT '{}'::jsonb NOT NULL
);

-- Create an index on id_swap since it's a primary key and marked with index=True
CREATE INDEX IF NOT EXISTS ix_swaps_id_swap ON swaps (id_swap);