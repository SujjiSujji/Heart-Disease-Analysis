-- Sample SQL Queries for Heart Disease Analysis
-- These queries demonstrate data exploration and analytics

USE heart_disease_db;

-- 1. Overall statistics
SELECT * FROM heart_disease_stats;

-- 2. Gender-wise heart disease distribution
SELECT 
    gender,
    COUNT(*) as total_patients,
    SUM(heart_disease) as has_heart_disease,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as percentage
FROM patient_data
GROUP BY gender
ORDER BY percentage DESC;

-- 3. Age group analysis
SELECT 
    CASE 
        WHEN age < 30 THEN '18-29'
        WHEN age < 40 THEN '30-39'
        WHEN age < 50 THEN '40-49'
        WHEN age < 60 THEN '50-59'
        WHEN age < 70 THEN '60-69'
        ELSE '70+'
    END as age_group,
    COUNT(*) as total,
    SUM(heart_disease) as heart_disease_cases,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as percentage
FROM patient_data
GROUP BY age_group
ORDER BY age_group;

-- 4. Diabetes and Stroke correlation
SELECT 
    diabetes,
    stroke,
    COUNT(*) as patient_count
FROM patient_data
GROUP BY diabetes, stroke
ORDER BY diabetes, stroke;

-- 5. Impact of smoking and alcohol
SELECT 
    smoking,
    alcohol_drinking,
    COUNT(*) as total,
    SUM(heart_disease) as heart_disease_count,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as heart_disease_pct
FROM patient_data
GROUP BY smoking, alcohol_drinking
ORDER BY heart_disease_pct DESC;

-- 6. Race-wise distribution
SELECT 
    race,
    COUNT(*) as total_patients,
    SUM(heart_disease) as heart_disease_cases,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as percentage
FROM patient_data
GROUP BY race
ORDER BY percentage DESC;

-- 7. General health vs heart disease
SELECT 
    general_health,
    COUNT(*) as total,
    SUM(heart_disease) as cases,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as percentage
FROM patient_data
GROUP BY general_health
ORDER BY FIELD(general_health, 'Excellent', 'Very good', 'Good', 'Fair', 'Poor');

-- 8. Physical activity impact
SELECT 
    physical_activity,
    COUNT(*) as total,
    SUM(heart_disease) as heart_disease_cases,
    ROUND(SUM(heart_disease) * 100.0 / COUNT(*), 2) as percentage
FROM patient_data
GROUP BY physical_activity;

-- 9. BMI categories vs diabetes
SELECT 
    CASE 
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi < 25 THEN 'Normal'
        WHEN bmi < 30 THEN 'Overweight'
        ELSE 'Obese'
    END as bmi_category,
    ROUND(AVG(age), 1) as avg_age,
    COUNT(*) as total,
    SUM(diabetes) as diabetes_cases,
    ROUND(SUM(diabetes) * 100.0 / COUNT(*), 2) as diabetes_pct
FROM patient_data
WHERE bmi IS NOT NULL
GROUP BY bmi_category
ORDER BY FIELD(bmi_category, 'Underweight', 'Normal', 'Overweight', 'Obese');

-- 10. Triple condition (stroke + heart disease + diabetes)
SELECT 
    COUNT(*) as total_with_all_three
FROM patient_data
WHERE stroke = 1 AND heart_disease = 1 AND diabetes = 1;

SELECT 
    stroke,
    heart_disease,
    diabetes,
    COUNT(*) as patient_count
FROM patient_data
GROUP BY stroke, heart_disease, diabetes
ORDER BY patient_count DESC;

-- Performance optimization queries
-- Count records
SELECT COUNT(*) as total_records FROM patient_data;

-- Check for null values
SELECT 
    SUM(CASE WHEN age IS NULL THEN 1 ELSE 0 END) as null_age,
    SUM(CASE WHEN gender IS NULL THEN 1 ELSE 0 END) as null_gender,
    SUM(CASE WHEN bmi IS NULL THEN 1 ELSE 0 END) as null_bmi,
    SUM(CASE WHEN heart_disease IS NULL THEN 1 ELSE 0 END) as null_heart_disease
FROM patient_data;
