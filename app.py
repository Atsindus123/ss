# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd

# # Load the model from the .pkl file
# with open('car.pkl', 'rb') as file:
#     model = pickle.load(file)

# # List of car names
car_names = [
    'audi a3', 'audi a4', 'audi a6', 'audi q3', 'bmw 3 series',
    'bmw 5 series', 'bmw x1', 'bmw x3', 'chevrolet aveo u va',
    'chevrolet beat', 'chevrolet cruze', 'chevrolet enjoy',
    'chevrolet optra', 'chevrolet optra magnum', 'chevrolet sail uva',
    'chevrolet spark', 'datsun go', 'datsun go plus', 'datsun redi go',
    'fiat grand punto', 'fiat linea', 'fiat punto evo',
    'fiat punto pure', 'ford ecosport', 'ford fiesta',
    'ford fiesta classic', 'ford figo', 'ford figo aspire',
    'ford freestyle', 'ford ikon', 'ford new figo', 'honda accord',
    'honda amaze', 'honda br-v', 'honda brio', 'honda city',
    'honda city zx', 'honda civic', 'honda crv', 'honda jazz',
    'honda mobilio', 'honda wr-v', 'hyundai accent', 'hyundai aura',
    'hyundai creta', 'hyundai elite i20', 'hyundai eon',
    'hyundai getz prime', 'hyundai grand i10',
    'hyundai grand i10 nios', 'hyundai i10', 'hyundai i20',
    'hyundai i20 active', 'hyundai new elantra', 'hyundai new santro',
    'hyundai santa fe', 'hyundai santro', 'hyundai santro xing',
    'hyundai sonata transform', 'hyundai tucson new', 'hyundai venue',
    'hyundai verna', 'hyundai xcent', 'isuzu d-max v cross',
    'isuzu mu-7', 'jeep compass', 'kia seltos', 'mahindra bolero',
    'mahindra e2o', 'mahindra kuv100', 'mahindra marazzo',
    'mahindra maxximo', 'mahindra nuvosport', 'mahindra quanto',
    'mahindra renault logan', 'mahindra reva', 'mahindra scorpio',
    'mahindra thar', 'mahindra tuv300', 'mahindra verito',
    'mahindra xuv 3oo', 'mahindra xuv500', 'mahindra xylo',
    'maruti 800', 'maruti a star', 'maruti alto', 'maruti alto 800',
    'maruti alto k10', 'maruti baleno', 'maruti celerio',
    'maruti celerio x', 'maruti ciaz', 'maruti dzire', 'maruti eeco',
    'maruti ertiga', 'maruti esteem', 'maruti ignis',
    'maruti new  wagon-r', 'maruti omni', 'maruti omni e',
    'maruti ritz', 'maruti s cross', 'maruti s presso', 'maruti swift',
    'maruti swift dzire', 'maruti sx4', 'maruti vitara brezza',
    'maruti wagon r', 'maruti wagon r 1.0', 'maruti wagon r duo',
    'maruti wagon r stingray', 'maruti xl6', 'maruti zen',
    'maruti zen estilo', 'mercedes benz a class',
    'mercedes benz c class', 'mercedes benz cla class',
    'mercedes benz cls class', 'mercedes benz e class',
    'mercedes benz gla class', 'mercedes benz ml class', 'mg hector',
    'mg zs ev', 'mitsubishi outlander', 'nissan evalia',
    'nissan micra', 'nissan micra active', 'nissan nissan kicks',
    'nissan sunny', 'nissan terrano', 'opel astra', 'renault captur',
    'renault duster', 'renault fluence', 'renault kwid',
    'renault lodgy', 'renault pulse', 'renault scala',
    'renault triber', 'skoda fabia', 'skoda laura', 'skoda octavia',
    'skoda rapid', 'skoda superb', 'skoda yeti', 'ssangyong rexton',
    'tata aria', 'tata bolt', 'tata harrier', 'tata hexa',
    'tata indica ev2', 'tata indica v2', 'tata indica vista',
    'tata indigo cs', 'tata indigo ecs', 'tata manza', 'tata nano',
    'tata nexon', 'tata safari', 'tata safari storme',
    'tata sumo gold', 'tata tiago', 'tata tigor', 'tata zest',
    'toyota camry', 'toyota corolla', 'toyota corolla altis',
    'toyota etios', 'toyota etios liva', 'toyota fortuner',
    'toyota glanza', 'toyota innova', 'toyota innova crysta',
    'toyota prius', 'toyota yaris', 'volkswagen ameo',
    'volkswagen cross polo', 'volkswagen jetta', 'volkswagen polo',
    'volkswagen vento', 'volvo s60', 'volvo xc 60'
]
citys=[
    'ahmedabad', 'bengaluru', 'chennai', 'faridabad', 'ghaziabad',
    'gurgaon', 'hyderabad', 'kolkata', 'lucknow', 'mumbai',
    'new delhi', 'noida', 'pune'
]

