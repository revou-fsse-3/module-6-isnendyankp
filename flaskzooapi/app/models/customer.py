from app.utils.database import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=True)

    # method to return the customer as a dictionary
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone
        }