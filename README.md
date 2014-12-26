`aergs`
=======

### Acquire and assign environment variables to an object

Set attributes on an instance:

    from aergs import Aergsx

    args = Aergs(consumer_key='CONSUMER_KEY')
    assert args.consumer_key == os.environ.get('CONSUMER_KEY')

To use keyword args in a function or class, call the `.as_dict` method:

    # Example using a twitter library.
    from twitter import Api

    args = Aergs(**{
        'consumer_key': 'CONSUMER_KEY',
        'consumer_secret': 'CONSUMER_SECRET',
        'access_token_key': 'ACCESS_TOKEN',
        'access_token_secret': 'ACCESS_SECRET',
    })

    # Instantiate a client.
    client = Api(**args.as_dict())

which is the equivalent of some incarnation of:

    client = Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                 consumer_secret=os.environ.get('CONSUMER_SECRET'),
                 access_token_key=os.environ.get('ACCESS_TOKEN'),
                 access_token_secret=os.environ.get('ACCESS_SECRET'))

### Install

    $ python setup.py install
