import json
from odoo import http
from odoo.http import request

#Get all students data without filter type this http://localhost:8069/get_total_studentsjs/
class Snippet(http.Controller):
    @http.route('/get_total_studentsjs', auth='public', type='http', methods=['GET'])
    def get_total_students(self):
        try:
            # Fetch student data
            students = request.env['collage.student'].sudo().search_read([], ['name', 'dept', 'gender'])
            # Wrap the student data in a dictionary
            response_data = {
                'students': students
            }
            return request.make_response(json.dumps(response_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
#To get data based on every students id type this http://localhost:8069/get_total_studentsjs/19 where 19 is id
class Snippet(http.Controller):
    @http.route('/get_total_studentsjs/<int:student_id>', auth='public', type='http', methods=['GET'])
    def get_total_students(self, student_id=None):
        try:
            if student_id is not None:
                # Fetch student data by ID
                student = request.env['collage.student'].sudo().search_read([('id', '=', student_id)], ['id', 'name', 'dept', 'gender'])
                
                if student:
                    return request.make_response(json.dumps(student[0]), headers={'Content-Type': 'application/json'})
                else:
                    return request.make_response(json.dumps({'error': 'Student not found'}), headers={'Content-Type': 'application/json'}, status=404)
            else:
               
                students = request.env['collage.student'].sudo().search_read([], ['name', 'dept', 'gender'])
                response_data = {'students': students}
                return request.make_response(json.dumps(response_data), headers={'Content-Type': 'application/json'})
        except Exception as e:
            return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
