from data.User import Info

from data.members import Members


class info_receive:
    def get(self):
        info = Info.query.all()
        print(Info.name)

class members_receive:
    def get(self):
        members = Members.query.all()
        print(Members.name)
