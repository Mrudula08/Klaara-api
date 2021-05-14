import psycopg2
from flask import Flask, request, make_response
from psycopg2.extras import RealDictCursor

from common.app_configurations import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def establish_connection():
    """
    This definition is to establish connection to the database
    """
    db_connection = None
    try:
        db_connection = psycopg2.connect(database=database_name,
                                         user=user_name,
                                         password=password,
                                         host=host, port=port)

    except Exception as error:
        print(f"Unable to reach the database server. Please contact the technical team for more details.")
    return db_connection


def get_query_parameters():
    params = request.args
    branch_name = params.get('q', '')
    limit = params.get('limit', 100)
    offset = params.get('offset', 0)
    return branch_name, limit, offset


def parse_json(result):
    """
    This definition is to parse the result and return the result in expected format
    """
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
        db_connection = establish_connection()
        result_json = {'branches': list}
        branch_name, limit, offset = get_query_parameters()
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

    return make_response(result_json)


@app.route('/api/branches', methods=["GET"])
def get_details():
    try:
        db_connection = establish_connection()
        result_json = {'branches': list}
        branch_name, limit, offset = get_query_parameters()
        table_name = 'branches'
        query = f"select * from {table_name} " \
                f"where Lower(branch) like Lower('%{branch_name}%') " \
                f"or Lower(city) like Lower('%{branch_name}%') " \
                f"or Lower(district) like Lower('%{branch_name}%') " \
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
    return make_response(result_json)


if __name__ == '__main__':
    app.run(debug=True)
