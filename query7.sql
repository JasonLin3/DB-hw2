SELECT COUNT(DISTINCT Category.category)
FROM Category, Item
WHERE Category.item_id = Item.item_id
AND Item.currently > 100
AND Item.num_bids > 0;
