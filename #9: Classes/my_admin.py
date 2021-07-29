from admin import Admin


admin_0 = Admin('anna', 'smith', 'asmith', 'annasmith@mail.com', 29)
privileges_0 = ['can add post', 'can delete post', 'can ban user']
admin_0.describe_user()
admin_0.privileges.privileges = privileges_0
admin_0.privileges.show_privileges()
