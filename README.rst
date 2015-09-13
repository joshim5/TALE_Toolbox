===============================
TALE Toolbox
===============================

Generate reference sequences for TALEs built with the TALE Toolbox described in Sanjana et al., Nature Protocols (2012) and in Cong L, et al., Nature Communications (2012).

Quickstart
----------

First, run the following commands to bootstrap your environment.


::

    git clone https://github.com/joshim5/TALE_Toolbox
    cd TALE_Toolbox
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.


Deployment
----------

In your production environment, make sure the ``TALE_TOOLBOX_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test
