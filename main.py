import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import time
import folium
import webbrowser  # Importez la bibliothèque webbrowser
from gtts import gTTS
import playsound

key = "****************************"  #Geocoder API Key needs to paste here "your key"
number = "+*******************"
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
#print(service_name)
while True:

    geocoder = OpenCageGeocode(key)
    query = str(location)
    result = geocoder.geocode(query)
    #print(result)

    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    print("votre attitude est {}".format(lat),"et","votre longtitude est {}".format(lng))





# Coordonnées de quelques points (latitude, longitude)
    locations = [
        
             (36.8075, 10.1761),  # Station 1
             (36.8237, 10.1604),  # Station 2
             (36.8042, 10.1723),  # Station 3
             (36.8139, 10.1856),  # Station 4
                 
            ]

# Création de la carte centrée sur une coordonnée de départ
    map_center = (36.8964, 10.1866)   # Coordonnées de Petite Ariana, Tunis
    my_map = folium.Map(location=map_center, zoom_start=3)
    folium.Marker(map_center,icon=folium.Icon(color='red')).add_to(my_map)
# Ajout des marqueurs pour chaque emplacement
    for loc in locations:
        folium.Marker(location=loc).add_to(my_map)
        

# Sauvegarde de la carte au format HTML
    file_path = "locations_map.html"
    my_map.save(file_path)

# Ouvrir automatiquement le fichier dans Google Chrome
    webbrowser.get("firefox").open(file_path)  # Assurez-vous que Chrome est votre navigateur par défaut
   
    if(lat, lng) in locations :
        # Le message de code à convertir en voix
                    
            code_message = """ vous avez arrivée au station de bus """

                # Convertir le message de code en voix
            tts = gTTS(text=code_message, lang='fr')  # 'fr' pour le français
            tts.save('code_message.mp3')  # Enregistrer le fichier audio

                # Lire le fichier audio à travers le casque
            playsound.playsound('code_message.mp3')




    time.sleep(10)


