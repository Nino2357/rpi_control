# rpi_control

Lien GitHub : https://github.com/Nino2357/rpi_control

Code source domotique sur Raspberry Pi 4

### Structure du code :

3 parties :

* Acquisition
    + Exterieur
    + Interne 
* Display 
    + Lcd 
    + Terminal
* Analysis
    + Stockage
    + Analyse

### Données affichées sur menu lcd (usage des 3 boutons) :

1er bouton, défilement des différents panneaux,

1. Heure/Date
    - Shutdown (demande confirmation)
    - Reboot (demande confirmation)
1. Température/Humidité/Luminosité (extérieur)
1. Réseau internet (Ping,Download,Upload)
1. Température des composants interne
1. Chronometre
    - Remise a 0
    - Start/ pause
1. Minuteur
    - Changement de chiffre
    - Chiffre +1
1. Compteur
    - Remise à 0
    - Compteur +1


