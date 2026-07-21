"""
Cognit Hub Web Application
"""

from flask import Flask, render_template, request

from cognit.kernel.kernel import CognitKernel
from cognit.orchestrator.orchestrator import TaskOrchestrator

app = Flask(__name__)

# Initialize Kernel
kernel = CognitKernel()
kernel.initialize()
kernel.start()

# Initialize Task Orchestrator
orchestrator = TaskOrchestrator()


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        goal = request.form.get("goal", "").strip()

        if goal:
            result = orchestrator.execute(goal)

    return render_template(
        "index.html",
        status=kernel.status(),
        result=result,
    )


@app.route("/health")
def health():
    return {
        "status": "ok",
        "kernel": kernel.status(),
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
    
