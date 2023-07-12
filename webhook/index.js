const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 8300;

app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    //console.log('Received webhook:', req.body);
    const status = req.body.status;
    if (status === 'done') {
        const result_url = req.body.result_url;
        console.log('File is ready at: ' + result_url);
    } else {
        console.log("File is not ready. status :" + status);
    }
    res.sendStatus(200);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});