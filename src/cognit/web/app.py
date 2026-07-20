"""
CognitOS Web Application

Flask entry point for the CognitOS dashboard.
"""

from flask import Flask, render_template

from cognit.kernel.kernel import CognitKernel

app = Flask(__name__)

# Create the Kernel
kernel = CognitKernel()

# Initialize all kernel services
kernel.initialize()

# Start the runtime
kernel.start()


@app.route("/")
def home():
    """Home Dashboard"""

    return render_template(
        "index.html",
        status=kernel.status()
    )


@app.route("/health")
def health():
    """Health Check"""

    return {
        "status": "ok",
        "kernel": kernel.status()
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
    
