from app import db
from datetime import datetime,date
import enum

class StatusType(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.String(191), index=True, nullable=True)
    agent_code = db.Column(db.String(191), index=True, nullable=True)
    customerahmno = db.Column(db.String(191), index=True, nullable=True)
    username = db.Column(db.String(191), index=True, nullable=True)
    branch_code = db.Column(db.String(191),nullable=True)
    email = db.Column(db.String(191), index=True, nullable=True)
    phone_number = db.Column(db.String(191), index=True, nullable=True)
    fullname = db.Column(db.String(191), nullable=True)
    password = db.Column(db.String(191), nullable=True)
    address = db.Column(db.String(191), nullable=True)
    postcode = db.Column(db.String(11), nullable=True)
    province_id = db.Column(db.String(36), nullable=True)
    city_id = db.Column(db.String(36), nullable=True)
    district_id = db.Column(db.String(36), nullable=True)
    gender = db.Column(db.Integer,nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(StatusType), nullable=False, default="INACTIVE")
    identity_number = db.Column(db.String(191), nullable=True)
    user_id = db.Column(db.String(191),index=True, nullable=True)
    user_type = db.Column(db.String(191), index=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Customer {}>'.format(self.name)



    