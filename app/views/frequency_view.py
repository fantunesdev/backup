from flask import render_template

from app import app
from app.services import frequency_service


@app.route('/frequencies')
def get_frequencies():
    frequencies = frequency_service.get_frequencies()
    return render_template('frequency/get_frequencies.html', frequencies=frequencies)


@app.route('/frequencies/<int:frequency_id>')
def get_frequency_id(frequency_id):
    frequency = frequency_service.get_frequency_id(frequency_id)
    return render_template('frequency/detail_frequency.html', frequency=frequency)