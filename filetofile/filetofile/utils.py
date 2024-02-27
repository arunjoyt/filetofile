import frappe
import datetime

def generate_filename(prefix='', extension='.txt'):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{prefix}{formatted_time}{extension}"
    return filename

@frappe.whitelist()
def to_csv():
    #site_path = frappe.get_site_path()
    filename = generate_filename(prefix='file_', extension='.csv')
    file_with_path = frappe.utils.get_path('public/files',filename)
    with open(file_with_path,"a") as f:
        f.write("1,2,3\n")
    processed_file_doc = frappe.get_doc(doctype='ProcessedFile', processed_file=filename)
    processed_file_doc.save()