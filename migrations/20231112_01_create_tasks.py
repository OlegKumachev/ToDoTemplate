from yoyo import step

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            due_date DATE,
            is_completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """,
        """
        DROP TABLE IF EXISTS tasks CASCADE;
        """
    )
]
