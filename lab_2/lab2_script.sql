CREATE TABLE IF NOT EXISTS Contractor
(
    id        INTEGER PRIMARY KEY,
    name      TEXT,
    group_id  INTEGER,
    region_id INTEGER,
    UNN       TEXT,
    address   TEXT,
    FOREIGN KEY (group_id) REFERENCES 'Group' (id),
    FOREIGN KEY (region_id) REFERENCES Region (id)
);
CREATE TABLE IF NOT EXISTS Affiliate
(
    id            INTEGER PRIMARY KEY,
    contractor_id INTEGER,
    name          TEXT,
    address       TEXT,
    FOREIGN KEY (contractor_id) REFERENCES Contractor (id)
);
CREATE TABLE IF NOT EXISTS Region
(
    id   INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS 'Group'
(
    id   INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS Account
(
    id            INTEGER PRIMARY KEY,
    contractor_id INTEGER,
    bank          TEXT,
    account       TEXT,
    currency      TEXT,
    FOREIGN KEY (contractor_id) REFERENCES Contractor (id)
);
INSERT INTO `Group` (id, name)
VALUES (1, 'Торговые предприятия'),
       (2, 'Производственные предприятия'),
       (3, 'Компании, работающие в сфере услуг');
-- Заполнение справочника регионов
INSERT INTO Region (id, name)
VALUES (1, 'Минск'),
       (2, 'Брест'),
       (3, 'Витебск'),
       (4, 'Гомель'),
       (5, 'Гродно'),
       (6, 'Могилев');
-- Заполнение таблицы подрядчиков
INSERT INTO Contractor (id, name, group_id, region_id, unn, address)
VALUES (1, 'ОАО "Беларуськалий"', 2, 4, '111111111', 'ул. Ленина, 3'),
       (2, 'ООО "Атлант-М"', 1, 1, '123456789', 'ул. Космонавтов, 1'),
       (3, 'ООО "ТиссенКрупп Беларусь"', 2, 1, '987654321', 'ул. Ленина, 2'),
       (4, 'ОАО "Нафтан"', 2, 2, '222222222', 'ул. Космонавтов, 4');
INSERT INTO Affiliate (id, contractor_id, name, address)
VALUES (1, 1, 'Завод "Белкалий-1"', 'ул. Ленина, 5'),
       (2, 1, 'Завод "Белкалий-2"', 'ул. Ленина, 6'),
       (3, 2, 'Магазин "Атлант-М"', 'ул. Космонавтов, 2'),
       (4, 2, 'Магазин "Молоко и мед"', 'ул. Космонавтов, 3'),
       (5, 3, 'Завод "ТиссенКрупп"', 'ул. Ленина, 4');
INSERT INTO Account (id, contractor_id, bank, account, currency)
VALUES (1, 1, 'Белгазпромбанк', '12345678910111213141', 'BYN'),
       (2, 1, 'Белгазпромбанк', '98765432109876543210', 'USD'),
       (3, 2, 'Беларусбанк', '11111111111111111111', 'BYN'),
       (4, 3, 'Беларусбанк', '22222222222222222222', 'USD'),
       (5, 4, 'Приорбанк', '33333333333333333333', 'BYN');