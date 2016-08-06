# Examples to use impyla to run queries against Impala and HiveServer2 

Current impyla requires Python 2.6+ or 3.3+

# Installation

To install it, the easiest way is to use "pip"

```
sudo pip install impyla
```

The examples uses pandas library, so you will also need to install it

```
sudo pip install pandas
```

# Running the test

you will need to update the Constants.py file to set corect values the following:

```
Constants.IMPALA_URL
Constants.IMPALA_PORT
```

then simply run:

```
python impala-examples.py
```
