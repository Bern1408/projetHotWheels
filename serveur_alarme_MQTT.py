import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
PORT = 1883
TOPIC_NAME = "lab8/alerte"
GET_HISTORY = "lab8/get_historique"
SEND_HISTORY = "lab8/historique"

historique_incidents = []

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[INFO] Connexion réussie au Broker ({BROKER_ADDRESS})")
        client.subscribe(TOPIC_NAME)
        client.subscribe(GET_HISTORY)
        print(F"[INFO] Abonnement aux topics : {TOPIC_NAME} et {GET_HISTORY}")
    else:
        print(f"[ERREUR] Échec de connexion. Code retour : {rc}")

def on_message(cliet, userdata, msg):
    donne_recue = msg.payload.decode("utf-8")
    historique_incidents.append(donne_recue)

    if msg.topic == GET_HISTORY:
        client.publish(SEND_HISTORY, str(historique_incidents))
        print(f"[PUBLISH] Historique")
    elif msg.topic == TOPIC_NAME:
        print(f"[MESSAGE] Reçu sur {msg.topic} -> {donne_recue}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, PORT)

print("--- Démarrage du Subscriber (Attente de données...) ---")
client.loop_forever()