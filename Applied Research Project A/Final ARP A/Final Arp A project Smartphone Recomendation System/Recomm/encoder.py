# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:00:12 2019

@author: Sudarshan
"""

import age
import gender
import annualincome
import features
import mainreason
import mobileos
import professions
import willingamount
import purpose


class DataEncoder:
    
    #function defined to encode age  Tested
    def GetAgeEncoded(self , agevalue):
        if(agevalue == age.BELOW_20):
            return age.BELOW_20_CODE
        elif(agevalue == age.BETWEEN_20_30):
            return age.BETWEEN_20_30_CODE
        elif(agevalue == age.BETWEEN_30_40):
            return age.BETWEEN_30_40_CODE
        elif(agevalue == age.BETWEEN_40_50):
            return age.BETWEEN_40_50_CODE
        else:
            raise Exception('unexpected input in age encoder ' + str(agevalue))
            return
        
        #to encode the annual income Tested
    def GetAnnualIncomeEncoded(self, annualincomevalue):
        if(annualincomevalue == annualincome.BELOW_10K):
            return annualincome.BELOW_10K_CODE
        elif(annualincomevalue == annualincome.BETWEEN_10K_20K):
            return annualincome.BETWEEN_10K_20K_CODE
        elif(annualincomevalue == annualincome.ABOVE_20K):
            return annualincome.ABOVE_20K_CODE
        else:
            raise Exception('unexpected input in annual income encoder ' + str(annualincomevalue))
            return
        
     #to encode the gender and tested   
    def GetGenderEncoded(self,gendervalue):  
        if(gendervalue == gender.MALE):
            return gender.MALE_CODE
        elif(gendervalue == gender.FEMALE):
            return gender.FEMALE_CODE
        else:
            raise Exception('unexpected input in gender encoder ' + str(gendervalue))
            return
      
       #to encode the willing amount Tested
    def GetWillAmtEncoded(self,willamtvalue):
        if(willamtvalue == willingamount.BELOW_300):
            return willingamount.BELOW_300_CODE
        elif(willamtvalue == willingamount.BETWEEN_300_700):
            return willingamount.BETWEEN_300_700_CODE
        elif(willamtvalue == willingamount.ABOVE_700):
            return willingamount.ABOVE_700_CODE
        else: 
            raise Exception('unexpected input in Willing Amount encoder ' + str(willamtvalue))
            return
        
        #Mobile OS encoding
    def GetMobileOsEncoded(self,mobosvalue):
        if(mobosvalue == mobileos.ANDROID):
            return mobileos.ANDROID_CODE
        elif(mobosvalue == mobileos.IOS):
            return mobileos.IOS_CODE
        elif(mobosvalue == mobileos.WINDOWS):
            return mobileos.WINDOWS_CODE
        else:
            raise Exception('unexpected input in Mobile OS encoder ' + str(mobosvalue))
            return
        
        
      #Profession Encode
    def GetProfessionsEncoded(self,professionvalue):
        if(professionvalue == professions.ACCOUNTANT):
            return professions.ACCOUNTANT_CODE
        elif(professionvalue == professions.BUSINESSMAN):
            return professions.BUSINESSMAN_CODE
        elif(professionvalue == professions.HEALTH_PROFESSIONAL):
            return professions.HEALTH_PROFESSIONAL_CODE
        elif(professionvalue == professions.IT):
            return professions.IT_CODE
        elif(professionvalue == professions.LAWYER):
            return professions.LAWYER_CODE
        elif(professionvalue == professions.PHOTOGRAPHER):
            return professions.PHOTOGRAPHER_CODE
        elif(professionvalue == professions.POLICE_OFFICER):
            return professions.POLICE_OFFICER_CODE
        elif(professionvalue == professions.PROFESSOR):
            return professions.PROFESSOR_CODE
        elif(professionvalue == professions.STUDENT):
            return professions.STUDENT_CODE
        else:
            raise Exception('unexpected input in Profession encoder ' + str(professionvalue))
            return
        
        #encoding main reasons
    def GetMainReasonEncoded(self, mainreasonvalue):
         if(mainreasonvalue == mainreason.BRAND):
             return mainreason.BRAND_CODE
         elif(mainreasonvalue == mainreason.FEATURES):
             return mainreason.FEATURES_CODE
         elif(mainreasonvalue == mainreason.PRICE):
             return mainreason.PRICE_CODE
         elif(mainreasonvalue == mainreason.SECURITY):
             return mainreason.SECURITY_CODE
         else:
             raise Exception('unexpected input in main reason encoder ' + str(mainreasonvalue))
             return
             
    #defined inside features     
    def GetCameraFeatureEncoded(self, camerafeature):
        if(camerafeature == features.CAMERA):
            return features.CAMERA_CODE_YES
        else:
            return features.CAMERA_CODE_NO
        
    def GetBatteryLifeEncoded(self, batterylifefeature):
        if(batterylifefeature == features.BATTERY_LIFE):
            return features.BATTERY_LIFE_CODE_YES
        else:
            return features.BATTERY_LIFE_CODE_NO
    
    def GetProcessorEncoded(self, performancefeature):
        if(performancefeature == features.PROCESSOR):
            return features.PROCESSOR_CODE_YES
        else:
            return features.PROCESSOR_CODE_NO
    
    def GetMemoryEncoded(self, memoryfeature):
        if(memoryfeature == features.MEMORY):
            return features.MEMORY_CODE_YES
        else:
            return features.MEMORY_CODE_NO
        
    def GetScreenResolutionEncoded(self, screenresfeature):
        if(screenresfeature == features.SCREEN_RESOLUTION):
            return features.SCREEN_RESOLUTION_CODE_YES
        else:
            return features.SCREEN_RESOLUTION_CODE_NO
        
    
    def GetGamingEncoded(self, gamingpurpose):
        if(gamingpurpose ==  purpose.GAMING):
            return purpose.GAMING_CODE_YES
        else:
            return purpose.GAMING_CODE_NO
        
    def GetPhotographyEncoded(self, photographypurpose):
        if(photographypurpose ==  purpose.PHOTOGRAPHY):
            return purpose.PHOTOGRAPHY_CODE_YES
        else:
            return purpose.PHOTOGRAPHY_CODE_NO
    
    
    
        
    
            
        
            
        
    
    
    
    
        
            

        
    
            
            
            
     