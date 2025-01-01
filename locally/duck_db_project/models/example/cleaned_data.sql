WITH raw_data AS (
    SELECT * 
    FROM {{ ref('Sales_Product_Combined') }}  -- Reference the seed file
)


SELECT
    "Order ID",
    Product,
    "Quantity Ordered",
     "Price",  -- Remove commas and convert to DECIMAL
    "Order Date",
    "Purchase Address"
FROM raw_data
WHERE "Price" IS NOT NULL
