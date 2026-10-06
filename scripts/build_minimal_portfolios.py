"""Build monochrome previews and the finalized black-first homepage."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
p = json.loads((ROOT / 'content/profile.json').read_text())
projects = {
    'nemotron': ('Speech recognition', 'A speech-to-text engine for Apple Silicon, with a macOS app for dictation.'),
    'rag': ('Document search', 'Upload PDFs and ask questions. Get answers with references to the source passages.'),
    'vision': ('Developer tooling', 'A local image-analysis tool that lets text-only coding agents understand screenshots and images.'),
}
contributions = {
    'nemotron': [
        'Built a streaming pipeline that keeps transcription context between audio chunks, with bounded audio history and incremental encoder/decoder state.',
        'Added checks against the reference implementation, configurable lookahead, a latency benchmark, and a macOS dictation app.'
    ],
    'rag': [
        'Combined semantic and keyword search, then reranked the results to choose relevant passages for each question.',
        'Built background PDF processing, duplicate detection, document-management APIs, and streamed answers. Added unit tests and Qdrant integration tests in GitHub Actions.'
    ],
    'vision': [
        'Built an npm-packaged TypeScript extension that sends image questions to a persistent Python inference process, keeping the local vision model loaded between calls.',
        'Added request tracking, readiness checks, timeouts, and process-exit handling. The tool is disabled when the coding agent already supports vision.'
    ],
}
rows = []
for key, (category, description) in projects.items():
    project = p['projects'][key]
    bullets = ''.join(f'<li>{escape(item)}</li>' for item in contributions[key])
    rows.append(f'''<article class="project-row" id="project-{key}">
      <div class="project-name"><h3><a href="{escape(project['url'])}" target="_blank" rel="noopener">{escape(project['name'])} <span class="arrow" aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a></h3><p class="eyebrow">{escape(category)}</p></div>
      <div class="project-copy"><p class="project-purpose">{escape(description)}</p><p class="contribution-label">My contribution</p><ul class="contribution-list">{bullets}</ul><p class="project-stack">{escape(project['stack'])}</p></div>
    </article>''')
e = p['experience']
ed = p['education']
experience = [
    'Developed BizInsights, a seven-stage company-research workflow covering market analysis, competitors, SWOT, and value propositions.',
    'Connected web crawling and URL discovery to LLM-based extraction, using Pydantic schemas to validate research outputs.',
    'Built FastAPI endpoints and analysis-status tracking with DynamoDB metadata and S3 result storage; implemented Google OAuth and role-based access.',
    'Worked on AWS voice campaign orchestration, concurrency control, and post-call reporting using Lambda, SQS, DynamoDB, and EventBridge.'
]
experience_html = '<ul class="contribution-list">' + ''.join(f'<li>{escape(item)}</li>' for item in experience) + '</ul>'
skills_html = ''.join(f'<p class="skill-line"><span>{escape(label)}</span>{escape(values)}</p>' for label, values in p['portfolio_skills'])
values = {
    '{{PROJECTS}}': '\n'.join(rows), '{{LOCATION}}': p['location'],
    '{{COMPANY}}': e['company'], '{{DATES}}': e['dates'],
    '{{JOB_TITLE}}': e['title'], '{{JOB_LOCATION}}': e['location'],
    '{{EDUCATION}}': ed['degree'] + ' · ' + ed['school'],
    '{{EDUCATION_DETAIL}}': ed['detail'] + ' · ' + ed['dates'],
    '{{EMAIL}}': p['email'], '{{GITHUB}}': p['github'], '{{LINKEDIN}}': p['linkedin'],
    '{{EXPERIENCE}}': experience_html, '{{SKILLS}}': skills_html,
    '{{EDUCATION_DATES}}': ed['dates'], '{{EDUCATION_FACTS}}': ed['detail'],
}
for theme, name, color in [('light', 'white', '#ffffff'), ('dark', 'black', '#101010')]:
    html = (ROOT / 'templates/portfolio-minimal.html').read_text()
    for token, value in values.items():
        html = html.replace(token, value if token in ('{{PROJECTS}}', '{{EXPERIENCE}}', '{{SKILLS}}') else escape(value, quote=True))
    for token, value in {
        '{{THEME}}': theme, '{{VARIANT}}': name.title() + '-first', '{{THEME_COLOR}}': color,
        '{{LIGHT_CURRENT}}': 'aria-current="page"' if theme == 'light' else '',
        '{{DARK_CURRENT}}': 'aria-current="page"' if theme == 'dark' else '',
    }.items():
        html = html.replace(token, value)
    assert '{{' not in html
    destination = ROOT / f'portfolio-{name}.html'
    destination.write_text(html)
    print(f'Built {destination.name}')
    if name == 'black':
        # The finalized homepage no longer needs the design comparison control.
        start = html.index('    <div class="theme-choice"')
        end = html.index('    </div>', start) + len('    </div>\n')
        (ROOT / 'index.html').write_text(html[:start] + html[end:])
        print('Built index.html (black-first)')
