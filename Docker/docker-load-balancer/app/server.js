const express = require('express')
const os = require('os')

const app = express()

app.get('/', (_, res)=> {
	return res.status(200).json({'message': `hello from ${os.hostname()}`});
});

app.listen(3000, () => {
	console.log("listening on port 3000")
})

