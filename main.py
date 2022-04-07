import os
from handlers.database import Database
from helpers import load_config


# TODO ADD LOGGING

def run():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    config = load_config(config_path=config_path)
    ciran = Database(config=config)
    while True:
        print("Please select operation from numbers 1-8, where: ",
              "1 - create new table for new branch of Market, "
              "2 - insert value into existing branch",
              "3 - delete value from selected branch, "
              "4 - show detailed information about the products in the branch",
              "5 - search product in the branch",
              "6 - sort selected product by purchase price",
              "7 - sort selected product by sale price",
              "8 - update current product parameters by id or insert new products if it doesn't exists",
              "9 - create new market database", sep='\n')
        commands = {1: ciran.create_table,
                    2: ciran.insert,
                    3: ciran.delete_values_from_table,
                    4: ciran.show_branch_products,
                    5: ciran.search_product,
                    6: ciran.sort_by_purchase_price,
                    7: ciran.sort_by_sale_price,
                    8: ciran.insert_update_params,
                    9: ciran.create_database}
        number = int(input("Select number: "))
        commands[number]()


if __name__ == '__main__':
    run()
