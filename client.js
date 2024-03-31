const net = require('net');

const client = new net.Socket();
client.connect(6000, 'localhost', function() {
    console.log('Connected');

    // サーバーに送信するリクエストの作成
    const request = {
        method: "subtract",
        params: [42, 23],
        param_types: ["int", "int"],
        id: 1
    };

    client.write(JSON.stringify(request));
});

client.on('data', function(data) {
    console.log('Received: ' + data);
    client.destroy(); //サーバーを終了
});

client.on('close', function() {
    console.log('Connection closed');//サーバーを終了
});
