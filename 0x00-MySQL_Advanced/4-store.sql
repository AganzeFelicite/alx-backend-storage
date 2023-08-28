-- Creating a trigger that decreases the quantity on each insert
CREATE TRIGGER decrease_quantity 
AFTER INSERT  ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
