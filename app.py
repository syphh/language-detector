from flask import Flask, render_template, request
import detectlanguage as dl

dl.configuration.api_key = '21b0e2c7cf444787f680d96ff5d3ea8f'

application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('index.html')

@application.route('/detect_language', methods=['POST'])
def detect_language():
    print(request.form)
    text = request.form['input_text']

    result_name = 'UNKNOWN'
    icon_link = ''
    try:
        result_code = dl.simple_detect(text)
        for language in dl.languages():
            if language['code'] == result_code:
                result_name = language['name']
                break
        result_code = 'gb' if result_code == 'en' else result_code
        icon_link = 'https://flagcdn.com/60x45/' + result_code.lower() + '.png'
    except Exception as e:
        print(e)
    return render_template('index.html', detected_language=result_name, icon_link=icon_link)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)