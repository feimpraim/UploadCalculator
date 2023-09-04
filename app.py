from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_size = float(request.form['file_size'])
        file_size_unit = request.form['file_size_unit']
        internet_speed_mbps = float(request.form['internet_speed'])

        if file_size_unit == 'GB':
            file_size_mb = file_size * 1024  # Convert GB to MB
        else:
            file_size_mb = file_size

        upload_time_seconds = (file_size_mb * 8) / internet_speed_mbps
        upload_time_hours = int(upload_time_seconds // 3600)
        upload_time_minutes = int((upload_time_seconds % 3600) // 60)
        upload_time_seconds_remainder = int(upload_time_seconds % 60)

        return render_template(
            'index.html',
            upload_time=(upload_time_hours, upload_time_minutes, upload_time_seconds_remainder)
        )

    return render_template('index.html', upload_time=None)

if __name__ == '__main__':
    app.run(debug=True)
