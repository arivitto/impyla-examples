# Examples to use impyla to run queries against Impala and HiveServer2 

# Requirements

Those examples use impyla to connect to Impala, so impyla will be required.

Current impyla requires Python 2.6+ or 3.3+

To install it, the easiest way is to use "pip"

```
sudo pip install impyla
```

The examples also uses pandas library, so you will also need to install it

```
sudo pip install pandas
```

To connect to Kerberized Impala, you will also need to install the following: 

```
pip install thrift_sasl
pip install sasl
```

# Running the test

you will need to update the Constants.py file to set correct values for the following constants:

```
# the URL for impala daemon that is not kerberized
Constants.IMPALA_URL
# the URL for impala daemon that is kerberized (without LDAP)
Constants.IMPALA_KERBEROS_URL
# typically the default is 21050, if the same, you don't need to update it
Constants.IMPALA_PORT
```

then simply run:

```
python impala-examples.py
```

or

```
python impala-kerberos.py
```

