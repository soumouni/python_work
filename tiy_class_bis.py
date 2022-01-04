#9-10 imported restaurant
from tiy_module_class import Restaurant
mon_plaisir=Restaurant('mon plaisir', 'algerian traditional food')
mon_plaisir.describe_restaurant()

#9-11 imported admin
#import module_users
#user=module_users.Admin('Hachemi', 'Mimouni', 'Algiers', 42, 0)
#privilege=module_users.Privileges()
#privilege.show_privileges()

#9-12 multiple modules
import module_admin

user2=module_admin.Admin('Moussadegh', 'Mimouni', 'Algiers', 70, 1)

privilege=module_admin.Privileges()
privilege.show_privileges()
user2.describe_user()