from impala.dbapi import connect
from impala.util import as_pandas
from Constants import Constants

conn = connect(host=Constants.IMPALA_URL, port=Constants.IMPALA_PORT)
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

# execute some statements to create new tables and insert data
cursor.execute("DROP TABLE IF EXISTS impyla_test")
cursor.execute("CREATE TABLE impyla_test (a int, b string)")
cursor.execute("INSERT OVERWRITE TABLE impyla_test VALUES (1, 'test'), (2, 'another test')")

cursor.execute('SELECT * FROM impyla_test LIMIT 100')
results = cursor.fetchall()

print '=' * Constants.NUM_OF_SEPARATOR
print "Displaying data in table impyla_test"
for r in results:
    print " | ".join(str(x) for x in r)

print ""

print "=" * Constants.NUM_OF_SEPARATOR
# you can also use pandas to display the output, however, please
# keep in mind that this will fetch the entire dataset, so if
# data is big, you might run into memory issues
cursor.execute('SELECT * FROM impyla_test LIMIT 100')
df = as_pandas(cursor)
print df

print ""
