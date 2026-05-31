async function run() {

    const goal = document.getElementById("goal").value;

    const res = await fetch("/run", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({goal})
    });

    const data = await res.json();

    document.getElementById("out").innerText =
        JSON.stringify(data, null, 2);
}