city_re=[
    '-do', 'Unknown', 'agra', 'ahmedabad', 'ahmedabad east',
    'ahmednagar', 'airoli', 'alibag', 'aligarh', 'allahabad', 'ambala',
        'ambernath', 'amravati', 'anand', 'ananthapur', 'arantangi',
        'auraiya', 'aurangabad', 'badaun', 'badlapur', 'bahadurgarh',
        'bahraich', 'balurghat', 'bangalore central',
        'bangalore k r puram', 'bangalore south', 'bangaloresouth',
        'banglore-cafe dly', 'baramati', 'barasat', 'bardoli', 'bareilly',
        'bavla', 'bawal', 'beed', 'belapur', 'belgaum', 'bengaluru',
        'bharuch', 'bhavnagar', 'bhayander', 'bhimavaram', 'bhiwandi',
        'bhiwani', 'bhuj', 'bidadi', 'botad', 'bulandshahar',
        'bulandshahr', 'chandigarh', 'chandrapur', 'charkhi dadri',
        'chengalpattu', 'chennai', 'chennai south', 'chennai west',
        'cheyyar', 'chickballapur', 'chikamagalur', 'chikmagalur', 'dahod',
        'dantewada', 'dehardun', 'delhi', 'delhi west', 'devanahalli',
        'dharwad', 'dharward', 'dombivali', 'east godavari',
        'electronic city', 'eluru', 'etawah', 'faizabad', 'faridabad',
        'gandhi nagar', 'gandhinagar', 'ghaziabad', 'gonda', 'gorakhpur',
        'goregaon', 'goutam  budd  nagar', 'gulbarga', 'guntur', 'gurgaon',
        'hardoi', 'haridwar', 'hathras', 'himatnagar', 'hisar', 'hosur',
        'howrah', 'hyderabad', 'jalandhar', 'jalgaon', 'jamnagar',
        'jhajjar', 'jhalawar', 'kaithal', 'kakinada', 'kalamboli',
        'kalwan', 'kalyan', 'kanchipuram', 'kanpur', 'karad', 'karaikudi',
        'karnal', 'karwar', 'kashipur', 'khambhalia', 'kharagpur',
        'kharghar', 'khopoli', 'kolar', 'kolhapur', 'kolkata',
        'kolkatta south', 'kurnool', 'latur', 'lucknow', 'madikeri',
        'madurai', 'madurantakam', 'mahad', 'mahendragarh', 'mahesana',
        'malvani', 'mangalore', 'mathura', 'meerut', 'meham', 'mehsana',
        'mira road', 'mumbai', 'mumbai atc', 'mumbai east', 'mumbai west',
        'muzafarnagar', 'muzaffarnagar', 'mysore', 'nadiad', 'nagpur',
        'nalasopara', 'nashik', 'navi mumbai', 'navimumbai', 'navsari',
        'nerul', 'new delhi', 'neyveli', 'noida', 'osmanabad', 'palanpur',
        'palghar', 'pali', 'palwal', 'panchkula', 'panipat', 'panvel',
        'patan', 'pen', 'pratapgarh', 'proddatur', 'pudukkottai', 'pune',
        'raebarely', 'raigarh', 'raipur', 'rajahmundry', 'rajkot',
        'rajpipala', 'rampur', 'ranchi', 'rangareddy', 'ranipet',
        'ratnagiri', 'ravulapalam', 'rewari', 'rohtak', 'rothak', 'sagar',
        'saharanpur', 'salem', 'sanpada', 'satara', 'sholinganallur',
        'shrirampur', 'shriwardhan', 'sindhudurg', 'sitapur', 'sivagangai',
        'sohana', 'solapur', 'sonepat', 'sonipat', 'srikakulam',
        'sriperumbudur', 'sultanpur', 'surat', 'surendranagar',
        'tadepalligudem', 'thane', 'thane (w)', 'thanjavur',
        'tiruchirappalli', 'tirupati', 'tirupattur', 'tiruppur',
        'tiruvallur', 'tiruvananamalai', 'tiruvannamalai', 'trichy',
        'tumkur', 'udupi', 'ulhasnagar', 'ullal', 'vadodara', 'valsad',
        'vasai', 'vashi', 'vellore', 'vijayawada', 'virar', 'virudhunagar',
        'visakhapatnam', 'vishakapatnam', 'vishakhapatanam', 'wada',
        'yamunanagar', 'yavatmal'
]

