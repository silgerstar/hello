from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    """
    두 수를 입력받아 합을 반환하는 API 엔드포인트
    요청 형식: JSON {"num1": 숫자, "num2": 숫자}
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'JSON 데이터가 필요합니다'}), 400
        
        num1 = data.get('num1')
        num2 = data.get('num2')
        
        if num1 is None or num2 is None:
            return jsonify({'error': 'num1과 num2가 필요합니다'}), 400
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except (ValueError, TypeError):
            return jsonify({'error': 'num1과 num2는 숫자여야 합니다'}), 400
        
        result = num1 + num2
        
        return jsonify({
            'num1': num1,
            'num2': num2,
            'sum': result
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add', methods=['GET'])
def add_numbers_get():
    """
    GET 요청으로도 두 수를 입력받을 수 있는 엔드포인트
    쿼리 파라미터: ?num1=숫자&num2=숫자
    """
    try:
        num1_str = request.args.get('num1')
        num2_str = request.args.get('num2')
        
        if num1_str is None or num2_str is None:
            return jsonify({'error': 'num1과 num2 쿼리 파라미터가 필요합니다'}), 400
        
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except (ValueError, TypeError):
            return jsonify({'error': 'num1과 num2는 숫자여야 합니다'}), 400
        
        result = num1 + num2
        
        return jsonify({
            'num1': num1,
            'num2': num2,
            'sum': result
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    """
    홈 엔드포인트 - API 사용법 안내
    """
    return jsonify({
        'message': '두 수의 합을 계산하는 API',
        'endpoints': {
            'POST /add': 'JSON 형식으로 {"num1": 숫자, "num2": 숫자}를 전송',
            'GET /add': '쿼리 파라미터로 ?num1=숫자&num2=숫자 형식으로 요청'
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

