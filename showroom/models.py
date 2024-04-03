from showroom import db

class Car(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  cost = db.Column(db.Integer, nullable=False)
  year = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return f"Car('{self.name}', '{self.cost}', '{self.year}')"