state=[
        'Unknown', 'andhra pradesh', 'chandigarh', 'chhattisgarh', 'delhi',
        'gujarat', 'haryana', 'jharkhand', 'karnataka', 'maharashtra',
        'punjab', 'rajasthan', 'tamil nadu', 'telangana', 'uttar pradesh',
        'uttarakhand', 'west bengal'
]


com=[
    'audi', 'bmw', 'chevrolet', 'datsun', 'fiat', 'ford', 'honda',
        'hyundai', 'isuzu', 'jeep', 'kia', 'mahindra', 'mahindra renault',
        'maruti', 'mercedes benz', 'mg', 'mitsubishi', 'nissan', 'opel',
        'renault', 'skoda', 'ssangyong', 'tata', 'toyota', 'volkswagen',
        'volvo'
]

models=[
    '3 series', '5 series', '800', 'a class', 'a star', 'a3', 'a4',
        'a6', 'accent', 'accord', 'alto', 'alto 800', 'alto k10', 'amaze',
        'ameo', 'aria', 'astra', 'aura', 'aveo u va', 'baleno', 'beat',
        'bolero', 'bolt', 'br-v', 'brio', 'c class', 'camry', 'captur',
        'celerio', 'celerio x', 'ciaz', 'city', 'city zx', 'civic',
        'cla class', 'cls class', 'compass', 'corolla', 'corolla altis',
        'creta', 'cross polo', 'cruze', 'crv', 'd-max v cross', 'duster',
        'dzire', 'e 20', 'e class', 'ecosport', 'eeco', 'elite i20',
        'enjoy', 'eon', 'ertiga', 'esteem', 'etios', 'etios liva',
        'evalia', 'fabia', 'fiesta', 'fiesta classic', 'figo',
        'figo aspire', 'fluence', 'fortuner', 'freestyle', 'getz prime',
        'gla class', 'glanza', 'go', 'go plus', 'grand i10',
        'grand i10 nios', 'grand punto', 'harrier', 'hector', 'hexa',
        'i10', 'i20', 'i20 active', 'ignis', 'ikon', 'indica ev2',
        'indica v2', 'indica vista', 'indigo cs', 'indigo ecs', 'innova',
        'innova crysta', 'jazz', 'jetta', 'kicks', 'kuv100', 'kwid',
        'laura', 'linea', 'lodgy', 'logan', 'manza', 'marazzo', 'maxximo ',
        'micra', 'micra active', 'ml class', 'mobilio', 'mu-7', 'nano',
        'new  wagon-r', 'new elantra', 'new figo', 'new santro', 'nexon ',
        'nuvosport', 'octavia', 'omni', 'omni e', 'optra', 'optra magnum',
        'outlander', 'polo', 'prius', 'pulse', 'punto evo', 'punto pure ',
        'q3', 'quanto', 'rapid', 'redi go', 'reva', 'rexton', 'ritz',
        's cross', 's presso', 's60', 'safari', 'safari storme',
        'sail uva', 'santa fe', 'santro', 'santro xing', 'scala',
        'scorpio', 'seltos', 'sonata transform', 'spark', 'sumo gold',
        'sunny', 'superb', 'swift', 'swift dzire', 'sx4', 'terrano',
        'thar', 'tiago', 'tigor', 'triber', 'tucson new', 'tuv300',
        'vento', 'venue', 'verito', 'verna', 'vitara brezza', 'wagon r',
        'wagon r 1.0', 'wagon r duo', 'wagon r stingray', 'wr-v', 'x1',
        'x3', 'xc60', 'xcent', 'xl6', 'xuv 3oo', 'xuv500', 'xylo', 'yaris',
        'yeti', 'zen', 'zen estilo', 'zest', 'zs ev'
]
# # # Define a function for encoding categorical features
# # def encode_features(df):
# #     # Example encoding (you need to adjust this based on how your model was trained)
# #     # Convert categorical variables to dummy/indicator variables
# #     df_encoded = pd.get_dummies(df, drop_first=True)
# #     return df_encoded

