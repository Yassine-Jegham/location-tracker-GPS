# location-tracker-GPS
Ce script Python utilise la bibliothèque phonenumbers pour extraire des informations de localisation et de fournisseur de services à partir d'un numéro de téléphone spécifié. Il utilise ensuite l'API OpenCage Geocoder pour convertir ces informations en coordonnées géographiques (latitude et longitude). Ces coordonnées sont affichées sur une carte interactive créée avec la bibliothèque Folium. Si les coordonnées correspondent à l'une des gares de bus précisées dans la liste, le code génère une notification vocale pour informer de l'arrivée à la gare de bus. Le code s'exécute en boucle infinie pour une surveillance continue de la localisation. Assurez-vous de personnaliser la liste des stations de bus et de remplacer la clé d'API OpenCage par la vôtre pour l'utilisation correcte de l'API. Ce code peut être utile pour le suivi de localisation en temps réel avec des notifications vocales.

# Requirements
* Python 3.x
* PyTorch
* OpenCV
* YOLOv5
* roboflow
* ultralytics
* torch
* Pillow
* tensorboard

# References
[ [YOLOv5]]https://github.com/ultralytics/yolov5

[[[ roboflow ]] ]https://roboflow.com/

# Resultats
