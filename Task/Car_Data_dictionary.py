car_data={
        "Ev":{"Hyundai":{"i10":{"price":3200000,"model":"Hicross"},
                    "creta":{"price":4300000,"model":"Neu"}},
                "TATA":{"Nexon":{"price":2500000,"model":"SUV"},
                    "Harrier":{"price":2600000,"model":"SUV XL"}}},
        "Petrol":{"Hyundai":{"i20":{"price":2100000,"model":"Hybreed"},
                            "Creta":{"price":2530000,"model":"Hicross_P"},
                            "i10":{"price":1450000,"model":"Compact"}}},
        "Diesel":{"Hyundai":{"i20":{"price":1970000,"model":"Hybreed_D"},
                        "Swift":{"price":3500000,"model":"Hicross_D"},
                        "i10":{"price":1350000,"model":"Compact_D"}},
                "Maruti":{"Baleno":{"price":1790000,"model":"120_cc"},
                          "Swift":{"price":3120000,"model":"swift_dezire"},
                          "Brezza":{"price":2780000,"model":"Premium_deluxe"}}}                
}   

while True:
    print(f"1) Search by car type\n2) Search Maruti cars\n3) Search Swift Cars\n4) Exit")
    choice=int(input("Enter a choice: "))
    match choice:
        case 1:
            car_type=input("Enter car types --- ev,petrol or diesel: ").capitalize()
            for k,v in car_data.items():
                if k==car_type:
                    print(k)
                    for k1,v1 in v.items():
                        print(f"\t{k1}\t\n{v1}")
        case 2:
            for k,v in car_data.items():
                for k1,v1 in v.items():
                    if k1=='Maruti':
                        print(f"{k1}\t\n{v1}")
        case 3:
            for k,v in car_data.items():
                for k1,v1 in v.items():
                    for k2,v2 in v1.items():
                        if k2=="Swift":
                            print(f"{k2}\t\n{v2}")
        case 4:
            print("You've successfully exited the program")
            break