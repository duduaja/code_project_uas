import requests
from flask import Flask,render_template,request,url_for
import json
import os

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    Kota = "East+Java"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Tourist+Destination+In+"+Kota+"&type=tourist_attraction&language=en&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_response = json.loads(response.text)

    poi = json_response["results"]

    photoref1 = poi[0]["photos"][0]["photo_reference"]
    photoref2 = poi[1]["photos"][0]["photo_reference"]
    photoref3 = poi[3]["photos"][0]["photo_reference"]
    photoref4 = poi[4]["photos"][0]["photo_reference"]

    urlphoto1 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref1+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto2 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref2+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto3 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref3+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto4 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref4+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"

    responsephoto1 = requests.get(urlphoto1)
    responsephoto2 = requests.get(urlphoto2)
    responsephoto3 = requests.get(urlphoto3)
    responsephoto4 = requests.get(urlphoto4)


    photo1 = open('static/img/Foto_Lokasi1.jpg',"wb")
    photo1.write(responsephoto1.content)
    photo1.close()

    photo2 = open('static/img/Foto_Lokasi2.jpg',"wb")
    photo2.write(responsephoto2.content)
    photo2.close()

    photo3 = open('static/img/Foto_Lokasi3.jpg',"wb")
    photo3.write(responsephoto3.content)
    photo3.close()

    photo4 = open('static/img/Foto_Lokasi4.jpg',"wb")
    photo4.write(responsephoto4.content)
    photo4.close()

    destinationname1 = poi[0]["name"]
    destinationname2 = poi[1]["name"]
    destinationname3 = poi[3]["name"]
    destinationname4 = poi[4]["name"]

    url_maps1="http://maps.google.com/?q="+destinationname1.replace(" ","+")+"+"+Kota
    url_maps2="http://maps.google.com/?q="+destinationname2.replace(" ","+")+"+"+Kota
    url_maps3="http://maps.google.com/?q="+destinationname3.replace(" ","+")+"+"+Kota
    url_maps4="http://maps.google.com/?q="+destinationname4.replace(" ","+")+"+"+Kota
    

    DetailLokasi1 = {
        "name" : poi[0]["name"],
        "placeid":poi[0]["place_id"],
        "rating":poi[0]["rating"],
        "totalrating":poi[0]["user_ratings_total"],
        "address":poi[0]["formatted_address"],
        "photo":photo1,
        "maps": url_maps1
    }
    DetailLokasi2 = {
        "name" : poi[1]["name"],
        "placeid":poi[1]["place_id"],
        "rating":poi[1]["rating"],
        "totalrating":poi[1]["user_ratings_total"],
        "address":poi[1]["formatted_address"],
        "photo":photo2,
        "maps": url_maps2
    }
    DetailLokasi3 = {
        "name" : poi[3]["name"],
        "placeid":poi[3]["place_id"],
        "rating":poi[3]["rating"],
        "totalrating":poi[3]["user_ratings_total"],
        "address":poi[3]["formatted_address"],
        "photo":photo3,
        "maps": url_maps3
    }
    DetailLokasi4 = {
        "name" : poi[4]["name"],
        "placeid":poi[4]["place_id"],
        "rating":poi[4]["rating"],
        "totalrating":poi[4]["user_ratings_total"],
        "address":poi[4]["formatted_address"],
        "photo":photo4,
        "maps": url_maps4
    }
    return render_template('startingpage.html',Kota=Kota,DetailLokasi1=DetailLokasi1,DetailLokasi2=DetailLokasi2,DetailLokasi3=DetailLokasi3,DetailLokasi4=DetailLokasi4)

@app.route('/aboutus.html')
def abouts():
    return render_template("aboutus.html")

@app.route('/hasil', methods=['POST','GET'])
def get_poi():
    Kota = request.form['kota']
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=Tourists+Destinations+In+"+Kota+"&type=tourist_attraction&language=en&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_response = json.loads(response.text)

    poi = json_response["results"]

    photoref1 = poi[0]["photos"][0]["photo_reference"]
    photoref2 = poi[1]["photos"][0]["photo_reference"]
    photoref3 = poi[2]["photos"][0]["photo_reference"]
    photoref4 = poi[3]["photos"][0]["photo_reference"]

    urlphoto1 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref1+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto2 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref2+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto3 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref3+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"
    urlphoto4 = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=900&maxheight=900&photo_reference="+photoref4+"&key=AIzaSyCDBFhximQ7r34GQIfZTa6MzKbVRBsRDFs"

    responsephoto1 = requests.get(urlphoto1)
    responsephoto2 = requests.get(urlphoto2)
    responsephoto3 = requests.get(urlphoto3)
    responsephoto4 = requests.get(urlphoto4)


    photo1 = open('static/img/Foto_Lokasi1.jpg',"wb")
    photo1.write(responsephoto1.content)
    photo1.close()

    photo2 = open('static/img/Foto_Lokasi2.jpg',"wb")
    photo2.write(responsephoto2.content)
    photo2.close()

    photo3 = open('static/img/Foto_Lokasi3.jpg',"wb")
    photo3.write(responsephoto3.content)
    photo3.close()

    photo4 = open('static/img/Foto_Lokasi4.jpg',"wb")
    photo4.write(responsephoto4.content)
    photo4.close()

    destinationname1 = poi[0]["name"]
    destinationname2 = poi[1]["name"]
    destinationname3 = poi[3]["name"]
    destinationname4 = poi[4]["name"]

    url_maps1="http://maps.google.com/?q="+destinationname1.replace(" ","+")+"+"+Kota
    url_maps2="http://maps.google.com/?q="+destinationname2.replace(" ","+")+"+"+Kota
    url_maps3="http://maps.google.com/?q="+destinationname3.replace(" ","+")+"+"+Kota
    url_maps4="http://maps.google.com/?q="+destinationname4.replace(" ","+")+"+"+Kota
    

    DetailLokasi1 = {
        "name" : poi[0]["name"],
        "placeid":poi[0]["place_id"],
        "rating":poi[0]["rating"],
        "totalrating":poi[0]["user_ratings_total"],
        "address":poi[0]["formatted_address"],
        "photo":photo1,
        "maps": url_maps1
    }
    DetailLokasi2 = {
        "name" : poi[1]["name"],
        "placeid":poi[1]["place_id"],
        "rating":poi[1]["rating"],
        "totalrating":poi[1]["user_ratings_total"],
        "address":poi[1]["formatted_address"],
        "photo":photo2,
        "maps": url_maps2
    }
    DetailLokasi3 = {
        "name" : poi[2]["name"],
        "placeid":poi[2]["place_id"],
        "rating":poi[2]["rating"],
        "totalrating":poi[2]["user_ratings_total"],
        "address":poi[2]["formatted_address"],
        "photo":photo3,
        "maps": url_maps3
    }
    DetailLokasi4 = {
        "name" : poi[3]["name"],
        "placeid":poi[3]["place_id"],
        "rating":poi[3]["rating"],
        "totalrating":poi[3]["user_ratings_total"],
        "address":poi[3]["formatted_address"],
        "photo":photo4,
        "maps": url_maps4
    }
    return render_template('indexhasil.html',Kota=Kota,DetailLokasi1=DetailLokasi1,DetailLokasi2=DetailLokasi2,DetailLokasi3=DetailLokasi3,DetailLokasi4=DetailLokasi4)