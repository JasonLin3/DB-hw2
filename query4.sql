SELECT Item.item_id
FROM Item
WHERE Item.currently = (SELECT MAX(Item.currently)
			FROM Item);
