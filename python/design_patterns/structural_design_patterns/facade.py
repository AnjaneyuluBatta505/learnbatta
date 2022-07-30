# service classes
class AccountInfo:
    def get_account_info(self, acc_id):
        # get account id
        info = {"account_id": "AC123", "name": "Anji"}
        return info


class DeliveryInfo:
    def get_package_info(self, package_id):
        info = {
            "name": "Cricket KIT",
            "address": "Hyderabad, Telangana, India"
        }
        return info

# facade class
class CustomerRepresentative:
    def __init__(self):
        self.account = AccountInfo()
        self.delivery = DeliveryInfo()
    
    def get_info(self, acc_id, package_id):
        acc = self.account.get_account_info(acc_id)
        pckg = self.delivery.get_package_info(package_id)
        print("account:", acc)
        print("package:", pckg)

if __name__ == '__main__':
    represntative = CustomerRepresentative()
    represntative.get_info("AC123", "PG5577")
