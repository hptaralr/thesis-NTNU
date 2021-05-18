const runAllAlgorithmsHandler = () => {
    setLoading(true);
    axios({
        url: 'http://localhost:5000/allAlgorithms',
    	method: 'POST'
    }).then((response) => {
    	setFile(response.data);
    	setLoading(false);
    	console.log(response.data);
    });
};