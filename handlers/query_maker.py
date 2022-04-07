import logging.config
from helpers import load_config
import os
logger_path = os.path.join(os.path.dirname(__file__), '../logs/market_log_config.yaml')
log_config = load_config(config_path=logger_path)
logging.config.dictConfig(log_config['loggers'])
logger = logging.getLogger('market_user')


class QueryMaker:
    def __init__(self, config):
        self.name = config['database']['params']['database']

    @staticmethod
    def create_table():
        table_name = input("Select table name: ").lower()
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id INT PRIMARY KEY,
        name varchar(30),
        quantity INT,
        purchase_price INT,
        sale_price INT,
        delivery_company varchar(30) 
        )"""
        logger.info(f"Creating table {table_name}...")
        return query

    @staticmethod
    def add_values_into_table():
        table_name = input("Enter branch name: ").lower()
        name = input("Input product name: ").lower()
        quantity = int(input("Input quantity: "))
        purchase_price = int(input("Input purchase price: "))
        sale_price = int(input("Input sale price: "))
        delivery_company = str(input("Input delivery_company: ")).lower()
        query = f"""INSERT INTO {table_name} (name, quantity, purchase_price, sale_price,
                    delivery_company) VALUES('{name}', '{quantity}', '{purchase_price}', '{sale_price}',
                    '{delivery_company}')"""
        logger.info(f"Trying to add {name} to table...")
        return query

    def delete_value_from_table(self):
        table_name = input("Enter table name:  ").lower()
        name = input("Select name to delete from table: ").lower()
        query = f"""DELETE FROM {self.name}.{table_name} where name='{name}'"""
        logger.info(f"Deleting product {name} from {table_name}...")
        return query

    def show_table(self):
        table_name = input("Enter branch name:  ").lower()
        query = f"""SELECT id, name, quantity, purchase_price, sale_price, delivery_company 
        FROM {self.name}.{table_name};"""
        logger.info("Creating request ....")
        return query

    def search_product(self):
        table_name = input("Enter branch name:  ").lower()
        name = input("Enter product name:  ").lower()
        query = f"""SELECT * FROM {self.name}.{table_name} WHERE name='{name}';"""
        logger.info()
        return query

    def sort_products_by_sale_price(self):
        table_name = input("Enter branch name:  ").lower()
        print("1 - sort by increasing, 2 - sort by decreasing")
        sort_dict = {1: "ASC", 2: "DESC"}
        x = int(input("Your choice: "))
        user_select = sort_dict[x]
        min_parametr = int(input("Select minimal parameter: "))
        max_parametr = int(input("Select maximal parameter: "))
        query = f"""SELECT * FROM {self.name}.{table_name} WHERE sale_price BETWEEN {min_parametr} 
        AND {max_parametr} ORDER BY id {user_select}"""
        return query

    def sort_products_by_purchase_price(self):
        table_name = input("Enter branch name:  ").lower()
        print("1 - sort by increasing, 2 - sort by decreasing")
        sort_dict = {1: "ASC", 2: "DESC"}
        x = int(input("Your choice: "))
        user_select = sort_dict[x]
        min_parameter = int(input("Select minimal parameter: "))
        max_parameter = int(input("Select maximal parameter: "))
        query = f"""SELECT * FROM {self.name}.{table_name} WHERE purchase_price BETWEEN {min_parameter} 
        AND {max_parameter} ORDER BY id {user_select} """
        return query

    def insert_or_update(self):
        table_name = input("Enter branch name:  ").lower()
        prod_id = int(input("Enter product id:  ").lower())
        quantity = int(input("Input quantity: "))
        purchase_price = int(input("Input purchase price: "))
        sale_price = int(input("Input sale price: "))
        delivery_company = str(input("Input delivery_company: ")).lower()
        query = f"""INSERT INTO {self.name}.{table_name} SET id={prod_id} ON DUPLICATE KEY UPDATE quantity={quantity},
         purchase_price={purchase_price}, sale_price={sale_price}, delivery_company='{delivery_company}';"""
        return query
