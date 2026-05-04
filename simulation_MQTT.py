import paho.mqtt.client as mqtt
from datetime import timedelta
import time
import json
import os

BROKER_ADDRESS = "localhost"
PORT = 1883
TOPIC_NAME = "racepi/course"
GET_HISTORY = "racepi/get_historique"
HISTORY = "racepi/historique"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[INFO] Connexion réussie au Broker ({BROKER_ADDRESS})")
        client.subscribe(HISTORY)
        print(F"[INFO] Abonnement au topic : {HISTORY}\n")
    else:
        print(f"[ERREUR] Échec de connexion. Code retour : {rc}")

def on_message(cliet, userdata, msg):
    donne_recue = (msg.payload.decode("utf-8"))
    print(f"[Historique] Reçu sur {msg.topic} :")
    donne_recue = json.loads(donne_recue)
    for data in donne_recue:
        print(data)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER_ADDRESS, PORT)
    print(f"Connecté au Broker. Envoi sur le topic : {TOPIC_NAME}")

    client.loop_start()
    time.sleep(0.5)

    cpt = 1
    choix = 0
    while True:
        print('=======MENU=======\n1 = Données course(écrire)\n2 = Données course(automatique)\n3 = historique\n')
        choix = input("Votre choix : ")
        
        if choix == '1' or choix == '2':
            if choix == '1':
                id = input("\nSaisir nom du pilote/voiture : ")

                capteur1 = input("C1 : appuyez une touche")
                heure_depart = time.strftime('%H:%M')
                depart = time.monotonic()
                capteur1 = str(timedelta(seconds=(time.monotonic() - depart))).split(':')[1] + ":" + str(timedelta(seconds=(time.monotonic() - depart))).split(':')[2]

                capteur2 = input("C2 : appuyez une touche")
                capteur2 = str(timedelta(seconds=(time.monotonic() - depart))).split(':')[1] + ":" + str(timedelta(seconds=(time.monotonic() - depart))).split(':')[2]

                capteur3 = input("C3 : appuyez une touche")
                capteur3 = str(timedelta(seconds=(time.monotonic() - depart))).split(':')[1] + ":" + str(timedelta(seconds=(time.monotonic() - depart))).split(':')[2]

                capteur4 = input("C4 : appuyez une touche")
                capteur4 = str(timedelta(seconds=(time.monotonic() - depart))).split(':')[1] + ":" + str(timedelta(seconds=(time.monotonic() - depart))).split(':')[2]
            elif choix == '2':
                id = "Bot"
                heure_depart = "12:00"
                capteur1 = "01:03.345014"
                capteur2 = "03:64.230482"
                capteur3 = "06:01.023948"
                capteur4 = "08:12.043651"
            test_course = {"id":id,"c1":capteur1,"c2":capteur2,"c3":capteur3,"c4":capteur4,"heure":heure_depart}
            message = f"(COURSE # {cpt}) {test_course}"

            client.publish(TOPIC_NAME, message)
            print(f"[PUBLISH] {message}")
            
            cpt += 1
        elif choix == '3':
            client.publish(GET_HISTORY, "historique")
            time.sleep(0.25)
        
        input("\nAppuyez ENTRÉE pour retourner au menu")
        os.system('cls' if os.name == 'nt' else 'clear')    

except KeyboardInterrupt:
    print("\n[STOP] Déconnexion du client...")
    client.disconnect()
