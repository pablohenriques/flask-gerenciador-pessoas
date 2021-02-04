from app import app, db
from app.utils import valida_usuario

if __name__ == "__main__":
    db.create_all()
    valida_usuario()
    app.run()
