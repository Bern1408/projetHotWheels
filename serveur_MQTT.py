import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
PORT = 1883

TOPIC_RACE = "racepi/race"    #Topic qui reçoit les informations d'une course
TOPIC_RACE_RESULTS = "racepi/results" 
TOPIC_GET_HISTORY = "racepi/get_historique" #Topic de démande de historique
TOPIC_SEND_HISTORY = "racepi/historique"  #Topic d'evoi d'historique

historique_courses = [] #Array qui enregistre les informations des courses

#Fonction de connexion MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[INFO] Connexion réussie au Broker ({BROKER_ADDRESS})")
        client.subscribe(TOPIC_RACE)
        client.subscribe(TOPIC_GET_HISTORY)
        print(F"[INFO] Abonnement aux topics : {TOPIC_RACE} et {TOPIC_GET_HISTORY}")
    else:
        print(f"[ERREUR] Échec de connexion. Code retour : {rc}")

#Fonction de gestion des messages reçues
def on_message(client, userdata, msg):
    donne_recue = msg.payload.decode("utf-8")
    
    #Démande de historique
    if msg.topic == TOPIC_GET_HISTORY:
        client.publish(TOPIC_SEND_HISTORY, str(historique_courses))
        print(f"[PUBLISH] Historique")

    #Données de course
    elif msg.topic == TOPIC_RACE:
        historique_courses.append(str(donne_recue))
        client.publish(TOPIC_RACE_RESULTS, donne_recue)
        print(f"[MESSAGE] Reçu sur {msg.topic} -> {donne_recue}")

#Initialisation du client MQTT
client = mqtt.Client()

#Configuration du client
client.on_connect = on_connect
client.on_message = on_message

#Connexion avec le client MQTT
client.connect(BROKER_ADDRESS, PORT)

print("--- Démarrage du Subscriber (Attente de données...) ---")
client.loop_forever()   #Loop qui garde le client en constant état d'attente de données