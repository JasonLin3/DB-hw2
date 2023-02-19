drop table if exists Item;
drop table if exists User;
drop table if exists Bid;
drop table if exists Category;

create table Item(item_id int, 
                seller_id varchar(255), 
                name varchar(255), 
                currently real, 
                buy_price real, 
                started date, 
                ends date, 
                first_bid real, 
                num_bids int, 
                description text,
                PRIMARY KEY(item_id),
                FOREIGN KEY (seller_id) REFERENCES User(user_id));

create table User(user_id int, 
                rating int, 
                location varchar(255), 
                country varchar(255),
                PRIMARY KEY(user_id));

create table Bid(user_id varchar(255), 
                item_id int, 
                time date, 
                amount real,
                PRIMARY KEY (user_id, item_id, time),
                FOREIGN KEY (user_id) REFERENCES User(user_id),
                FOREIGN KEY (item_id) REFERENCES Item(item_id));

create table Category(category varchar(255), 
                item_id int,
                PRIMARY KEY(category, item_id),
                FOREIGN KEY (item_id) REFERENCES Item(item_id));
