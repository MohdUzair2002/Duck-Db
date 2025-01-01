SELECT
    "Order ID"::INTEGER AS order_id,
    Product AS product,
    "Quantity Ordered"::INTEGER AS quantity,
    "Price"::DECIMAL AS price_each,
    -- Try parsing the date and return NULL if the date is invalid
    CASE
        WHEN TRY_CAST(STRPTIME("Order Date", '%d-%m-%Y') AS DATE) IS NULL THEN 'Invalid Date'
        ELSE STRPTIME("Order Date", '%d-%m-%Y')
    END AS order_date,
    "Purchase Address" AS purchase_address
FROM {{ ref('Sales_Product_Combined') }}
WHERE
    TRY_CAST("Order ID" AS INTEGER) IS NOT NULL
