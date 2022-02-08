#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Chargements des packages pour la lecture du page
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

#Chargements des packages pour l extraction des données
from bs4 import BeautifulSoup


# In[ ]:


#Chargement de la contenu du page et prevention des éventuelles erreurs
try:
    html = urlopen('https://www.welcometothejungle.com/fr/jobs')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('Welcometojungle!')
    
#Lecture des balises et des informations de la page
soup = BeautifulSoup(html.read(), 'xml')

#Extraction sur les  des donnees dans la section 'Entreprises du moment'
tags=soup.find_all('div',class_='nwf9oq-3 cduwUV')
for index,t in enumerate(tags):
    print(f'Titre du travail {t.header.text}')
    print(f'Descriptions du travail: {t.ul.text}')
    print(f"Liens vers le travail: {t.a['href']}")
    print('**************************************')
    
#Extraction sur les  des donnees dans la section 'Oh my job'    
tags=soup.find_all('li',class_='sc-kJpAUB hhgAgT')
for index,t in enumerate(tags):
    print(f'Les métiers{t.text}')
    print(f"Liens vers le travail: {t.a['href']}")
    print('++++++++++++++++++++++++++++++++++++++')

Titre du travail:ARMIS
Descriptions du travail: Big Data, Intelligence artificielle / Machine Learning, PublicitéParisEntre 50 et 250 salariés
Liens vers le travail: /fr/companies/armis
**************************************
Titre du travail:Ministère de l'Intérieur
Descriptions du travail: Administration publiqueParis, Alençon, Bobigny, Bordeaux, Créteil, Lille, Nanterre, Toulouse, Tulle> 2000 salariés
Liens vers le travail: /fr/companies/ministere-de-l-interieur
**************************************
Titre du travail:Viaxoft
Descriptions du travail: SaaS / Cloud Services, TourismeMarseilleEntre 50 et 250 salariés
Liens vers le travail: /fr/companies/viaxoft
**************************************
Titre du travail:Monoprix
Descriptions du travail: Grande distributionClichy, Aix-En-Provence, Aix-Les-Bains, Ajaccio, Amiens, Angers, Annecy, Annemasse, Antibes, Antony, Arcachon, Arcueil, Argenteuil, Ascain, Asnières-Sur-Seine, Aubagne, Aubervilliers, Auray, Auxerre, Avignon, Bagnères-De-Bigorre, Bayonne, Belfort, Besançon, Bois-Colombes, Bondy, Bordeaux, Boulogne-Billancourt, Bourg-La-Reine, Bourges, Bron, Brunoy, Caen, Cannes, Carcassonne, Castres, Chalon-Sur-Saône, Chambéry, Champigny-Sur-Marne, Charenton-Le-Pont, Chartres, Chatou, Chaville, Chelles, Châlons-En-Champagne, Châtellerault, Colmar, Colombes, Compiègne> 2000 salariés
Liens vers le travail: /fr/companies/monoprix
**************************************
Les métiersOh My Job : les métiers de la Tech’Ils ont le vent en poupe, mais quel est vraiment leur quotidien ? On a donné la parole à des professionnels de la tech. 28 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-technologie
++++++++++++++++++++++++++++++++++++++
Les métiersOh My Job : les métiers du businessBusiness developer, Account manager, Supply Chain Manager… Les métiers du business sont nombreux et variés. Découvrez-les !21 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-business
++++++++++++++++++++++++++++++++++++++
Les métiersOh My Job : les métiers du marketing et de la com’En pleine expansion à l'ère du digital, ces métiers attirent. Mais quel est leur quotidien ? 12 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-marketing-communication
++++++++++++++++++++++++++++++++++++++
Les métiersOh My Job : les métiers du retail et de la venteIls sont bien plus variés et complets que ce que l’on peut penser ! Découvrez toute la palette de ces métiers humains et challengeants.3 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-retail-vente
++++++++++++++++++++++++++++++++++++++
Les métiersOh My Job : les métiers de la créationLes métiers de la création font rêver mais sont souvent mal compris. Découvrez-les grâce à des à des témoignages de professionnels du secteur.4 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-creation
++++++++++++++++++++++++++++++++++++++
Les métiersOh My Job : les métiers de l’administratifDRH, comptabilité, juriste, secrétariat… Les métiers de l’administratif sont nécessaires au bon fonctionnement d’une entreprise. Immersion. 8 contenus
Liens vers le travail: /fr/collections/metiers/oh-my-job-metiers-administratif
++++++++++++++++++++++++++++++++++++++
# In[ ]:




