from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Table, CheckConstraint


db = SQLAlchemy()

class Class(db.Model):
    __tablename__ = 'Class'
    Class_ID = db.Column(db.String(15), primary_key=True)
    Dance_Style = db.Column(db.String(50), nullable=False)
    Dance_Level = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Numeric(4, 2), nullable=False, CheckConstraint('Price > 0'))
    Room_Number = db.Column(db.String(10), nullable=False)
    Duration = db.Column(db.Numeric(2, 1), nullable=False)
    Time_Slot_ID = db.Column(db.String(6), db.ForeignKey('Time_Slot.Time_Slot_ID'))

    time_slot = db.relationship('Time_Slot', backref='classes')

class Student(db.Model):
    __tablename__ = 'Student'
    Student_ID = db.Column(db.Integer, primary_key=True)
    First = db.Column(db.String(20), nullable=False)
    Last = db.Column(db.String(20), nullable=False)
    Interests = db.Column(db.Text, nullable=True)
    Email = db.Column(db.String(50), nullable=False)
    Phone_Number = db.Column(db.String(15), nullable=True)

class Enrollment(db.Model):
    __tablename__ = 'Enrollment'
    Studio_ID = db.Column(db.String(10), db.ForeignKey('Studio.Studio_ID'), primary_key=True)
    Student_ID = db.Column(db.Integer, db.ForeignKey('Student.Student_ID'), primary_key=True)

    studio = db.relationship('Studio', backref='enrollments')
    student = db.relationship('Student', backref='enrollments')