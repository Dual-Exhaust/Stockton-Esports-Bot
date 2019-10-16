import discord


class Roles:
    def __init__(self):
        pass

    @staticmethod
    def check_role_exists(role, guild):
        for x in guild.roles:
            if role == x.name:
                return True
        return False

    @staticmethod
    def check_role_is_allowed(role):
        if role == "Admin" or role == "Moderator" or role == "Channel Builder" or role == "Content Creation" \
                or role == "Game Manager" or role == "Reaction Role" or role == "Team Captain" \
                or role == "Auth-ed" or role == "Player":
            return False
        return True

    @staticmethod
    def check_user_is_authed(user):
        for role in user.roles:
            if role.name == "Auth-ed":
                return True
        return False

    @staticmethod
    def check_user_has_role(role, user):
        for x in user.roles:
            if role == x.name:
                return True
        return False

    async def add_role(self, role, user):
        for each in user.guild.roles:
            if role.upper() == each.name.upper():
                role = each.name
        if self.check_user_is_authed(user=user):
            if self.check_role_exists(role=role, guild=user.guild):
                if self.check_role_is_allowed(role=role):
                    if not self.check_user_has_role(role=role, user=user):
                        role = discord.utils.get(user.guild.roles, name=role)
                        await user.add_roles(role)
                        return True
        return False

    async def remove_role(self, role, user):
        for each in user.guild.roles:
            if role.upper() == each.name.upper():
                role = each.name
        if self.check_user_is_authed(user=user):
            if self.check_role_exists(role=role, guild=user.guild):
                if self.check_role_is_allowed(role=role):
                    if self.check_user_has_role(role=role, user=user):
                        role = discord.utils.get(user.guild.roles, name=role)
                        await user.remove_roles(role)
                        return True
        return False



