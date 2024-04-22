import psycopg2

def connect_db():
    connect = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        host='localhost', 
        password="Rgill42",
        port=5432
    )
    return connect

def main():
    try:
        connect = connect_db()
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        return
    
    try:
        while True:
            print("""
Welcome to the Database CLI Interface!
Please select an option:
1. Insert a New Customer From Sao Paulo
2. Remove All Payments From the Payment Table made with vouchers
3. Update All Sellers Located in Campinas to Sao Paulo
4. Search for All Customers Located in the City of Franca
5. Calculate the Average Payment Value from All Recorded Payments
6. Sort Payment Table Based off Recorded Payments in Descending Order
7. Join the Customer and Order tables for Customers who have Placed Orders
8. Show Product Weights and their Counts, Grouped by Weight
9. Select Order IDs with 5 Star Reviews
10. Add a New Product Category 'Electrodomésticos' (Appliances) and List a New Item In The Product Table
11. Exit\n""")

            user_choice = input("Enter your choice (1-11): ")

            if user_choice == '1':
                current = connect.cursor()
                current.execute("INSERT INTO Customer VALUES ('h9z3e5vq7k6n2t4y1b0m8lpxo2c4r6qx', '14409', 'sao paulo', 'SP');")
                connect.commit()
                print("\nNew customer successfully inserted")

            elif user_choice == '2':
                current = connect.cursor()
                current.execute("DELETE FROM Payment P WHERE P.payment_type = 'voucher';")
                connect.commit()

                print("\nAll payment methods made with vouchers have been successfully removed")


            elif user_choice == '3':
                current = connect.cursor()
                current.execute("Update Seller Set seller_city = 'sao paulo' Where seller_city = 'campinas';")
                connect.commit()
   
                print("\nSuccessfully updated the city location for all sellers living in campinas to sao paulo")

            elif user_choice == '4':
                current = connect.cursor()
                current.execute("SELECT * FROM Customer WHERE customer_city = 'franca';")
                rows = current.fetchall()
                connect.commit()

                for row in rows:
                    print(row)

            elif user_choice == '5':
                current = connect.cursor()
                current.execute("SELECT AVG(payment_value) FROM Payment")
                row = current.fetchall()
                average_payment = round(row[0][0], 2)
                connect.commit()
   
                print(f"The average of all payment amounts comes to: {average_payment}")


            elif user_choice == '6':
                current = connect.cursor()
                current.execute("SELECT * FROM Payment ORDER BY payment_value DESC;")
                rows = current.fetchall()
                connect.commit()

                for row in rows:
                    print(row)


            elif user_choice == '7':
                current = connect.cursor()
                current.execute("SELECT DISTINCT C.customer_id From Customer C Inner Join Orders O ON C.customer_id = O.customer_id;")
                rows = current.fetchall()
                connect.commit()

                for row in rows:
                    print(row)                   


            elif user_choice == '8':
                current = connect.cursor()
                current.execute("SELECT P.product_weight_g, Count(*) From Product P Group By P.product_weight_g ORDER BY P.product_weight_g DESC;")
                rows = current.fetchall()
                connect.commit()

                for row in rows:
                    print(row)    


            elif user_choice == '9':
                current = connect.cursor()
                current.execute("SELECT O.order_id From Orders O Where O.order_id In (Select R.order_id From Review R Where R.review_score = 5);")
                rows = current.fetchall()
                connect.commit()

                for row in rows:
                    print(row)


            elif user_choice == '10':
                current = connect.cursor()
                
                current.execute("""
BEGIN TRANSACTION;

-- Step 1: Insert a new product category
INSERT INTO ProductCategory (product_category_name, product_category_name_english) VALUES ('Electrodomésticos', 'Appliances');

-- Step 2: Insert a new product with the newly created category
INSERT INTO Product (product_id, product_category_name, product_name_length, product_description_length, product_photos_qty,
product_weight_g, product_length_cm, product_height_cm, product_width_cm)
VALUES ('p4j9k3s6v2a8t0n5o1l7m2i8r3e5y0z', 'Electrodomésticos', 14, 250, 2, 50, 15, 20, 35);
COMMIT;
""")    
                connect.commit()
                print("Succesfully created a new product category and listed a newly associated item")


            elif user_choice == '11':
                print("Succesfully Exited Ecommerce CLI")
                break

            else:
                print("\nInvalid choice, please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        connect.close()

main()
