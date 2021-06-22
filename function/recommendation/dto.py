class LEVELDTO:
    def __init__(self, newbrand, newmodel, newprice, newcategory, newshutter, newexposure, newtest_level):
        self.brand = newbrand        
        self.model = newmodel        
        self.price = newprice        
        self.category = newcategory        
        self.shutter = newshutter        
        self.exposure = newexposure        
        self.test_level = newtest_level

    def getBrand(self):
        return self.brand

    def setBrand(self, newbrand):
        self.brand = newbrand

    def getModel(self):
        return self.model

    def setModel(self, newmodel):
        self.model = newmodel

    def getPrice(self):
        return self.Price

    def setPrice(self, newprice):
        self.price = newprice

    def getCategory(self):
        return self.category

    def setCategory(self, newcategory):
        self.category = newcategory

    def getShutter(self):
        return self.shutter

    def setShutter(self, newshutter):
        self.shutter = newshutter

    def getExposure(self):
        return self.exposure

    def setExposure(self, newexposure):
        self.exposure = newexposure

    def getTest_level(self):
        return self.test_level

    def setTest_level(self, newtest_level):
        self.test_level = newtest_level

    def __str__(self):
        return '브랜드 : ' + self.brand + '모델명 : ' + self.model + '가격 : ' + self.price + '카테고리 : ' + self.category + '셔터 : ' + self.shutter + '노출측정방식 : ' + self.exposure + '레벨 : ' + self.test_level