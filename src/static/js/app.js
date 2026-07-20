async function executeMission() {

    const mission = document.getElementById("mission").value.trim();

    if (!mission) {
        alert("Please enter a mission.");
        return;
    }

    const output = document.getElementById("output");
    output.textContent = "Executing mission...";

    try {

        const response = await fetch("/api/plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mission: mission
            })
        });

        const data = await response.json();

        let text = "Mission: " + data.mission + "\n\n";

        if (data.logs && data.logs.length > 0) {
            text += data.logs.join("\n");
        } else if (data.tasks) {
            data.tasks.forEach(task => {
                text += "• " + task.title + "\n";
            });
        } else {
            text += "No output returned.";
        }

        output.textContent = text;

    } catch (err) {
        output.textContent = "Error: " + err;
    }
}
