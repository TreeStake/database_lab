USE kinderdb;

DROP TRIGGER IF EXISTS prevent_toy_update;
DROP TRIGGER IF EXISTS prevent_toy_delete;
DROP TRIGGER IF EXISTS validate_child_name;

DELIMITER //
CREATE TRIGGER prevent_toy_update
BEFORE UPDATE ON toy
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Оновлення даних у таблиці toy заборонено.';
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER prevent_toy_delete
BEFORE DELETE ON toy
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Видалення рядків з таблиці toy заборонено.';
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER validate_child_name
BEFORE INSERT ON child
FOR EACH ROW
BEGIN
    IF NEW.name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Недопустиме ім`я. Дозволені лише: Svitlana, Petro, Olha, Taras.';
    END IF;
END;
//
DELIMITER ;