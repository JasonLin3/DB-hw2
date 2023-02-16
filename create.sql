drop table if exists Item;
drop table if exists User;
drop table if exists Bid;
drop table if exists Category;

create table Item(id, seller_id, name, currently, buy_price, started, ends, first_bid, num_bids, description);
create table User(id, rating, location, country);
create table Bid(bidder_id, item_id, time, amount);
create table Category(category, item_id);
