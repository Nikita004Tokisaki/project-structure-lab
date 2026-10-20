from flask import render_template


def register_routes(app) -> None:
    @app.route("/")
    def index():
        return render_template("index.html", title="project-structure-lab")

    @app.route("/api/health")
    def health():
        return {"status": "ok"}