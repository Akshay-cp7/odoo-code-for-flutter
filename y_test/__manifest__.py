{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 10,
    'summary': 'Manage student information',
    'description': 'This module allows you to manage student information',
    'author': 'Akshay C P',
    'depends': ['base','mail'],
     'data': [
    'security/ir.model.access.csv',
    'views/student_view_only.xml',
    'views/student_view.xml',
    'views/menu.xml'],
    'installable': True,
    'application': True,


}