# # Define the main function for the Streamlit app

# st.title("Car Price Prediction")
# st.write("Enter the details of the car to predict its price:")

#     # User inputs
# car_name = st.text_input('Car Name')
# yr_mfr = st.number_input('Year of Manufacture', min_value=1900, max_value=2024, value=2015)
# fuel_type = st.selectbox('Fuel Type', ['diesel', 'electric', 'petrol', 'petrol & cng', 'petrol & lpg'])
# kms_run = st.number_input('Kilometers Run', min_value=0, value=50000)
# city = st.selectbox('City',[
#     'ahmedabad', 'bengaluru', 'chennai', 'faridabad', 'ghaziabad',
#     'gurgaon', 'hyderabad', 'kolkata', 'lucknow', 'mumbai',
#     'new delhi', 'noida', 'pune'
# ])
# body_type = st.selectbox('Body Type',['Unknown', 'hatchback', 'luxury sedan', 'luxury suv', 'sedan','suv'])
# transmission = st.selectbox('Transmission', ['Unknown', 'automatic', 'manual'])
# registered_city = st.selectbox('Registered City',[
#     '-do', 'Unknown', 'agra', 'ahmedabad', 'ahmedabad east',
#     'ahmednagar', 'airoli', 'alibag', 'aligarh', 'allahabad', 'ambala',
#         'ambernath', 'amravati', 'anand', 'ananthapur', 'arantangi',
#         'auraiya', 'aurangabad', 'badaun', 'badlapur', 'bahadurgarh',
#         'bahraich', 'balurghat', 'bangalore central',
#         'bangalore k r puram', 'bangalore south', 'bangaloresouth',
#         'banglore-cafe dly', 'baramati', 'barasat', 'bardoli', 'bareilly',
#         'bavla', 'bawal', 'beed', 'belapur', 'belgaum', 'bengaluru',
#         'bharuch', 'bhavnagar', 'bhayander', 'bhimavaram', 'bhiwandi',
#         'bhiwani', 'bhuj', 'bidadi', 'botad', 'bulandshahar',
#         'bulandshahr', 'chandigarh', 'chandrapur', 'charkhi dadri',
#         'chengalpattu', 'chennai', 'chennai south', 'chennai west',
#         'cheyyar', 'chickballapur', 'chikamagalur', 'chikmagalur', 'dahod',
#         'dantewada', 'dehardun', 'delhi', 'delhi west', 'devanahalli',
#         'dharwad', 'dharward', 'dombivali', 'east godavari',
#         'electronic city', 'eluru', 'etawah', 'faizabad', 'faridabad',
#         'gandhi nagar', 'gandhinagar', 'ghaziabad', 'gonda', 'gorakhpur',
#         'goregaon', 'goutam  budd  nagar', 'gulbarga', 'guntur', 'gurgaon',
#         'hardoi', 'haridwar', 'hathras', 'himatnagar', 'hisar', 'hosur',
#         'howrah', 'hyderabad', 'jalandhar', 'jalgaon', 'jamnagar',
#         'jhajjar', 'jhalawar', 'kaithal', 'kakinada', 'kalamboli',
#         'kalwan', 'kalyan', 'kanchipuram', 'kanpur', 'karad', 'karaikudi',
#         'karnal', 'karwar', 'kashipur', 'khambhalia', 'kharagpur',
#         'kharghar', 'khopoli', 'kolar', 'kolhapur', 'kolkata',
#         'kolkatta south', 'kurnool', 'latur', 'lucknow', 'madikeri',
#         'madurai', 'madurantakam', 'mahad', 'mahendragarh', 'mahesana',
#         'malvani', 'mangalore', 'mathura', 'meerut', 'meham', 'mehsana',
#         'mira road', 'mumbai', 'mumbai atc', 'mumbai east', 'mumbai west',
#         'muzafarnagar', 'muzaffarnagar', 'mysore', 'nadiad', 'nagpur',
#         'nalasopara', 'nashik', 'navi mumbai', 'navimumbai', 'navsari',
#         'nerul', 'new delhi', 'neyveli', 'noida', 'osmanabad', 'palanpur',
#         'palghar', 'pali', 'palwal', 'panchkula', 'panipat', 'panvel',
#         'patan', 'pen', 'pratapgarh', 'proddatur', 'pudukkottai', 'pune',
#         'raebarely', 'raigarh', 'raipur', 'rajahmundry', 'rajkot',
#         'rajpipala', 'rampur', 'ranchi', 'rangareddy', 'ranipet',
#         'ratnagiri', 'ravulapalam', 'rewari', 'rohtak', 'rothak', 'sagar',
#         'saharanpur', 'salem', 'sanpada', 'satara', 'sholinganallur',
#         'shrirampur', 'shriwardhan', 'sindhudurg', 'sitapur', 'sivagangai',
#         'sohana', 'solapur', 'sonepat', 'sonipat', 'srikakulam',
#         'sriperumbudur', 'sultanpur', 'surat', 'surendranagar',
#         'tadepalligudem', 'thane', 'thane (w)', 'thanjavur',
#         'tiruchirappalli', 'tirupati', 'tirupattur', 'tiruppur',
#         'tiruvallur', 'tiruvananamalai', 'tiruvannamalai', 'trichy',
#         'tumkur', 'udupi', 'ulhasnagar', 'ullal', 'vadodara', 'valsad',
#         'vasai', 'vashi', 'vellore', 'vijayawada', 'virar', 'virudhunagar',
#         'visakhapatnam', 'vishakapatnam', 'vishakhapatanam', 'wada',
#         'yamunanagar', 'yavatmal'
# ])
# registered_state = st.selectbox('Registered State',[
#         'Unknown', 'andhra pradesh', 'chandigarh', 'chhattisgarh', 'delhi',
#         'gujarat', 'haryana', 'jharkhand', 'karnataka', 'maharashtra',
#         'punjab', 'rajasthan', 'tamil nadu', 'telangana', 'uttar pradesh',
#         'uttarakhand', 'west bengal'
# ])
# is_hot = st.selectbox('Is In Demand',['False',' True'])
# rto = st.text_input('RTO')
# make = st.selectbox('Make',[
#     'audi', 'bmw', 'chevrolet', 'datsun', 'fiat', 'ford', 'honda',
#         'hyundai', 'isuzu', 'jeep', 'kia', 'mahindra', 'mahindra renault',
#         'maruti', 'mercedes benz', 'mg', 'mitsubishi', 'nissan', 'opel',
#         'renault', 'skoda', 'ssangyong', 'tata', 'toyota', 'volkswagen',
#         'volvo'
# ])
# model = st.selectbox('Model',[
#     '3 series', '5 series', '800', 'a class', 'a star', 'a3', 'a4',
#         'a6', 'accent', 'accord', 'alto', 'alto 800', 'alto k10', 'amaze',
#         'ameo', 'aria', 'astra', 'aura', 'aveo u va', 'baleno', 'beat',
#         'bolero', 'bolt', 'br-v', 'brio', 'c class', 'camry', 'captur',
#         'celerio', 'celerio x', 'ciaz', 'city', 'city zx', 'civic',
#         'cla class', 'cls class', 'compass', 'corolla', 'corolla altis',
#         'creta', 'cross polo', 'cruze', 'crv', 'd-max v cross', 'duster',
#         'dzire', 'e 20', 'e class', 'ecosport', 'eeco', 'elite i20',
#         'enjoy', 'eon', 'ertiga', 'esteem', 'etios', 'etios liva',
#         'evalia', 'fabia', 'fiesta', 'fiesta classic', 'figo',
#         'figo aspire', 'fluence', 'fortuner', 'freestyle', 'getz prime',
#         'gla class', 'glanza', 'go', 'go plus', 'grand i10',
#         'grand i10 nios', 'grand punto', 'harrier', 'hector', 'hexa',
#         'i10', 'i20', 'i20 active', 'ignis', 'ikon', 'indica ev2',
#         'indica v2', 'indica vista', 'indigo cs', 'indigo ecs', 'innova',
#         'innova crysta', 'jazz', 'jetta', 'kicks', 'kuv100', 'kwid',
#         'laura', 'linea', 'lodgy', 'logan', 'manza', 'marazzo', 'maxximo ',
#         'micra', 'micra active', 'ml class', 'mobilio', 'mu-7', 'nano',
#         'new  wagon-r', 'new elantra', 'new figo', 'new santro', 'nexon ',
#         'nuvosport', 'octavia', 'omni', 'omni e', 'optra', 'optra magnum',
#         'outlander', 'polo', 'prius', 'pulse', 'punto evo', 'punto pure ',
#         'q3', 'quanto', 'rapid', 'redi go', 'reva', 'rexton', 'ritz',
#         's cross', 's presso', 's60', 'safari', 'safari storme',
#         'sail uva', 'santa fe', 'santro', 'santro xing', 'scala',
#         'scorpio', 'seltos', 'sonata transform', 'spark', 'sumo gold',
#         'sunny', 'superb', 'swift', 'swift dzire', 'sx4', 'terrano',
#         'thar', 'tiago', 'tigor', 'triber', 'tucson new', 'tuv300',
#         'vento', 'venue', 'verito', 'verna', 'vitara brezza', 'wagon r',
#         'wagon r 1.0', 'wagon r duo', 'wagon r stingray', 'wr-v', 'x1',
#         'x3', 'xc60', 'xcent', 'xl6', 'xuv 3oo', 'xuv500', 'xylo', 'yaris',
#         'yeti', 'zen', 'zen estilo', 'zest', 'zs ev'
# ])
# total_owners = st.number_input('Total Owners', min_value=0, value=1)
# fitness_certificate = st.selectbox('Fitness Certificate',['False', 'True', 'Unknown'])

