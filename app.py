import psycopg2
from flask import Flask, request
from psycopg2.extras import RealDictCursor

database_name = 'dd4h7h7tinee4k'
host = 'ec2-54-145-224-156.compute-1.amazonaws.com'
port = 5432
user_name = 'vitkjnvtwvfbam'
password = '021abdab98af0fc33727a76bb43a143090c4d6f6706027347eb26b422e20ce96'
db_connection = psycopg2.connect(database=database_name,
                                 user=user_name,
                                 password=password,
                                 host=host, port=port)

app = Flask(__name__)


def parse_json(result):
    final_result_list = list()
    try:
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

    except Exception as e:
        print(f"Error Occurred. Please contact the technical team for more details.")
    return final_result_list


@app.route('/api/branches/autocomplete', methods=["GET"])
def get_branch_details_in_ascending_order():
    try:
        result_json = {'branches': list}
        params = request.args
        branch_name = params.get('q')
        limit = params.get('limit', 100)
        offset = params.get('offset', 0)
        table_name = 'branches'
        query = f"select * from {table_name} " \
                f"where branch like '%{branch_name}%' " \
                f"order by ifsc asc " \
                f"limit {limit} " \
                f"offset {offset}"
        my_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        final_result_list = parse_json(result)
        result_json['branches'] = final_result_list
    except Exception as error:
        print(error)
        return f"Error Occurred. Please contact the technical team for more details."
    finally:
        db_connection.close()

    return result_json


@app.route('/api/branches', methods=["GET"])
def get_details():
    try:
        result_json = {'branches': list}
        params = request.args
        branch_name = params.get('q')
        limit = params.get('limit', 100)
        offset = params.get('offset', 0)
        print(branch_name, limit, offset)
        table_name = 'branches'
        query = f"select * from {table_name} " \
                f"where branch like '%{branch_name}%' " \
                f"or city like '%{branch_name}%' " \
                f"or district like '%{branch_name}%' " \
                f"order by ifsc asc " \
                f"limit {limit} " \
                f"offset {offset}"
        my_cursor = db_connection.cursor(cursor_factory=RealDictCursor)
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        final_result_list = parse_json(result)
        result_json['branches'] = final_result_list
    except Exception as error:
        return f"Error Occurred. Please contact the technical team for more details."
    finally:
        db_connection.close()


    return result_json


if __name__ == '__main__':
    app.run(debug=True)
