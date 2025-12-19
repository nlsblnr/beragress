from flask import Flask, render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta

jetzt = datetime.now()

tagesbeginn = datetime(jetzt.year, jetzt.month, jetzt.day, 7, 25)
tagesende = datetime(jetzt.year, jetzt.month, jetzt.day, 16, 50)
progress_tag = round((jetzt.timestamp()-tagesbeginn.timestamp())/(tagesende.timestamp()-tagesbeginn.timestamp()), ndigits=5)*100

monatsbeginn = datetime(jetzt.year, jetzt.month, 1)
monatsende = datetime(jetzt.year, jetzt.month, 1) + relativedelta(months=1)  - relativedelta(days=1)
progress_monat = round((jetzt.timestamp()-monatsbeginn.timestamp())/(monatsende.timestamp()-monatsbeginn.timestamp()), ndigits=5)*100
monatsverdienst = round(progress_monat/100*5000)

vertragsbeginn = datetime(2025, 12, 1)
vertragsende = datetime(2026, 6, 30)
progress_vertrag = round((jetzt.timestamp()-vertragsbeginn.timestamp())/(vertragsende.timestamp()-vertragsbeginn.timestamp()), ndigits=5)*100
bruttoverdienst = round(monatsverdienst+(jetzt.month%12)*5000)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', progress_tag=round(progress_tag, ndigits=5), progress_monat=round(progress_monat, ndigits=5), monatsverdienst=monatsverdienst, progress_vertrag=progress_vertrag, bruttoverdienst=bruttoverdienst)


if __name__ == '__main__':
    app.run(debug=True)

