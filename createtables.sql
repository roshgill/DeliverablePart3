CREATE TABLE Customer (
    customer_id CHAR(32) NOT NULL,
    customer_zip_code_prefix CHAR(5) NOT NULL,
    customer_city VARCHAR(255) NOT NULL,
    customer_state CHAR(2) NOT NULL,
    
    PRIMARY KEY (customer_id),
);


CREATE Table Seller(
	seller_id CHAR(32) NOT NULL,		   
	seller_zip_code_prefix CHAR(5) NOT NULL,
	seller_city VARCHAR(255) NOT NULL,
	seller_state  CHAR(2) NOT NULL,
	
	PRIMARY KEY(seller_id),
);


CREATE Table ProductCategory(
	product_category_name  VARCHAR(255) NOT NULL,		   
	product_category_name_english  VARCHAR(255) NOT NULL,

	PRIMARY KEY(product_category_name)
);


CREATE Table Orders(
	order_id  CHAR(32) NOT NULL,		   
	customer_id CHAR(32) NOT NULL,
	order_status VARCHAR(255),
	order_purchase_timestamp TIMESTAMP NOT NULL,
	order_approved_at TIMESTAMP,
	order_delivered_carrier_date  TIMESTAMP,
	order_delivered_customer_date  TIMESTAMP, 
        order_estimated_delivery_date  TIMESTAMP NOT NULL,

	PRIMARY KEY(order_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);


CREATE TABLE Payment (
    order_id CHAR(32) NOT NULL,
    payment_sequential INTEGER NOT NULL CHECK(payment_sequential > 0),
    payment_type VARCHAR(255) NOT NULL,
    payment_installments INTEGER NOT NULL CHECK(payment_installments >= 0),
    payment_value DECIMAL(15,2) NOT NULL,
    
    PRIMARY KEY (order_id, payment_sequential, payment_type)
);


CREATE TABLE Review (
    review_id CHAR(32) NOT NULL,
    order_id CHAR(32) NOT NULL,
    review_score INTEGER NOT NULL CHECK (review_score >= 1 AND review_score <= 5),
    review_comment_title VARCHAR(255),
    review_comment_message VARCHAR(255),
    review_creation_date TIMESTAMP NOT NULL,
    review_answer_timestamp TIMESTAMP NOT NULL,

    PRIMARY KEY(review_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);


CREATE TABLE Product (
    product_id CHAR(32) NOT NULL,
    product_category_name VARCHAR(255),
    product_name_length INTEGER CHECK (product_name_length > 0),
    product_description_length INTEGER CHECK (product_description_length > 0),
    product_photos_qty INTEGER CHECK (product_photos_qty >= 0),
    product_weight_g INTEGER CHECK (product_weight_g >= 0),
    product_length_cm INTEGER CHECK (product_length_cm >= 0),
    product_height_cm INTEGER CHECK (product_height_cm >= 0),
    product_width_cm INTEGER CHECK (product_width_cm >= 0),

    PRIMARY KEY(product_id),
    FOREIGN KEY (product_category_name) REFERENCES ProductCategory(product_category_name)
);