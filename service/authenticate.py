from model.manage import User, users_schema, user_schema
import json, jwt, datetime

class Authenticate():
    def login_action(self, request):
        try:
            email = request.json['email']
            password = request.json['password']
        except KeyError:
            raise KeyError()
        user =  User.query.filter_by(email=email,password=password).first()
        if not user:
            raise ValueError()
        token = jwt.encode({"payload":{"name":user.name, "email":user.email},"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRETKEY'])
        token = token.decode("utf-8")
        return token
    
    def register_action(self, request):
        try:
            name = request.json['name']
            email = request.json['email']
            password = request.json['password']
        except KeyError:
            raise KeyError()
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        token = jwt.encode({"payload":{"name":new_user.name, "email":new_user.email},"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRETKEY'])
        token = token.decode("utf-8")
        return token

        
