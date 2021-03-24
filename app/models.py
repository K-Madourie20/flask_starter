from . import db

class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(80))
    details = db.Column(db.String(80))
    spaces = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    located = db.Column(db.String(50))
    prop_type = db.Column(db.String(20))
    photo = db.Column(db.String(120))
        
    # class Proterty(db.Model):
    #     # You can use this to change the table name. The default convention is to use
    #     # the class name. In this case a class name of UserProfile would create a
    #     # user_profile (singular) table, but if we specify __tablename__ we can change it
    #     # to `user_profiles` or some other name.
    #     __tablename__ = 'properties'

    #     id = db.Column(db.Integer, primary_key=True)
    #     Title = db.Column(db.String(80))
    #     details = db.Column(db.String(80))
    #     rooms = db.Column(db.Integer)
    #     bathroom = db.Column(db.Integer)
    #     cost = db.Column(db.Integer)
    #     located = db.Column(db.String(50))
    #     prop_type = db.Column(db.String(20))
    #     photo = db.Column(db.String(120))

    def __init__(self, Title, details, rooms, bathroom, cost, located, prop_type, photo):
        self.Title = Title
        self.details = details
        self.rooms = rooms
        self.bathroom = bathroom
        self.cost = cost
        self.located = located
        self.prop_type = prop_type
        self.photo = photo


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' %  self.id
