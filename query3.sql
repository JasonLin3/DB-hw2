SELECT COUNT(*)
FROM (SELECT COUNT(*) AS 'CategoryCount'
      FROM Category, Item
      WHERE Category.item_id = Item.item_id
      GROUP BY Item.item_id) grouped
WHERE grouped.CategoryCount = 4;
