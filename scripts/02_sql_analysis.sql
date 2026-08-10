-- Query 1: Top 5 neighborhoods with the highest concentration of top-rated Tandoori & Biryani spots
SELECT 
    location, 
    COUNT(*) as restaurant_count,
    ROUND(AVG(rate), 2) as avg_rating
FROM bangalore_restaurants
WHERE is_tandoori_biryani = TRUE AND rate >= 4.0
GROUP BY location
ORDER BY restaurant_count DESC
LIMIT 5;

-- Query 2: Analyzing the "Dessert Premium"
-- Does serving late-night desserts correlate with higher overall ratings and order volumes (votes)?
SELECT 
    is_dessert_bakery,
    COUNT(*) as total_restaurants,
    ROUND(AVG(rate), 2) as average_rating,
    ROUND(AVG(votes), 0) as average_votes
FROM bangalore_restaurants
GROUP BY is_dessert_bakery;

-- Query 3: Identifying Cloud Kitchen expansion opportunities
-- Find areas with high average cost and high votes, but low density of restaurants
WITH location_metrics AS (
    SELECT 
        location,
        COUNT(*) as total_restaurants,
        AVG(cost_for_two) as avg_cost,
        SUM(votes) as total_demand
    FROM bangalore_restaurants
    GROUP BY location
)
SELECT 
    location, 
    total_restaurants, 
    ROUND(avg_cost, 0) as avg_cost, 
    total_demand
FROM location_metrics
WHERE total_restaurants < 200 AND avg_cost > 500
ORDER BY total_demand DESC;
