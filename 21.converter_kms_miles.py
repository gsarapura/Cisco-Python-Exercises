# Converter.
# Liters per every 100 km to miles per gallon and vice versa.
"""
Expected output:
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
"""

# 1 gallon equals to 3.785411784
gallon_liters = 3.785411784 
# 1 miles equals to 1.609344
miles_kms = 1.609344

def liters_100km_to_miles_gallon(liters):
    converted_miles = 100 / miles_kms

    converted_gallons = liters / gallon_liters

    miles_per_gallone = converted_miles / converted_gallons
    return miles_per_gallone

def miles_gallon_to_liters_100km(miles):
    converted_kms = miles * miles_kms
    # No need to convert gallons to liters sincewe need only 1 gallon.
    liter_per_100km = gallon_liters / converted_kms * 100

    return liter_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
