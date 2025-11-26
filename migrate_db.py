"""
database migration script to add new columns to existing expenses table.
This script handles both fresh installations and migrations from existing databases.
"""

import sqlite3
import os
from repository import DB_NAME


def check_table_schema():
    """Check the current schema of the expenses table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("PRAGMA table_info(expenses)")
        columns = [column[1] for column in cursor.fetchall()]
        conn.close()
        return columns
    except sqlite3.Error as e:
        conn.close()
        print(f"Error checking schema: {e}")
        return []


def migrate_database():
    """Add user_comments and tags columns to existing expenses table."""
    print("🔧 Starting database migration...")

    # Check if database exists
    if not os.path.exists(DB_NAME):
        print(f"📁 Database {DB_NAME} does not exist. Creating new database...")
        return

    # Check current schema
    current_columns = check_table_schema()
    print(f"📋 Current columns: {current_columns}")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        migration_needed = False

        # Check and add user_comments column
        if 'user_comments' not in current_columns:
            print("➕ Adding user_comments column...")
            cursor.execute("ALTER TABLE expenses ADD COLUMN user_comments TEXT")
            migration_needed = True
            print("✅ user_comments column added")
        else:
            print("✅ user_comments column already exists")

        # Check and add tags column
        if 'tags' not in current_columns:
            print("➕ Adding tags column...")
            cursor.execute("ALTER TABLE expenses ADD COLUMN tags TEXT")
            migration_needed = True
            print("✅ tags column added")
        else:
            print("✅ tags column already exists")

        if migration_needed:
            conn.commit()
            print("🎉 Database migration completed successfully!")
        else:
            print("✅ Database is already up to date")

        # Verify the migration
        final_columns = check_table_schema()
        print(f"📋 Final schema: {final_columns}")

        if 'user_comments' in final_columns and 'tags' in final_columns:
            print("✅ Migration verification successful")
            return True
        else:
            print("❌ Migration verification failed")
            return False

    except sqlite3.Error as e:
        print(f"❌ Migration error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


def create_fresh_database():
    """Create a fresh database with the complete schema."""
    print("🆕 Creating fresh database with enhanced schema...")

    # Remove existing database if it exists
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"🗑️  Removed existing {DB_NAME}")

    # Import and create fresh repository
    from repository import ExpenseRepository
    repo = ExpenseRepository()

    # Verify the schema
    columns = check_table_schema()
    print(f"📋 New database schema: {columns}")

    if 'user_comments' in columns and 'tags' in columns:
        print("✅ Fresh database created successfully!")
        return True
    else:
        print("❌ Fresh database creation failed!")
        return False


def main():
    """Main migration function with options."""
    print("🚀 Expense Tracker Database Migration Tool")
    print("=" * 50)

    if os.path.exists(DB_NAME):
        print(f"📁 Found existing database: {DB_NAME}")

        choice = input(
            "Choose an option:\n1. Migrate existing database\n2. Create fresh database\n3. Exit\nEnter choice (1-3): ")

        if choice == "1":
            success = migrate_database()
        elif choice == "2":
            success = create_fresh_database()
        else:
            print("👋 Exiting migration tool")
            return
    else:
        print(f"📁 No existing database found. Creating fresh {DB_NAME}...")
        success = create_fresh_database()

    if success:
        print("\n🎉 Migration completed successfully!")
        print("💡 You can now run the application with: python main.py")
    else:
        print("\n❌ Migration failed!")
        print("💡 Please check the error messages above and try again")


if __name__ == "__main__":
    main()