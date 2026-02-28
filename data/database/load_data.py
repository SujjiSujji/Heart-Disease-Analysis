"""
Database utility script to load CSV data into MySQL
Handles data import with proper type conversion and validation
"""

import mysql.connector
import pandas as pd
import os
from configparser import ConfigParser

def load_config():
    """Load database configuration from config.ini"""
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    config.read(config_path)
    
    db_config = {
        'host': config.get('DATABASE', 'host'),
        'user': config.get('DATABASE', 'user'),
        'password': config.get('DATABASE', 'password'),
        'database': config.get('DATABASE', 'database'),
        'port': config.getint('DATABASE', 'port')
    }
    return db_config

def load_csv_to_mysql(csv_file_path):
    """Load CSV data into MySQL database"""
    
    print("=" * 60)
    print("Loading Heart Disease Data into MySQL")
    print("=" * 60)
    
    # Read CSV file
    print(f"\n1. Reading CSV file: {csv_file_path}")
    df = pd.read_csv(csv_file_path)
    print(f"   ✓ Loaded {len(df)} records")
    print(f"   ✓ Columns: {', '.join(df.columns.tolist())}")
    
    # Load database configuration
    print("\n2. Loading database configuration...")
    db_config = load_config()
    print(f"   ✓ Host: {db_config['host']}")
    print(f"   ✓ Database: {db_config['database']}")
    
    # Connect to MySQL
    print("\n3. Connecting to MySQL...")
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print("   ✓ Connected successfully")
    except Exception as e:
        print(f"   ✗ Connection failed: {e}")
        return False
    
    # Prepare column mapping (adjust based on actual CSV structure)
    # This is a generic implementation - adjust column names as needed
    print("\n4. Preparing data for insertion...")
    
    # Get insert query template based on CSV columns
    # You'll need to adjust this based on actual CSV structure
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    insert_query = f"INSERT INTO patient_data ({columns}) VALUES ({placeholders})"
    
    # Insert data in batches
    print("\n5. Inserting data into database...")
    batch_size = 1000
    total_inserted = 0
    
    try:
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            data = [tuple(row) for row in batch.values]
            cursor.executemany(insert_query, data)
            conn.commit()
            total_inserted += len(batch)
            print(f"   ✓ Inserted {total_inserted}/{len(df)} records", end='\r')
        
        print(f"\n   ✓ All {total_inserted} records inserted successfully")
        
        # Verify insertion
        cursor.execute("SELECT COUNT(*) FROM patient_data")
        count = cursor.fetchone()[0]
        print(f"\n6. Verification: {count} records in database")
        
        print("\n" + "=" * 60)
        print("✓ Data loading completed successfully!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n   ✗ Error inserting data: {e}")
        conn.rollback()
        return False
        
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Path to CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'heart_disease_data.csv')
    
    if not os.path.exists(csv_path):
        print(f"✗ CSV file not found: {csv_path}")
        print("Please run data/download_dataset.py first")
        exit(1)
    
    load_csv_to_mysql(csv_path)
