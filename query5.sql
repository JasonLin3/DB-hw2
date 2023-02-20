SELECT COUNT(DISTINCT User.user_id)
FROM User, Item
WHERE Item.seller_id = User.user_id
AND User.rating > 1000;
