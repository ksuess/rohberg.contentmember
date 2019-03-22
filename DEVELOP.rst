Using the development buildout
------------------------------

Create a virtualenv in the package::

    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg

Emails
-----------

Emails are masked. Use script like the following to make mailto-link work.

::

          // masking email
          $("a").each(function() {
              let emaildomainpart = $(this).attr("data-emaildomainpart");
              if (emaildomainpart) {
                  let mail = "mailto:" + $(this).attr("href") + "@" + emaildomainpart;
                  $(this).click( function(event) {
                      event.preventDefault();
                      document.location = mail;
                      return false;
                  });
              }
          });
