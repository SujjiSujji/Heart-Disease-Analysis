-- Heart Disease Analysis Database Schema
-- Creates the database and table structure for heart disease patient data

DROP DATABASE IF EXISTS heart_disease_db;
CREATE DATABASE heart_disease_db;
USE heart_disease_db;

-- Main patient data table
CREATE TABLE patient_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Demographics
    age INT,
    gender VARCHAR(10),
    race VARCHAR(50),
    
    -- Physical Metrics
    bmi DECIMAL(5,2),
    height_cm DECIMAL(6,2),
    weight_kg DECIMAL(6,2),
    
    -- Health Metrics
    cholesterol INT,
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    
    -- Medical Conditions (Binary: 0=No, 1=Yes)
    heart_disease TINYINT,
    diabetes TINYINT,
    stroke TINYINT,
    kidney_disease TINYINT,
    skin_cancer TINYINT,
    other_cancer TINYINT,
    copd TINYINT,
    arthritis TINYINT,
    depression TINYINT,
    
    -- Lifestyle Factors (Binary: 0=No, 1=Yes)
    smoking TINYINT,
    alcohol_drinking TINYINT,
    physical_activity TINYINT,
    
    -- Health Status
    general_health VARCHAR(20),
    mental_health_days INT,
    physical_health_days INT,
    difficulty_walking TINYINT,
    
    -- Sleep
    sleep_hours DECIMAL(4,2),
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Indexes for performance
    INDEX idx_heart_disease (heart_disease),
    INDEX idx_age (age),
    INDEX idx_gender (gender),
    INDEX idx_race (race),
    INDEX idx_diabetes (diabetes),
    INDEX idx_stroke (stroke),
    INDEX idx_smoking (smoking),
    INDEX idx_physical_activity (physical_activity),
    INDEX idx_general_health (general_health)
);

-- Create a view for quick statistics
CREATE VIEW heart_disease_stats AS
SELECT 
    COUNT(*) as total_patients,
    SUM(heart_disease) as heart_disease_count,
    SUM(diabetes) as diabetes_count,
    SUM(stroke) as stroke_count,
    ROUND(AVG(age), 2) as avg_age,
    ROUND(AVG(bmi), 2) as avg_bmi
FROM patient_data;

-- Display schema info
SHOW TABLES;
DESCRIBE patient_data;

SELECT 'Database schema created successfully!' as Status;
