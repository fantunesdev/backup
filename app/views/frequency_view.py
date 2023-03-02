from flask import render_template, redirect, url_for, request

from app import app
from app.forms import frequency_form
from app.models import Frequency
from app.services import frequency_service


@app.route('/frequencies/create', methods=['GET', 'POST'])
def create_frequency():
    form_frequency = frequency_form.FrequencyForm()
    if form_frequency.validate_on_submit():
        new_frequency = Frequency(
            description=form_frequency.description.data
        )
        frequency_service.create_frequency(new_frequency)
        return redirect(url_for('configure_settings'))
    return render_template('frequency/form_frequency.html', form_frequency=form_frequency)


@app.route('/frequencies')
def get_frequencies():
    frequencies = frequency_service.get_frequencies()
    return render_template('frequency/get_frequencies.html', frequencies=frequencies)


@app.route('/frequencies/<int:frequency_id>')
def get_frequency_id(frequency_id):
    frequency = frequency_service.get_frequency_id(frequency_id)
    return render_template('frequency/detail_frequency.html', frequency=frequency)


@app.route('/frequencies/update/<int:frequency_id>', methods=['GET', 'POST'])
def update_frequency(frequency_id):
    old_frequency = frequency_service.get_frequency_id(frequency_id)
    form_frequency = frequency_form.FrequencyForm(obj=old_frequency)
    if form_frequency.validate_on_submit():
        new_frequency = Frequency(
            description=form_frequency.description.data
        )
        frequency_service.update_frequency(old_frequency, new_frequency)
        return redirect(url_for('configure_settings'))
    return render_template('frequency/form_frequency.html', form_frequency=form_frequency)


@app.route('/frequencies/delete/<int:frequency_id>', methods=['GET', 'POST'])
def delete_frequency(frequency_id):
    frequency = frequency_service.get_frequency_id(frequency_id)
    if request.method == 'POST':
        frequency_service.delete_frequency(frequency)
        return redirect(url_for('configure_settings'))
    return render_template('frequency/detail_frequency.html', frequency=frequency)
