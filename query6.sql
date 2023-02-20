SELECT COUNT(DISTINCT Item.seller_id)
FROM Item, Bid
WHERE Item.seller_id = Bid.user_id;
