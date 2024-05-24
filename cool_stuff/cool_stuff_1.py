from rr_connection_manager import PostgresConnection, SQLServerConnection


conn = PostgresConnection(app="radar_live", tunnel=True)
# conn = SQLServerConnection(app='renalreg_live')

conn.connection_check()




















































# if __name__ == '__main__':
#     conn.connection_check()