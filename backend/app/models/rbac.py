from app.extensions import db

class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  # e.g. "add_user", "edit_shipment"
    description = db.Column(db.String(255))

class RoleAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'), nullable=False)

    role = db.relationship('Role', backref='permissions')
    action = db.relationship('Action')
