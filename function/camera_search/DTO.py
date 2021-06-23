#카메라정보를 보유하게 되는 구조의 class, 객체로 관리
class CameraDTO:
    def __init__(self,nbrand,nmodel,nprice,ncategory,nshutter,nexposure,nlevel):
        self.brand = nbrand
        self.model = nmodel
        self.price = nprice
        self.category = ncategory
        self.shutter = nshutter
        self.exposure = nexposure
        self.level = nlevel

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price

    def getCategory(self):
        return self.category

    def getShutter(self):
        return self.shutter

    def getExposure(self):
        return self.exposure
    
    def getLevel(self):
        return self.level
    

    def setBrand(self,nbrand):
        self.brand = nbrand

    def setModel(self,nmodel):
        self.model = nmodel

    def setPrice(self,nprice):
        self.price = nprice

    def setFormat(self,nformat):
        self.format = nformat

    def __str__(self):
        return 'Brand : ' + self.brand + 'Model : ' + self.model + 'Price : ' + self.price + 'Format : ' + self.format
        