INSERT INTO `address` (`street`, `building_number`)
VALUES
('Chuprynky', '12'),
('Konovaltsia', '45'),
('Sakharova', '67'),
('Kulparkivska', '23'),
('Pivnichna', '8'),
('Heroiv UPA', '91'),
('Antonovycha', '14'),
('Povstanska', '33'),
('Hordynskykh', '59'),
('Kyivska', '77');

INSERT INTO `kindergarten` (`number`, `adress_id`)
VALUES
('101', 1),
('102', 2),
('103', 3),
('104', 4),
('105', 5),
('106', 6),
('107', 7),
('108', 8),
('109', 9),
('110', 10);

INSERT INTO `salary` (`amount`, `experience`)
VALUES
(30000, '2 years'),
(32000, '3 years'),
(35000, '4 years'),
(37000, '5 years'),
(39000, '6 years'),
(40000, '7 years'),
(42000, '8 years'),
(45000, '9 years'),
(47000, '10 years'),
(50000, '12 years');

INSERT INTO `dismissal` (`date`, `reason`)
VALUES
('2023-05-12', 'Dismissal'),
('2022-10-23', 'Health'),
('2021-09-10', 'Career change'),
('2020-12-05', 'Personal reasons'),
('2019-11-18', 'Relocation'),
('2023-07-01', 'Dismissal'),
('2022-04-22', 'Another job'),
('2021-08-13', 'Family reasons'),
('2020-01-15', 'Dismissal'),
('2019-03-30', 'Job change');

INSERT INTO `educator` (`name`, `surname`, `kindergarten_id`, `hire`, `salary_id`, `dismissal_id`)
VALUES
('Anna', 'Koval', 1, '2018-04-10', 1, NULL),
('Ivan', 'Dovzhenko', 2, '2019-09-15', 2, 1),
('Maria', 'Hardash', 3, '2020-01-20', 3, NULL),
('Dmytro', 'Lisovyi', 4, '2016-06-30', 4, 2),
('Olena', 'Bondar', 5, '2017-11-25', 5, NULL),
('Sofia', 'Martyniuk', 6, '2018-03-18', 6, 3),
('Olha', 'Honcharenko', 7, '2019-02-12', 7, NULL),
('Oleksii', 'Volkov', 8, '2020-05-28', 8, NULL),
('Maksym', 'Kovtun', 9, '2021-09-14', 9, NULL),
('Mykhailo', 'Shevchenko', 10, '2022-07-19', 10, 4);

INSERT INTO `group` (`name`, `amount`, `educators_id`, `kindergarten_id`)
VALUES
('Stars', '20', 1, 1),
('Sunshine', '18', 2, 2),
('Rainbow', '22', 3, 3),
('Butterflies', '19', 4, 4),
('Bunnies', '21', 5, 5),
('Lions', '25', 6, 6),
('Bears', '23', 7, 7),
('Tigers', '20', 8, 8),
('Penguins', '24', 9, 9),
('Seagulls', '22', 10, 10);

INSERT INTO `child` (`name`, `age`, `group_id`, `kindergarten_id`)
VALUES
('Lev', 5, 1, 1),
('Nazar', 6, 2, 2),
('Oleksandra', 5, 3, 3),
('Emma', 4, 4, 4),
('Alina', 6, 5, 5),
('Sofia', 5, 6, 6),
('Izabella', 4, 7, 7),
('Mia', 5, 8, 8),
('Alina', 4, 9, 9),
('Hanna', 6, 10, 10);

INSERT INTO `toy` (`name`, `number`, `group_id`, `group_educators_id`, `group_kindergarten_id`)
VALUES
('Ball', '15', 1, 1, 1),
('Doll', '12', 2, 2, 2),
('Puzzle', '10', 3, 3, 3),
('Car', '20', 4, 4, 4),
('Blocks', '30', 5, 5, 5),
('Teddy Bear', '10', 6, 6, 6),
('Train', '15', 7, 7, 7),
('Truck', '8', 8, 8, 8),
('Robot', '5', 9, 9, 9),
('Lego', '25', 10, 10, 10);

INSERT INTO `event` (`name`, `date`, `educators_id`, `educators_kindergarten_id`)
VALUES
('Christmas Party', '2023-12-25', 1, 1),
('Graduation', '2023-06-15', 2, 2),
('Sports Day', '2023-08-20', 3, 3),
('Parents Day', '2023-05-12', 4, 4),
('Talent Show', '2023-10-01', 5, 5),
('Spring Picnic', '2023-04-15', 6, 6),
('Science Fair', '2023-09-23', 7, 7),
('Book Week', '2023-11-10', 8, 8),
('Art Exhibition', '2023-07-05', 9, 9),
('Music Day', '2023-03-22', 10, 10);

INSERT INTO `award` (`name`, `money`)
VALUES
('Best Teacher', 1000),
('Excellence in Education', 2000),
('Innovation Award', 1500),
('Leadership Award', 2500),
('Teamwork Award', 1200),
('Community Impact', 1800),
('Service Award', 2200),
('Creativity Award', 1600),
('Mentorship Award', 1900),
('Dedication Award', 2100);

INSERT INTO `educator_has_awards` (`educators_id`, `educators_kindergarten_id`, `awards_id`)
VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);
