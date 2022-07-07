import csv
import os
import sys

# exam schema: "nrow", "acid", "anon_code"
def extract_solutions_from_file(filename, qname, output_base):
    num_correct = 0
    num_incorrect = 0
    num_student = 0

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for (i, row) in enumerate(reader):
            if i == 0:
                # header row
                continue
            try:
                acid, qname, anon_code = row
            except ValueError:
                print ("bad row:",i, row)
                raise
            
            student_id = 'student_' + str(acid)
            num_student += 1

            with open(os.path.join(output_base, '%s%ss.py' % (qname, student_id)), 'w') as sol_file:
                sol_file.write(anon_code)

    print "Number of code solutions:", num_student

if __name__ == '__main__':
    qname = sys.argv[2]
    output_base = os.path.join(sys.argv[2], qname)
    
    try:
        os.makedirs(output_base)
    except OSError:
        pass
    extract_solutions_from_file(sys.argv[1], qname, output_base)
