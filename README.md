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

# Running the test

you will need to update the Constants.py file to set correct values for the following constants:

```
Constants.IMPALA_URL
Constants.IMPALA_PORT
```

then simply run:

```
python impala-examples.py
```
