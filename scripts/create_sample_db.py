import sqlite3
import os

def create_sample_database():
    """Create a sample database with some tables and data"""
    
    # Create database directory if it doesn't exist
    os.makedirs('../database', exist_ok=True)
    
    # Create database connection
    conn = sqlite3.connect('../database/sample.db')
    cursor = conn.cursor()
    
    # Create customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        city TEXT,
        country TEXT,
        created_date DATE
    )
    ''')
    
    # Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        category TEXT,
        price DECIMAL(10,2),
        cost DECIMAL(10,2),
        stock_quantity INTEGER,
        supplier_id INTEGER
    )
    ''')
    
    # Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date DATE,
        total_amount DECIMAL(10,2),
        status TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')
    
    # Create order_items table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price DECIMAL(10,2),
        FOREIGN KEY (order_id) REFERENCES orders (order_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')
    
    # Create categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL,
        description TEXT,
        parent_category_id INTEGER,
        FOREIGN KEY (parent_category_id) REFERENCES categories (category_id)
    )
    ''')
    
    # Create suppliers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL,
        contact_person TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        city TEXT,
        country TEXT
    )
    ''')
    
    # Create reviews table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        customer_id INTEGER,
        rating INTEGER CHECK(rating >= 1 AND rating <= 5),
        review_text TEXT,
        review_date DATE,
        FOREIGN KEY (product_id) REFERENCES products (product_id),
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')
    
    # Create shipping_addresses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS shipping_addresses (
        address_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        address_line1 TEXT NOT NULL,
        address_line2 TEXT,
        city TEXT NOT NULL,
        state TEXT,
        postal_code TEXT,
        country TEXT NOT NULL,
        is_default BOOLEAN DEFAULT 0,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')
    
    # Create payments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        payment_method TEXT,
        amount DECIMAL(10,2),
        payment_date DATETIME,
        status TEXT,
        transaction_id TEXT,
        FOREIGN KEY (order_id) REFERENCES orders (order_id)
    )
    ''')
    
    # Create inventory table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        warehouse_location TEXT,
        quantity_available INTEGER,
        quantity_reserved INTEGER,
        reorder_level INTEGER,
        last_updated DATETIME,
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')
    
    # Create discounts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS discounts (
        discount_id INTEGER PRIMARY KEY,
        discount_code TEXT UNIQUE,
        discount_type TEXT, -- 'percentage' or 'fixed'
        discount_value DECIMAL(10,2),
        minimum_order_amount DECIMAL(10,2),
        start_date DATE,
        end_date DATE,
        is_active BOOLEAN DEFAULT 1,
        usage_limit INTEGER,
        usage_count INTEGER DEFAULT 0
    )
    ''')
    
    # Insert sample data
    customers_data = [
        (1, 'John', 'Doe', 'john.doe@email.com', 'New York', 'USA', '2023-01-15'),
        (2, 'Jane', 'Smith', 'jane.smith@email.com', 'London', 'UK', '2023-02-20'),
        (3, 'Carlos', 'Rodriguez', 'carlos.r@email.com', 'Madrid', 'Spain', '2023-03-10'),
        (4, 'Emily', 'Johnson', 'emily.j@email.com', 'Toronto', 'Canada', '2023-04-05'),
        (5, 'Michael', 'Brown', 'michael.b@email.com', 'Sydney', 'Australia', '2023-05-12')
    ]
    
    products_data = [
        (1, 'Laptop Pro', 'Electronics', 1299.99, 899.99, 50, 101),
        (2, 'Smartphone X', 'Electronics', 699.99, 489.99, 120, 102),
        (3, 'Coffee Maker', 'Appliances', 89.99, 62.99, 75, 103),
        (4, 'Running Shoes', 'Sports', 129.99, 89.99, 200, 104),
        (5, 'Office Chair', 'Furniture', 249.99, 174.99, 30, 105),
        (6, 'Wireless Mouse', 'Electronics', 29.99, 19.99, 150, 101),
        (7, 'Water Bottle', 'Sports', 19.99, 12.99, 300, 104)
    ]
    
    orders_data = [
        (1, 1, '2023-06-01', 1329.98, 'Completed'),
        (2, 2, '2023-06-02', 729.98, 'Completed'),
        (3, 3, '2023-06-03', 159.98, 'Pending'),
        (4, 1, '2023-06-04', 279.98, 'Completed'),
        (5, 4, '2023-06-05', 89.99, 'Shipped'),
        (6, 5, '2023-06-06', 149.98, 'Completed')
    ]
    
    order_items_data = [
        (1, 1, 1, 1, 1299.99),  # Order 1: Laptop Pro
        (2, 1, 6, 1, 29.99),    # Order 1: Wireless Mouse
        (3, 2, 2, 1, 699.99),   # Order 2: Smartphone X
        (4, 2, 6, 1, 29.99),    # Order 2: Wireless Mouse
        (5, 3, 4, 1, 129.99),   # Order 3: Running Shoes
        (6, 3, 6, 1, 29.99),    # Order 3: Wireless Mouse
        (7, 4, 5, 1, 249.99),   # Order 4: Office Chair
        (8, 4, 6, 1, 29.99),    # Order 4: Wireless Mouse
        (9, 5, 3, 1, 89.99),    # Order 5: Coffee Maker
        (10, 6, 4, 1, 129.99),  # Order 6: Running Shoes
        (11, 6, 7, 1, 19.99)    # Order 6: Water Bottle
    ]
    
    # Categories data
    categories_data = [
        (1, 'Electronics', 'Electronic devices and gadgets', None),
        (2, 'Computers', 'Computer hardware and accessories', 1),
        (3, 'Mobile Devices', 'Smartphones and tablets', 1),
        (4, 'Home & Kitchen', 'Home and kitchen appliances', None),
        (5, 'Appliances', 'Kitchen and home appliances', 4),
        (6, 'Sports & Outdoors', 'Sports equipment and outdoor gear', None),
        (7, 'Footwear', 'Sports and casual shoes', 6),
        (8, 'Furniture', 'Home and office furniture', None),
        (9, 'Office Furniture', 'Desks, chairs, and office equipment', 8)
    ]
    
    # Suppliers data
    suppliers_data = [
        (101, 'TechCorp Solutions', 'Alice Johnson', 'alice@techcorp.com', '+1-555-0101', '123 Tech St', 'San Francisco', 'USA'),
        (102, 'Mobile Masters', 'Bob Smith', 'bob@mobilemasters.com', '+1-555-0102', '456 Mobile Ave', 'Austin', 'USA'),
        (103, 'Kitchen Plus', 'Carol Williams', 'carol@kitchenplus.com', '+1-555-0103', '789 Kitchen Blvd', 'Chicago', 'USA'),
        (104, 'SportsPro Ltd', 'David Brown', 'david@sportspro.com', '+44-20-5550104', '321 Sports Rd', 'London', 'UK'),
        (105, 'FurniWorld', 'Emma Davis', 'emma@furniworld.com', '+1-555-0105', '654 Furniture Way', 'New York', 'USA')
    ]
    
    # Reviews data
    reviews_data = [
        (1, 1, 1, 5, 'Excellent laptop! Very fast and reliable.', '2023-06-15'),
        (2, 1, 4, 4, 'Great performance, but a bit pricey.', '2023-07-01'),
        (3, 2, 2, 5, 'Love this phone! Amazing camera quality.', '2023-06-10'),
        (4, 3, 5, 4, 'Good coffee maker, easy to use.', '2023-06-20'),
        (5, 4, 1, 5, 'Very comfortable running shoes.', '2023-06-25'),
        (6, 4, 3, 4, 'Good quality, fit perfectly.', '2023-07-05'),
        (7, 5, 4, 3, 'Chair is okay, could be more comfortable.', '2023-06-30'),
        (8, 6, 2, 5, 'Perfect mouse for work and gaming.', '2023-07-10'),
        (9, 7, 5, 5, 'Great water bottle, keeps drinks cold all day.', '2023-07-15')
    ]
    
    # Shipping addresses data
    shipping_addresses_data = [
        (1, 1, '123 Main St', 'Apt 4B', 'New York', 'NY', '10001', 'USA', 1),
        (2, 1, '456 Work Plaza', 'Suite 200', 'New York', 'NY', '10002', 'USA', 0),
        (3, 2, '789 London St', None, 'London', None, 'SW1A 1AA', 'UK', 1),
        (4, 3, '321 Madrid Ave', None, 'Madrid', None, '28001', 'Spain', 1),
        (5, 4, '654 Toronto Rd', 'Unit 12', 'Toronto', 'ON', 'M5V 3A1', 'Canada', 1),
        (6, 5, '987 Sydney Blvd', None, 'Sydney', 'NSW', '2000', 'Australia', 1)
    ]
    
    # Payments data
    payments_data = [
        (1, 1, 'Credit Card', 1329.98, '2023-06-01 14:30:00', 'Completed', 'TXN123456'),
        (2, 2, 'PayPal', 729.98, '2023-06-02 16:45:00', 'Completed', 'PP789012'),
        (3, 3, 'Credit Card', 159.98, '2023-06-03 10:15:00', 'Pending', 'TXN345678'),
        (4, 4, 'Debit Card', 279.98, '2023-06-04 12:20:00', 'Completed', 'DB901234'),
        (5, 5, 'Credit Card', 89.99, '2023-06-05 09:30:00', 'Completed', 'TXN567890'),
        (6, 6, 'PayPal', 149.98, '2023-06-06 18:10:00', 'Completed', 'PP234567')
    ]
    
    # Inventory data
    inventory_data = [
        (1, 1, 'Warehouse A', 45, 5, 10, '2023-11-01 08:00:00'),
        (2, 2, 'Warehouse A', 115, 5, 20, '2023-11-01 08:00:00'),
        (3, 3, 'Warehouse B', 70, 5, 15, '2023-11-01 08:00:00'),
        (4, 4, 'Warehouse C', 195, 5, 25, '2023-11-01 08:00:00'),
        (5, 5, 'Warehouse B', 25, 5, 10, '2023-11-01 08:00:00'),
        (6, 6, 'Warehouse A', 145, 5, 30, '2023-11-01 08:00:00'),
        (7, 7, 'Warehouse C', 295, 5, 50, '2023-11-01 08:00:00')
    ]
    
    # Discounts data
    discounts_data = [
        (1, 'WELCOME10', 'percentage', 10.00, 50.00, '2023-01-01', '2023-12-31', 1, 1000, 45),
        (2, 'SUMMER20', 'percentage', 20.00, 100.00, '2023-06-01', '2023-08-31', 1, 500, 123),
        (3, 'NEWUSER25', 'fixed', 25.00, 75.00, '2023-01-01', '2023-12-31', 1, None, 67),
        (4, 'BLACKFRIDAY', 'percentage', 30.00, 200.00, '2023-11-24', '2023-11-27', 0, 200, 0),
        (5, 'FREESHIP', 'fixed', 15.00, 30.00, '2023-01-01', '2023-12-31', 1, None, 234)
    ]
    
    # Insert data
    cursor.executemany('INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)', customers_data)
    cursor.executemany('INSERT OR IGNORE INTO categories VALUES (?, ?, ?, ?)', categories_data)
    cursor.executemany('INSERT OR IGNORE INTO suppliers VALUES (?, ?, ?, ?, ?, ?, ?, ?)', suppliers_data)
    cursor.executemany('INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?)', products_data)
    cursor.executemany('INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?, ?)', orders_data)
    cursor.executemany('INSERT OR IGNORE INTO order_items VALUES (?, ?, ?, ?, ?)', order_items_data)
    cursor.executemany('INSERT OR IGNORE INTO reviews VALUES (?, ?, ?, ?, ?, ?)', reviews_data)
    cursor.executemany('INSERT OR IGNORE INTO shipping_addresses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', shipping_addresses_data)
    cursor.executemany('INSERT OR IGNORE INTO payments VALUES (?, ?, ?, ?, ?, ?, ?)', payments_data)
    cursor.executemany('INSERT OR IGNORE INTO inventory VALUES (?, ?, ?, ?, ?, ?, ?)', inventory_data)
    cursor.executemany('INSERT OR IGNORE INTO discounts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', discounts_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Enhanced sample database created successfully!")
    print("Tables created:")
    print("  Core tables: customers, products, orders, order_items")
    print("  Extended tables: categories, suppliers, reviews, shipping_addresses")
    print("  Business tables: payments, inventory, discounts")
    print("Total: 11 tables with comprehensive e-commerce data")
    print("Sample data inserted for advanced text-to-SQL functionality")

if __name__ == '__main__':
    create_sample_database()
