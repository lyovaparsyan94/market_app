# import logging
# import logging.config
# import os
# from helpers import load_config
# logger = logging.getLogger(__name__)
# logger_path = os.path.join(os.path.dirname(__file__), 'loggers.yml')
# log_config = load_config(config_path=logger_path)
# log = logging.getLogger('loggers.yml')
# logging.config.dictConfig(log_config['loggers'])
# # logging.basicConfig(filename='test.logs', level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
# # logging.basicConfig(**log_config['loggers'])
#
#
#
# class Employee:
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#         logging.info(f"Created employer: {self.f_name} {self.l_name}")
#
#     def email(self):
#         try:
#             logging.info(f"Creating mail for employer: {self.f_name} {self.l_name}")
#             return f'{self.f_name}.{self.l_name}@mail.ru'.lower()
#         except AttributeError as e:
#             logger.exception(f"Error,")
#
#     def full_name(self):
#         return f'{self.f_name} {self.l_name}'
#
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("William", "Saroyan")
# emp_3 = Employee("Wilsdfsdfliam", "sdfsdf")
# print(emp_1.email())
# print(emp_2.full_name())
# print(emp_3.full_name())
