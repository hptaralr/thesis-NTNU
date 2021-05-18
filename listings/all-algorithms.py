@app.route("/allAlgorithms", methods=['POST', 'GET'])
def runAllAlgorithms():
    path='uploads/'
    csv_results = 'results.csv'
    json_results = 'results.json'
    if request.method == 'POST':
        if (os.listdir(path)):
            fun.runISO_Metrics();
            fun.runFaceQNet();
            if os.path.exists(csv_results):
                os.remove(csv_results)      
            fun.save_results_to_file('ISO_metrics/results.csv', 'ISO')
            fun.save_results_to_file('FaceQnet/scores_quality.csv', 'FaceQNet')
            if os.path.exists(json_results): 
                os.remove(json_results)
            fun.save_results_to_json(csv_results)
            return send_file(json_results)