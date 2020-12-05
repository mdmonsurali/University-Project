from flask import Flask, render_template, request
from recomm_ann import RecommendationSystem
from encodinginputvars import InputEncoders
from morerecommendations import MoreRecommendations
from mobiledatareader import SmartphoneInformation

app = Flask(__name__)


recommendation_system = RecommendationSystem()
input_encoders = InputEncoders()
more_recommendation = MoreRecommendations()
smartphone_information = SmartphoneInformation()

recommendation_alternatives = [] 


@app.route('/Recommendation_System#home')

def home():
    return render_template('index.html#home')

@app.route('/Recommendation_System#about')

def about():
    return render_template('index.html#about')

@app.route('/Recommendation_System#services')

def service():
    return render_template('index.html#services')

@app.route('/Recommendation_System#team')

def team():
    return render_template('index.html#team')

@app.route('/Recommendation_System#contact')

def contact():
    return render_template('index.html#contact')

@app.route('/visualization')

def visualization():
    return render_template('visualization.html')

@app.route('/Other_recomm1')

def Other_recomm():  
    phone1_name = recommendation_alternatives[0]
    phone1_url = smartphone_information.GetSmartPhoneImage(phone1_name)
    phone1_price_in_euro = smartphone_information.GetSmartPhonePrice(phone1_name)  
    phone1_os = smartphone_information.GetSmartPhoneOS(phone1_name)
    phone1_screen = smartphone_information.GetSmartPhoneDisplayInfo(phone1_name)
    phone1_memory = smartphone_information.GetSmartPhoneStorage(phone1_name)
    phone1_S_camera = smartphone_information.GetSmartPhoneSelfieCamera(phone1_name)
    phone1_M_camera = smartphone_information.GetSmartPhoneMainCamera(phone1_name)    
    phone1_display_size = smartphone_information.GetSmartPhoneDisplaySize(phone1_name)
    phone1_RAM = smartphone_information.GetSmartPhoneRAM(phone1_name)
    phone1_Battery = smartphone_information.GetSmartPhoneBattery(phone1_name)
       
    return render_template('Other_recomm1.html', phone1 = phone1_name,
                               url1 = phone1_url,
                               other_recomm1_price_euro = phone1_price_in_euro,
                               phone1_os = phone1_os,
                               phone1_screen = phone1_screen,
                               phone1_memory = phone1_memory,
                               phone1_S_camera = phone1_S_camera,
                               phone1_M_camera = phone1_M_camera,
                               phone1_display_size = phone1_display_size,
                               phone1_RAM = phone1_RAM,
                               phone1_Battery = phone1_Battery)

@app.route('/Other_recomm2')

def Other_recomm2():
    phone2_name = recommendation_alternatives[1]
    phone2_url = smartphone_information.GetSmartPhoneImage(phone2_name)
    phone2_price_in_euro = smartphone_information.GetSmartPhonePrice(phone2_name)
    phone2_os = smartphone_information.GetSmartPhoneOS(phone2_name)
    phone2_screen = smartphone_information.GetSmartPhoneDisplayInfo(phone2_name)
    phone2_memory = smartphone_information.GetSmartPhoneStorage(phone2_name)
    phone2_S_camera = smartphone_information.GetSmartPhoneSelfieCamera(phone2_name)
    phone2_M_camera = smartphone_information.GetSmartPhoneMainCamera(phone2_name)    
    phone2_display_size = smartphone_information.GetSmartPhoneDisplaySize(phone2_name)
    phone2_RAM = smartphone_information.GetSmartPhoneRAM(phone2_name)
    phone2_Battery = smartphone_information.GetSmartPhoneBattery(phone2_name)
    
    return render_template('Other_recomm2.html',phone2 = phone2_name,
                               url2 = phone2_url,
                               other_recomm2_price_euro =phone2_price_in_euro,
                               phone2_os = phone2_os,
                               phone2_screen = phone2_screen,
                               phone2_memory = phone2_memory,
                               phone2_S_camera = phone2_S_camera,
                               phone2_M_camera = phone2_M_camera,
                               phone2_display_size = phone2_display_size,
                               phone2_RAM = phone2_RAM,
                               phone2_Battery = phone2_Battery,)

