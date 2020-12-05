# -*- coding: utf-8 -*-
from mobiledatareader import SmartphoneInformation
from pricetag import PriceTag
from collections import OrderedDict


class MoreRecommendations:
    
    smartphone_info = SmartphoneInformation()
    price_tag = PriceTag()
    
    data = smartphone_info.phone_data
    
    all_phones = list(data.keys())
    
    len(all_phones)
        
    def GetMoreRecommendations(self, major_recommendation):
        similar_ram = []
        similar_ram_battery = []
        similar_ram_battery_maincamera = []
        
        more_recomm = []
        for i in range (len(self.all_phones)):
            if(major_recommendation != self.all_phones[i]):
                if(self.smartphone_info.GetSmartPhoneRAM(major_recommendation) == self.smartphone_info.GetSmartPhoneRAM(self.all_phones[i])):
                    similar_ram.append(self.all_phones[i])
                    if(self.smartphone_info.GetSmartPhoneBatteryTag(major_recommendation) == self.smartphone_info.GetSmartPhoneBatteryTag(self.all_phones[i])):
                        similar_ram_battery.append(self.all_phones[i])
                        if(self.smartphone_info.GetSmartPhoneMainCameraTag(major_recommendation) == self.smartphone_info.GetSmartPhoneMainCameraTag(self.all_phones[i])):
                            similar_ram_battery_maincamera.append((self.all_phones[i]))
                            if(self.smartphone_info.GetSmartPhoneStorage(major_recommendation) == self.smartphone_info.GetSmartPhoneStorage(self.all_phones[i])):
                                more_recomm.append(self.all_phones[i])
        
        return more_recomm
    
    
    def GetMoreRecommendations1(self, major_recommendation):
        recommended_score_1 = {}
        recommended_score_2 = {}
        recommended_score_3 = {}
        recommended_score_4 = {}
        
        for i in range (len(self.all_phones)):
            recommend_score = 0
            if(major_recommendation != self.all_phones[i]):
                if(self.smartphone_info.GetSmartPhoneRAM(major_recommendation) == self.smartphone_info.GetSmartPhoneRAM(self.all_phones[i])):
                    recommend_score += 1
                if(self.smartphone_info.GetSmartPhoneBatteryTag(major_recommendation) == self.smartphone_info.GetSmartPhoneBatteryTag(self.all_phones[i])):
                    recommend_score += 1
                if(self.smartphone_info.GetSmartPhoneMainCameraTag(major_recommendation) == self.smartphone_info.GetSmartPhoneMainCameraTag(self.all_phones[i])):
                    recommend_score += 1
                if(self.smartphone_info.GetSmartPhoneStorage(major_recommendation) == self.smartphone_info.GetSmartPhoneStorage(self.all_phones[i])):
                    recommend_score += 1
                
                if(recommend_score == 1):
                    recommended_score_1[self.all_phones[i]] = self.smartphone_info.GetSmartPhonePrice(self.all_phones[i])
                elif(recommend_score == 2):
                    recommended_score_2[self.all_phones[i]] = self.smartphone_info.GetSmartPhonePrice(self.all_phones[i])
                elif(recommend_score == 3):
                    recommended_score_3[self.all_phones[i]] = self.smartphone_info.GetSmartPhonePrice(self.all_phones[i])
                elif(recommend_score == 4):
                    recommended_score_4[self.all_phones[i]] = self.smartphone_info.GetSmartPhonePrice(self.all_phones[i])
                
       
        
        d1 = OrderedDict(sorted(recommended_score_1.items(), key=lambda t: t[1]))
        d2 = OrderedDict(sorted(recommended_score_2.items(), key=lambda t: t[1]))
        d3 = OrderedDict(sorted(recommended_score_3.items(), key=lambda t: t[1]))
        d4 = OrderedDict(sorted(recommended_score_4.items(), key=lambda t: t[1]))
        
        d5 = {**d4,**d3,**d2,**d1}
        
        minor_recommendations = list(d5.keys())
        return minor_recommendations[0:4]


  