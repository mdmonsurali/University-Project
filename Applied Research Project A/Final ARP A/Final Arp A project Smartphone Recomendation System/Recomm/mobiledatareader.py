# -*- coding: utf-8 -*-

from smartphoneattributes import SmartphoneAttributesInfo
from firebase import firebase 


class SmartphoneInformation:
    
     firebase= firebase.FirebaseApplication('https://arpa-b0988.firebaseio.com', authentication=None)
     phone_data = firebase.get('/', None)
    
     smartphone_attributes = SmartphoneAttributesInfo()

     def GetSmartphoneData(self,phone_name,attribute):
        return self.phone_data[phone_name][attribute]
    
    
    
     def GetSmartPhoneDisplaySize(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.DISPLAY_SIZE)
    
     def GetSmartPhoneDisplayInfo(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.DISPLAY_INFORMATION)
    
     def GetSmartPhoneOS(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.OS)
    
     def GetSmartPhoneOSTag(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.OS_TAG)
    
     def GetSmartPhoneRAM(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.RAM)
    
     def GetSmartPhoneStorage(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.STORAGE)
    
     def GetSmartPhonePrice(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.PRICE)
    
     def GetSmartPhonePriceTag(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.PRICE_TAG)
    
     def GetSmartPhoneBattery(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.BATTERY)
    
     def GetSmartPhoneBatteryTag(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.BATTERY_TAG)
    
     def GetSmartPhoneSelfieCamera(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.SELFIE_CAMERA)
    
     def GetSmartPhoneMainCamera(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.MAIN_CAMERA)
    
     def GetSmartPhoneMainCameraTag(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.MAIN_CAMERA_TAG)
    
     def GetSmartPhoneImage(self,phone_name):
        return self.GetSmartphoneData(phone_name,self.smartphone_attributes.IMAGE)
    
    
    
    
    
    
    
    
        
    

