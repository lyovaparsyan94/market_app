import os
import pymysql
from pymysql import connect
from handlers.query_maker import QueryMaker, logger
# import logging
# import logging.config
# from helpers import load_config
# logger_path = os.path.join(os.path.dirname(__file__), '../logs/market_log_config.yaml')
# log_config = load_config(config_path=logger_path)
# logging.config.dictConfig(log_config['loggers'])
# logger = logging.getLogger('market_user')


class Database:
    def __init__(self, config):

        self.connection = connect(**config['database']['params'],
                                  cursorclass=pymysql.cursors.DictCursor)

        self.query_maker = QueryMaker(config=config)

    @staticmethod
    def close_connection(connection, cursor):
        cursor.close()
        connection.close()
        logger.info("Connection was closed")

    def execute_and_commit(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        logger.info("Trying to execute query...")
        logger.info("Saving changes...")
        self.connection.commit()
        logger.info("Changes successfully completed")

    def create_database(self):
        try:
            print("Trying to connect...")
            query = self.query_maker.create_db()
            print("Connection is successful")
            self.execute_and_commit(query)
            print(f"Database successfully created")
        except Exception as e:
            logger.critical("Database didn't created")
            print(e)
        finally:
            self.connection.close()

    def create_table(self):
        query = self.query_maker.create_table()
        cursor = self.connection.cursor()
        cursor.execute(query)

    def insert(self):
        query = self.query_maker.add_values_into_table()
        self.execute_and_commit(query)
        print("-" * 20)

    def delete_values_from_table(self):
        query = self.query_maker.delete_value_from_table()
        self.execute_and_commit(query)
        logger.info(f"The value successfully deleted...")
        print("-" * 20)

    def show_branch_products(self):
        query = self.query_maker.show_table()
        logger.info("Connecting to database...")
        cursor = self.connection.cursor()
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            print("-" * 20)
            print(f"id: {product['id']}, {product['name']}, quantity: {product['quantity']}, "
                  f"purchase price: {product['purchase_price']}, sale price: {product['sale_price']}, "
                  f"delivery company: {product['delivery_company']}")
        print("-" * 20)

    def search_product(self):
        query = self.query_maker.search_product()
        cursor = self.connection.cursor()
        cursor.execute(query)
        logger.info(f"Trying to connect database")
        products = cursor.fetchall()
        for product in products:
            print("-" * 20)
            print(f"id: {product['id']}, {product['name']}, quantity: {product['quantity']}, "
                  f"purchase price: {product['purchase_price']}, sale price: {product['sale_price']}, "
                  f"delivery company: {product['delivery_company']}")
        print("-" * 20)


    def sort_by_sale_price(self):
        query = self.query_maker.sort_products_by_sale_price()
        cursor = self.connection.cursor()
        logger.info(f"Trying to connect database, {'%(funcName)s'}")
        cursor.execute(query)
        products = cursor.fetchall()
        logger.info("Sorting")
        for product in products:
            print("-" * 20)
            print(f"id: {product['id']}, {product['name']}, quantity: {product['quantity']}, "
                  f"purchase price: {product['purchase_price']}, sale price: {product['sale_price']}, "
                  f"delivery company: {product['delivery_company']}")
        print("-" * 20)

    def sort_by_purchase_price(self):
        query = self.query_maker.sort_products_by_purchase_price
        cursor = self.connection.cursor()
        logger.info("Connecting to database...")
        cursor.execute(query)
        products = cursor.fetchall()
        logger.info("Sorting products..")
        for product in products:
            print(f"id: {product['id']}, {product['name']}, quantity: {product['quantity']}, "
                  f"purchase price: {product['purchase_price']}, sale price: {product['sale_price']}, delivery company: {product['delivery_company']}")
        print("-" * 20)

    def insert_update_params(self):
        query = self.query_maker.insert_or_update()
        self.execute_and_commit(query)
        print("The changes have been successfully completed... ")
        print("-" * 20)