#     # Prepare the input data as a DataFrame+++-
# if st.button('Predict'):    
#     features={
#         'Car Name': car_name,
#         'Year of Manufacture': yr_mfr,
#         'Fuel Type': fuel_type,
#         'Kilometers Run': kms_run,
#         'City': city,
#         'Body Type': body_type,
#         'Transmission': transmission,
#         'Registered City': registered_city,
#         'Registered State': registered_state,
#         'Is In Demand': is_hot,
#         'RTO': rto,
#         'Make': make,
#         'Model': model,
#         'Total Owners': total_owners,
#         'Fitness Certificate': fitness_certificate
#     }

#     # Encode the features
#     input_df = pd.DataFrame([features])

#     # Ensure that the encoded input data has the same columns as the training data
#     predicted_price = model.predict(input_df)[0]
#     st.subheader(f'Predicted Price: {predicted_price:.2f}')
#     # Reorder columns to match the training data
#     # predicted_price = model.predict(input_df)
     




# import streamlit as st
# import pickle
# import numpy as np

# # Load the model from the .pkl file
# with open('car.pkl', 'rb') as file:
#     model = pickle.load(file)

# # Function to predict car price
# def predict_car_price(features):
#     return model.predict([features])[0]

# # Streamlit app
# st.title('Car Price Predictor')

# # Input fields
# car_name = st.text_input('Car Name')
# yr_mfr = st.number_input('Year of Manufacture', min_value=1900, max_value=2024, step=1)
# fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'Electric', 'Hybrid'])
# kms_run = st.number_input('Kilometers Run', min_value=0)
# city = st.text_input('City')
# body_type = st.selectbox('Body Type', ['Sedan', 'Hatchback', 'SUV', 'Convertible', 'Coupe', 'Minivan', 'Truck'])
# transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
# registered_city = st.text_input('Registered City')
# registered_state = st.text_input('Registered State')
# is_hot = st.selectbox('Is Hot', ['Yes', 'No'])
# rto = st.text_input('RTO')
# make = st.text_input('Make')
# model = st.text_input('Model')
# total_owners = st.number_input('Total Owners', min_value=0)
# fitness_certificate = st.selectbox('Fitness Certificate', ['Yes', 'No'])

# # Predict button
# if st.button('Predict Price'):
#     features = [
#         car_name, yr_mfr, fuel_type, kms_run, city, body_type,
#         transmission, registered_city, registered_state, is_hot,
#         rto, make, model, total_owners, fitness_certificate
#     ]
#     prediction = predict_car_price(features)
#     st.write(f'The predicted sale price of the car is: {prediction}')

# To run the app, use the following command in your terminal:
# streamlit run your_script_name.py

import streamlit as st
import pickle
import pandas as pd