@app.route('/Other_recomm3')

def Other_recomm3():
    phone3_name = recommendation_alternatives[2]
    phone3_url = smartphone_information.GetSmartPhoneImage(phone3_name)
    phone3_price_in_euro = smartphone_information.GetSmartPhonePrice(phone3_name)
    phone3_os = smartphone_information.GetSmartPhoneOS(phone3_name)
    phone3_screen = smartphone_information.GetSmartPhoneDisplayInfo(phone3_name)
    phone3_memory = smartphone_information.GetSmartPhoneStorage(phone3_name)
    phone3_S_camera = smartphone_information.GetSmartPhoneSelfieCamera(phone3_name)
    phone3_M_camera = smartphone_information.GetSmartPhoneMainCamera(phone3_name)    
    phone3_display_size = smartphone_information.GetSmartPhoneDisplaySize(phone3_name)
    phone3_RAM = smartphone_information.GetSmartPhoneRAM(phone3_name)
    phone3_Battery = smartphone_information.GetSmartPhoneBattery(phone3_name)
    return render_template('Other_recomm3.html',phone3 =phone3_name,
                               url3 = phone3_url,
                               other_recomm3_price_euro =phone3_price_in_euro,
                               phone3_os = phone3_os,
                               phone3_screen = phone3_screen,
                               phone3_memory = phone3_memory,
                               phone3_S_camera = phone3_S_camera,
                               phone3_M_camera = phone3_M_camera,
                               phone3_display_size = phone3_display_size,
                               phone3_RAM = phone3_RAM,
                               phone3_Battery = phone3_Battery)

@app.route('/Other_recomm4')

def Other_recomm4():
    phone4_name = recommendation_alternatives[3]
    phone4_url = smartphone_information.GetSmartPhoneImage(phone4_name)
    phone4_price_in_euro = smartphone_information.GetSmartPhonePrice(phone4_name)
    phone4_os = smartphone_information.GetSmartPhoneOS(phone4_name)
    phone4_screen = smartphone_information.GetSmartPhoneDisplayInfo(phone4_name)
    phone4_memory = smartphone_information.GetSmartPhoneStorage(phone4_name)
    phone4_S_camera = smartphone_information.GetSmartPhoneSelfieCamera(phone4_name)
    phone4_M_camera = smartphone_information.GetSmartPhoneMainCamera(phone4_name)    
    phone4_display_size = smartphone_information.GetSmartPhoneDisplaySize(phone4_name)
    phone4_RAM = smartphone_information.GetSmartPhoneRAM(phone4_name)
    phone4_Battery = smartphone_information.GetSmartPhoneBattery(phone4_name)
    return render_template('Other_recomm4.html',phone4 = phone4_name,
                               url4 =phone4_url,
                               other_recomm4_price_euro =phone4_price_in_euro,
                               phone4_os = phone4_os,
                               phone4_screen = phone4_screen,
                               phone4_memory = phone4_memory,
                               phone4_S_camera = phone4_S_camera,
                               phone4_M_camera = phone4_M_camera,
                               phone4_display_size = phone4_display_size,
                               phone4_RAM = phone4_RAM,
                               phone4_Battery = phone4_Battery)

@app.route('/Recommendation_System')

def home_page():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])

