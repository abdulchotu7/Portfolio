"""Generate the static portfolio; all professional claims live in profile.json."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT / "content/profile.json").read_text())

cards = []
for key in p["focus"]["ai"]["web_order"]:
    project = p["projects"][key]
    steps = ''.join(f'<li>{escape(step)}</li>' for step in project['pipeline'])
    angles = ''.join(f'<p data-focus-copy="{focus}"' + (' hidden' if focus == 'swe' else '') + f'>{escape(project[focus][0])}</p>' for focus in ('ai', 'swe'))
    cards.append(f'''<li class="project-item" data-project="{key}">
      <article class="project">
        <div class="project-heading"><span class="eyebrow">{escape(project['category'])}</span><a class="repo-link" href="{project['url']}" target="_blank" rel="noopener">GitHub <span class="sr-only">for {escape(project['name'])} (opens in a new tab)</span><span aria-hidden="true">↗</span></a></div>
        <h3>{escape(project['name'])}</h3>
        <p class="project-description">{escape(project['description'])}</p>
        <ol class="pipeline" aria-label="{escape(project['name'])} workflow">{steps}</ol>
        <div class="project-angle">{angles}</div>
        <details><summary>Inside the implementation<span class="sr-only"> of {escape(project['name'])}</span></summary><p>{escape(project['detail'])}</p></details>
        <p class="stack">{escape(project['stack'])}</p>
      </article>
    </li>''')

experience = ''.join(f'<ul class="work-bullets" data-focus-copy="{focus}"' + (' hidden' if focus == 'swe' else '') + '>' + ''.join(f'<li>{escape(bullet)}</li>' for bullet in p['experience'][focus]) + '</ul>' for focus in ('ai', 'swe'))
skills = ''.join(f'<ul class="skill-list" data-focus-copy="{focus}" role="list"' + (' hidden' if focus == 'swe' else '') + '>' + ''.join(f'<li><h3>{escape(label)}</h3><p>{escape(values)}</p></li>' for label, values in p['focus'][focus]['skills']) + '</ul>' for focus in ('ai', 'swe'))
values = {'{{PROJECTS}}': '\n'.join(cards), '{{EXPERIENCE}}': experience, '{{SKILLS}}': skills,
          '{{DATES}}': escape(p['experience']['dates']), '{{EMAIL}}': p['email'], '{{LINKEDIN}}': p['linkedin'], '{{GITHUB}}': p['github'],
          '{{EDUCATION}}': escape(p['education']['degree'] + ' · ' + p['education']['school']), '{{EDUCATION_DETAIL}}': escape(p['education']['detail'] + ' · ' + p['education']['dates']),
          '{{FOCUS_CONFIG}}': json.dumps({k: v['web_order'] for k, v in p['focus'].items()})}
template = (ROOT / 'templates/portfolio.html').read_text()
for key, value in values.items():
    template = template.replace(key, value)
assert '{{' not in template, 'Unreplaced template token'
(ROOT / 'index.html').write_text(template)
print('Built index.html from content/profile.json and templates/portfolio.html')
