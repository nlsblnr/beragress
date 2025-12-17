from flask import Flask, render_template
import time
from datetime import date, datetime, timedelta

jetzt = datetime.now()

tagesbeginn = datetime(jetzt.year, jetzt.month, jetzt.day, 7, 25)
tagesende = datetime(jetzt.year, jetzt.month, jetzt.day, 16, 50)
progress_tag = round((jetzt.timestamp()-tagesbeginn.timestamp())/(tagesende.timestamp()-tagesbeginn.timestamp()), ndigits=5)*100

if jetzt.day < 25:
    monatsbeginn = datetime(jetzt.year, jetzt.month, 1)
    monatsende = datetime(jetzt.year, jetzt.month, 25)
elif jetzt.day >= 25 and jetzt.month < 12:
    monatsbeginn = datetime(jetzt.year, jetzt.month, 25)
    monatsende = datetime(jetzt.year, jetzt.month+1, 25)
elif jetzt.day >= 25 and jetzt.month == 12:
    monatsbeginn = datetime(jetzt.year, jetzt.month, 25)
    monatsende = datetime(jetzt.year+1, 1, 25)
progress_monat = round((jetzt.timestamp()-monatsbeginn.timestamp())/(monatsende.timestamp()-monatsbeginn.timestamp()), ndigits=5)*100
monatsverdienst = progress_monat/100*5000

vertragsbeginn = datetime(2025, 12, 1)
vertragsende = datetime(2026, 6, 30)
progress_vertrag = round((jetzt.timestamp()-vertragsbeginn.timestamp())/(vertragsende.timestamp()-vertragsbeginn.timestamp()), ndigits=5)*100
bruttoverdienst = progress_vertrag/100*35000

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', progress_tag=progress_tag, progress_monat=progress_monat, monatsverdienst=monatsverdienst, progress_vertrag=progress_vertrag, bruttoverdienst=bruttoverdienst)


if __name__ == '__main__':
    app.run(debug=True)
