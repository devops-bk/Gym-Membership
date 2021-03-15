class GymSupervisor:

    regimen = {}
    members = dict()

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def addmember(cls, member):
        GymSupervisor.members[member.getContactno()] = member

obj = GymSupervisor('GS007', 'Anthony')