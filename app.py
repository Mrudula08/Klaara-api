import psycopg2
from flask import Flask, request
from psycopg2.extras import RealDictCursor

database_name = 'd540m3ncb1j1ae'
host = 'ec2-18-215-111-67.compute-1.amazonaws.com'
port = 5432
db_connection = psycopg2.connect(database=database_name,
                           user='qoyzgrzpybkuoa',
                           password='81e449bc72ef10c318673cb71228b58d56a491b405275a143aa77b4604358d2e',
                           host=host, port=port)


app = Flask(__name__)



@app.route('/api/branches/autocomplete',methods=["GET"])
def get_branch_details_in_ascending_order():
    try:
        result_json = {'branches': list}
        params = request.args
        branch_name = params.get('q')
        limit = params.get('limit',100)
        offset = params.get('offset',0)
        table_name = 'branches'
        query = f"select * from {table_name} where branch like '%{branch_name}%' order by ifsc asc limit {limit} offset {offset}"
        print(query)
        my_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        final_result_list = list()
        for each_row in result:
            each_json = {
                "ifsc": each_row['ifsc'],
                "bank_id": int(each_row['bank_id']),
                "branch": each_row['branch'],
                "address": each_row['address'],
                "city": each_row['city'],
                "district": each_row['district'],
                "state": each_row['state']
            }
            final_result_list.append(each_json)

        result_json['branches'] = final_result_list
        db_connection.commit()
        db_connection.close()
    except Exception as error:
        print(error)
        return f"Error Occurred. Please contact the technical team for more details."

    return result_json


@app.route('/api/branches',methods=["GET"])
def get_branch_details():
    try:
        result_json = {'branches': list}
        params = request.args
        branch_name = params.get('q')
        limit = params.get('limit',100)
        offset = params.get('offset',0)
        print(branch_name,limit,offset)
        table_name = 'branches'
        query = f"select * from {table_name} where branch like '%{branch_name}%' or city like '%{branch_name}%' or district like '%{branch_name}%' order by ifsc asc limit {limit} offset {offset}"
        my_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        final_result_list = list()
        for each_row in result:
            each_json = {
                "ifsc": each_row['ifsc'],
                "bank_id": int(each_row['bank_id']),
                "branch": each_row['branch'],
                "address": each_row['address'],
                "city": each_row['city'],
                "district": each_row['district'],
                "state": each_row['state']
            }
            final_result_list.append(each_json)

        result_json['branches'] = final_result_list
        db_connection.commit()
        db_connection.close()

    except Exception as error:
        return f"Error Occurred. Please contact the technical team for more details."

    return result_json


if __name__ == '__main__':
    app.run(debug=True)



