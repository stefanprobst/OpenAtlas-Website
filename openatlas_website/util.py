from typing import Iterator

from flask import url_for

from openatlas_website import app
from openatlas_website.data.institute import institutes
from openatlas_website.data.team import team


@app.context_processor
def inject_menu() -> dict[list[str]]:
    content = ['about', 'projects', 'cooperation', 'software', 'team',
               'events', 'news']
    menu = [{'name': 'about', 'to': url_for('about')},
            {'name': 'projects',
             'to': url_for('projects')},
            {'name': 'team',
             'to': url_for('team')},
            {'name': 'manual',
             'to': 'https://manual.openatlas.eu'},
            {'name': 'documentation',
             'to': 'https://redmine.openatlas.eu/projects/uni/wiki'}]

    external_links = [{'name': 'Demo', 'to': 'https://demo.openatlas.eu'},
                      {'name': 'Development Demo',
                       'to': 'https://demo-dev.openatlas.eu'},
                      {'name': 'Features',
                       'to': 'https://manual.openatlas.eu/features.html'},
                      {'name': 'Manual', 'to': 'https://manual.openatlas.eu'},
                      {'name': 'Documentation',
                       'to': 'https://redmine.openatlas.eu/projects/uni/wiki'},
                      {'name': 'Model',
                       'to': 'https://demo.openatlas.eu/overview/model'},
                      {'name': 'Code',
                       'to': 'https://github.com/craws/OpenAtlas'}
                      ]
    return dict(menu=menu, content=content, external_links=external_links)


@app.template_filter()
def display_institutes(institutes_: Iterator[str]) -> str:
    html = ''
    for name in institutes_:
        html += f"""
        <a
            href="{institutes[name]['url']}"
            target="_blank"
            class="without-decoration">
            <img
                class="projects-institutes"
                src="/static/images/institutes/{institutes[name]['logo']}"
                alt="{institutes[name]['name']}"
                title="{institutes[name]['name']}">
        </a>"""
    return f'{html}'


@app.template_filter()
def display_team_member(name: str) -> str:
    person = team[name]
    html = f"""
    <div class="row">
    <div class="col-md-auto mb-4">
        <img class="team" src="/static/images/team/{person['img']}" alt="">
        <br>"""
    if person['image_license']:
        html += f'<span class="image-license">{person["image_license"]}</span>'
    return html + f"""
        </div>
        <div class="col">
            <p>
                <span style="font-weight: bold;">{name}</span><br>
                {person['function']}<br>
                <a href="mailto:{['person.email']}">{person['email']}</a>
            </p>
            <p>{person['text']}</p>
      </div></div>"""