def index():
    
    if request.method == "POST" :
        age_inp = request.form['user_age']
        gender_inp = request.form['user_sex']
        annual_income_inp = request.form['user_income']
        willing_amt_inp = request.form['user_willing_amount']
        profession_inp = request.form['user_profession']
        mobile_os_inp = request.form['user_os']
        main_reason_inp = request.form['user_reason']
        gaming_inp= request.form['user_game']
        photgrphy_inp = request.form['user_photography']
        camera_inp = request.form['user_camera']
        battery_life_inp= request.form['user_battery']
        processor_inp = request.form['user_processor']
        memory_inp = request.form['user_storage']
        screen_resolution_inp = request.form['user_resolution']
        
        global major_recommendation
        
        major_recommendation = recommendation_system.Recommend(input_encoders.EncodeInputs(gender_inp,age_inp,annual_income_inp,
                                                                    willing_amt_inp,profession_inp,mobile_os_inp,
                                                                    main_reason_inp,gaming_inp,photgrphy_inp,
                                                                    camera_inp,battery_life_inp,processor_inp,memory_inp,
                                                                    screen_resolution_inp))

        major_recomm_os = smartphone_information.GetSmartPhoneOS(major_recommendation)
        major_recomm_screen = smartphone_information.GetSmartPhoneDisplayInfo(major_recommendation)
        major_recomm_display_size = smartphone_information.GetSmartPhoneDisplaySize(major_recommendation)
        major_recomm_RAM = smartphone_information.GetSmartPhoneRAM(major_recommendation)
        major_recomm_memory = smartphone_information.GetSmartPhoneStorage(major_recommendation)
        major_recomm_selfie_camera = smartphone_information.GetSmartPhoneSelfieCamera(major_recommendation)
        major_recomm_main_camera = smartphone_information.GetSmartPhoneMainCamera(major_recommendation)
        major_recomm_battery = smartphone_information.GetSmartPhoneBattery(major_recommendation)
        major_recomm_price = smartphone_information.GetSmartPhonePrice(major_recommendation)
        major_recomm_url = smartphone_information.GetSmartPhoneImage(major_recommendation)

        global recommendation_alternatives
        recommendation_alternatives = more_recommendation.GetMoreRecommendations1(major_recommendation)
     
        phone1_name = recommendation_alternatives[0]
        phone1_url = smartphone_information.GetSmartPhoneImage(phone1_name)
        phone1_price_in_euro = smartphone_information.GetSmartPhonePrice(phone1_name) 
            
        phone2_name = recommendation_alternatives[1]
        phone2_url = smartphone_information.GetSmartPhoneImage(phone2_name)
        phone2_price_in_euro = smartphone_information.GetSmartPhonePrice(phone2_name)
        
        phone3_name = recommendation_alternatives[2]
        phone3_url = smartphone_information.GetSmartPhoneImage(phone3_name)
        phone3_price_in_euro = smartphone_information.GetSmartPhonePrice(phone3_name)
        
        phone4_name = recommendation_alternatives[3]
        phone4_url = smartphone_information.GetSmartPhoneImage(phone4_name)
        phone4_price_in_euro = smartphone_information.GetSmartPhonePrice(phone4_name)
        
        print("recommendation complete")

       	return render_template("output.html",url = major_recomm_url, 
                               name = major_recommendation , 
                               OS = major_recomm_os,
                               Screen = major_recomm_screen, 
                               Display_size = major_recomm_display_size, 
                               RAM = major_recomm_RAM, 
                               Memory = major_recomm_memory, 
                               S_camera = major_recomm_selfie_camera, 
                               M_Camera = major_recomm_main_camera,
                               Battery = major_recomm_battery , 
                               Price = major_recomm_price,
                               phone1 = phone1_name,
                               url1 = phone1_url,
                               other_recomm1_price_euro = phone1_price_in_euro,
                               phone2 = phone2_name,
                               url2 = phone2_url,
                               other_recomm2_price_euro =phone2_price_in_euro,
                               phone3 =phone3_name,
                               url3 = phone3_url,
                               other_recomm3_price_euro =phone3_price_in_euro,
                               phone4 = phone4_name,
                               url4 =phone4_url,
                               other_recomm4_price_euro =phone4_price_in_euro
                               )
           
    return render_template('form.html')

if __name__ == "__main__":
    app.run()
    
