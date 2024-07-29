# def write_to_db():
#     raise FileExistsError("File error occured")
#
#
# def create_user(password):
#     try:
#         print()
#         write_to_db()
#     except FileExistsError:
#         print()
#
#
# def divide10By(num):
#         return 10 / num
#
#
#
# def debitAmount(amount):
#     try:
#         raise RuntimeError
#         print("amount debited")
#     except RuntimeError:
#         print("amount not debited")
#
# def credit_amount(amount):
#     print("amount credited")
# def start():
#     print("diving number by...")
#     debitAmount(1)
#     credit_amount(1)
#     # print("payment debited")
#     # print("payment credited...")
#
# start()
#
# try:
#     raise RuntimeError
#     print("try something")
# finally:
#     print("finally....")
#
#
# print("release lock..")

class TransactionFailed(Exception):
    pass


try:
    print("try something")
    raise TransactionFailed

except RuntimeError:
    print("RuntimeError")
else:
    print("opps...")
finally:
    print("finally...")