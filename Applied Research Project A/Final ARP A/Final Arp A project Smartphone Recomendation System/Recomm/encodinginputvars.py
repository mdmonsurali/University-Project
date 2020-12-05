# -*- coding: utf-8 -*-

import numpy as nmp
from encoder import DataEncoder
class InputEncoders:
    
    data_encoder = DataEncoder()

    def convert(self,arr):
        return nmp.asarray(arr)
    
    def EncodeInputs(self,gender,age,annual_income,willing_amt,profession,mobile_os,main_reason,gaming,photography,camera,battery,processor,memory,screen_res):
        gender_inp_encoded = self.convert(self.data_encoder.GetGenderEncoded(gender))
        age_inp_encoded = self.convert(self.data_encoder.GetAgeEncoded(age))
        annual_income_inp_encoded = self.convert(self.data_encoder.GetAnnualIncomeEncoded(annual_income))
        willing_amt_inp_encoded = self.convert(self.data_encoder.GetWillAmtEncoded(willing_amt))
        profession_inp_encoded = self.convert(self.data_encoder.GetProfessionsEncoded(profession))
        mobile_os_inp_encoded = self.convert(self.data_encoder.GetMobileOsEncoded(mobile_os))
        main_reason_inp_encoded = self.convert(self.data_encoder.GetMainReasonEncoded(main_reason)) 
        #purpose inps
        gaming_inp_encoded = self.convert(self.data_encoder.GetGamingEncoded(gaming))
        photgrphy_inp_encoded = self.convert(self.data_encoder.GetPhotographyEncoded(photography))
        #features inputs
        camera_inp_encoded = self.convert(self.data_encoder.GetCameraFeatureEncoded(camera))
        battery_life_inp_encoded = self.convert(self.data_encoder.GetBatteryLifeEncoded(battery))
        processor_inp_encoded = self.convert(self.data_encoder.GetProcessorEncoded(processor))
        memory_inp_encoded = self.convert(self.data_encoder.GetMemoryEncoded(memory))
        screen_res_inp_encoded = self.convert(self.data_encoder.GetScreenResolutionEncoded(screen_res))
        #encoded input pass it to the predictor
        input_encoded = nmp.asmatrix(nmp.concatenate([gender_inp_encoded,age_inp_encoded,annual_income_inp_encoded,willing_amt_inp_encoded,
                                                  profession_inp_encoded,mobile_os_inp_encoded,main_reason_inp_encoded,
                                                  gaming_inp_encoded,photgrphy_inp_encoded,camera_inp_encoded,
                                                  battery_life_inp_encoded,processor_inp_encoded,memory_inp_encoded,
                                                  screen_res_inp_encoded]))
        return input_encoded

    
    