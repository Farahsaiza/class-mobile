class mobile () :
    def __init__(self, company_name, model, color, capacities, processor, operating_system, price ) :
        self.company_name =  company_name
        self.model  =  model
        self.color =  color
        self.capacities = capacities
        self.processor=  processor
        self.price = price
        self.operating_system = operating_system



    def info(self):
        print("the mobile's company_name is: {}, the mobile's model is: {}, the color is: {}, capacities: {},  processor: {},operating_system:{}, price: {}"
              .format(self.company_name , self.model , self.color , self.capacities , self.processor , self.price , self.operating_system))
        

phone1 = mobile("Apple", "IPhone 11 Pro", "red", "64,128,256 GB", "Apple A13" , "IOS 13 to 17.X", "3000DH")
phone2 = mobile("Apple", "IPhone 12 Pro", "grey", "128,256,512 GB", "Apple A14" , "IOS 14.1 to 17.X", "6000DH")
phone3 = mobile("Apple", "IPhone 13 Pro", "light blue", "128,256,512 GB, 1  TB", "Apple A15" , "IOS 15 to 17.X", "12000DH")

phone1.info()
phone2.info()
phone3.info()