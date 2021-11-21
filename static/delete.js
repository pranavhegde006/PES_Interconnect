function delete1(id) {
    console.log(id);
    fetch('http://localhost:5000/dele', {
        method: 'POST',
        headers: {
        // 'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({ids: id})
        }).then(res => res.json())
        .then(res => console.log(res));
}