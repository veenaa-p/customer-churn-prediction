
/*
Customer Churn SQL Analysis

Dataset: Telco Customer Churn
Table Name: customers

The following queries analyze churn trends,
contract types, tenure, monthly charges,
and payment methods.
*/

-- 1. Overall churn rate
SELECT Churn, COUNT(*) as total, 
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2) AS percentage
FROM customers
GROUP BY Churn;

-- 2. Churn by contract type
SELECT Contract, Churn, COUNT(*) as total
FROM customers
GROUP BY Contract, Churn
ORDER BY Contract;

-- 3. Average monthly charges by churn
SELECT Churn, ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM customers
GROUP BY Churn;

-- 4. Churn by tenure group
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-1 Year'
        WHEN tenure <= 24 THEN '1-2 Years'
        WHEN tenure <= 48 THEN '2-4 Years'
        ELSE '4+ Years'
    END AS tenure_group,
    Churn,
    COUNT(*) AS total
FROM customers
GROUP BY tenure_group, Churn
ORDER BY tenure_group;

-- 5. Top payment methods among churned customers
SELECT PaymentMethod, COUNT(*) as churned_count
FROM customers
WHERE Churn = 'Yes'
GROUP BY PaymentMethod
ORDER BY churned_count DESC;