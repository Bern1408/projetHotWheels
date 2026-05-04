import paho.mqtt.client as mqtt
import time
import os

BROKER_ADDRESS = "localhost"
TOPIC_NAME = "lab8/alerte"
GET_HISTORY = "lab8/get_historique"
HISTORY = "lab8/historique"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[INFO] Connexion réussie au Broker ({BROKER_ADDRESS})")
        client.subscribe(HISTORY)
        print(F"[INFO] Abonnement au topic : {HISTORY}\n")
    else:
        print(f"[ERREUR] Échec de connexion. Code retour : {rc}")

def on_message(cliet, userdata, msg):
    donne_recue = (msg.payload.decode("utf-8"))
    print(f"[Historique] Reçu sur {msg.topic} -> {donne_recue}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER_ADDRESS, 1883)
    print(f"Connecté au Broker. Envoi sur le topic : {TOPIC_NAME}")

    client.loop_start()
    time.sleep(0.5)

    cpt = 1
    choix = 0
    while True:
        print('=======MENU=======\n1 = alarme(écrire)\n2 = alarme(automatique)\n3 = historique\n')
        choix = input("Votre choix : ")
        
        if choix == '1' or choix == '2':
            if choix == '1':
                zone_incident = input("\nSaisir zone de l'incident: ")
                heure_incident = time.strftime('%H:%M')
                #heure_incident = input("Saisir heure de l'incident: ")
            elif choix == '2':
                zone_incident = "Salon"
                heure_incident = "12:00"
            test_incident = {"zone":zone_incident,"heure":heure_incident}
            message = f"(ALERTE # {cpt}) {test_incident}"

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
