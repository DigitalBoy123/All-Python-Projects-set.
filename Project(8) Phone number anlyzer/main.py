try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, format_number, timezone, PhoneNumberFormat 
    from phonenumbers import number_type, PhoneNumberType

    number = str(input("Enter you number in: "))
    if not number.startswith("+"):
        print("The number must start with + sign")
        exit()

    my_number= phonenumbers.parse(number)

    if phonenumbers.is_valid_number(my_number):

        # Location of the give number
        location= geocoder.description_for_number(my_number,"en")
        print(f"The country is: {location}")
        
        # The service provider of the network/sim
        Carrier_SP= carrier.name_for_number(my_number,"en")
        print(f"The network provider is: {Carrier_SP}")
        
        # The code of the country
        code = my_number.country_code
        print(f"The code for country is: {code}")
        
        # The national number
        nat_num = format_number(my_number, PhoneNumberFormat.NATIONAL)
        print(f"The national number is: {nat_num[:2]}******{nat_num[-2:]}")
        
        # The regional code
        region_code = phonenumbers.region_code_for_number(my_number)
        print(f"The region code is: {region_code}")

        # The timezone of the number in the country
        tim_zone = timezone.time_zones_for_number(my_number)
        print(f"The time zone is: {tim_zone}")
        
        # The international number with code
        inter_num = format_number(my_number, PhoneNumberFormat.INTERNATIONAL)
        print(f"The international number is: {inter_num[:3]}********{inter_num[-2:]}")

        # The type of number
        num_type = number_type(my_number)
        type_mapping = {
            PhoneNumberType.FIXED_LINE: "Fixed Line",
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed or Mobile",
        PhoneNumberType.TOLL_FREE: "Toll Free",
        PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        PhoneNumberType.SHARED_COST: "Shared Cost",
        PhoneNumberType.VOIP: "VOIP",
        PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.UNKNOWN: "Unknown",
        PhoneNumberType.VOICEMAIL: "Voicemail",
        
        }
        print(f"The number type is: {type_mapping.get(num_type, "Unknown")}")

    else: # Incase the number is not correct then this block will run and popup message will be showed
        print("No the number is not valid")

except Exception as e:
    print(f"Error: {e}") # The handler of all program to prevent the program from crash

 


 