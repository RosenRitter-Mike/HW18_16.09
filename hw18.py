'''

Questions:

a. Done

b.
Product -> Category (One to Many)
Product -> Nutritions (One to One)
Products_Orders -> Orders (Many to Many)
Products_Orders -> Products (Many to Many)

c.
Done

d.
i.
SELECT pr.name, cat.name category, nut.calories, nut.fats, nut.sugar
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)

ii.
SELECT po.order_id, pr.name, cat.name category, nut.calories, nut.fats, nut.sugar
FROM orders ord
JOIN products_orders po USING(order_id)
JOIN products pr USING(product_id)
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)

iii.
INSERT INTO products_orders (order_id, product_id, amount) VALUES
(1, 15, 1),  -- Cookies
(2, 24, 1),  -- Pineapple
(3, 25, 3),  -- Strawberries
(4, 25, 5),  -- Strawberries
(5, 7, 1);   -- Pepsi

iv.
UPDATE products SET price = price + 0.5;

v.
MIN(total_price), AVG(total_price), MAX(total_price) from orders

vi.
SELECT o.customer_name
FROM orders o
WHERE order_id = (
    SELECT order_id
    FROM (SELECT order_id, COUNT(*) cnt
            FROM orders ord
            JOIN products_orders po USING(order_id)
            group by order_id
            ORDER by cnt DESC
            LIMIT 1)
);

vii.
------------ max buy product ---------
SELECT name
from products p
where product_id = (SELECT product_id from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)
WHERE amnt = (SELECT MAX(amnt) from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)))
------------ min buy product ---------
SELECT name
from products p
where product_id = (SELECT product_id from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)
WHERE amnt = (SELECT MIN(amnt) from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)))
------------ avg buy product ---------
SELECT name
from products p
where product_id = (SELECT product_id from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)
WHERE amnt = (SELECT ROUND(AVG(amnt)) from (
SELECT po.product_id, SUM(po.amount) amnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
group by po.product_id
ORDER by amnt desc)))

viii.
------- max by category -------------
SELECT categ
FROM (
SELECT categ, COUNT(*) cat_cnt
FROM (SELECT po.product_id, pr.name, pr.price, cat.name categ, nut.calories, nut.fats, nut.sugar
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po USING(product_id)
JOIN orders o USING(order_id)
)
GROUP BY categ)
WHERE cat_cnt = (SELECT MAX(cat_cnt)
FROM (
SELECT categ, COUNT(*) cat_cnt
FROM (SELECT po.product_id, pr.name, pr.price, cat.name categ, nut.calories, nut.fats, nut.sugar
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po USING(product_id)
JOIN orders o USING(order_id)
)
GROUP BY categ))

-------- min by category ------------------
SELECT categ
FROM (
SELECT categ, COUNT(*) cat_cnt
FROM (SELECT po.product_id, pr.name, pr.price, cat.name categ, nut.calories, nut.fats, nut.sugar
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po USING(product_id)
JOIN orders o USING(order_id)
)
GROUP BY categ)
WHERE cat_cnt = (SELECT MIN(cat_cnt)
FROM (
SELECT categ, COUNT(*) cat_cnt
FROM (SELECT po.product_id, pr.name, pr.price, cat.name categ, nut.calories, nut.fats, nut.sugar
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po USING(product_id)
JOIN orders o USING(order_id)
)
GROUP BY categ))

ix.
SELECT name
FROM (SELECT pr.name, COUNT(*) cnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
GROUP BY pr.name
ORDER BY cnt DESC)
WHERE cnt = (SELECT MAX(cnt) max_cnt
FROM (SELECT pr.name, COUNT(*) cnt
FROM products pr
JOIN category cat USING(category_id)
JOIN nutritions nut USING(product_id)
JOIN products_orders po using(product_id)
JOIN orders o USING(order_id)
GROUP BY pr.name
ORDER BY cnt DESC));

'''

