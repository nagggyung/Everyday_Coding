-- SELECT TRUNCATE(134566, -4);
-- result : 130000
-- Truncate(number, range to be truncated): Return a number truncated to 2 decimal places


-- 처음 보는 풀이

SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY TRUNCATE(PRICE, -4)
ORDER BY PRICE_GROUP ASC;

