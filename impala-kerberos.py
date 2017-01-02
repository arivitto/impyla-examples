from impala.dbapi import connect
from impala.util import as_pandas
from Constants import Constants

conn = connect(host=Constants.IMPALA_KERBEROS_URL, port=Constants.IMPORT_KERBEROS_PORT, auth_mechanism='GSSAPI')
cursor = conn.cursor()

cursor.execute("SHOW TABLES")
# After running .execute(), Impala will store the result sets on the server
# until it is fetched. Use the method .fetchall() to pull the entire result
# set over the network (you should only do it if you know dataset is small)
tables = cursor.fetchall()

print "=" * Constants.NUM_OF_SEPARATOR
print "Displaying list of tables"
# the result is a list of tuples
for t in tables:
    # we know that each row in SHOW TABLES result
    # should only contains one table name
    print t[0]

print ""
