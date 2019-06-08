# Created by Alexander Watzinger and others. Please see README.md for licensing information
from collections import OrderedDict

from flask import render_template

from openatlas_website import app


@app.route('/events')
def events():
    upcoming = OrderedDict([
        ('2019-06-18', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'WUK',
                        'name': 'OpenAtlas and THANADOS summer meeting',
                        'link': '',
                        'title': ''}),
        ('2019-07-03', {'country': 'United Kingdom',
                        'city': 'Leeds',
                        'institute': 'University of Leeds',
                        'name': 'International Medieval Congress 2019',
                        'link': 'https://www.imc.leeds.ac.uk/imc2019/',
                        'title': '''OpenAtlas - An open source application to map historical data 
                                    with CIDOC CRM'''}),
        ])
    past = OrderedDict([
        ('2019-05-16', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'Austrian Academy of Sciences',
                        'name': 'Digitising Patterns of Power - Book and Project Presentation',
                        'link': 'https://dpp.oeaw.ac.at/repository/Programm_DPP_16Mai2019.pdf',
                        'title': 'OpenAtlas unter die Haube geschaut'}),
        ('2019-02-20', {'country': 'Czech Republic',
                        'city': 'Prague',
                        'institute': 'Institute of Archaeology of the Czech Academy of Sciences',
                        'name': 'Networking meeting with AIS',
                        'link': '',
                        'title': ''}),
        ('2019-02-13', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'University of Vienna',
                        'name': 'Prosopography Hackathon',
                        'link': 'https://acdh.univie.ac.at/nachrichten/single-view/news/linking-past-people-a-prosopography-hackathon-at-the-uni-of-vienna/?tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Baction%5D=detail&cHash=b3c6c21d5d122910b03f0c0b3f65228e',
                        'title': ''}),
        ('2018-10-19', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'Austrian Academy of Sciences',
                        'name': 'DPP Concluding Conference',
                        'link': 'https://dpp.oeaw.ac.at/conference/index.php?site=program',
                        'title': 'OpenAtlas - How to Grow Software for Historians'}),
        ('2018-07-03', {'country': 'United Kingdom',
                        'city': 'Leeds',
                        'institute': 'University of Leeds',
                        'name': 'International Medieval Congress 2018',
                        'link': 'https://www.imc.leeds.ac.uk/imcarchive/2018/sessions/840/%22Presentation%22:https://redmine.craws.net/attachments/download/467/how_to_grow_software_for_historians.pdf',
                        'title': 'OpenAtlas - How to Grow Software for Historians'}),
        ('2018-05-29', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'Austrian Centre for Digital Humanities',
                        'name': 'ACDH Tool Gallery - CIDOC CRM',
                        'link': 'https://www.oeaw.ac.at/acdh/about/news-archive/news-detail/article/acdh-tool-gallery-41',
                        'title': 'OpenAtlas'}),
        ('2017-07-03', {'country': 'United Kingdom',
                        'city': 'Leeds',
                        'institute': 'University of Leeds',
                        'name': 'International Medieval Congress 2017',
                        'link': 'http://imc.leeds.ac.uk/dbsql02/AQueryServlet?*id=30&*formId=30&*context=IMC&conference=2017&sessionId=7539&chosenPaperId=&*servletURI=https://imc.leeds.ac.uk/dbsql02/AQueryServlet',
                        'title': 'Relational Modelling of Historical Data - Concepts and Challenges'}),
        ('2017-06-20', {'country': 'Germany',
                        'city': 'Bochum',
                        'institute': 'Ruhr-University Bochum',
                        'name': 'Regesten und Register, Netzwerke und Karten',
                        'link': '',
                        'title': 'OpenAtlas'}),
        ('2016-09-28', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'Institute for Medieval Research',
                        'name': 'Digitising Patterns of Power',
                        'link': 'https://dpp.oeaw.ac.at/workshop/',
                        'title': 'OpenAtlas'}),
        ('2016-07-08', {'country': 'United Kingdom',
                        'city': 'Leeds',
                        'institute': 'University of Leeds',
                        'name': 'International Medieval Congress 2016',
                        'link': 'https://www.imc.leeds.ac.uk/imcarchive/2016/sessions/803/',
                        'title': 'Relational Modelling of Historical Data - A Technical Perspective'}),
        ('2016-04-13', {'country': 'Austria',
                        'city': 'Vienna',
                        'institute': 'Institute for Medieval Research',
                        'name': 'Entangled Worlds Congress',
                        'link': 'https://www.dasanderemittelalter.net/conference-entangled-worlds/',
                        'title': 'OpenAtlas'}),
        ('2015-12-16', {'country': 'Czech Republic',
                        'city': 'Brno',
                        'institute': 'Masaryk University',
                        'name': 'OpenAtlas Workshop',
                        'link': '',
                        'title': ''})])
    return render_template('events.html', past=past, upcoming=upcoming)
