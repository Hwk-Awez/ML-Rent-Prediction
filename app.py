from math import *
from flask import Flask,render_template,request

states=['Uttar Pradesh', 'Assam', 'Bihar', 'Karnataka', 'Kerala', 'Odisha', 'Delhi', 'Madhya Pradesh', 'Maharashtra', 'Telangana', 'Andhra Pradesh', 'Rajasthan', 'West Bengal', 'Andaman and Nicobar Islands', 'Chhattisgarh', 'Jharkhand', 'Tripura', 'Chandigarh', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Meghalaya', 'Punjab', 'Tamil Nadu', 'Uttarakhand', 'Puducherry']

furnished=['Fully-furnished', 'Semi-furnished', 'Non-furnished']

#final={'floors': -0.8160249161987986, 'bathrooms': 1.0379926583090182, 'bedrooms': -70.49179316058473, 'parkings': -0.7039849659596787, 'area': -91.70875248607305, 'Semi-furnished': 12.099837547212514, 'Non-furnished': 0, 'Fully-furnished': -21.284903641667626, 'Andhra Pradesh': 1.8398246327445122, 'Assam': 0.06185755168195818, 'Bihar': 5.042119423421269, 'Chandigarh': 0.35442715221939425, 'Chhattisgarh': 0.5922174671884016, 'Delhi': 1.1847895018699763, 'Gujarat': -0.26493834504944097, 'Haryana': 0.20732488538250488, 'Himachal Pradesh': -0.26560189691053515, 'Jammu and Kashmir': -0.12891159677130856, 'Jharkhand': 1.8839176285938755, 'Karnataka': -0.3982004542880652, 'Kerala': 0.7419387472738814, 'Madhya Pradesh': 2.7798084074261546, 'Maharashtra': 1.5528882639018493, 'Meghalaya': 0.3052295302898248, 'Odisha': -4.128480385453984, 'Puducherry': 0.6825310808471278, 'Punjab': -1.0946399962292797, 'Rajasthan': -1.3669641212231143, 'Tamil Nadu': 5.6917244303481205, 'Telangana': -7.25093283537427, 'Tripura': 0.5905857986631158, 'Uttar Pradesh': -2.246336339796662, 'Uttarakhand': 0.5110347576767628, 'West Bengal': -6.098259492289008}

final={'floors': 0.5550448278022724, 'bathrooms': 0.9678752246229948, 'bedrooms': -13.521382109965508, 'parkings': 0.4829329550472194, 'area': -19.231658708250443,'Non-furnished':0, 'Semi-furnished': -2.5348768218608653, 'Fully-furnished': -5.7852074120275665, 'Andhra Pradesh': -1.399156406099987, 'Assam': 0.4420852925300147, 'Bihar': -3.20050124481432, 'Chhattisgarh': 0.6686772085681753, 'Delhi': -0.8180772522176213, 'Haryana': 0.10193038102306717, 'Jharkhand': -2.1652575010263564, 'Karnataka': 1.336747197236203, 'Kerala': 0.9996464752602311, 'Madhya Pradesh': -0.661570411268957, 'Maharashtra': -1.5214504859902651, 'Meghalaya': 0.20233053349814503, 'Odisha': -0.18796266140409526, 'Puducherry': 0.2430903927453813, 'Punjab': 0.6680535102437353, 'Rajasthan': -1.6731294375163452, 'Tamil Nadu': 3.8007620908130972, 'Telangana': -0.49290658292052403, 'Tripura': 0.15722179666026914, 'Uttar Pradesh': -0.4370995199731656, 'Uttarakhand': -0.09867414613026751, 'West Bengal': 2.1980762501608}

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():

    finalrent=0

    if request.method=='POST':

        finalrent=0

        state=request.form.get('states')
        furnish=request.form.get('furnishing')
        floors=float(request.form.get('floors'))
        bathrooms=float(request.form.get('bathrooms'))
        bedrooms=float(request.form.get('bedrooms'))
        parkings=float(request.form.get('parkings'))
        area=float(request.form.get('area'))

        #Problem: All form values come as strings,convert to integere or float first...

        finalrent += final[state]
        finalrent += final[furnish]
        finalrent += floors * final['floors']
        finalrent += bathrooms * final['bathrooms']
        finalrent += bedrooms * final['bedrooms']
        finalrent += parkings * final['parkings']
        finalrent += area * final['area']

        finalrent=round(finalrent,2)
        if(finalrent < 0):
            finalrent *= -1


        return render_template('index.html',states=states,finalrent=finalrent,furnished=furnished)
    return render_template('index.html',states=states,finalrent=finalrent,furnished=furnished)