# Load the model from the .pkl file
try:
    with open('anish.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Function to predict car price
def predict_car_price(features):
    try:
        # Convert features to a DataFrame
        columns = [
            'car_name', 'yr_mfr', 'fuel_type', 'kms_run', 'city', 'body_type',
            'transmission', 'registered_city', 'registered_state',
            'rto', 'make', 'model', 'total_owners'
        ]
        features_df = pd.DataFrame([features], columns=columns)
        prediction = model.predict(features_df)[0]
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

# Streamlit app
# st.title('Car Price Predictor')
st.title('🚗 Car Price Predictor 📈')
# Input fields
car_name = st.selectbox('Car Name',car_names)
yr_mfr = st.number_input('Year of Manufacture', min_value=1900, max_value=2024, step=1)
fuel_type = st.selectbox('Fuel Type', ['diesel', 'electric', 'petrol', 'petrol & cng', 'petrol & lpg'])
kms_run = st.number_input('Kilometers Run', min_value=0)
city = st.selectbox('City',citys)
body_type = st.selectbox('Body Type', ['Sedan', 'Hatchback', 'SUV', 'Convertible', 'Coupe', 'Minivan', 'Truck'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
registered_city = st.selectbox('Registered City',city_re)
registered_state = st.selectbox('Registered State',state)
# is_hot = st.selectbox('Is Hot', ['False', 'True'])
rto = st.text_input('RTO')
make = st.selectbox('Make',com)
car_model = st.selectbox('Model',models)  # Renamed to car_model to avoid conflict with model variable
total_owners = st.number_input('Total Owners', min_value=0)
# fitness_certificate = st.selectbox('Fitness Certificate', ['False', 'True', 'Unknown'])

# Predict button
if st.button('Predict Price'):
    features = [
        car_name, yr_mfr, fuel_type, kms_run, city, body_type,
        transmission, registered_city, registered_state,
        rto, make, car_model, total_owners
    ]
    prediction = predict_car_price(features)
    if prediction is not None:
        st.write(f'The predicted sale price of the car is: {prediction}')

# # To run the app, use the following command in your terminal:
# # streamlit run your_script_name.py


# import streamlit as st
# import pickle
# import pandas as pd

# # Load the model from the .pkl file
# try:
#     with open('anish.pkl', 'rb') as file:
#         model = pickle.load(file)
# except Exception as e:
#     st.error(f"Oops! Something went wrong: {e}")
#     st.stop()

# Function to predict car price
# def predict_car_price(features):
#     try:
#         # Convert features to a DataFrame
#         columns = [
#             'Car Name', 'Year of Manufacture', 'Fuel Type', 'Kilometers Run', 'City', 'Body Type',
#             'Transmission', 'Registered City', 'Registered State',
#             'RTO', 'Make', 'Model', 'Total Owners'
#         ]
#         features_df = pd.DataFrame([features], columns=columns)
#         prediction = model.predict(features_df)[0]
#         return prediction
#     except Exception as e:
#         st.error(f"Oops! Prediction failed: {e}")
#         return None

# # Streamlit app
# st.title('🚗 Car Price Predictor 📈')

# Add car image as wallpaper
# st.image('anish.jpg', use_column_width=True)  # Replace 'car_image.jpg' with your image file path

# # Input fields
# car_name = st.selectbox('Car Name', car_names)
# yr_mfr = st.number_input('Year of Manufacture', min_value=1900, max_value=2024, step=1)
# fuel_type = st.selectbox('Fuel Type', ['Diesel', 'Electric', 'Petrol', 'Petrol & CNG', 'Petrol & LPG'])
# kms_run = st.number_input('Kilometers Run', min_value=0)
# city = st.selectbox('City', citys)
# body_type = st.selectbox('Body Type', ['Sedan', 'Hatchback', 'SUV', 'Convertible', 'Coupe', 'Minivan', 'Truck'])
# transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
# registered_city = st.selectbox('Registered City', city_re)
# registered_state = st.selectbox('Registered State', state)
# rto = st.text_input('RTO')
# make = st.selectbox('Make', com)
# car_model = st.selectbox('Model', models)  # Renamed to car_model to avoid conflict with model variable
# total_owners = st.number_input('Total Owners', min_value=0)

# # Predict button
# if st.button('Predict Price'):
#     features = [
#         car_name, yr_mfr, fuel_type, kms_run, city, body_type,
#         transmission, registered_city, registered_state,
#         rto, make, car_model, total_owners
#     ]
#     prediction = predict_car_price(features)
#     if prediction is not None:
#         st.success(f'💰 The predicted sale price of the car is: {prediction}')
# # 