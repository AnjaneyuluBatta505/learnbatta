from abc import ABC

class AbsAddress(ABC):
    line: str
    city: str
    country: str
    pin: str

class VendorAddress:
    def __init__(self, line1, line2, line3, city, country, pin):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.city = city
        self.country = country
        self.pin = pin

class CustomerAddress(AbsAddress):
    def __init__(self, line, city, country, pin):
        self.line = line
        self.city = city
        self.country = country
        self.pin = pin

class VendorAddressAdapter:
    def __init__(self, vendor_address):
        self.line = f'{vendor_address.line1}, {vendor_address.line2}, {vendor_address.line3}'
        self.city = vendor_address.city
        self.country = vendor_address.country
        self.pin = vendor_address.pin


# client
def print_address(address):
    print(f'{address.line}, {address.city}, {address.country}, {address.pin}')


if __name__ == '__main__':
    address1 = CustomerAddress("101/HG", "Goldberg", "Sambala", 99099090)
    address2 = VendorAddress("105", "HG", "Hydro", "Mercury", "Gondwana", 88088080)
    address2_adapt = VendorAddressAdapter(address2)

    for address in [address1, address2_adapt]:
        print_address(address)
