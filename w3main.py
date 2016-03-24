def transfer_c_f():
    cf=raw_input("celsius of fahreheit: ")

    if(cf=='c'):
        print "You entered celsius, please input celsisus value"
        temp=raw_input("celsius value: ")
        f_temp=float(temp)
        tem=(f_temp *1.8)+32
        print tem
    else:
        print "You entered fahreheit, please input fahreheit value"
        temp=raw_input("fahreheit value:")
        f_temp=float(temp)
        tem=(f_temp-32)/1.8
    
    print tem
    
    
transfer_c_f()